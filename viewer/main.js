const { main, button, div, pre, span, p } = van.tags;

const prepareNe = (line) => {
  const [word, ...contextSplit] = line.split(": ");
  const context = contextSplit.join(": ");
  const right = [word];
  const wrong = [
    word.startsWith("не ")
      ? word.replace("не ", "не")
      : word.replace("не", "не "),
  ];
  const hiddenContext = ` ${context}`
    .replaceAll(new RegExp(`${word}`, "gi"), `<span> ${word}</span>`)
    .replaceAll(/ не /gi, " не")
    .replaceAll(/ не/gi, " не?");

  const all = [...right, ...wrong];
  all.sort();

  return {
    right,
    all,
    context: hiddenContext,
  };
};

const Question = ({ right, all, context }, next) => {
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
    p({ innerHTML: context, class: "context" }),
    () =>
      div(
        { class: "button-list near-bottom" },
        all.map((w) =>
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
    Await({ value: fetch("/parser/ne.txt").then((x) => x.text()) }, (text) => {
      const lines = text.split("\n");

      const randomIndex = () => Math.floor(Math.random() * lines.length);
      const i = van.state(randomIndex());

      const next = (r) => {
        incTotal();
        if (r === true) {
          incRight();
        }
        i.val = randomIndex();
      };
      return div(() => Question(prepareNe(lines[i.val]), next));
    }),
  );
};

van.add(document.body, Quiz());
