import matplotlib.pyplot as plt
from file_handler import load_list
def display_bar_graph():
    patients = load_list("patients.txt")
    doctors = load_list("doctors.txt")
    appointments = load_list("appointments.txt")
    bills = load_list("bills.txt")
    categories = ["Patients", "Doctors", "Appointments", "Bills"]
    values = [
        len(patients),
        len(doctors),
        len(appointments),
        len(bills)
    ]
    plt.bar(categories, values)
    plt.title("Hospital Data - Bar Graph")
    plt.xlabel("Category")
    plt.ylabel("Count")
    for i in range(len(values)):
        plt.text(i, values[i], str(values[i]), ha='center', va='bottom')
    plt.show()
def display_line_graph():
    patients = load_list("patients.txt")
    doctors = load_list("doctors.txt")
    appointments = load_list("appointments.txt")
    bills = load_list("bills.txt")
    x = ["Patients", "Doctors", "Appointments", "Bills"]
    y = [
        len(patients),
        len(doctors),
        len(appointments),
        len(bills)
    ]
    plt.plot(x, y, marker='o')
    plt.title("Hospital Data - Line Graph")
    plt.xlabel("Category")
    plt.ylabel("Count")
    plt.grid(True)
    for i in range(len(y)):
        plt.text(x[i], y[i], str(y[i]), ha='center', va='bottom')
    plt.show()
def display_graph_menu():
    while True:
        print("""
===== GRAPH MENU =====
1. Bar Graph (Overview)
2. Line Graph (Trend)
3. Back to Main Menu
""")
        choice = input("Enter choice: ")

        if choice == "1":
            display_bar_graph()
        elif choice == "2":
            display_line_graph()
        elif choice == "3":
            break
        else:
            print("Invalid choice\n")
display_graph_menu()
