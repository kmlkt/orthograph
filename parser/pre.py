from common import with_upper
from word import normal_handle

normal_handle(
    "pre",
    r" пр[еи][А-яё]+",
    with_upper("^пр?"),
    [("?", "е"), ("?", "и")],
)
