_input = str(input()).split(' ')
scores = [float(i) for i in _input]
scores.sort()
score = (scores[1] + scores[2]) / 2
print(round(score, 2))
