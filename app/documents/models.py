from datetime import datetime

class Document:
    def __init__(self, filename, uploaded_by, team_name):
        self.filename = filename
        self.uploaded_by = uploaded_by
        self.team_name = team_name
        self.status = "pending"
        self.uploaded_at = datetime.utcnow()  # Call the function!
        self.review_comment = None

doc = Document(filename, user["email"], team["name"])