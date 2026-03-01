import json
import re

from common import FILES, exercise

found = {}

ignore = list[str]()
with open("ne_ignore.txt", encoding="utf8") as file:
    ignore = [x.strip() for x in file.readlines()]

for file_name in FILES:
    with open(file_name, encoding="utf8") as file:
        text = file.read()
        sentences = re.split(r"[.!?()\[\]«»$]", text)
        for sentence in sentences:
            sentence = sentence.strip().strip("—–").strip().replace("\n", " ")
            modsentence = sentence

            words = [
                str(x).strip()
                for x in re.findall(r" [Нн][еи][ ]?[А-яё]+", f" {sentence}")
            ]

            words = [
                x
                for x in words
                if not any(f"{x.lower()}$".startswith(y) for y in ignore)
            ]

            mod = dict[str, str]()

            for word in words:
                mod[word] = (
                    f"^{word}".replace("^не ", "^не")
                    .replace("^не", "^не?")
                    .replace("^Не ", "^Не")
                    .replace("^Не", "^Не?")
                    .replace("^ни ", "^ни")
                    .replace("^ни", "^ни?")
                    .replace("^Ни ", "^Ни")
                    .replace("^Ни", "^Ни?")
                )[1:]
                modsentence = modsentence.replace(word, mod[word])

            for word in words:
                slitnoword = mod[word].replace("?", "")
                razdelnoword = mod[word].replace("?", " ")
                wrongword = slitnoword if word == razdelnoword else razdelnoword
                options = [slitnoword, razdelnoword]
                found[f"н{word[1:]}"] = {
                    "options": options,
                    "context": modsentence,
                    "right": [word],
                }

with open(exercise("ne"), "w", encoding="utf8") as dest:
    json.dump(list(found.values()), dest, ensure_ascii=False)
