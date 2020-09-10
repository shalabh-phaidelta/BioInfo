import structures as structs


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
    #print(seq.count('C'))
    #print(seq.count('G'))
    return round((seq.count('C') + seq.count('G')) / len(seq) * 100)

#70-20+1=51
def gc_content_subsec(seq:list, window=20):
    result = []
    for i in range(0, len(seq) - window + 1 , window): # len(seq) - window + 1 because in py the last(stop value in range or list) value is not considered
        subseq = seq[i:i + window]
        result.append(gc_content(subseq))
    
    return result


def translate_seq(seq, init_pos=0):
    return [structs.DNA_Codons[ seq[pos:pos+3] ] for pos in range(init_pos, len(seq)-3,3) ]


def codon_usage(seq, amino_acid):    
    pass