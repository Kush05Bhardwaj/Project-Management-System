from datetime import datetime

class Evaluation:
    def __init__(self, team_name, mentor_email, marks, remarks):
        self.team_name = team_name
        self.mentor_email = mentor_email
        self.marks = marks
        self.remarks = remarks
        self.created_at = datetime.utcnow()
