# _______MARKSHEET PROGRAM______#

from os import system
import os
from collections import Counter

# --- FUNCTION: Display the menu options ---
def menu():
    print("\n______ MARKSHEET MENU ______")
    print("1. Add a grade")
    print("2. Edit a student's grade")
    print("3. Delete a student's grade")
    print("4. View marksheet")
    print("5. Exit")
    print("6. Clear screen")
    print("7. View individual student")  # NEW OPTION


# --- GLOBAL VARIABLES ---
gradeBook = {}
admin_index = 1


# --- FUNCTION: Add new students ---
def addStudents(grade_book):
    global admin_index
    while True:
        name = input("\nEnter student's name (or 'q' to return to menu): ").strip().capitalize()
        if name.lower() == 'q':
            break

        try:
            mtc = int(input("MTC: "))
            sci = int(input("SCI: "))
            eng = int(input("ENG: "))
            sst = int(input("SST: "))

            # Validate marks
            for mark in [mtc, sci, eng, sst]:
                if mark < 0 or mark > 100:
                    print("⚠️ Marks must be between 0 and 100.\n")
                    return

            grade_book[admin_index] = {
                'Name': name,
                'MTC': mtc,
                'SCI': sci,
                'ENG': eng,
                'SST': sst
            }
            print(f"✅ Student {name} added successfully with Admin No: {admin_index:02}")
            admin_index += 1
            return grade_book

        except ValueError:
            print("⚠️ Please enter numbers only for marks.")


# --- FUNCTION: Delete students ---
def deleteStudents(grade_book):
    delete_student = input("Enter Admin No. to delete (or 'q' to cancel): ").strip()
    if delete_student.lower() == 'q':
        return
    try:
        delete_student = int(delete_student)
        if delete_student in grade_book:
            removed = grade_book.pop(delete_student)
            print(f"🗑️ {removed['Name']} (Admin No: {delete_student}) deleted successfully!")
        else:
            print("⚠️ No student found with that Admin No.")
    except ValueError:
        print("⚠️ Invalid input. Enter a number.")


# --- FUNCTION: Edit students ---
def editStudents(grade_book):
    try:
        admin_no = int(input("Enter Admin No. of student to edit: "))
        if admin_no not in grade_book:
            print("⚠️ No student found with that Admin No.")
            return
        student = grade_book[admin_no]
        print(f"Editing {student['Name']}'s marks. Leave blank to keep current value.")

        for subject in ['MTC', 'SCI', 'ENG', 'SST']:
            new_mark = input(f"{subject} ({student[subject]}): ").strip()
            if new_mark:
                try:
                    mark_val = int(new_mark)
                    if 0 <= mark_val <= 100:
                        student[subject] = mark_val
                    else:
                        print("⚠️ Marks must be between 0 and 100.")
                except ValueError:
                    print(f"⚠️ Invalid entry for {subject}, keeping old mark.")
        print(f"✅ {student['Name']}'s marks updated successfully!")
    except ValueError:
        print("⚠️ Invalid input. Enter a valid Admin No.")


# --- FUNCTION: View all students' marks + statistics ---
def viewMarksheet(grade_book):
    if not grade_book:
        print("📄 No students available yet.")
        return

    headers = ["Admin", "Name", "MTC", "SCI", "ENG", "SST", "TOTAL", "AVERAGE"]
    col_widths = [6, 15, 5, 5, 5, 5, 7, 8]

    for i, h in enumerate(headers):
        print(f"{h:<{col_widths[i]}}", end="")
    print("\n" + "-" * sum(col_widths))

    total_mtc = total_sci = total_eng = total_sst = 0
    num_students = len(grade_book)

    # Write CSV
    with open("marksheet.csv", "w") as f:
        f.write(",".join(headers) + "\n")
        for admin, student in grade_book.items():
            total = student['MTC'] + student['SCI'] + student['ENG'] + student['SST']
            avg = total / 4
            print(f"{admin:<6}{student['Name']:<15}{student['MTC']:<5}{student['SCI']:<5}"
                  f"{student['ENG']:<5}{student['SST']:<5}{total:<7}{avg:<8.2f}")
            f.write(f"{admin},{student['Name']},{student['MTC']},{student['SCI']},"
                    f"{student['ENG']},{student['SST']},{total},{avg:.2f}\n")

            total_mtc += student['MTC']
            total_sci += student['SCI']
            total_eng += student['ENG']
            total_sst += student['SST']

        print("-" * sum(col_widths))
        print(f"{'Totals':<21}{total_mtc:<5}{total_sci:<5}{total_eng:<5}{total_sst:<5}")
        print(f"{'Averages':<21}{total_mtc/num_students:<5.1f}{total_sci/num_students:<5.1f}"
              f"{total_eng/num_students:<5.1f}{total_sst/num_students:<5.1f}")

        # Write totals & averages
        f.write("\n")
        f.write(f"TOTALS,,{total_mtc},{total_sci},{total_eng},{total_sst},,\n")
        f.write(f"AVERAGES,,{total_mtc / num_students:.1f},{total_sci / num_students:.1f},"
                f"{total_eng / num_students:.1f},{total_sst / num_students:.1f},,\n")

        # --- NEW: STATISTICS SECTION ---
        marks_data = {
            "MTC": [s["MTC"] for s in grade_book.values()],
            "SCI": [s["SCI"] for s in grade_book.values()],
            "ENG": [s["ENG"] for s in grade_book.values()],
            "SST": [s["SST"] for s in grade_book.values()]
        }

        print("\nSUBJECT STATISTICS")
        print("-" * 50)
        print(f"{'Subject':<10}{'Mode':<10}{'Highest':<10}")
        f.write("\n")
        f.write("SUBJECT STATISTICS")
        f.write("\nSUBJECT,MODE,HIGHEST,LOWEST\n")

        for subject, marks in marks_data.items():
            mode_mark = Counter(marks).most_common(1)[0][0]
            highest = max(marks)
            lowest = min(marks)
            print(f"{subject:<10}{mode_mark:<10}{highest:<10}{lowest:<10}")
            f.write(f"{subject},{mode_mark},{highest},{lowest}\n")



    print("\n Marksheet saved to marksheet.csv successfully!")
    try:
        os.startfile("marksheet.csv")
        print("📂 Opening marksheet.csv in Excel...\n")
    except Exception as e:
        print(f"⚠️ Could not open file automatically: {e}")


# --- FUNCTION: View individual student ---
def viewIndividual(grade_book):
    if not grade_book:
        print("📄 No students available yet.")
        return
    try:
        admin_no = int(input("Enter Admin No. of student to view: "))
        if admin_no not in grade_book:
            print("⚠️ No student found with that Admin No.")
            return

        s = grade_book[admin_no]
        total = s['MTC'] + s['SCI'] + s['ENG'] + s['SST']
        avg = total / 4
        print("\n----- INDIVIDUAL STUDENT REPORT -----")
        print(f"Admin No: {admin_no}")
        print(f"Name: {s['Name']}")
        print(f"MTC: {s['MTC']}")
        print(f"SCI: {s['SCI']}")
        print(f"ENG: {s['ENG']}")
        print(f"SST: {s['SST']}")
        print(f"Total: {total}")
        print(f"Average: {avg:.2f}")
        print("------------------------------------\n")

    except ValueError:
        print("⚠️ Invalid Admin No. entered.")


# --- FUNCTION: Clear the screen ---
def clearScreen():
    system('cls')
    print("🧹 Screen cleared!\n")


# ---------- MAIN PROGRAM LOOP ----------
while True:
    menu()
    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            addStudents(gradeBook)
        elif choice == 2:
            editStudents(gradeBook)
        elif choice == 3:
            deleteStudents(gradeBook)
        elif choice == 4:
            viewMarksheet(gradeBook)
        elif choice == 5:
            print("👋 Exiting... Goodbye!")
            break
        elif choice == 6:
            clearScreen()
        elif choice == 7:
            viewIndividual(gradeBook)
        else:
            print("⚠️ Please enter a valid choice (1–7).")
    except ValueError:
        print("⚠️ Please enter a number between 1 and 7.")
