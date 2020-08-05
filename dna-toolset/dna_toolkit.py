
Nucleotides = ["A","C","G","T"]
DNA_Reverse_Complement = {"A":"T", "T":"A", "C":"G", "G":"C"}


def validate_seq(dna_seq):
    dna_seq = dna_seq.upper()
    for nuc in dna_seq:
        if nuc not in Nucleotides:
            return "Invalid seq!"
    
    return dna_seq.upper()


def count_nucleotide_freq(seq):
    """Returns a dict of freq for each base"""
    nucl_freq_dict = {'A':0, 'C':0, 'G':0, 'T':0, }
    for nucl in seq:
        nucl_freq_dict[nucl] += 1
    
    return nucl_freq_dict


def transcription(seq):
    """ DNA->RNA by replacing T with U"""
    seq = seq.replace("T", 'U')
    
    return seq


def reverse_complement(seq):
    #return transcription(seq[::-1])
    #return seq.maketrans("ATCG", "TAGC")[::-1]
    return "".join([DNA_Reverse_Complement[nuc] for nuc in seq])[::-1]


def gc_content(seq:list):
    return round(seq.count('C') + seq.count('G') / len(seq) * 100)


def gc_content_subsec(seq:list, window=20):
    result = []
    for i in range(0, len(seq) - window + 1, window):
        subseq = seq[i:i + window]
        result.append(gc_content(subseq))
    
    return result
