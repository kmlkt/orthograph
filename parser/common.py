from itertools import product
from typing import Iterable

FILES = ["bk", "bulba", "dubr", "dushi", "pin", "shinel", "stanc", "vim12", "vim34"]
FILES = [f"../sources/{x}.txt" for x in FILES]


def files():
    for file_name in FILES:
        with open(file_name, encoding="utf8") as file:
            yield file.read()


def exercise(rule):
    return f"../exercises/{rule}.json"


def str_product(*groups):
    return ("".join(x) for x in product(*groups))


def first_upper(word: str):
    if word.startswith("^"):
        return "^" + word[1].upper() + word[2:]
    else:
        return word[0].upper() + word[1:]


def with_upper(*words: str):
    for word in words:
        yield first_upper(word)
        yield word


def list_regex(options: Iterable[str]):
    return f"(?:{'|'.join(options)})"
