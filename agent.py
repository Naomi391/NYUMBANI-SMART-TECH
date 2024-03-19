class Agent:
    def __init__(self, agent_id, name, email, phone, agency):
        self.agent_id = agent_id
        self.name = name
        self.email = email
        self.phone = phone
        self.agency = agency

@staticmethod
def list_agents_by_agency(agents, agency_name):
    agents_in_agency = [agent for agent in agents if agent.agency == agency_name]
    return agents_in_agency


