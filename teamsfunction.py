# teams.py

# example of a functional approach
def full_name(team_dict):
    return team["city"] + " " + team["name"]

teams = [
    {"name": "Yankees", "city": "New York"},
    {"name": "Mets", "city": "New York"},
    {"name": "Nationals", "city": "Washington"}
]

for team in teams:
    print(full_name(team)) #> functional approach (pass the object to the function)


    