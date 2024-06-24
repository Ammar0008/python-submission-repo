class StudentGrades:
    def __init__(self):
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def calculate_gpa(self, average):
        if average >= 90:
            return 4.0
        elif average >= 80:
            return 3.0
        elif average >= 70:
            return 2.0
        elif average >= 60:
            return 1.0
        else:
            return 0.0

    def determine_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def display_overall_grade(self):
        average = self.calculate_average()
        gpa = self.calculate_gpa(average)
        letter_grade = self.determine_letter_grade(average)

        print(f"Average Grade: {average:.2f}")
        print(f"GPA: {gpa:.1f}")
        print(f"Letter Grade: {letter_grade}")

if __name__ == "__main__":
    student_grades = StudentGrades()

    while True:
        subject = input("Enter subject (or 'done' to finish): ")
        if subject.lower() == 'done':
            break
        grade = float(input(f"Enter grade for {subject}: "))
        student_grades.add_grade(grade)

    student_grades.display_overall_grade()
