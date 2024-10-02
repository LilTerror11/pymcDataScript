import re


def getFuncParams(line: str) -> str:
    return re.search(r"\(\"(.*)\"\)", line).group(1)

def parseFile(path: str):
    with open(path) as f:
        code = f.read().split("\n")

    lines = code
    for index, line in enumerate(lines):
        if line == "":
            code.pop(index)

    for line in code:
        if re.search(r"print\(", line):
            print(f"say {getFuncParams(line)}")


parseFile("test.pmds")