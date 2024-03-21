import sqlite3

def get_agents_data():
    conn = sqlite3.connect('realestate.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Agents")
    agents_data = cursor.fetchall()
    conn.close()
    return agents_data

def get_landlords_data():
    conn = sqlite3.connect('realestate.db')  
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Landlords")
    landlords_data = cursor.fetchall()
    conn.close()
    return landlords_data

def get_properties_data():
    conn = sqlite3.connect('realestate.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Properties")
    properties_data = cursor.fetchall()
    conn.close()
    return properties_data

def get_leased_properties_data():
    conn = sqlite3.connect('realestate.db')  
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Leases")
    leased_properties = cursor.fetchall()
    conn.close()
    return leased_properties


def get_leased_apartments():
    try:
        conn = sqlite3.connect('your_database.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Lease")
        leased_apartments = cursor.fetchall()
        cursor.close()
        conn.close()
        return leased_apartments
    except sqlite3.Error as e:
        print("Error retrieving leased apartments:", e)
        return None
    
def get_rent_payments_data():
    conn = sqlite3.connect('realestate.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM RentPayments")
    rent_payments_data = cursor.fetchall()
    conn.close()
    return rent_payments_data

def get_eviction_notices_data():
    conn = sqlite3.connect('realestate.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM EvictionNotices")
    eviction_notices_data = cursor.fetchall()
    conn.close()
    return eviction_notices_data