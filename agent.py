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
