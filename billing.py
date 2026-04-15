from file_handler import save_list

def add_bill(bills):
    bill_id = input("Bill ID: ")
    pid = input("Patient ID: ")
    room = float(input("Room Charge: "))
    doc = float(input("Doctor Fee: "))
    med = float(input("Medicine Cost: "))

    total = room + doc + med
    bills.append([bill_id, pid, str(room), str(doc), str(med), str(total)])

    save_list("bills.txt", bills)
    print("Bill generated\n")

def display_bills(bills):
    print("\nBILL LIST")
    if not bills:
        print("No bills\n")
        return
    for b in bills:
        print("Bill:", b[0], "PID:", b[1], "Total:", b[5])
    print()
