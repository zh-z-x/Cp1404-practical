from datetime import datetime

class Project:

    def __init__(self, name, start_date, priority, cost_estimate, completion):
        self.name = name
        self.start_date = start_date
        self.priority = int(priority)
        self.cost_estimate = float(cost_estimate)
        self.completion = int(completion)