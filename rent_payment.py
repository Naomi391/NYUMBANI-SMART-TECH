class RentPayment:
    def __init__(self, payment_id, lease_id, tenant_name, payment_date, amount_paid, payment_method):
        self.payment_id = payment_id
        self.lease_id = lease_id
        self.tenant_name = tenant_name
        self.payment_date = payment_date
        self.amount_paid = amount_paid
        self.payment_method = payment_method
