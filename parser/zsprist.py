from common import list_regex, str_product, with_upper
from word import normal_parse, save

ZS = ["з", "с"]


def zs_common(prist):
    return with_upper(*str_product(["^"], ["не", ""], prist))


def zs_regex(forms: list[str], replace: list[str]):
    return f" [А-яё]*{
        list_regex(f'{x.replace('?', list_regex(replace))}' for x in forms)
    }[бвгджзклмнпрстфхцчшщ][А-яё]*"


def zs_options(replace: list[str]):
    return [("?", x) for x in replace]


def zs_parse(forms: list[str], replace: list[str] = ZS):
    return normal_parse(
        "zsprist",
        zs_regex(forms, replace),
        zs_common(forms),
        zs_options(replace),
    )


save(
    "zsprist",
    [
        *zs_parse(["бе?"]),
        *zs_parse(["во?"]),
        *zs_parse(["?"]),
        *zs_parse(["обе?"]),
        *zs_parse(["ро?"]),
        *zs_parse(["ра?"]),
        *zs_parse(["и?"]),
    ],
)
