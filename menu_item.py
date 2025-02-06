class MenuItem:
    def __init__(self, name, category, description):
        self.name = name
        self.category = category
        self.description = description

    def display_info(self):
        return f"{self.name} ({self.category}): {self.description}"