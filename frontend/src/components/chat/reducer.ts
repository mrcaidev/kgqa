import { nanoid } from "nanoid";

export type State = {
  messages: Message[];
  isWaiting: boolean;
};

export type Action =
  | { type: "addQuestion"; payload: string }
  | { type: "addAnswer"; payload: string };

type Reducer = (state: State, action: Action) => State;

export const reducer: Reducer = (state, action) => {
  const { type, payload } = action;

  switch (type) {
    case "addQuestion":
      return {
        messages: [
          ...state.messages,
          { id: nanoid(), type: "question", content: payload },
        ],
        isWaiting: true,
      };
    case "addAnswer":
      return {
        messages: [
          ...state.messages,
          { id: nanoid(), type: "answer", content: payload },
        ],
        isWaiting: false,
      };
    default:
      return state;
  }
};
