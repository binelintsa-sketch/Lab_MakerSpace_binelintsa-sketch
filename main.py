from models import Member, Equipment, Loan
from database import init_db

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
    print("\n--- List All Members ---")
    try:
        members = Member.get_all()
        if not members:
            print("No members found in database.")
            return
        for m in members:
            print(f"ID: {m.member_id} | Name: {m.name} | Email: {m.email} | Phone: {m.phone or 'N/A'}")
    except Exception as e:
        print(f"Error retrieving members: {e}")

def add_equipment_ui():
    print("\n--- Add New Equipment ---")
<<<<<<< HEAD
    name = input("Enter Equipment Name: ").strip()
    category = input("Enter Category: ").strip()

    if not name or not category:
        print("Error: Name and Category are required.")
        return

    try:
        item = Equipment(name=name, category=category)
        eq_id = item.save()
        print(f"Equipment created successfully with ID: {eq_id}")
=======
    title = input("Enter Equipment Title: ").strip()
    category = input("Enter Category: ").strip()

    if not title:
        print("Error: Title is required.")
        return

    try:
        item = Equipment(title=title, category=category)
        item_id = item.save()
        print(f"Equipment added successfully with ID: {item_id}")
>>>>>>> main.py
    except Exception as e:
        print(f"Error saving equipment: {e}")

def list_available_equipment_ui():
    print("\n--- Available Equipment ---")
<<<<<<< HEAD
    items = Equipment.get_available()
    if not items:
        print("No available equipment found.")
        return

    for item in items:
        print(
            f"ID: {item.equipment_id} | Name: {item.name} | Category: {item.category}"
        )

=======
    try:
        items = Equipment.get_available()
        if not items:
            print("No equipment currently available.")
            return
        for item in items:
            print(f"ID: {item.equipment_id} | Title: {item.title} | Category: {item.category}")
    except Exception as e:
        print(f"Error listing equipment: {e}")
>>>>>>> main.py

def checkout_equipment_ui():
    print("\n--- Checkout Equipment ---")
    try:
        member_id = int(input("Enter Member ID: ").strip())
        equipment_id = int(input("Enter Equipment ID: ").strip())
        
        loan = Loan(member_id=member_id, equipment_id=equipment_id)
        loan_id = loan.create_loan()
        print(f"Equipment {equipment_id} checked out successfully to Member {member_id}. Loan ID: {loan_id}")
    except ValueError:
        print("Error: Member ID and Equipment ID must be numbers.")
    except Exception as e:
        print(f"Error checking out equipment: {e}")

def return_equipment_ui():
    print("\n--- Return Equipment ---")
    try:
        equipment_id = int(input("Enter Equipment ID to Return: ").strip())
        if Loan.return_loan(equipment_id):
            print(f"Equipment {equipment_id} returned successfully.")
        else:
            print(f"No active loan found for Equipment ID {equipment_id}.")
    except ValueError:
        print("Error: Equipment ID must be a number.")
    except Exception as e:
        print(f"Error returning equipment: {e}")

def delete_member_ui():
    print("\n--- Delete Member ---")
    try:
        member_id = int(input("Enter Member ID to delete: ").strip())
        if Member.delete(member_id):
            print(f"Member {member_id} and associated loans deleted successfully.")
        else:
            print(f"No member found with ID {member_id}.")
    except ValueError:
        print("Error: Please enter a valid numerical ID.")
    except Exception as e:
        print(f"Error deleting member: {e}")

def main():
    init_db()  # Ensures tables exist
    while True:
        print("\n=============================================")
        print("   CAMPUS MAKERSPACE CHECKOUT SYSTEM CLI")
        print("=============================================")
        print("1. Add New Member")
        print("2. List All Members")
        print("3. Add New Equipment")
        print("4. List Available Equipment")
        print("5. Checkout Equipment")
        print("6. Return Equipment")
        print("7. Delete Member")
        print("8. Exit")
        print("=============================================")
        
        choice = input("Select an option (1-8): ").strip()

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
            delete_member_ui()
        elif choice == "8":
            print("\nThank you for using the MakerSpace Checkout System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

if __name__ == "__main__":
    main()