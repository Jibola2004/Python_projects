import csv
import random
class Quiz:
    def __init__(self, filename="quiz_data.csv"):
        self.data = {}
        self.score = 0
        self.filename = filename

    def populate_data(self):
        self.data.clear()
        try:
            with open(self.filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.data[row['Question']] = row['Answer']
            print(f"\n📖 Loaded {len(self.data)} questions from '{self.filename}'")
        except FileNotFoundError:
            print(f"\n⚠️ File '{self.filename}' not found.")

    def ask_question(self, question, correct_answer):
        still_guessing = True
        attempt = 0
        while still_guessing and attempt < 3:
            user_answer = input(f"{question} ➜ ")
            if user_answer.strip().lower() == correct_answer.lower():
                print("✅ Correct Answer!")
                self.score += 1
                still_guessing = False
            else:
                attempt += 1
                if attempt < 3:
                    print("❌ Wrong answer. Try again.")
                else:
                    print(f"❗ The correct answer was: {correct_answer}")

    def start_quiz(self):
        self.populate_data()
        if not self.data:
            print("No questions available to start the quiz.")
            return

        print("\n🎯 Starting Quiz...")
        questions = list(self.data.items())
        random.shuffle(questions)
        for question, answer in questions:
            self.ask_question(question, answer)

        print(f"\n🏁 Quiz Finished! Your Score: {self.score}/{len(self.data)}")


def main():
    quiz = Quiz()
    quiz.start_quiz()

if __name__ == "__main__":
    main()
