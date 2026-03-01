const { main, button, div, pre, span, p } = van.tags;

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
    () =>
      div(
        { class: "button-list near-bottom" },
        options.map((w) =>
          button({ class: buttonClass(w), onclick: () => check(w) }, w),
        ),
      ),
    () =>
      checked.val
        ? div(
            { class: "button-list bottom" },
            button({ onclick: () => next(false) }, "Продолжить"),
          )
        : "",
  );
};

const Stat = (right, total) => {
  if (total === 0) {
    return "";
  }
  const percent = Math.ceil((right / total) * 100);
  return div({ class: "stat" }, `${percent}%`);
};

const Quiz = () => {
  const right = van.state(parseInt(localStorage.getItem("right") ?? "0", 10));
  const total = van.state(parseInt(localStorage.getItem("total") ?? "0", 10));

  const incRight = () => {
    right.val++;
    localStorage.setItem("right", right.val.toString());
  };

  const incTotal = () => {
    total.val++;
    localStorage.setItem("total", total.val.toString());
  };

  return main(
    () => Stat(right.val, total.val),
    Await(
      { value: fetch(`${EXERCISE_FILES}/ne.json`).then((x) => x.json()) },
      (questions) => {
        const randomIndex = () => Math.floor(Math.random() * questions.length);
        const i = van.state(randomIndex());

        const next = (r) => {
          incTotal();
          if (r === true) {
            incRight();
          }
          i.val = randomIndex();
        };
        return div(() => Question(questions[i.val], next));
      },
    ),
  );
};

van.add(document.body, Quiz());
