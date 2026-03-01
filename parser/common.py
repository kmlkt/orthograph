FILES = ["bk", "bulba", "dubr", "dushi", "pin", "shinel", "stanc", "vim12", "vim34"]
FILES = [f"../sources/{x}.txt" for x in FILES]


def exercise(rule):
    return f"../exercises/{rule}.txt"
