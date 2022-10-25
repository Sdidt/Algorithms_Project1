import fastaparser

def open_file(path):
    """
    Args:
        path (String): file path to the genome string

    returns:
        genome (String): The entire genome
    """
    with open(path) as file:
        parser = fastaparser.Reader(file, parse_method='quick')
        for seq in parser:
            genome = seq.sequence
            break
        # for seq in parser:
        #    print('Header: ', seq.header)
        #    print(seq.sequence)
        #    print('Sequence: ', len(seq.sequence))
        #    break
        return genome