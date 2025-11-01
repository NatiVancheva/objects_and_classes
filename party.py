class Party:
    def __init__(self, people):
        self.people = []

party = Party()
line = input()
while line != "End":
    party.people.append(line)
print(f"Going: {", ".join(party.people)}")
print(f"Total: {len(party.people)}")