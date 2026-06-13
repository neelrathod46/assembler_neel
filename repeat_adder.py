import random
REPEAT_SIZE = 60
REPEAT_COUNT = 4
SEQ_SIZE = 1025
nt = {0:'A', 1:'C', 2:'T', 3:'G'}

def create_repeated_sequence(filename, show_locations=False):
    seq = ""
    with open(filename, 'r') as f:
        seq = list(f.read())
    repeat_seq = seq.copy()
    marker_seq = seq
    return add_repeats(repeat_seq, marker_seq, show_locations)    

def generate_repeat():
    return [nt[random.randint(0,3)] for _ in range(REPEAT_SIZE)]
    
def add_repeats(seq, marker_seq, show_locations = False):
    marker_seq = seq.copy()
    repeat = generate_repeat()
    for _ in range(REPEAT_COUNT):
        i = random.randint(0,SEQ_SIZE-REPEAT_COUNT)
        seq[i:i+REPEAT_COUNT] = repeat[:]
        
        marker_seq[i:i+REPEAT_COUNT] = '.' * REPEAT_SIZE
    if show_locations:
        print(f"{seq}\n\nREPEAT LOCATIONS (dots)\n{marker_seq}")
    return seq










