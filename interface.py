from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print_info(self):
        pass

class Saveable(ABC):
    @abstractmethod
    def save(self):
        pass

class Document(Printable, Saveable):
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def print_info(self):
        print(f"Document: {self.title}")
        print(self.content)

    def save(self):
        print(f"Saving {self.title} to disk...")

doc = Document("Report", "Q4 Results...")
doc.print_info()
doc.save()