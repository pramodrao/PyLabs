filename = input("Enter a file name: ")
try:
    file = open(filename)
    spamConfidenceTotal = 0.0
    spamConfidenceCount = 0
    for line in file:
        if line.startswith("X-DSPAM-Confidence"):
            spamconfidence = float(line.split(":")[1].strip())
            spamConfidenceCount = spamConfidenceCount + 1
            spamConfidenceTotal = spamConfidenceTotal + spamconfidence
    print("Average spam confidence: " ,(spamConfidenceTotal/spamConfidenceCount))
except FileNotFoundError():
    print("File", filename, "does not exist.")
except:
    print("Invalid Operation")
