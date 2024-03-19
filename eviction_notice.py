class EvictionNotice:
    def __init__(self, notice_id, tenant_id, lease_id, notice_date, message, status):
        self.notice_id = notice_id
        self.tenant_id = tenant_id
        self.lease_id = lease_id
        self.notice_date = notice_date
        self.message = message
        self.status = status
