with open('./sequence2.txt', 'r') as f1:
    seq = f1.read()
    seq = seq[::-1]
with open('./reverseseq2', 'w') as f2:
    f2.write(seq)
