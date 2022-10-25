import time

def brute_force(genome, pattern):
    """
    Args:
        genome (String): The main genome in which we need to check whether a pattern exists
        pattern (String): substring that needs to be found in the genome

    returns:
        result (List): The indexes where in the pattern exists is returned
                       If the pattern does not exist in the genome, an empty array is returned
    """
    t0 = time.time()
    indices = []
    i = 0
    while i < len(genome) - len(pattern) + 1:
        j = 0
        if genome[i] == pattern[j]:
            j += 1
            while j < len(pattern) and genome[i + j] == pattern[j]:
                j += 1
        if j == len(pattern):
            indices.append(i)
        i += 1
    t1 = time.time()
    return indices, (t1 - t0)