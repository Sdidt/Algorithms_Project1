from open_fna import open_file
import os
from brute_force_search import brute_force
from rabin_karp import rabin_karp
from kmp import kmp


def compute_using_method(choice, genome, pattern, flag):
    """
    Args:
        choice (Integer): It is the number which is used to decide which algorithm to use.
                          {
                              1: brute_force
                              2: knuth_morris_pratt
                              3: rabin_karp
                          }
        genome (String): The main genome in which we need to check whether a pattern exists
        pattern (String): substring that needs to be found in the genome
        flag (Boolean): Boolean value to determine whether or not fna file is used
    """
    if choice == 1:
        ans, total = brute_force(genome, pattern)
    elif choice == 2:
        ans, total = kmp(genome, pattern)
    else:
        ans, total = rabin_karp(genome, pattern)
    if len(ans) == 0:
        print("Pattern does not occur in genome.")
    else:
        print("Pattern occurs in genome at following positions (0-based indexing):")
        print(ans)
    print("Total time consumed (in seconds): ", total)
    if flag:
        print("Size of file (in bytes): ", os.path.getsize(path))


while True:
    print("Choose one of the following options:")
    print("1. Brute Force Search")
    print("2. KMP")
    print("3. Rabin-Karp")
    print("4. Exit")
    choice = int(input())
    if choice == 4:
        exit()
    print("Would you like to input string and pattern?")
    ch = input()
    flag = False
    if ch == 'n' or ch == 'N':
        flag = True
        print("Enter the path of the fna file.")
        path = input()
        genome = open_file(path)
        genome = genome.upper()
        print("Enter the pattern to be searched in the genome.")
        pattern = input()
        if len(pattern) > len(genome):
            print('Please enter a pattern that is smaller than the genome.')
            continue
    else:
        print("Enter the genome:")
        genome = input()
        print("Enter the pattern:")
        pattern = input()
        if len(pattern) > len(genome):
            print('Please enter a pattern that is smaller than the genome.')
            continue
    compute_using_method(choice, genome, pattern, flag)
