# SRP SCO
# Single Responsibility Principle (SRP)
# Seperation of Concerns (SCO)
# Author: Kenan Bolat

class Journal:
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count += 1
        self.entries.append(text)

    def remove_entry(self, index):
        del self.entries[index]

    def __str__(self):
        return "\n".join(self.entries)

    def save(self, filename):
        file = open(filename, "w")
        file.write(str(self))
        file.close()


class PersistanceManager:
    @staticmethod
    def save_to_file(journal, filename):
        file = open(filename, "w")
        file.write(str(journal))
        file.close()


j = Journal()
j.add_entry("I cried today.")
j.add_entry("I ate a bug.")
print(f'Journal entries: \n{j}')

filename = r"journal.txt"
PersistanceManager.save_to_file(j, filename)
with open(filename) as f:
    print(f.read())