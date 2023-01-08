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
    <main class="min-h-0 grow flex flex-col gap-6 relative pt-4 pb-8">
      {isWaiting && <Waiting />}
      <div class="grow flex flex-col-reverse px-4 py-2 list-none overflow-y-auto overscroll-contain">
        <ol class="space-y-4">
          {messages.map(({ id, type, content }) => (
            <li key={id}>
              <Message type={type}>{content}</Message>
            </li>
          ))}
        </ol>
      </div>
      <Ask dispatch={dispatch} />
    </main>
  );
};
