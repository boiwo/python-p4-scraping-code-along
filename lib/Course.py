# class Course:
#     pass
class Course:
    def __init__(self, title, schedule, description):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __repr__(self):
        return f"Course(title={self.title}, schedule={self.schedule}, description={self.description})"
class Course:
    def __init__(self, title="", schedule="", description=""):
        self.title = title
        self.schedule = schedule
        self.description = description

    def __repr__(self):
        return f"Course(title={self.title}, schedule={self.schedule}, description={self.description})"
