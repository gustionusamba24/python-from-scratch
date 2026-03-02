from na45_csv.main_2 import prepare_csv, write_data, read_data, delete_data


def control_flow():
    while True:
        print("Choose mode:")
        print("1. Write data")
        print("2. Read data")
        print("3. Delete by row")
        print("4. Exit")

        mode = input("Choice (1/2/3/4): ")
        if mode == "1":
            name = input("Name: ")
            email = input("Email: ")
            phone = input("Phone: ")
            write_data(name, email, phone)
        elif mode == "2":
            read_data()
        elif mode == "3":
            row_data = int(input("Row index: "))
            delete_data(row_data)
        elif mode == "4":
            break
        else:
            print("Invalid mode")


def main():
    prepare_csv()
    control_flow()


if __name__ == "__main__":
    main()
