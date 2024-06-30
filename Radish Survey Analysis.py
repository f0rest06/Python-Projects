# Create an empty dictionary for associating radish names
# with vote counts
counts = {}

# Create an empty list with the names of everyone who voted
voted = []

# Check if someone has voted already and return True or False
def has_already_voted(name):
    if name in voted:
        print(name + " has already voted!")
        return True
    return False

# Count a vote for the radish variety named 'radish'
def count_vote(radish):
    if not radish in counts:
        # First vote for this variety
        counts[radish] = 1
    else:
        # Increment the radish count
        counts[radish] = counts[radish] + 1

with open("radishsurvey.txt") as file:
    for line in file:
        line = line.strip()
        name, vote = line.split(" - ")
        name = name.strip().capitalize().replace("  ", " ")
        vote = vote.strip().capitalize().replace("  ", " ")

        if not has_already_voted(name):
            count_vote(vote)
        voted.append(name)

    print("Results:")
    print()
    for name in counts:
        print(name + ": " + str(counts[name]))
