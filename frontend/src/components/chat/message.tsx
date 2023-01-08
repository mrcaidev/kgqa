import type { ComponentChildren } from "preact";

type Props = {
  type: "question" | "answer";
  children: ComponentChildren;
};

export const Message = ({ type, children }: Props) => {
  const style =
    "w-fit max-w-[90%] px-5 py-3 rounded overflow-hidden text-ellipsis " +
    (type === "question"
      ? "ml-auto bg-sky-200 dark:bg-sky-800"
      : "mr-auto bg-gray-200 dark:bg-gray-800");

  return <p class={style}>{children}</p>;
};
