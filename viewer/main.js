const { main, button, div, pre, span, p, select, option } = van.tags;

const Question = ({ right, options, context }, next) => {
  const checked = van.state(false);

  const check = (word) => {
    if (right.includes(word)) {
      next(true);
    } else {
      checked.val = true;
    }
  };

  const buttonClass = (word) =>
    checked.val ? (right.includes(word) ? "right" : "wrong") : "";

  return div(
    p({
      innerHTML: context.replaceAll("[", "<span>").replaceAll("]", "</span>"),
      class: "context",
    }),
    div(
      { class: "actions" },
      () =>
        div(
          { class: "button-list" },
          options.map((w) =>
            button({ class: buttonClass(w), onclick: () => check(w) }, w),
          ),
        ),
      () =>
        checked.val
          ? div(
              { class: "button-list" },
              button({ onclick: () => next(false) }, "Продолжить"),
            )
          : "",
    ),
  );
};

const Stat = (right, total) => {
  if (total === 0) {
    return "";
  }
  const percent = Math.ceil((right / total) * 100);
  return div({ class: "stat" }, `${percent}%`);
};

const RULES = {
  ne: "Не слитно / раздельно",
  pre: "Пре / при",
};

const Picker = (rule) =>
  select(
    {
      onchange: (e) => {
        rule.val = e.target.value;
      },
    },
    Object.keys(RULES).map((x) =>
      option({ value: x, selected: x === rule.val }, RULES[x]),
    ),
  );

const __CACHE = {};

const cached_fetch = async (path) => {
  if (!(path in __CACHE)) {
    const resp = await fetch(path);
    __CACHE[path] = await resp.json();
  }
  return __CACHE[path];
};

const Quiz = () => {
  const right = van.state(parseInt(localStorage.getItem("right") ?? "0", 10));
  const total = van.state(parseInt(localStorage.getItem("total") ?? "0", 10));
  const rule = van.state("pre");

  const incRight = () => {
    right.val++;
    localStorage.setItem("right", right.val.toString());
  };

  const incTotal = () => {
    total.val++;
    localStorage.setItem("total", total.val.toString());
  };

  return main(
    Picker(rule),
    () => Stat(right.val, total.val),
    () =>
      Await(
        {
          value: cached_fetch(`${EXERCISE_FILES}/${rule.val}.json`),
        },
        (questions) => {
          const randomIndex = () =>
            Math.floor(Math.random() * questions.length);
          const i = van.state(randomIndex());

          const next = (r) => {
            incTotal();
            if (r === true) {
              incRight();
            }
            i.val = randomIndex();
          };
          return Question(questions[i.val], next);
        },
      ),
  );
};

van.add(document.body, Quiz());
