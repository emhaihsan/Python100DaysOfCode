class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer



if "__name__" == "__main__":
    new_q = Question("What is the answer to life, the universe and everything?", 42)
    print(new_q.text)