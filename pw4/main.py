from input import *
from output import *
from domain import student, course 
def main():
        while True:
            print("\n1. Add students")
            print("2. Add courses")
            print("3. Input marks for a course")
            print("4. Calculate GPA")
            print("5. List students")
            print("6. List courses")
            print("7. Show marks for a course")
            print("8. Exit")
            choice = input("Enter your choice: ")
            if choice == "1":
                add_student()
            elif choice == "2":
                add_course()
            elif choice == "3":
                input_marks()
            elif choice == "4":
                cal_gpa()
            elif choice == "5":
                list_students()
            elif choice == "6":
                list_courses()
            elif choice == "7":
                show_marks()
            elif choice == "8":
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please try again.")
if __name__ == "__main__":
    main()