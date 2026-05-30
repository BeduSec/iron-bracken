class DomainController:
    def __init__(self, domain="bracken.local"):
        self.domain = domain
        self.users = {}

    def add_user(self, username, password):
        self.users[username] = password
