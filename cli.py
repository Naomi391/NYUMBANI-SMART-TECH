import sqlite3
from colorama import Fore, Style
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
            return 'Landlord', email
    return None


def tenant_login():
    email = input("Enter tenant's email: ")
    password = input("Enter tenant's password: ")
    tenants_data = get_tenants_data()
    for tenant in tenants_data:
        if tenant[2] == email and tenant[3] == password:
            return 'Tenant', email
    
    return None

def add_tenant(TenantID, Name, Email, Phone, Address, AgentID):
        conn = sqlite3.connect('realestate.db')
        cursor = conn.cursor()

        print(Fore.GREEN + "Adding a new tenant: ")
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
    print("9. Go Back")

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

    elif user_input == '9':
        print("Going back to the main menu...")
        return "back"

    else:
        print("Invalid choice. Please try again.")

def landlord_options(landlord_email):
    conn = sqlite3.connect('realestate.db')
    cursor = conn.cursor()

    print("Landlord options:")
    print("0. Exit")
    print("1. Display agents")
    print("2. Display leased apartments")
    print("3. Display the rents paid")
    print("4. Display the eviction notices")
    print("5. Go Back")

    user_input = input("Enter your choice: ")
    
    if user_input == '0':
        print("Exiting the program. Goodbye!")
        exit()

    elif user_input == '1':
        cursor.execute("SELECT Agents.* FROM Agents INNER JOIN Landlords ON Agents.AgentID = Landlords.AgentID WHERE Landlords.Email = ?", (landlord_email,))
        agents_data = cursor.fetchall()

        if agents_data: 
            print("List of my Agents:")
            for agent in agents_data:
                print(f"Agent ID: {agent[0]}, Name: {agent[1]}, Email: {agent[2]}, Phone: {agent[3]}, Agency: {agent[4]}")
        else:
            print("No agents found.")

    elif user_input == '2':
    # Query to retrieve leased apartments belonging to the logged-in landlord using INNER JOIN
        cursor.execute("SELECT Leases.*, Properties.* FROM Leases INNER JOIN Properties ON Leases.PropertyID = Properties.PropertyID INNER JOIN Landlords ON Properties.LandlordID = Landlords.LandlordID WHERE Landlords.Email = ?", (landlord_email,))
        leased_apartments_data = cursor.fetchall()

        if leased_apartments_data:
            print("List of My Leased Apartments:")
            for apartment in leased_apartments_data:
                print(f"Lease ID: {apartment[0]}, Tenant ID: {apartment[1]}, Property ID: {apartment[2]}, Lease Start Date: {apartment[3]}, Lease End Date: {apartment[4]}, Rent Amount: {apartment[5]}, Security Deposit: {apartment[6]}, Tenant Name: {apartment[7]}, Property Name: {apartment[9]}, Address: {apartment[10]}")
        else:
            print("No leased apartments found.")

        
    elif user_input == '3':
        cursor.execute("SELECT RentPayments.* FROM RentPayments INNER JOIN Leases ON RentPayments.LeaseID = Leases.LeaseID INNER JOIN Properties ON Leases.PropertyID = Properties.PropertyID INNER JOIN Landlords ON Properties.LandlordID = Landlords.LandlordID WHERE Landlords.Email = ?", (landlord_email,))
        rent_payments_data = cursor.fetchall()

        if rent_payments_data:
            print("List of Rent Payments:")
            for payment in rent_payments_data:
                print(f"Payment ID: {payment[0]}, Property ID: {payment[1]}, Tenant Name: {payment[5]}, Amount: {payment[3]}, Payment Date: {payment[2]}, Payment Method: {payment[4]}")
        else:
            print("No rent payments found.")

    elif user_input == '4':
        cursor.execute("SELECT EvictionNotices.* FROM EvictionNotices INNER JOIN Leases ON EvictionNotices.LeaseID = Leases.LeaseID INNER JOIN Properties ON Leases.PropertyID = Properties.PropertyID INNER JOIN Landlords ON Properties.LandlordID = Landlords.LandlordID WHERE Landlords.Email = ?", (landlord_email,))
        eviction_notices_data = cursor.fetchall()

        if eviction_notices_data:
            print("List of Eviction Notices:")
            for notice in eviction_notices_data:
                print(f"Notice ID: {notice[0]}, Property ID: {notice[1]}, Tenant Name: {notice[6]}, Notice Date: {notice[3]}, Message: {notice[4]}")
        else:
            print("No eviction notices found.")

    elif user_input == '5':
        print("Going back to the main menu...")
        return "back"
    
    else:
        print("Invalid choice. Please try again.")

    cursor.close()
    conn.close()

def tenant_options(logged_in_tenant_email):
    conn = sqlite3.connect('realestate.db')
    cursor = conn.cursor()

    print("Tenant options:")
    print("0. Exit")
    print("1. Display the rents paid")
    print("2. Display the eviction notices")
    print("3. Go Back")

    user_input = input("Enter your choice: ")

    if user_input == '0':
        print("Exiting the program. Goodbye!")
        exit()

    elif user_input == '1':
        cursor.execute("SELECT RentPayments.* FROM RentPayments INNER JOIN Tenants ON RentPayments.TenantName = Tenants.Name WHERE Tenants.Email = ?", (logged_in_tenant_email,))
        rent_payments_data = cursor.fetchall()

        if rent_payments_data:
            print("List of My Latest Rent Payment:")
            for payment in rent_payments_data:
                print(f"Payment ID: {payment[0]}, Property ID: {payment[1]}, Tenant Name: {payment[5]}, Amount: {payment[3]}, Payment Date: {payment[2]}, Payment Method: {payment[4]}")
        else:
            print("No rent payments found.")

    elif user_input == '2':
        cursor.execute("SELECT EvictionNotices.* FROM EvictionNotices INNER JOIN Tenants ON EvictionNotices.TenantName = Tenants.Name WHERE Tenants.Email = ?", (logged_in_tenant_email,))
        
        eviction_notices_data = cursor.fetchall()

        if eviction_notices_data:
            print("List of Eviction Notices:")
            for notice in eviction_notices_data:
                print(f"Notice ID: {notice[0]}, Property ID: {notice[1]}, Tenant Name: {notice[6]}, Notice Date: {notice[3]}, Message: {notice[4]}")
        else:
            print("No eviction notices found.")

    elif user_input == '3':
        print("Going back to the main menu...")
        return "back"
    
    else:
        print("Invalid choice. Please try again.")

    cursor.close()
    conn.close()



def main():
    print("Welcome to Nyumbani Smart Tech CLI")
    print("Please select an option:")
    print("0. Exit")
    print("1. Agent login")
    print("2. Landlord login")
    print("3. Tenant login")
    print("4. Go Back")

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
        login_result = landlord_login()
        if login_result:
            user_role, landlord_email = login_result
            print("Landlord login successful. Proceeding to landlord options...")
            landlord_options(landlord_email)
        else:
            print("Landlord login failed. Please try again or register as a landlord.")
    elif user_input == '3':
        login_result = tenant_login()
        if login_result:
            user_role, logged_in_tenant_email = login_result
            print("Tenant login successful. Proceeding to tenant options...")
            tenant_options(logged_in_tenant_email)
        else:
            print("Tenant login failed. Please try again or register as a tenant.")

    elif user_input == '4':
        print("Going back to the main menu...")
        return "back"
    
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()