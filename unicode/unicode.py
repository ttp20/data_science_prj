file = open("unicode.txt", encoding="utf8")
result = file.read()
result = result.split("\n")

UNICODE = {}
for line in result:
    words = line.split(" ")
    UNICODE[words[1]] = words[0]

print(UNICODE)
