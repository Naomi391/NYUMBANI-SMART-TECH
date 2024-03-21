# Import necessary modules
from helpers import get_agents_data, get_landlords_data, get_properties_data, get_leased_properties_data, get_rent_payments_data, get_eviction_notices_data

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
        
def display_leased_properties():
    leased_properties = get_leased_properties_data()  
    if leased_properties:
        print("Leased Properties:")
        for property in leased_properties:
            print(f"Lease ID: {property[0]}, Tenant ID: {property[1]}, Tenant Name: {property[7]}, Property ID: {property[2]}, Lease Start Date: {property[3]}, Lease End Date: {property[4]}, Rent Amount: {property[5]}, Security Deposit: {property[6]}")
    else:
        print("No leased properties found.")

def display_paid_rents():
    rent_payments_data = get_rent_payments_data()
    if rent_payments_data:
        print("Paid Rents:")
        for payment in rent_payments_data:
            print(f"Payment ID: {payment[0]}, Lease ID: {payment[1]}, Tenant Name: {payment[5]}, Payment Date: {payment[2]}, Amount Paid: {payment[3]}, Payment Method: {payment[4]}")
    else:
        print("No rent payments found.")
        

def display_eviction_notices():
    eviction_notices_data = get_eviction_notices_data()
    if eviction_notices_data:
        print("Eviction Notices:")
        for notice in eviction_notices_data:
            print(f"{notice[6]}, you have been served an eviction notice.")
            print(f"Notice ID: {notice[0]}, Tenant ID: {notice[1]}, Tenant Name: {notice[6]}, Lease ID: {notice[2]}, Notice Date: {notice[3]}, Message: {notice[4]}, Status: {notice[5]}")
    else:
        print("No eviction notices found.")

        
def main():
    # Your CLI menu code goes here
    print("Welcome to Nyumbani Smart Tech CLI")
    print("Please select an option:")
    print("1. Display agents")
    print("2. Display landlords")
    print("3. Display properties")
    print("4. Display leased apartments")
    print("5. Display the rents paid")
    print("6. Display the eviction notices")
    print("7. Other options...")
    

    user_input = input("Enter your choice: ")
    
    if user_input == '1':
        display_agents()
    elif user_input == '2':
        display_landlords()
    elif user_input == '3':
        display_properties()
    elif user_input == '4':
        display_leased_properties()
    elif user_input == '5':
        display_paid_rents()
    elif user_input == '6':
        display_eviction_notices()
    elif user_input == '7':
        # Add other options...
        pass
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



