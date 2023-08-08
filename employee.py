def main():
    employee = get_employee()
    print(f"{employee['name']} from {employee['department']}")

def get_employee():
    employee = {}
    employee['name'] = input("Name: ")
    employee['department'] = input("Department: ")
    return employee

if __name__ == "__main__":
    main()