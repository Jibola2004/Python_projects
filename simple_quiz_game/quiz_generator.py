import csv

class QuizGenerator:
    def __init__(self, filename='quiz_data.csv'):
        self.filename = filename
        self.quiz_data = {}

    def add_question(self, question, answer):
        self.quiz_data[question] = answer

    def input_questions(self):
        print("📋 Enter quiz questions and answers (type 'exit' to stop):")
        while True:
            question = input("\nEnter quiz question: ").strip()
            if question.lower() == 'exit':
                break
            answer = input("Enter answer: ").strip()
            self.add_question(question, answer)

    def save_to_csv(self):
        with open(self.filename, 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            for question, answer in self.quiz_data.items():
                writer.writerow([question, answer])
        print(f"\n✅ Quiz data saved to '{self.filename}'")

    def load_from_csv(self):
        self.quiz_data.clear()
        try:
            with open(self.filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.quiz_data[row['Question']] = row['Answer']
            print(f"\n📖 Loaded {len(self.quiz_data)} questions from '{self.filename}'")
        except FileNotFoundError:
            print(f"\n⚠️ File '{self.filename}' not found.")

    def display_quiz(self):
        if not self.quiz_data:
            print("⚠️ No quiz data available.")
        for question, answer in self.quiz_data.items():
            print(f"\n❓ {question}\n✅ Answer: {answer}")


# === Driver code ===
def main():
    quiz = QuizGenerator()

    while True:
        print("\n🎯 Quiz Generator")
        print("1. Add new quiz questions")
        print("2. Load quiz data from CSV")
        print("3. Quit")

        choice = input("Choose an option: ").strip()

        if choice == '1':
            quiz.input_questions()
            quiz.save_to_csv()
        elif choice == '2':
            quiz.load_from_csv()
            quiz.display_quiz()
        elif choice == "3":
            print('Thank you!!!')
            break
        else:
            print("❌ Invalid option. Try again.")


if __name__ == "__main__":
    main()
