import { useReducer } from "preact/hooks";
import { Ask } from "./ask";
import { Message } from "./message";
import { reducer } from "./reducer";
import { Waiting } from "./waiting";

export const Chat = () => {
  const [{ messages, isWaiting }, dispatch] = useReducer(reducer, {
    messages: [],
    isWaiting: false,
  });

  return (
    <main class="flex flex-col gap-6 relative max-w-5xl h-screen px-8 pt-20 pb-8 mx-auto">
      {isWaiting && <Waiting />}
      <ol class="grow flex flex-col gap-4 pr-4 py-2 list-none overflow-auto">
        {messages.map(({ id, type, content }) => (
          <Message key={id} type={type}>
            {content}
          </Message>
        ))}
      </ol>
      <Ask dispatch={dispatch} />
    </main>
  );
};
