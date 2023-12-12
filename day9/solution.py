lines = open('day9/data.txt').read().splitlines()

SUM1 = 0
SUM2 = 0
for line in lines:
    seqs = [[int(x) for x in line.split()]]
    while not(all([True if x == 0 else False for x in seqs[-1]])):  # Check last sequence is all 0
        seq = [seqs[-1][i] - seqs[-1][i-1] for i in range(1,len(seqs[-1]))]
        seqs.append(seq)
    val1 = 0
    val2 = 0
    for seq in seqs[-2::-1]:
        val1 += seq[-1]          # part 1
        val2 = seq[0] - val2     # part 2
    SUM1 += val1
    SUM2 += val2

print("Part 1: ", str(SUM1) + "\nPart 2: ", str(SUM2))

        


