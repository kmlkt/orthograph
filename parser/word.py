import itertools
import json
import re

from common import exercise, files


def ignore_list(rule):
    with open(f"{rule}_ignore.txt", encoding="utf8") as file:
        return [x.strip() for x in file.readlines()]


def parse(rule, _ignore, word_re, to_common: list, to_options: list):
    found = {}

    def need_ignore(word):
        return any(y in f"^{word.lower()}$" for y in _ignore)

    def to_key(word):
        return f"{word[0].lower()}{word[1:]}"

    for text in files():
        mod = dict[str, str]()
        sentences = re.split(r"[.!?()\[\]«»$]", text)
        for sentence in sentences:
            sentence = sentence.strip().strip("—–").strip().replace("\n", " ")
            modsentence = sentence

            words = [str(x).strip() for x in re.findall(word_re, f" {sentence}")]

            words = [x for x in words if not need_ignore(x)]

            if "него" in words:
                print("Asas")

            for word in words:
                if word not in mod:
                    mod[word] = f"^{word}$"
                    for k, v in to_common:
                        mod[word] = mod[word].replace(k, v)
                    mod[word] = mod[word][1:-1]
                modsentence = modsentence.replace(word, mod[word])

            for word in words:
                if word not in found:
                    options = [mod[word].replace(k, v) for k, v in to_options]
                    found[to_key(word)] = {
                        "options": options,
                        "context": modsentence.replace(mod[word], f"[{mod[word]}]"),
                        "right": [word],
                    }

    return list(found.values())


def write(rule, exercises):
    with open(exercise(rule), "w", encoding="utf8") as dest:
        json.dump(exercises, dest, ensure_ascii=False)


def normal_flow(rule, word_re, to_common: list, to_options: list):
    write(rule, parse(rule, ignore_list(rule), word_re, to_common, to_options))
