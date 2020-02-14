text = "X-DSPAM-Confidence:    0.8475";
length = len(text)
confidence_s = text[text.find(':')+1 : length].strip()
confidence = float(confidence_s)
print(confidence)
