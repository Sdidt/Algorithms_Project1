import random
import time


def _hash_func(pattern, prime_number, x):
    """
    Args:
        pattern (String): substring that needs to be found in the genome
        prime_number (Integer): large prime used for computation of hash funcion
        x (Integer): random value chosen between 1 and p - 1 used as argument for hash function

    returns:
        ans (Integer): Hash value of the pattern
    """
    ans = 0
    i = len(pattern) - 1
    while i >= 0:
        ans = (ans * x + ord(pattern[i])) % prime_number
        i -= 1
    return ans


def precomputeHashes(genome, pattern, prime_number, x):
    """
    Args:
        genome (String): The main genome in which we need to check whether a pattern exists
        pattern (String): substring that needs to be found in the genome
        prime_number (Integer): large prime used for computation of hash funcion
        x (Integer): random value chosen between 1 and p - 1 used as argument for hash function

    returns:
        hashes (List): An array containing all the hashes
    """

    '''Rolling Hash'''
    hashes = [0 for _ in range(len(genome) - len(pattern) + 1)]
    hashes[len(genome) - len(pattern)] = _hash_func(genome[len(genome) - len(pattern):len(genome)], prime_number, x)
    y = 1
    i = 1
    """
    Purpose of below loop is to compute x^|pattern| mod prime_number, by multiplying iteratively and taking
    mod at each step.
    """
    while i <= len(pattern):
        y = (y * x) % prime_number
        i += 1
    i = len(genome) - len(pattern) - 1
    while i >= 0:
        """
            Recurrence Relation
                The reccurence relation is - 
                            
                            hashes[i]= x.hashes[i+1]+(genome[i]-genome[i+|pattern|].x^|pattern|) mod prime_number
                
                x^|pattern| in the above equation has been replaced by y as it was precomputed for this purpose
        """
        hashes[i] = (x * hashes[i + 1] + ord(genome[i]) - y * ord(genome[i + len(pattern)])) % prime_number
        i -= 1
    return hashes


def rabin_karp(genome, pattern):
    """
    Args:
        genome (String): The main genome in which we need to check whether a pattern exists
        pattern (String): substring that needs to be found in the genome

    returns:
        result (List): The indexes where in the pattern exists is returned
                       If the pattern does not exist in the genome, an empty array is returned
    """
    t0 = time.time()
    prime_number = 10000003
    x = random.randint(1, prime_number - 1)
    result = []
    pHash = _hash_func(pattern, prime_number, x)
    hashes = precomputeHashes(genome, pattern, prime_number, x)
    for i in range(0, len(genome) - len(pattern) + 1):
        if pHash != hashes[i]:
            continue
        j = 0
        while j < len(pattern) and genome[i + j] == pattern[j]:
            j += 1
        if j == len(pattern):
            result.append(i)
    t1 = time.time()
    return result, (t1 - t0)
