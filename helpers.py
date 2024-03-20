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



