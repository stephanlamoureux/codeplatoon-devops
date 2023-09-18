import csv

with open("nfl_teams.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

print("\n")

# same as above, but returned as a dictionary
with open("nfl_teams.csv") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(row)

# write to the csv file
with open("nfl_teams.csv", mode="a") as nfl_file:
    nfl_writer = csv.writer(nfl_file)
    nfl_writer.writerow([4, "Packers", 6, 4])
    nfl_writer.writerow([5, "Vikings", 8, 2])

print("\n")
# show the new additions
with open("nfl_teams.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)

# write to a dictionary
with open("nfl_teams.csv", mode="a") as csv_file:
    fieldnames = ["id", "team", "wins", "losses"]
    nfl_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    nfl_writer.writerow({"id": 6, "team": "Giants", "wins": 6, "losses": 4})
    nfl_writer.writerow({"id": 7, "team": "Lions", "wins": 8, "losses": 2})

print("\n")
# show the new additions
with open("nfl_teams.csv") as csv_file:
    csv_reader = csv.reader(csv_file)
    for row in csv_reader:
        print(row)
