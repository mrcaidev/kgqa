import { useState } from "preact/hooks";
import type { Action } from "./reducer";

type ResponseJson = { answer: string };

const fetchAnswer = async (question: string) => {
  if (import.meta.env.DEV) {
    return "开发环境不会真的请求后端";
  }

  const url = new URL("/", import.meta.env.VITE_API_BASE_URL);
  const response = await fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question }),
  });

  if (!response.ok) {
    return "抱歉，网络连接失败，请稍后再试";
  }

  const json: ResponseJson = await response.json();
  const { answer } = json;

  if (!answer) {
    console.error(JSON.stringify(json));
    return "抱歉，未知错误，请稍后再试";
  }

  return answer;
};

type Props = {
  dispatch: (action: Action) => void;
};

export const Ask = ({ dispatch }: Props) => {
  const [question, setQuestion] = useState("");

  const handleEnter = async (event: KeyboardEvent) => {
    if (event.key !== "Enter" || !question) {
      return;
    }

    setQuestion("");
    dispatch({ type: "addQuestion", payload: question });
    const answer = await fetchAnswer(question);
    dispatch({ type: "addAnswer", payload: answer });
  };

  return (
    <input
      type="text"
      value={question}
      onInput={(event) => setQuestion(event.currentTarget.value)}
      onKeyDown={handleEnter}
      autoFocus
      placeholder="请输入问题，按回车发送"
      class="min-w-0 px-5 py-3 rounded focus:outline outline-2 outline-offset-0 outline-gray-300 dark:outline-gray-700 bg-gray-200 dark:bg-gray-800 placeholder:text-gray-600 dark:placeholder:text-gray-400"
    />
  );
};
