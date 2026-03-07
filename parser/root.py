from common import list_regex, str_product, with_upper
from prist import PRIST
from word import normal_parse, save

OA = ["о", "а"]
EI = ["е", "и"]


def root_common(roots: list[str]):
    return with_upper(*str_product(["^"], PRIST, roots))


def root_regex(forms: list[str], replace: list[str]):
    return f" [А-яё]*{
        list_regex(
            f'[{x[0].upper()}{x[0]}]{x[1:].replace('?', list_regex(replace))}'
            for x in forms
        )
    }[А-яё]*"


def root_options(replace: list[str]):
    return [("?", x) for x in replace]


def root_parse(forms: list[str], replace: list[str]):
    return normal_parse(
        "root",
        root_regex(forms, replace),
        root_common(forms),
        root_options(replace),
    )


save(
    "root",
    [
        *root_parse(["л?г"], OA),
        *root_parse(["ск?к", "ск?ч"], OA),
        *root_parse(["р?с", "р?щ"], OA),
        *root_parse(["г?р"], OA),
        *root_parse(["з?р"], OA),
        *root_parse(["тв?р"], OA),
        *root_parse(["к?с"], OA),
        *root_parse(["б?р"], EI),
        *root_parse(["п?р"], EI),
        *root_parse(["д?р"], EI),
        *root_parse(["т?р"], EI),
        *root_parse(["м?р"], EI),
        *root_parse(["бл?ст"], EI),
        *root_parse(["ж?г"], EI),
        *root_parse(["ст?л"], EI),
        *root_parse(["ч?т"], EI),
        *root_parse(["м?к"], EI),
        *root_parse(["р?вн"], EI),
        *root_parse(["пл?в"], ["о", "а", "ы"]),
    ],
)
