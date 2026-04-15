from file_handler import save_list

def add_appointment(appointments, patients, doctors):
    pid = input("Enter Patient ID: ")
    if not any(p[0] == pid for p in patients):
        print("Patient not found\n")
        return

    did = input("Doctor ID: ")
    if not any(d[0] == did for d in doctors):
        print("Doctor not found\n")
        return

    date = input("Date: ")
    appointments.append([pid, did, date])
    save_list("appointments.txt", appointments)
    print("Appointment booked\n")

def display_appointments(appointments):
    print("\nAPPOINTMENTS")
    if not appointments:
        print("No appointments\n")
        return
    for a in appointments:
        print("PID:", a[0], "DID:", a[1], "Date:", a[2])
    print()

def discharge_patient(patients, appointments):
    pid = input("Enter Patient ID: ")

    new_appointments = [a for a in appointments if a[0] != pid]
    if len(new_appointments) == len(appointments):
        print("Patient not admitted\n")
        return patients, appointments

    save_list("appointments.txt", new_appointments)

    new_patients = [p for p in patients if p[0] != pid]
    save_list("patients.txt", new_patients)

    print("Patient discharged\n")
    return new_patients, new_appointments
