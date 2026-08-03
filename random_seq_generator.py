import random
nt = ['A', 'T', 'C', 'G']
SEQ_SIZE = 2000
seq = []
with open('./output.txt', 'w') as f:
    for _ in range(SEQ_SIZE):
        seq.append(nt[random.randint(0,3)])
    seq = "".join(seq)
    f.write(seq)    


