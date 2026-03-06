from common import with_upper
from word import normal_handle

normal_handle(
    "pre",
    r" [Пп]р[еи][А-яё]+",
    with_upper("^пр?"),
    [("?", "е"), ("?", "и")],
)
