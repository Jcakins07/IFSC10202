
class Student:
    def __init__(self, firstname, lastname, tnumber, scores):

        self.FirstName = firstname
        self.LastName = lastname
        self.TNumber = tnumber
        self.Grades = scores  

    def RunningAverage(self):
        """Calculates average of non-blank grades."""
        valid_scores = [float(s) for s in self.Grades if s.strip() != ""]
        if len(valid_scores) == 0:
            return 0.0
        return sum(valid_scores) / len(valid_scores)

    def TotalAverage(self):
        """Calculates average treating blanks as zeros."""
        all_scores = [float(s) if s.strip() != "" else 0.0 for s in self.Grades]
        if len(all_scores) == 0:
            return 0.0
        return sum(all_scores) / len(all_scores)

    def LetterGrade(self):
        """Returns letter grade based on TotalAverage."""
        avg = self.TotalAverage()
        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"


def main():
    try:
        
        with open("10.Project Student Scores.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue  

                
                parts = [p.strip() for p in line.split(",")]

                firstname = parts[0]
                lastname = parts[1]
                tnumber = parts[2]
                scores = parts[3:]  #

                
                student = Student(firstname, lastname, tnumber, scores)

                
                print(f"\nStudent: {student.FirstName} {student.LastName} ({student.TNumber})")
                print(f"Running Average: {student.RunningAverage():.2f}")
                print(f"Semester Average: {student.TotalAverage():.2f}")
                print(f"Letter Grade: {student.LetterGrade()}")

    except FileNotFoundError:
        print("Error: '10.Project Student Scores.txt' not found in this directory.")


if __name__ == "__main__":
    main()
