import { useReducer } from "preact/hooks";
import { Ask } from "./ask";
import { Hint } from "./hint";
import { Message } from "./message";
import { reducer } from "./reducer";
import { Waiting } from "./waiting";

export const Chat = () => {
  const [{ messages, isWaiting }, dispatch] = useReducer(reducer, {
    messages: [],
    isWaiting: false,
  });

  return (
    <main class="min-h-0 grow flex flex-col gap-4 relative pb-8">
      {isWaiting && <Waiting />}
      {messages.length === 0 ? (
        <Hint />
      ) : (
        <div class="grow flex flex-col-reverse p-4 pt-8 list-none overflow-y-auto overscroll-contain">
          <ol class="space-y-4">
            {messages.map(({ id, type, content }) => (
              <li key={id}>
                <Message type={type}>{content}</Message>
              </li>
            ))}
          </ol>
        </div>
      )}
      <Ask dispatch={dispatch} />
    </main>
  );
};
