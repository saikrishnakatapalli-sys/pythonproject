from file_handler import save_list

def add_doctor(doctors):
    did = input("Doctor ID: ")
    name = input("Name: ")
    dept = input("Department: ")
    doctors.append([did, name, dept])
    save_list("doctors.txt", doctors)
    print("Doctor added\n")

def display_doctors(doctors):
    print("\nDOCTOR LIST")
    if not doctors:
        print("No doctors\n")
        return
    for d in doctors:
        print("ID:", d[0], "Name:", d[1], "Department:", d[2])
    print()
