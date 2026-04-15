from file_handler import create_file, load_list
from patient import *
from doctor import *
from appointment import *
from billing import *

# Create data files
create_file("patients.txt")
create_file("doctors.txt")
create_file("appointments.txt")
create_file("bills.txt")

# Load data
patients = load_list("patients.txt")
doctors = load_list("doctors.txt")
appointments = load_list("appointments.txt")
bills = load_list("bills.txt")

print("======HOSPITAL MANAGEMENT SYSTEM======")

while True:
    print("""
1. Add Patient
2. Display Patients
3. Search Patient
4. Update Patient
5. Delete Patient
6. Add Doctor
7. Display Doctors
8. Book Appointment
9. Display Appointments
10. Discharge Patient
11. Add Bill
12. Display Bills
13. Exit
""")
    choice = input("Enter choice: ")

    if choice == "1": add_patient(patients)
    elif choice == "2": display_patients(patients)
    elif choice == "3": search_patient(patients)
    elif choice == "4": update_patient(patients)
    elif choice == "5": patients = delete_patient(patients)
    elif choice == "6": add_doctor(doctors)
    elif choice == "7": display_doctors(doctors)
    elif choice == "8": add_appointment(appointments, patients, doctors)
    elif choice == "9": display_appointments(appointments)
    elif choice == "10": patients, appointments = discharge_patient(patients, appointments)
    elif choice == "11": add_bill(bills)
    elif choice == "12": display_bills(bills)
    elif choice == "13":
        print("====THE END====")
        break
    else:
        print("Invalid choice\n")
