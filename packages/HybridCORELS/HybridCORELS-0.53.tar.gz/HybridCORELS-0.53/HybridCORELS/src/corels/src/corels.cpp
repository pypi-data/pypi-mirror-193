#include "queue.h"
#include <algorithm>
#include <iostream>
#include <stdio.h>

#if defined(R_BUILD)
 #define STRICT_R_HEADERS
 #include "R.h"
 // textual substitution
 #define printf Rprintf
#endif

Queue::Queue(std::function<bool(Node*, Node*)> cmp, char const *type)
    : q_(new q (cmp)), type_(type) {}

Queue::~Queue() {
    if(q_)
        delete q_;
}

int* inconsistent_groups_indices;
int* inconsistent_groups_min_card;
int* inconsistent_groups_max_card;
int nb_incons_groups;
rule_t* black_box_errors;

/*
 * Performs incremental computation on a node, evaluating the bounds and inserting into the cache,
 * queue, and permutation map if appropriate.
 * This is the function that contains the majority of the logic of the algorithm.
 *
 * parent -- the node that is going to have all of its children evaluated.
 * parent_not_captured -- the vector representing data points NOT captured by the parent.
 */
void evaluate_children(CacheTree* tree, Node* parent, tracking_vector<unsigned short, DataStruct::Tree> parent_prefix,
        VECTOR parent_not_captured, Queue* q, PermutationMap* p) {
    VECTOR captured, captured_zeros, not_captured, not_captured_zeros, not_captured_equivalent, remaining_black_box_errors;
    int num_captured, c0, c1, captured_correct;
    int num_not_captured, d0, d1, default_correct, num_not_captured_equivalent, parent_errors, num_remaining_black_box_errors;
    bool prediction, default_prediction;
    double lower_bound, objective, parent_lower_bound, lookahead_bound;
    double rule_accuracy; // Hybrid model addition
    int rule_support; // Hybrid model addition
    double parent_equivalent_minority;
    double equivalent_minority = 0.;
    int nsamples = tree->nsamples();
    int nrules = tree->nrules();
    double c = tree->c();
    double beta = tree-> beta();
    double threshold = c * nsamples;
    rule_vinit(nsamples, &remaining_black_box_errors);
    rule_vinit(nsamples, &captured);
    rule_vinit(nsamples, &captured_zeros);
    rule_vinit(nsamples, &not_captured);
    rule_vinit(nsamples, &not_captured_zeros);
    rule_vinit(nsamples, &not_captured_equivalent);
    int i, len_prefix;
    len_prefix = parent->depth() + 1;
    parent_lower_bound = parent->lower_bound();
    parent_equivalent_minority = parent->equivalent_minority();
    if(parent->depth() == 0){
        parent_errors = 0;
    } else {
        parent_errors = parent->get_prefix_errors();
    }
    std::set<std::string> verbosity = logger->getVerbosity();
    double t0 = timestamp();
    for (i = 1; i < nrules; i++) {
        double t1 = timestamp();
        // check if this rule is already in the prefix
        if (std::find(parent_prefix.begin(), parent_prefix.end(), i) != parent_prefix.end())
            continue;
        // captured represents data captured by the new rule
        rule_vand(captured, parent_not_captured, tree->rule(i).truthtable, nsamples, &num_captured);
        // lower bound on antecedent support
        if ((tree->ablation() != 1) && (num_captured < threshold))
            continue;
        rule_vand(captured_zeros, captured, tree->label(0).truthtable, nsamples, &c0);
        c1 = num_captured - c0;
        if (c0 > c1) {
            prediction = 0;
            captured_correct = c0;
        } else {
            prediction = 1;
            captured_correct = c1;
        }
        // lower bound on accurate antecedent support
        if ((tree->ablation() != 1) && (captured_correct < threshold))
            continue;
        // subtract off parent equivalent points bound because we want to use pure lower bound from parent
        rule_support = num_captured; // Hybrid model addition
        rule_accuracy = (double)((double)captured_correct/(double)num_captured); // Hybrid model addition
        
        //double parent_equivalent_minority_num = (parent_equivalent_minority * (double)nsamples);
        //double parent_errors = (parent_lower_bound - ((len_prefix-1) * c))*(nsamples-parent_equivalent_minority_num);
        int n_errors_overall = parent_errors + (num_captured - captured_correct);
        //std::cout << "parent_equivalent_minority_num = " << parent_equivalent_minority_num << ", " << "parent_errors = " << parent_errors << ", n_errors_overall = " << n_errors_overall << std::endl;
        //lower_bound = parent_lower_bound - parent_equivalent_minority + (double)(num_captured - captured_correct) / nsamples + c;
        lower_bound = ((double)n_errors_overall/(double) (nsamples)) + (len_prefix * c); // valid for both (but not tight)
        //double error_only = (lower_bound - (len_prefix * c));
        //double n_errors_overall = error_only * nsamples;
        logger->addToLowerBoundTime(time_diff(t1));
        logger->incLowerBoundNum();
        if (lower_bound >= tree->min_objective()) // hierarchical objective lower bound
	        continue;
        double t2 = timestamp();
        rule_vandnot(not_captured, parent_not_captured, captured, nsamples, &num_not_captured);
        rule_vand(not_captured_zeros, not_captured, tree->label(0).truthtable, nsamples, &d0);
        d1 = num_not_captured - d0;
        if (d0 > d1) {
            default_prediction = 0;
            default_correct = d0;
        } else {
            default_prediction = 1;
            default_correct = d1;
        }
        // Hybrid model addition: don't consider the default decision
        //objective = lower_bound + beta*(double)((double)num_not_captured/(double)nsamples); // (double)(num_not_captured - default_correct) / nsamples;
        
        if(black_box_errors == nullptr){ // interpr-then-bb-training
            if (inconsistent_groups_indices != NULL){ // no collab mode
                objective = ((double)n_errors_overall/(double)(nsamples - num_not_captured)) + (len_prefix * c) + beta*(double)((double)num_not_captured/(double)nsamples);
            } else { // collab mode
                rule_vand(not_captured_equivalent, not_captured, tree->minority(0).truthtable, nsamples, &num_not_captured_equivalent);
                objective = ((double)(n_errors_overall+num_not_captured_equivalent)/(double)(nsamples)) + (len_prefix * c) + beta*(double)((double)num_not_captured/(double)nsamples);
            }
        } else { // bb-then-interpr-training
            rule_vand(remaining_black_box_errors, black_box_errors[1].truthtable, not_captured, nsamples, &num_remaining_black_box_errors);
            objective = (((double) (n_errors_overall + num_remaining_black_box_errors))/(double)(nsamples)) + (len_prefix * c) + beta*(double)((double)num_not_captured/(double)nsamples);
        }
        
        logger->addToObjTime(time_diff(t2));
        logger->incObjNum();
        bool support_ok = ((double)num_not_captured/(double)nsamples) < (1.0 - tree->min_coverage());
        // (**)
        if (tree->has_minority()) { 
            if(black_box_errors == nullptr){ // interpr-then-bb-training
                // Tight bound:
                if (inconsistent_groups_indices != NULL){ // no collab mode
                    int minority_to_capture = 0;
                    int total_incons_to_capture = 0;
                    double current_error_rate = (double)n_errors_overall/(double)(nsamples - num_not_captured);
                    for(int i = 0; i < nb_incons_groups; i++){
                        if(rule_isset(not_captured, inconsistent_groups_indices[i], tree->nsamples())){ // incons group i not captured by prefix
                            if((double) inconsistent_groups_min_card[i]/ (double) (inconsistent_groups_min_card[i]+inconsistent_groups_max_card[i]) <= current_error_rate){ // and capturing it could improve objective function (lower error rate)
                                minority_to_capture += inconsistent_groups_min_card[i];
                                total_incons_to_capture+=(inconsistent_groups_min_card[i]+inconsistent_groups_max_card[i]);
                                //std::cout << "Current error rate = " << current_error_rate << ", incons min = " << inconsistent_groups_min_card[i] << "/" << (inconsistent_groups_min_card[i]+inconsistent_groups_max_card[i]) << std::endl;
                            }
                        
                        }
                    }
                    lower_bound = ((double)(n_errors_overall+minority_to_capture)/(double) (nsamples-(num_not_captured - total_incons_to_capture))) + (len_prefix * c);
                    // Other (older) simpler (but not tight) computation
                    // rule_vand(not_captured_equivalent, not_captured, tree->minority(0).truthtable, nsamples, &num_not_captured_equivalent);
                    // Right below occurs the new (tighter) bound computation
                    // lower_bound = ((double)n_errors_overall/(double) (nsamples-num_not_captured_equivalent)) + (len_prefix * c);
                    // (it considers that in the best case we can never classify correctly more than all equivalent majorities of inconsistent groups)
                    // (and ignores minority for error computation for simplicity (or else, for the LB to be valid we should choose which groups to consider))
                    // (as done in the above, tight computation)
                } else { // collab mode
                    lower_bound = ((double)(n_errors_overall+num_not_captured_equivalent)/(double) (nsamples)) + (len_prefix * c);
                }
            } else { // bb-then-interpr-training
                rule_vand(not_captured_equivalent, not_captured, tree->minority(0).truthtable, nsamples, &num_not_captured_equivalent);
                equivalent_minority = (double)(num_not_captured_equivalent) / nsamples;
                lower_bound += equivalent_minority;
            }
            
        }
        // equivalent_minority = 0;
        if (objective < tree->min_objective() && support_ok) {
            if (verbosity.count("progress")) {
                printf("min(objective): %1.5f -> %1.5f, length: %d, cache size: %zu, lower bound: %1.5f\n",
                   tree->min_objective(), objective, len_prefix, tree->num_nodes(), lower_bound);
            }
            logger->setTreeMinObj(objective);
            tree->update_min_objective(objective);
            tree->update_opt_rulelist(parent_prefix, i);
            tree->update_opt_predictions(parent, prediction, default_prediction);
            tree->update_opt_support(parent, rule_support); // HybridCORELS: keep track of support and accuracy for each rule in the prefix
            tree->update_opt_accuracy(parent, rule_accuracy); // HybridCORELS: keep track of support and accuracy for each rule in the prefix
            // dump state when min objective is updated
            logger->dumpState();
        }
        // TODO FOR DEBUG, REMOVE 
        /*else if (objective < tree->min_objective()){
            std::cout << "Objective was better (" << objective <<  ") but support is only " << 1.0 - (double)num_not_captured/(double)nsamples << std::endl;
        }*/
        // calculate equivalent points bound to capture the fact that the minority points can never be captured correctly
        // (**) was here
        if (tree->ablation() != 2)
            lookahead_bound = lower_bound + c;
        else
            lookahead_bound = lower_bound;
        // only add node to our datastructures if its children will be viable
        if (lookahead_bound < tree->min_objective()) {
            double t3 = timestamp();
            // check permutation bound
            Node* n = p->insert(i, nrules, prediction, default_prediction,
                                   lower_bound, objective, parent, num_not_captured, nsamples,
                                   len_prefix, c, equivalent_minority, tree, not_captured, parent_prefix);
            logger->addToPermMapInsertionTime(time_diff(t3));
            // n is NULL if this rule fails the permutaiton bound
            if (n) {
                n->set_rule_support(rule_support); // Hybrid model addition
                n->set_rule_accuracy(rule_accuracy); // Hybrid model addition
                n->set_prefix_errors(n_errors_overall); // Hybrid model addition
                double t4 = timestamp();
                tree->insert(n);
                logger->incTreeInsertionNum();
                logger->incPrefixLen(len_prefix);
                logger->addToTreeInsertionTime(time_diff(t4));
                double t5 = timestamp();
                q->push(n);
                logger->setQueueSize(q->size());
                if (tree->calculate_size())
                    logger->addQueueElement(len_prefix, lower_bound, false);
                logger->addToQueueInsertionTime(time_diff(t5));
            }
        } // else:  objective lower bound with one-step lookahead
    }

    rule_vfree(&captured);
    rule_vfree(&captured_zeros);
    rule_vfree(&not_captured);
    rule_vfree(&not_captured_zeros);
    rule_vfree(&not_captured_equivalent);

    logger->addToRuleEvalTime(time_diff(t0));
    logger->incRuleEvalNum();
    logger->decPrefixLen(parent->depth());
    if (tree->calculate_size())
        logger->removeQueueElement(len_prefix - 1, parent_lower_bound, false);
    if (parent->num_children() == 0) {
        tree->prune_up(parent);
    } else {
        parent->set_done();
        tree->increment_num_evaluated();
    }
}

static size_t num_iter = 0;
static double min_objective = 0.0;
static VECTOR captured, not_captured;
static double start = 0.0;

/*
 * Explores the search space by using a queue to order the search process.
 * The queue can be ordered by DFS, BFS, or an alternative priority metric (e.g. lower bound).
 */
void bbound_begin(CacheTree* tree, Queue* q, rule_t* bb_errors, int* inconsistent_groups_indices_c, 
                  int* inconsistent_groups_min_card_c, int* inconsistent_groups_max_card_c, int nb_incons_groups_c) {
    start = timestamp();
    num_iter = 0;
    rule_vinit(tree->nsamples(), &captured);
    rule_vinit(tree->nsamples(), &not_captured);

    logger->setInitialTime(start);
    logger->initializeState(tree->calculate_size());
    // initial log record
    logger->dumpState();

    min_objective = 1.0;
    tree->insert_root();
    logger->incTreeInsertionNum();
    q->push(tree->root());
    logger->setQueueSize(q->size());
    logger->incPrefixLen(0);
    // log record for empty rule list
    logger->dumpState();
    inconsistent_groups_indices = inconsistent_groups_indices_c;
    inconsistent_groups_min_card = inconsistent_groups_min_card_c;
    inconsistent_groups_max_card = inconsistent_groups_max_card_c;
    black_box_errors = bb_errors;
    //if(black_box_errors != nullptr)
    //    std::cout << "c++ computed bb error rate = " << (double)count_ones_vector(black_box_errors[1].truthtable, tree->nsamples()) / (double) tree->nsamples() << std::endl;
    nb_incons_groups = nb_incons_groups_c;
}

void bbound_loop(CacheTree* tree, Queue* q, PermutationMap* p) {
    double t0 = timestamp();
    std::set<std::string> verbosity = logger->getVerbosity();
    size_t queue_min_length = logger->getQueueMinLen();
    int cnt;
    std::pair<Node*, tracking_vector<unsigned short, DataStruct::Tree> > node_ordered = q->select(tree, captured);
    logger->addToNodeSelectTime(time_diff(t0));
    logger->incNodeSelectNum();
    if (node_ordered.first) {
        double t1 = timestamp();
        // not_captured = default rule truthtable & ~ captured
        rule_vandnot(not_captured,
                     tree->rule(0).truthtable, captured,
                     tree->nsamples(), &cnt);
        evaluate_children(tree, node_ordered.first, node_ordered.second, not_captured, q, p);
        logger->addToEvalChildrenTime(time_diff(t1));
        logger->incEvalChildrenNum();

        if (tree->min_objective() < min_objective) {
            min_objective = tree->min_objective();
            if (verbosity.count("loud"))
                printf("before garbage_collect. num_nodes: %zu\n", tree->num_nodes());
            logger->dumpState();
            tree->garbage_collect();
            logger->dumpState();
            if (verbosity.count("loud"))
                printf("after garbage_collect. num_nodes: %zu\n", tree->num_nodes());
        }
    }
    logger->setQueueSize(q->size());
    if (queue_min_length < logger->getQueueMinLen()) {
        // garbage collect the permutation map: can be simplified for the case of BFS
        queue_min_length = logger->getQueueMinLen();
        //pmap_garbage_collect(p, queue_min_length);
    }
    ++num_iter;
    if ((num_iter % 10000) == 0) {
        if (verbosity.count("loud"))
            printf("iter: %zu, tree: %zu, queue: %zu, pmap: %zu, time elapsed: %f\n",
                   num_iter, tree->num_nodes(), q->size(), p->size(), time_diff(start));
    }
    if ((num_iter % logger->getFrequency()) == 0) {
        // want ~1000 records for detailed figures
        logger->dumpState();
    }
}

int bbound_end(CacheTree* tree, Queue* q, PermutationMap* p, bool early){//}, rule_t* rules, rule_t* labels) {
    std::set<std::string> verbosity = logger->getVerbosity();
    bool print_queue = 0;
    logger->dumpState(); // second last log record (before queue elements deleted)
    if (verbosity.count("loud"))
        printf("iter: %zu, tree: %zu, queue: %zu, pmap: %zu, time elapsed: %f\n",
               num_iter, tree->num_nodes(), q->size(), p->size(), time_diff(start));

    if (!early) {
        if (q->empty()) {
            if (verbosity.count("progress"))
                printf("Exited because queue empty\n");
        }
        else if (verbosity.count("progress"))
            printf("Exited because max number of nodes in the tree was reached\n");
    }

    // Print out queue
    ofstream f;
    if (print_queue) {
        char fname[] = "queue.txt";
        if (verbosity.count("progress")) {
            printf("Writing queue elements to: %s\n", fname);
        }
        f.open(fname, ios::out | ios::trunc);
        f << "lower_bound objective length frac_captured rule_list\n";
    }

    // Exiting early skips cleanup
    if(!early) {
        // Clean up data structures
        if (verbosity.count("progress")) {
            printf("Deleting queue elements and corresponding nodes in the cache,"
                "since they may not be reachable by the tree's destructor\n");
            printf("\nminimum objective: %1.10f\n", tree->min_objective());
        }
        Node* node;
        double min_lower_bound = 1.0;
        double lb;
        size_t num = 0;
        while (!q->empty()) {
            node = q->front();
            q->pop();
            if (node->deleted()) {
                tree->decrement_num_nodes();
                logger->removeFromMemory(sizeof(*node), DataStruct::Tree);
                delete node;
            } else {
                lb = node->lower_bound() + tree->c();
                if (lb < min_lower_bound)
                    min_lower_bound = lb;
                if (print_queue) {
                    std::pair<tracking_vector<unsigned short, DataStruct::Tree>, tracking_vector<bool, DataStruct::Tree> > pp_pair = node->get_prefix_and_predictions();
                    tracking_vector<unsigned short, DataStruct::Tree> prefix = std::move(pp_pair.first);
                    tracking_vector<bool, DataStruct::Tree> predictions = std::move(pp_pair.second);
                    f << node->lower_bound() << " " << node->objective() << " " << node->depth() << " "
                      << (double) node->num_captured() / (double) tree->nsamples() << " ";
                    for(size_t i = 0; i < prefix.size(); ++i) {
                        f << tree->rule_features(prefix[i]) << "~"
                          << predictions[i] << ";";
                    }
                    f << "default~" << predictions.back() << "\n";
                    num++;
                }
            }
        }
        if (verbosity.count("progress"))
            printf("minimum lower bound in queue: %1.10f\n\n", min_lower_bound);
    }

    if (print_queue)
        f.close();
    // last log record (before cache deleted)
    logger->dumpState();

    if(!early) {
        rule_vfree(&captured);
        rule_vfree(&not_captured);
    }

    return num_iter;
}
