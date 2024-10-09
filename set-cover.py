# go check video https://www.youtube.com/watch?v=32nEoxB_pNU

import itertools
import random

# Generate the universe and the subsets, just getting the problem istance
def generate_universe_and_subsets(universe_size, num_subsets, min_set_size, max_set_size):
    universe = set(range(1, universe_size + 1))
    
    subsets = []
    remainin_elemets = set(universe)
    
    # while universe not completely coverd
    while remainin_elemets:
        set_size = random.randint(min_set_size, max_set_size)
        # Cover from the uncoverd elements
        new_subset = set(random.sample(list(remainin_elemets), min(set_size, len(remainin_elemets))))
        subsets.append(new_subset)
        remainin_elemets -= new_subset
        
    for _ in range(num_subsets - len(subsets)):
        set_size = random.randint(min_set_size, max_set_size)
        new_subset = set(random.sample(list(universe), set_size))
        subsets.append(new_subset)
    
    return universe, subsets

universe, subsets = generate_universe_and_subsets(universe_size=1000, num_subsets=100, min_set_size=5, max_set_size=50)
#print(universe)
        
#for s in subsets:
#    print(s)

# How to find the optimal solution
# Guarantee to find the solution, 2^n complexity exponentional run time complexitys
def brute_force_set_cover(universe, sets):
    n = len(sets)
    
    for i in range(1, n+1):
        # i represents the number of sets used, so if i=1 i'm saying is able to cover the whole universe with one set? ecc ...
        for subset in itertools.combinations(sets, i):
            if set.union(*subset) == universe:
                return subset
            

#print(set.union(*solution) == universe)


# Heuristic approach, greedy approach but not guarantee the solution is valid
# Total complexity of problem O(n_universe * n_sets) polynomial run time complexity
def greedy_set_cover(universe, sets):
    
    uncovered = universe.copy()
    solution = []
    
    # Worst case i have to go for the whole universe -> O(n_universe)
    while uncovered:
        # We have a bunch of sets that are not selected, we are searching for the combination that gives me the most intersections.
        # Iterate over O(n_sets) linear time
        best_set = max(sets, key=lambda s: len(s & uncovered))
        solution.append(best_set)
        uncovered -= best_set
    return solution

solution = greedy_set_cover(universe, subsets)
#print(universe)
#for s in subsets:
#    print(s)
print("solution greedy",solution)
print(len(solution))
#print(set.union(*solution) == universe)

solution = brute_force_set_cover(universe, subsets)
#print(universe)
#for s in subsets:
#    print(s)
print("solution brute",solution)
print(len(solution))