class Yorn :

    def question(self, question:str):
        self.question = question
        return self.ask_question()

    def ask_question(self):
        answer = input(f"{self.question} (y/n): ")
        return self._answer_handler(answer)

    def _answer_handler(self, answer):
        if answer.lower() in ["y", "ye","yes"]:
            return True
        elif answer.lower() in ["n", "no"]:
            return False
        else:
            self.ask_question()

yorn = Yorn()
question = yorn.question