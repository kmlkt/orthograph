import re

from common import FILES, exercise

found = dict[str, str]()

for file_name in FILES:
    with open(file_name) as file:
        text = file.read()
        contexts = re.findall(r"[^.!?…]+ [Нн]е[^ ][^.!?…]+[.!?…]", text)
        for context in contexts:
            scontext = str(context).strip()
            words = re.findall(r" [Нн]е[ ]?[А-я]+", scontext)
            for word in words:
                found["н" + str(word).strip()[1:]] = scontext

with open(exercise("ne"), "w", encoding="utf8") as dest:
    dest.write("\n".join(sorted(f"{k}: {found[k].replace('\n', ' ')}" for k in found)))
