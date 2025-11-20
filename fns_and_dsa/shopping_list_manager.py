# shopping_list_manager.py

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit\n")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.\n")

        elif choice == '2':
            item = input("Enter item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from your shopping list.\n")
            else:
                print(f"'{item}' is not in the shopping list.\n")

        elif choice == '3':
            print("\nYour Shopping List:")
            if len(shopping_list) == 0:
                print("(Empty)\n")
            else:
                for i, item in enumerate(shopping_list, start=1):
                    print(f"{i}. {item}")
                print()

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

