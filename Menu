import DSR as d
loan_calculations = []

while True:
    print("1. Calculate new loan")
    print("2. Display previous calculations")
    print("3. Edit Record")
    print("4. Exit")

    option = d.validate_input(input("Enter your choice: "), int)

    if option == 1:
        # Calculate new loan
        loan_calculations.append(d.calculate_new_loan(loan_calculations))
        print("Loan calculation successfully added.")

    elif option == 2:
        # View previous calculations
        d.view_previous_calculations(loan_calculations)

    elif option == 3:
        # Modify DSR threshold
        d.modify_dsr_threshold(loan_calculations)

    elif option == 4:
        # Delete previous calculations
        d.delete_specific_loan_calculation(loan_calculations)

    elif option == 5:
        # Exit
        print("Thank you for using the Housing Loan Calculator.")
        break

    else:
        print("Invalid option. Please enter a valid choice.")