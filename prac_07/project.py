"""CP1404 Practical - Project Class

Estimated time - 60 minutes
Actual time - 45 minutes
"""

class Project:
    """Represent a Project object"""
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a project instance"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        """Return a string representation of the project"""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Less than for Project objects, based on priority"""
        return self.priority < other.priority

    def is_compete(self):
        """Utility method: Return True if the project is 1000% complete."""
        return self.completion_percentage == 100

    def get_start_date_string(self):
        """Helper to get the start date as a formatted string."""
        return self.start_date.strftime('%d/%m/%Y')

