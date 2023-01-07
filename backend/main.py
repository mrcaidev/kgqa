import dotenv
from core import QA

dotenv.load_dotenv()

qa = QA()

while True:
    question = input("请输入问题：")
    answer = qa.answer(question)
    print(answer)
