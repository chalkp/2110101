code = str(input())

blob1 = code[3] + code[10] + code[17] + code[24] + code[31]
blob2 = code[7] + code[12] + code[17] + code[22] + code[27]
blob3 = str(int(blob1) + int(blob2) + 10000)
blob4 = blob3[-4:-1]
blob5 = (int(blob4[0]) + int(blob4[1]) + int(blob4[2])) % 10 + 1
blob6 = list(['0', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])[blob5]
blob7 = blob4 + blob6

print(blob7)
