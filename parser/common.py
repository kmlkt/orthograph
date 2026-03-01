FILES = ["bk", "bulba", "dubr", "dushi", "pin", "shinel", "stanc", "vim12", "vim34"]
FILES = [f"../sources/{x}.txt" for x in FILES]


def files():
    for file_name in FILES:
        with open(file_name, encoding="utf8") as file:
            yield file.read()


def exercise(rule):
    return f"../exercises/{rule}.json"
