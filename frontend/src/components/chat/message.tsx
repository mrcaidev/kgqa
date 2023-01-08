import type { ComponentChildren } from "preact";

type Props = {
  type: "question" | "answer";
  children: ComponentChildren;
};

export const Message = ({ type, children }: Props) => {
  const style =
    type === "question"
      ? "self-end bg-sky-200 dark:bg-sky-800"
      : "self-start bg-gray-200 dark:bg-gray-800";

  return <li class={"px-5 py-3 rounded " + style}>{children}</li>;
};
