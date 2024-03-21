import sqlite3

import sqlite3

class Agent:
    def __init__(self, agent_id, name, email, phone, agency):
        self.agent_id = agent_id
        self.name = name
        self.email = email
        self.phone = phone
        self.agency = agency

class AgentRepository:
    def __init__(self, db_file):
        self.db_file = db_file

    def get_agents(self):
        agents = []
        conn = sqlite3.connect(self.db_file)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Agents")
        rows = cursor.fetchall()
        for row in rows:
            agent = Agent(*row)
            agents.append(agent)
        conn.close()
        return agents

class EvictionNotice:
    def __init__(self, notice_id, tenant_id, lease_id, notice_date, message, status):
        self.notice_id = notice_id
        self.tenant_id = tenant_id
        self.lease_id = lease_id
        self.notice_date = notice_date
        self.message = message
        self.status = status

class Landlord:
    def __init__(self, landlord_id, agent_id, name, email, phone, address):
        self.landlord_id = landlord_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        self.agent_id = agent_id
   
class Lease:
    def __init__(self, leaseID, tenantID, propertyID, leaseStartDate, leaseEndDate, rentAmount, securityDeposit):
        self.leaseID = leaseID
        self.tenantID = tenantID
        self.propertyID = propertyID
        self.leaseStartDate = leaseStartDate
        self.leaseEndDate = leaseEndDate
        self.rentAmount = rentAmount
        self.securityDeposit = securityDeposit

class Property:
    def __init__(self, property_id, property_name, address, landlord_id):
        self.property_id = property_id
        self.property_name = property_name
        self.address = address
        self.landlord_id = landlord_id

class RentPayment:
    def __init__(self, payment_id, lease_id, tenant_name, payment_date, amount_paid, payment_method):
        self.payment_id = payment_id
        self.lease_id = lease_id
        self.tenant_name = tenant_name
        self.payment_date = payment_date
        self.amount_paid = amount_paid
        self.payment_method = payment_method

class Tenant:
    def __init__(self, tenant_id, name, email, phone, address):
        self.tenant_id = tenant_id
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address



