# Import necessary modules
from helpers import get_agents_data, get_landlords_data, get_properties_data

# Define your functions here
def display_agents():
    agents_data = get_agents_data()
    for agent in agents_data:
        print(f"Agent ID: {agent[0]}, Name: {agent[1]}, Email: {agent[2]}, Phone: {agent[3]}, Agency: {agent[4]}")

def display_landlords():
    landlords_data = get_landlords_data()
    for landlord in landlords_data:
        print(f"Landlord ID: {landlord[0]}, Name: {landlord[1]}, Email: {landlord[2]}, Phone: {landlord[3]}, Address: {landlord[4]}, Agent ID: {landlord[5]}")

def display_properties():
    properties_data = get_properties_data()
    for property in properties_data:
        print(f"Property ID: {property[0]}, Name: {property[1]}, Address: {property[2]}, Landlord ID: {property[3]}, Landlord Name:{property[4]}")
        
def main():
    # Your CLI menu code goes here
    print("Welcome to Nyumbani Smart Tech CLI")
    print("Please select an option:")
    print("1. Display agents")
    print("2. Display landlords")
    print("3. Display properties")
    print("4. Other options...")

    user_input = input("Enter your choice: ")
    
    if user_input == '1':
        display_agents()
    elif user_input == '2':
        display_landlords()
    elif user_input == '3':
        display_properties()
    elif user_input == '4':
        # Add other options...
        pass
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
