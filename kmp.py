import time

def kmp(genome, pattern):
    """
    Args:
        genome (String): The main genome in which we need to check whether a pattern exists
        pattern (String): substring that needs to be found in the genome

    returns:
        result (List): The indexes where in the pattern exists is returned
                       If the pattern does not exist in the genome, an empty array is returned
    """
    t0 = time.time()
    pattern_arrangement = buildPattern(pattern)
    i = 0
    j = 0
    result = []
    while i + len(pattern) - j <= len(genome):
        if genome[i] == pattern[j]:
            if j == len(pattern_arrangement) - 1:
                result.append(i - j)
                j = -1
            i += 1
            j += 1
        elif j > 0:
            j = pattern_arrangement[j - 1] + 1
        else:
            i += 1
    
    t1 = time.time()
    return result, (t1 - t0)


def buildPattern(pattern):
    """
    Args:
        pattern (String): The String for which we find the prefix-suffix pattern

    returns:
        pattern_arrangement (List): The prefix-suffix pattern is returned
    """
    pattern_arrangement = [-1 for i in pattern]
    j = 0
    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[j]:
            pattern_arrangement[i] = j
            i += 1
            j += 1
        elif j > 0:
            j = pattern_arrangement[j - 1] + 1
        else:
            i += 1
    return pattern_arrangement