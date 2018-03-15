

student_list = []

def CreateStudent():
    name = input("Please enter the new student's name: ")
    student_data = {
        'name': name,
        'marks': []
    }

    return student_data


def AddMark(student, mark):
    student['marks'].append(mark)


def CalculateAverageMark(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number


def PrintStudentDetails(student):
    print("{}, average mark: {}.".format(student['name'],
                                         CalculateAverageMark(student)))


def PrintStudentList(students):
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        PrintStudentDetails(student)


def Menu():
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")
    while selection != 'q':
        if selection == 'p':
            PrintStudentList(student_list)
        elif selection == 's':
            student_list.append(CreateStudent())
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            AddMark(student, new_mark)

        selection = input("Enter 'p' to print the student list, "
                          "'s' to add a new student, "
                          "'a' to add a mark to a student, "
                          "or 'q' to quit. "
                          "Enter your selection: ")

if __name__ == "__main__":
    Menu()
