# teams.py

# converting the functional to an Object-Oriented approach
class Team():
    def __init__(self, name, city, sport=None, roster=[]):
        # these are attributes / nouns
        self.name = name
        self.city = city
        self.sport = sport
        self.roster = roster

    # this is a property / noun
    # the @property decorator allows us to invoke this without trailing parentheses
    @property
    def full_name(self):
        return f"{team.city} {team.name}"

    # this is a method / verb
    def advertise(self):
        print("PLEASE COME TO", self.city.upper(), "TO SEE US PLAY")

    # this method doesn't require any information about the specific instance itself
    # the @staticmethod decorator allows us to omit passing "self" as a param
    @staticmethod
    def advertise_generically():
        print("PLEASE COME TO OUR GAMES")

if __name__ == "__main__":

    teams = [
        {"name": "Yankees", "city": "New York"},
        {"name": "Mets", "city": "New York"},
        {"name": "Nationals", "city": "Washington"}
    ]

    for d in teams:
        #print(team["city"] + " " + team["name"])
        #print(full_name(team)) #> functional approach
        team = Team(d["name"], d["city"])
        print(team.name)
        print(team.full_name) #> OOP (invoke the method on the object)
        team.advertise()