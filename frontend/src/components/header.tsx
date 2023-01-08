import { Film } from "./icons/film";
import { Github } from "./icons/github";

export const Header = () => (
  <header class="flex justify-between items-center gap-4 py-4 border-b border-b-gray-200 dark:border-b-gray-800">
    <div class="flex items-center gap-3 px-2 py-1">
      <Film />
      <p class="font-bold text-xl">电影知识问答</p>
    </div>
    <a
      href="https://github.com/mrcaidev/kgqa"
      target="_blank"
      rel="noreferrer"
      class="p-2 rounded hover:bg-gray-200 dark:hover:bg-gray-800"
    >
      <Github />
      <span class="sr-only">在GitHub上查看项目源代码</span>
    </a>
  </header>
);
