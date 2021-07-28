
import collections

import argparse

results = dict()

# Generate a list of all square numbers up until N.

def get_candidates(N):

    step = 1

    num = 0

    candidates = []

    while (num + step) <= N:

        num += step

        candidates.append(num)

        step += 2

    return candidates


def backtracking(N, a, k, sum):

    # If a solution has been found, add it to the results
    # list in the form of a set so as to avoid duplicated solutions

    if (sum == N and k == len(a)):

        # make a deep copy of a

        deep_copy = [x for x in a]

        # if something is contained in a, check for duplicates

        if results and len(a) in results:

            for solution in results.get(len(a)):

                if collections.Counter(a) == collections.Counter(solution):

                    #print(f'Not storing solution {a} because permutation {solution} already existent!')

                    return

        # print solution
        print(a)

        # add solutions to results
        if len(a) in results:

            results.get(len(a)).append(deep_copy)

        else:

            results[len(a)] = [deep_copy]

    # If sum has exceeded N or k has exceeded a's bounds, stop

    elif (sum > N or k >= len(a)):

        return

    # else continue with procedure

    else:

        candidates = get_candidates(N)

        #print(candidates)

        for candidate in candidates:

            if (sum + candidate) <= N:

                # print(f"Candidate: {candidate}")

                a[k] = candidate

                backtracking(N, a, k+1, sum+candidate)

def find_square_combinations(N):

    for i in range(1, N+1):

        a = [None] * i

        backtracking(N, a, 0, 0)


if __name__ == "__main__":

    # Create the argument parser and add arguments

    parser = argparse.ArgumentParser()

    parser.add_argument(dest='number', type=int, help="The number to compute all unique square decompositions for.")

    # Parse the input parameter

    args = parser.parse_args()

    find_square_combinations(args.number)