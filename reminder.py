class Reminder:
    def __init__(self, reminder_id, tenant_id, lease_id, reminder_date, message, status):
        self.reminder_id = reminder_id
        self.tenant_id = tenant_id
        self.lease_id = lease_id
        self.reminder_date = reminder_date
        self.message = message
        self.status = status
