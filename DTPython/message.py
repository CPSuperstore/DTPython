class Message:
    def __init__(self, identifier: str, body: str):
        self.identifier = identifier
        self.body = body

    def __repr__(self):
        return "<DTP Message identifier='{}' body='{}'>".format(self.identifier, self.body)
