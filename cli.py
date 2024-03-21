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

def add_tenant(TenantID, Name, Email, Phone, Address, AgentID):
        conn = sqlite3.connect('realestate.db')
        cursor = conn.cursor()

        print("Adding a new tenant:")
        sql = '''INSERT INTO Tenants (TenantID, Name, Email, Phone, Address, AgentID) 
             VALUES (?, ?, ?, ?, ?, ?)'''
        
        cursor.execute(sql, (TenantID, Name, Email, Phone, Address, AgentID))

        conn.commit()
        
        cursor.close()
        conn.close()
        
        print("New tenant added successfully.")

    
def delete_tenant(tenantID):
    conn = sqlite3.connect('realestate.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Tenants WHERE TenantID = ?", (tenantID,))
    existing_tenant = cursor.fetchone()

    if existing_tenant:
        sql = '''DELETE FROM Tenants WHERE TenantID = ?'''

        cursor.execute(sql, (tenantID,))

        conn.commit()
        conn.close()

        print("Tenant deleted successfully.")
    else:
        print("Tenant with ID", tenantID, "has already been deleted.")


def agent_options():
    print("Agent options:")
    print("0. Exit")
    print("1. Display agents")
    print("2. Display landlords")
    print("3. Display properties")
    print("4. Display leased apartments")
    print("5. Display the rents paid")
    print("6. Display the eviction notices")
    print("7. Add a new tenant")
    print("8. Delete a tenant") 

    user_input = input("Enter your choice: ")

    if user_input == '0':
        print("Exiting the program. Goodbye!")
        exit()

    elif user_input == '1':
        agents_data = get_agents_data()
        if agents_data:
            print("List of Agents:")
            for agent in agents_data:
                print(f"Agent ID: {agent[0]}, Name: {agent[1]}, Email: {agent[2]}, Phone: {agent[3]}, Agency: {agent[4]}")
        else:
            print("No agents found.")
    elif user_input == '2':
        landlords_data = get_landlords_data()
        if landlords_data:
            print("List of Landlords:")
            for landlord in landlords_data:
                print(f"Landlord ID: {landlord[0]}, Name: {landlord[1]}, Email: {landlord[2]}, Phone: {landlord[3]}, Agent Name: {landlord[6]}")
        else:
            print("No landlords found.")

    elif user_input == '3':
        properties_data = get_properties_data()
        if properties_data:
            print("List of Properties:")
            for property in properties_data:
                print(f"Property ID: {property[0]},     Name: {property[1]},    Address: {property[2]},     Landlord Name: {property[4]},   Type: {property[5]}")
        else:
            print("No properties found.")
    elif user_input == '4':
        leased_apartments_data = get_leased_properties_data()
        if leased_apartments_data:
            print("List of Leased Apartments:")
            for apartment in leased_apartments_data:
                print(f"Property ID: {apartment[1]}, Lease Start Date: {apartment[3]}, Lease End Date: {apartment[4]}, Rent Amount: {apartment[5]}, Security Deposit: {apartment[6]}, Tenant Name: {apartment[7]}")
        else:
            print("No leased apartments found.")
    elif user_input == '5':
        rent_payments_data = get_rent_payments_data()
        if rent_payments_data:
            print("List of Rent Payments:")
            for payment in rent_payments_data:
                print(f"Payment ID: {payment[0]}, Property ID: {payment[1]}, Tenant Name: {payment[5]}, Amount: {payment[3]}, Payment Date: {payment[2]}, Payment Method: {payment[4]}")
        else:
            print("No rent payments found.")
    elif user_input == '6':
        eviction_notices_data = get_eviction_notices_data()
        if eviction_notices_data:
            print("List of Eviction Notices:")
            for notice in eviction_notices_data:
                print(f"Notice ID: {notice[0]}, Property ID: {notice[1]}, Tenant Name: {notice[6]}, Notice Date: {notice[3]}, Message: {notice[4]}")
        else:
            print("No eviction notices found.")

    elif user_input == '7':
        ID = input("Enter tenant's ID: ")
        name = input("Enter tenant's name: ")
        email = input("Enter tenant's email: ")
        phone = input("Enter tenant's phone: ")
        address = input("Enter tenant's address: ")
        agentID = input("Enter tenant's agent ID: ")

        add_tenant(ID, name, email, phone, address, agentID) 

    elif user_input == '8':  
        tenantID = input("Enter tenant's ID to delete: ")
        delete_tenant(tenantID)

    else:
        print("Invalid choice. Please try again.")

def landlord_options():
    print("Landlord options:")
    print("0. Exit")
    print("1. Display agents")
    print("2. Display leased apartments")
    print("3. Display the rents paid")
    print("4. Display the eviction notices")

    user_input = input("Enter your choice: ")
    
    if user_input == '0':
        print("Exiting the program. Goodbye!")
        exit()

    elif user_input == '1':
        agents_data = get_agents_data()
        if agents_data:
            print("List of Agents:")
            for agent in agents_data:
                print(f"Agent ID: {agent[0]}, Name: {agent[1]}, Email: {agent[2]}, Phone: {agent[3]}, Agency: {agent[4]}")
        else:
            print("No agents found.")

    elif user_input == '2':
        leased_apartments_data = get_leased_properties_data()
        if leased_apartments_data:
            print("List of Leased Apartments:")
            for apartment in leased_apartments_data:
                print(f"Property ID: {apartment[1]}, Lease Start Date: {apartment[3]}, Lease End Date: {apartment[4]}, Rent Amount: {apartment[5]}, Security Deposit: {apartment[6]}, Tenant Name: {apartment[7]}")
        else:
            print("No leased apartments found.")
        
    elif user_input == '3':
        rent_payments_data = get_rent_payments_data()
        if rent_payments_data:
            print("List of Rent Payments:")
            for payment in rent_payments_data:
                print(f"Payment ID: {payment[0]}, Property ID: {payment[1]}, Tenant Name: {payment[5]}, Amount: {payment[3]}, Payment Date: {payment[2]}, Payment Method: {payment[4]}")
        else:
            print("No rent payments found.")

    elif user_input == '4':
        eviction_notices_data = get_eviction_notices_data()
        if eviction_notices_data:
            print("List of Eviction Notices:")
            for notice in eviction_notices_data:
                print(f"Notice ID: {notice[0]}, Property ID: {notice[1]}, Tenant Name: {notice[6]}, Notice Date: {notice[3]}, Message: {notice[4]}")
        else:
            print("No eviction notices found.")
    else:
        print("Invalid choice. Please try again.")

def tenant_options():
    print("Tenant options:")
    print("0. Exit")
    print("1. Display the rents paid")
    print("2. Display the eviction notices")

    user_input = input("Enter your choice: ")

    if user_input == '0':
        print("Exiting the program. Goodbye!")
        exit()

    elif user_input == '1':
        rent_payments_data = get_rent_payments_data()
        if rent_payments_data:
            print("List of Rent Payments:")
            for payment in rent_payments_data:
                print(f"Payment ID: {payment[0]}, Property ID: {payment[1]}, Tenant Name: {payment[5]}, Amount: {payment[3]}, Payment Date: {payment[2]}, Payment Method: {payment[4]}")
        else:
            print("No rent payments found.")

    elif user_input == '2':
        eviction_notices_data = get_eviction_notices_data()
        if eviction_notices_data:
            print("List of Eviction Notices:")
            for notice in eviction_notices_data:
                print(f"Notice ID: {notice[0]}, Property ID: {notice[1]}, Tenant Name: {notice[6]}, Notice Date: {notice[3]}, Message: {notice[4]}")
        else:
            print("No eviction notices found.")
    else:
        print("Invalid choice. Please try again.")



def main():
    print("Welcome to Nyumbani Smart Tech CLI")
    print("Please select an option:")
    print("0. Exit")
    print("1. Agent login")
    print("2. Landlord login")
    print("3. Tenant login")

    user_input = input("Enter your choice: ")
    
    if user_input == '0':
        print("Exiting the program. Goodbye!")
        exit()

    elif user_input == '1':
        user_role = agent_login()
        if user_role == 'Agent':
            print("Agent login successful. Proceeding to agent options...")
            agent_options()
        else:
            print("Agent login failed. Please try again or register as an agent.")
    elif user_input == '2':
        user_role = landlord_login()
        if user_role == 'Landlord':
            print("Landlord login successful. Proceeding to landlord options...")
            landlord_options()
        else:
            print("Landlord login failed. Please try again or register as a landlord.")
    elif user_input == '3':
        user_role = tenant_login()
        if user_role == 'Tenant':
            print("Tenant login successful. Proceeding to tenant options...")
            tenant_options()
        else:
            print("Tenant login failed. Please try again or register as a tenant.")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
