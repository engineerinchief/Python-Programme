with open("log.txt") as f:
    content = f.read()
if "python" in content:
    print("Word in content")
else:
    print("Word not in content")

