import sys

class Student:
    def __init__(self, name, roll, dept):
        self.name = name
        self.roll = roll
        self.dept = dept


class Quiz:
    def __init__(self, student):
        self.student = student
        self.score = 0

        self.questions = [
            ("1. Capital of France?", ["A. Berlin", "B. Paris", "C. Rome", "D. Madrid"], "B"),
            ("2. Who developed Python?", ["A. Guido van Rossum", "B. James Gosling", "C. Dennis Ritchie", "D. Bjarne Stroustrup"], "A"),
            ("3. Red planet?", ["A. Earth", "B. Mars", "C. Venus", "D. Jupiter"], "B"),
            ("4. CPU stands for?", ["A. Central Processing Unit", "B. Control Processing Unit", "C. Computer Personal Unit", "D. Central Program Unit"], "A"),
            ("5. Square root of 64?", ["A. 6", "B. 7", "C. 8", "D. 9"], "C"),
            ("6. Father of Computer?", ["A. Charles Babbage", "B. Alan Turing", "C. Bill Gates", "D. Steve Jobs"], "A"),
            ("7. Gas used in photosynthesis?", ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"], "C"),
            ("8. World War II ended in?", ["A. 1942", "B. 1945", "C. 1948", "D. 1950"], "B"),
            ("9. FIFO data structure?", ["A. Stack", "B. Queue", "C. Tree", "D. Graph"], "B"),
            ("10. Symbol for Gold?", ["A. Au", "B. Ag", "C. Gd", "D. Go"], "A"),
            ("11. Windows OS developed by?", ["A. Apple", "B. Google", "C. Microsoft", "D. IBM"], "C"),
            ("12. 15 × 6 ?", ["A. 80", "B. 85", "C. 90", "D. 95"], "C"),
            ("13. Largest ocean?", ["A. Indian", "B. Pacific", "C. Atlantic", "D. Arctic"], "B"),
            ("14. RAM stands for?", ["A. Random Access Memory", "B. Read Access Memory", "C. Run Access Memory", "D. Real Access Memory"], "A"),
            ("15. Smallest prime number?", ["A. 0", "B. 1", "C. 2", "D. 3"], "C"),
            ("16. HTML stands for?", ["A. Hyper Text Markup Language", "B. High Text Machine Language", "C. Hyper Tool Multi Language", "D. None"], "A"),
            ("17. Python is?", ["A. Programming Language", "B. Snake", "C. Movie", "D. Game"], "A"),
            ("18. 10 + 20 ?", ["A. 25", "B. 30", "C. 35", "D. 40"], "B"),
            ("19. Largest planet?", ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"], "C"),
            ("20. Input device?", ["A. Monitor", "B. Printer", "C. Keyboard", "D. Speaker"], "C")
        ]

    def start_quiz(self):

        for q, options, ans in self.questions:
            print("\n" + q)
            for opt in options:
                print(opt)

            user = input("Enter answer (A/B/C/D): ").upper()

            if user == ans:
                print("Correct!")
                self.score += 1
            else:
                for opt in options:
                    if opt.startswith(ans):
                        correct = opt
                print("Wrong!")
                print("Correct Answer:", correct)

        self.show_result()

    def show_result(self):

        print("\n===== RESULT =====")
        print("Name:", self.student.name)
        print("Roll:", self.student.roll)
        print("Department:", self.student.dept)
        print("Marks:", self.score, "/20")

        self.save_result()
        self.show_all_students()

    def save_result(self):

        with open("students.txt", "a") as file:
            file.write(
                f"{self.student.name},{self.student.roll},{self.student.dept},{self.score}/20\n"
            )

    def show_all_students(self):

        print("\n===== ALL STUDENT RECORDS =====")

        try:
            with open("students.txt", "r") as file:
                for line in file:
                    name, roll, dept, marks = line.strip().split(",")

                    print("Name:", name,
                          "| Roll:", roll,
                          "| Dept:", dept,
                          "| Marks:", marks)

        except FileNotFoundError:
            print("No records found.")


def main():

    while True:

        name = input("\nEnter Student Name: ")
        roll = input("Enter Roll Number: ")
        dept = input("Enter Department: ")

        student = Student(name, roll, dept)

        quiz = Quiz(student)
        quiz.start_quiz()

        retry = input("\nRetry quiz for same student? (yes/no): ").lower()
        if retry == "yes":
            quiz = Quiz(student)
            quiz.start_quiz()

        another = input("\nAdd another student? (yes/no): ").lower()
        if another != "yes":
            print("\nThank you for using Quiz Application!")
            sys.exit()


if __name__ == "__main__":
    main()
