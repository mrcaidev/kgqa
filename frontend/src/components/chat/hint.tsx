import { MessageSquare } from "components/icons/message-square";

const getRandomQuestion = () => {
  const questions = [
    "成龙演过多少电影",
    "张国荣的生日",
    "卧虎藏龙主要讲了什么",
  ];

  return questions[Math.floor(Math.random() * questions.length)];
};

export const Hint = () => (
  <div class="grow flex flex-col justify-center items-center text-center text-gray-600 dark:text-gray-400">
    <MessageSquare />
    <p class="mt-4">问我有关电影或演员的问题吧~</p>
    <p class="mt-1">试一试：{getRandomQuestion()}</p>
  </div>
);
