import sys
from database import create_tables
from models import Equipment, Loan, Member


def display_menu():
    print("\n" + "=" * 45)
    print("   CAMPUS MAKERSPACE CHECKOUT SYSTEM CLI   ")
    print("=" * 45)
    print("1. Add New Member")
    print("2. List All Members")
    print("3. Add New Equipment")
    print("4. List Available Equipment")
    print("5. Checkout Equipment")
    print("6. Return Equipment")
    print("7. Exit")
    print("=" * 45)


def add_member_ui():
    print("\n--- Add New Member ---")
    name = input("Enter Member Name: ").strip()
    email = input("Enter Member Email: ").strip()
    phone = input("Enter Phone Number (optional): ").strip()

    if not name or not email:
        print("Error: Name and Email are required.")
        return

    try:
        member = Member(name=name, email=email, phone=phone)
        member_id = member.save()
        print(f"Member created successfully with ID: {member_id}")
    except Exception as e:
        print(f"Error saving member: {e}")


def list_members_ui():
    print("\n--- Registered Members ---")
    members = Member.get_all()
    if not members:
        print("No members found in the system.")
        return

    for m in members:
        print(
            f"ID: {m.member_id} | Name: {m.name} | Email: {m.email} | Phone: {m.phone}"
        )


def add_equipment_ui():
    print("\n--- Add New Equipment ---")
    name = input("Enter Equipment Name: ").strip()
    category = input("Enter Category: ").strip()

    if not name or not category:
        print("Error: Name and Category are required.")
        return

    try:
        item = Equipment(name=name, category=category)
        eq_id = item.save()
        print(f"Equipment created successfully with ID: {eq_id}")
    except Exception as e:
        print(f"Error saving equipment: {e}")


def list_available_equipment_ui():
    print("\n--- Available Equipment ---")
    items = Equipment.get_available()
    if not items:
        print("No available equipment found.")
        return

    for item in items:
        print(
            f"ID: {item.equipment_id} | Name: {item.name} | Category: {item.category}"
        )


def checkout_equipment_ui():
    print("\n--- Checkout Equipment ---")
    try:
        member_id = int(input("Enter Member ID: ").strip())
        equipment_id = int(input("Enter Equipment ID: ").strip())
    except ValueError:
        print("Error: Member ID and Equipment ID must be integers.")
        return

    try:
        loan = Loan(member_id=member_id, equipment_id=equipment_id)
        loan_id = loan.checkout()
        print(
            f"Equipment checked out successfully! Loan ID: {loan_id} (Date: {loan.loan_date})"
        )
    except Exception as e:
        print(f"Error during checkout: {e}")


def return_equipment_ui():
    print("\n--- Return Equipment ---")
    try:
        loan_id = int(input("Enter Loan ID to return: ").strip())
    except ValueError:
        print("Error: Loan ID must be an integer.")
        return

    success = Loan.return_item(loan_id)
    if success:
        print(f"Loan ID {loan_id} returned successfully!")
    else:
        print(f"Error: Loan ID {loan_id} not found or already returned.")


def main():
    # Ensure database tables exist before starting CLI
    create_tables()

    while True:
        display_menu()
        choice = input("Select an option (1-7): ").strip()

        if choice == "1":
            add_member_ui()
        elif choice == "2":
            list_members_ui()
        elif choice == "3":
            add_equipment_ui()
        elif choice == "4":
            list_available_equipment_ui()
        elif choice == "5":
            checkout_equipment_ui()
        elif choice == "6":
            return_equipment_ui()
        elif choice == "7":
            print("\nThank you for using the MakerSpace Checkout System!")
            sys.exit(0)
        else:
            print("Invalid selection. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()