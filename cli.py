# Import necessary modules
import sqlite3
from helpers import get_agents_data, get_landlords_data, get_tenants_data, get_properties_data, get_leased_properties_data, get_rent_payments_data, get_eviction_notices_data

def agent_login():
    email = input("Enter agent's email: ")
    password = input("Enter agent's password: ")
    agents_data = get_agents_data()
    for agent in agents_data:
        if agent[2] == email and agent[3] == password:
            return 'Agent'
    return None

def landlord_login():
    email = input("Enter landlord's email: ")
    password = input("Enter landlord's password: ")
    landlords_data = get_landlords_data()
    for landlord in landlords_data:
        if landlord[2] == email and landlord[3] == password:
            return 'Landlord'
    return None

def tenant_login():
    email = input("Enter tenant's email: ")
    password = input("Enter tenant's password: ")
    
    tenants_data = get_tenants_data()
    for tenant in tenants_data:
        if tenant[2] == email and tenant[3] == password:
            return 'Tenant'
    
    return None

def main():
    print("Welcome to Nyumbani Smart Tech CLI")
    print("Please select an option:")
    print("1. Agent login")
    print("2. Landlord login")
    print("3. Tenant login")

    user_input = input("Enter your choice: ")
    
    if user_input == '1':
        user_role = agent_login()
        if user_role == 'Agent':
            print("Agent login successful. Proceeding to agent options...")
            # Call agent-specific functions or display menu for agents
        else:
            print("Agent login failed. Please try again or register as an agent.")
    elif user_input == '2':
        user_role = landlord_login()
        if user_role == 'Landlord':
            print("Landlord login successful. Proceeding to landlord options...")
            # Call landlord-specific functions or display menu for landlords
        else:
            print("Landlord login failed. Please try again or register as a landlord.")
    elif user_input == '3':
        user_role = tenant_login()
        if user_role == 'Tenant':
            print("Tenant login successful. Proceeding to tenant options...")
            # Call tenant-specific functions or display menu for tenants
        else:
            print("Tenant login failed. Please try again or register as a tenant.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()