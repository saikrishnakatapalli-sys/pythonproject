from file_handler import save_list

def add_patient(patients):
    pid = input("Patient ID: ")
    name = input("Name: ")
    age = input("Age: ")
    disease = input("Disease: ")
    patients.append([pid, name, age, disease])
    save_list("patients.txt", patients)
    print("Patient added\n")

def display_patients(patients):
    print("\nPATIENT LIST")
    if not patients:
        print("No patients\n")
        return
    for p in patients:
        print("ID:", p[0], "Name:", p[1], "Age:", p[2], "Disease:", p[3])
    print()

def search_patient(patients):
    pid = input("Enter Patient ID: ")
    for p in patients:
        if p[0] == pid:
            print("Found:", p, "\n")
            return
    print("Patient not found\n")

def update_patient(patients):
    pid = input("Enter Patient ID: ")
    for i, p in enumerate(patients):
        if p[0] == pid:
            name = input("Name: ")
            age = input("Age: ")
            disease = input("Disease: ")
            patients[i] = [pid, name, age, disease]
            save_list("patients.txt", patients)
            print("Updated\n")
            return
    print("Patient not found\n")

def delete_patient(patients):
    pid = input("Enter Patient ID: ")
    new_list = [p for p in patients if p[0] != pid]
    if len(new_list) == len(patients):
        print("Patient not found\n")
    else:
        save_list("patients.txt", new_list)
        print("Deleted\n")
    return new_list
