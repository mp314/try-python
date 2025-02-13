#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Genetic Algorithm from scratch
Jason Brownlee, Machine Learning Algorithms in Python,
Machine Learning Mastery, Available from
https://machinelearningmastery.com/machine-learning-with-python/,
accessed April 15th, 2018.
"""

# genetic algorithm search for continuous function optimization
from numpy.random import randint
from numpy.random import rand

# objective function
def continuous_function(x_value):
    '''Minimize this'''
    return x_value[0]**2.0 + x_value[1]**2.0

def decode(bounds, n_bits, bitstring):
    '''decode bitstring to numbers'''
    decoded = list()
    largest = 2**n_bits
    for i in range(len(bounds)):
        # extract the substring
        start, end = i * n_bits, (i * n_bits)+n_bits
        substring = bitstring[start:end]

        # convert bitstring to a string of chars
        chars = ''.join([str(s) for s in substring])

        # convert string to integer
        integer = int(chars, 2)

        # scale integer to desired range
        value = bounds[i][0] + (integer/largest) * (bounds[i][1] - bounds[i][0])

        # store
        decoded.append(value)
    #print(f"{bitstring} decoded {decoded}")
    return decoded

def selection(pop, scores, k=3):
    '''tournament selection'''
    # first random selection
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k-1):
        # check if better (e.g. perform a tournament)
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]

def crossover(point1, point2, r_cross):
    '''crossover two parents to create two children'''
    # children are copies of parents by default
    crossover1, crossover2 = point1.copy(), point2.copy()
    # check for recombination
    if rand() < r_cross:
        # select crossover point that is not on the end of the string
        crossover_point = randint(1, len(point1)-2)
        # perform crossover
        crossover1 = point1[:crossover_point] + point2[crossover_point:]
        crossover2 = point2[:crossover_point] + point1[crossover_point:]
    return [crossover1, crossover2]

def mutation(bitstring, r_mut):
    '''mutation operator'''
    for i in range(len(bitstring)):
        # check for a mutation
        if rand() < r_mut:
            # flip the bit
            bitstring[i] = 1 - bitstring[i]

def genetic_algorithm(objective, bounds, n_bits, n_iter, n_pop, r_cross, r_mut):
    '''genetic algorithm'''
    # initial population of random bitstring
    pop = [randint(0, 2, n_bits*len(bounds)).tolist() for _ in range(n_pop)]

    # keep track of best solution
    best, best_eval = 0, objective(decode(bounds, n_bits, pop[0]))
    # enumerate generations
    for gen in range(n_iter):
        # decode population
        decoded = [decode(bounds, n_bits, p) for p in pop]
        # evaluate all candidates in the population
        scores = [objective(d) for d in decoded]
        # check for new best solution
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
                print(f">{gen}, new best f({decoded[i]}) = {scores[i]:.8f}")
        # select parents
        selected = [selection(pop, scores) for _ in range(n_pop)]
        # create the next generation
        children = list()
        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            point1, point2 = selected[i], selected[i+1]
            # crossover and mutation
            for crossover_value in crossover(point1, point2, r_cross):
                # mutation
                mutation(crossover_value, r_mut)
                # store for next generation
                children.append(crossover_value)
        # replace population
        pop = children
    return [best, best_eval]

def main():
    '''Optimize continuous function'''
    # define range for input
    bounds = [[-5.0, 5.0], [-5.0, 5.0]]
    # define the total iterations
    n_iter = 100
    # bits per variable
    n_bits = 16
    # define the population size
    n_pop = 100
    # crossover rate
    r_cross = 0.9
    # mutation rate
    r_mut = 1.0 / (float(n_bits) * len(bounds))
    # perform the genetic algorithm search
    best, score = genetic_algorithm(continuous_function,
        bounds, n_bits, n_iter, n_pop, r_cross, r_mut)
    print('Done!')
    decoded = decode(bounds, n_bits, best)
    print(f"f({decoded}) = {score:.8f}")


if __name__ == "__main__":
    main()


