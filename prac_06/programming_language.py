"""
CP1404 Practical - Programming Language class.

Estimate: 30 minutes
Actual: 22 minutes
"""


class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        """
        Initialise a ProgrammingLanguage instance.

        name: string, the name of the language (e.g., "Python")
        typing: string, the typing system ("Dynamic" or "Static")
        reflection: boolean, whether the language supports reflection (True/False)
        year: integer, the year the language first appeared
        """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the programming language is dynamically typed."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage object."""
        return (f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, "
                f"First appeared in {self.year}")