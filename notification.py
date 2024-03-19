class Notification:
    def __init__(self, notification_id, sender_id, receiver_id, date, message, status):
        self.notification_id = notification_id
        self.sender_id = sender_id
        self.receiver_id = receiver_id
        self.date = date
        self.message = message
        self.status = status
