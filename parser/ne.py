from common import with_upper
from word import normal_handle

normal_handle(
    "ne",
    r" н[еи][ ]?[А-яё]+",
    with_upper("^не?", "^ни?"),
    [("?", " "), ("?", "")],
)
