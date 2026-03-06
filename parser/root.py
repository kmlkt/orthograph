from common import str_product, with_upper
from prist import PRIST
from word import normal_parse, write

write(
    "root",
    [
        *normal_parse(
            "lag",
            r" [А-яё]+[Лл](?:аг|ож)[А-яё]+",
            with_upper(*str_product(("^"), PRIST, ("л?г", "л?ж"))),
            [("?", "а"), ("?", "о")],
        ),
        *normal_parse(
            "skak",
            r" [А-яё]+[Сс]к(?:ак|оч)[А-яё]+",
            with_upper(*str_product(("^"), PRIST, ("ск?к", "ск?ч"))),
            [("?", "а"), ("?", "о")],
        ),
        *normal_parse(
            "rast",
            r" [А-яё]+[Рр][ао][сщ][А-яё]+",
            with_upper(*str_product(("^"), PRIST, ("р?с", "р?щ"))),
            [("?", "а"), ("?", "о")],
        ),
        *normal_parse(
            "gar",
            r" [А-яё]+[Гг][ао]р[А-яё]+",
            with_upper(*str_product(("^"), PRIST, ("г?р"))),
            [("?", "а"), ("?", "о")],
        ),
        *normal_parse(
            "gar",
            r" [А-яё]+[Зз][ао]р[А-яё]+",
            with_upper(*str_product(("^"), PRIST, ("з?р"))),
            [("?", "а"), ("?", "о")],
        ),
        *normal_parse(
            "gar",
            r" [А-яё]+[Тт]в[ао]р[А-яё]+",
            with_upper(*str_product(("^"), PRIST, ("тв?р"))),
            [("?", "а"), ("?", "о")],
        ),
        *normal_parse(
            "gar",
            r" [А-яё]+[Тт]в[ао]р[А-яё]+",
            with_upper(*str_product(("^"), PRIST, ("тв?р"))),
            [("?", "а"), ("?", "о")],
        ),
    ],
)
