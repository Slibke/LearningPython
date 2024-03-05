def maladiec(mldc_arg):
    print("Maladiec, starai " +mldc_arg)

name = input("Enter your name: ")
print(f"Welcome to the adventure, {name}!")

choice = input("Do you want to go (left) or (right)? ").lower()
if choice == "left":
    maladiec(name)
    print("You go left and encounter a talking cat...")
elif choice == "right":
    print("You go right and find a hidden treasure chest...")
else:
    print("Invalid choice. Try again.")