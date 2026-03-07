import itertools
import json
import re
from typing import Iterable, Tuple

from common import exercise, files


def ignore_list(rule):
    with open(f"../ignore/{rule}.txt", encoding="utf8") as file:
        return [x.strip() for x in file.readlines()]


def parse(
    rule,
    _ignore,
    word_re,
    common: Iterable[str],
    to_options: list[Tuple[str, str]],
):
    common = list(common)
    to_common = [
        *itertools.chain(
            *([(x.replace(y, z), x) for y, z in to_options] for x in common)
        )
    ]
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

            words = [
                str(x).strip()
                for x in re.findall(word_re, f" {sentence}", flags=re.IGNORECASE)
            ]

            if len(words) == 0:
                continue

            words = [
                x
                for x in words
                if not need_ignore(x) and any(k in f"^{x}$" for k, _ in to_common)
            ]

            if len(words) == 0:
                continue

            for word in words:
                if word not in mod:
                    mod[word] = f"^{word}$"
                    for k, v in to_common:
                        if k in mod[word]:
                            mod[word] = mod[word].replace(k, v)
                            break
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


def write_json(rule, exercises):
    with open(exercise(rule), "w", encoding="utf8") as dest:
        json.dump(exercises, dest, ensure_ascii=False)


def collect(exercises):
    return sorted(set((x["right"][0] for x in exercises)))


def write_words(words):
    with open("../debug/words.txt", "w", encoding="utf8") as dest:
        dest.writelines(f"{x}\n" for x in words)


def save(rule, exercises):
    write_json(rule, exercises)
    write_words(collect(exercises))


def normal_parse(
    rule,
    word_re,
    common: Iterable[str],
    to_options: list[Tuple[str, str]],
):
    return parse(rule, ignore_list(rule), word_re, common, to_options)


def normal_handle(
    rule, word_re, common: Iterable[str], to_options: list[Tuple[str, str]]
):
    exercises = normal_parse(rule, word_re, common, to_options)
    save(rule, exercises)
