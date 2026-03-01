from word import normal_flow

TO_COMMON = [
    ("^Пре", "^Пр?"),
    ("^При", "^Пр?"),
    ("^пре", "^пр?"),
    ("^при", "^пр?"),
]


normal_flow(
    "pre",
    r" [Пп]р[еи][А-яё]+",
    TO_COMMON,
    [("?", "е"), ("?", "и")],
)
