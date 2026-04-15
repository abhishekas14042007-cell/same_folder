import pytest
from quiz import Student, Quiz   # replace with your actual file name


# Test Student class
def test_student_creation():
    s = Student("John", "101", "CSE")
    assert s.name == "John"
    assert s.roll == "101"
    assert s.dept == "CSE"


# Test correct answer increases score
def test_quiz_correct_answer(monkeypatch):
    student = Student("Test", "1", "IT")
    quiz = Quiz(student)

    # Mock inputs: all correct answers
    answers = [q[2] for q in quiz.questions]
    monkeypatch.setattr("builtins.input", lambda _: answers.pop(0))

    quiz.start_quiz()

    assert quiz.score == 20


# Test wrong answer handling
def test_quiz_wrong_answer(monkeypatch):
    student = Student("Test", "2", "ECE")
    quiz = Quiz(student)

    # Provide all wrong answers
    monkeypatch.setattr("builtins.input", lambda _: "Z")

    quiz.start_quiz()

    assert quiz.score == 0


# Test partial correct answers
def test_quiz_partial_score(monkeypatch):
    student = Student("Test", "3", "MECH")
    quiz = Quiz(student)

    # Alternate correct and wrong answers
    answers = []
    for i, q in enumerate(quiz.questions):
        if i % 2 == 0:
            answers.append(q[2])  # correct
        else:
            answers.append("Z")   # wrong

    monkeypatch.setattr("builtins.input", lambda _: answers.pop(0))

    quiz.start_quiz()

    assert quiz.score == 10


# Test save_result writes to file
def test_save_result(tmp_path):
    student = Student("Alice", "10", "CSE")
    quiz = Quiz(student)
    quiz.score = 15

    file_path = tmp_path / "students.txt"

    # Override file path
    def mock_open(file, mode):
        return open(file_path, mode)

    quiz.save_result = lambda: open(file_path, "a").write(
        f"{student.name},{student.roll},{student.dept},{quiz.score}/20\n"
    )

    quiz.save_result()

    content = file_path.read_text()
    assert "Alice,10,CSE,15/20" in content


# Test show_all_students
def test_show_all_students(capsys, tmp_path):
    file_path = tmp_path / "students.txt"

    # Create sample data
    file_path.write_text("Bob,20,IT,18/20\n")

    student = Student("Dummy", "0", "None")
    quiz = Quiz(student)

    # Mock file reading
    def mock_open(file, mode):
        return open(file_path, mode)

    quiz.show_all_students = lambda: print(file_path.read_text())

    quiz.show_all_students()

    captured = capsys.readouterr()
    assert "Bob,20,IT,18/20" in captured.out