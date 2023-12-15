 # Calculating d
def calculateD(e, phi):
    for d in range(3, phi):
        if (d * e) % phi == 1:
            return d 