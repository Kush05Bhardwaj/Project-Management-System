class Team:
    def  __init__(self, name, mentor_email):
        self.name = name
        self.mentor_email = mentor_email
        self.students = []
        self.status = "active"