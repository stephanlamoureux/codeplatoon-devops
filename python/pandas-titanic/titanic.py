import pandas as pd
import math


df = pd.read_csv("titanic.csv")

print(
    """
⠀⠀⠀⠀⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣿⠻⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⠀⠀⠀
⠀⠀⠀⢀⣿⣿⠀⠈⠻⣿⣦⡀⠀⠀⢀⣴⣿⣦⡀⠀⠀⣠⣾⡿⠋⠀⠀⠀
⠀⠀⠀⣾⣿⣿⣷⣄⠀⠈⠻⣿⣦⣴⣿⠟⠉⠻⣿⣦⣾⡿⠋⠀⠀⣠⣾⡿
⠀⠀⠀⢿⣿⣿⣿⣿⣷⣄⠀⠈⠻⣿⣧⣄⠀⢠⡌⠻⣿⣦⡀⣠⣾⡿⠋⠀
⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣦⡀⠈⠹⢿⣷⣌⠁⢠⡌⠻⣿⣿⡋⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣦⡀⠈⠙⣿⣷⣄⠀⢠⡌⠻⣿⣦⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣦⡀⠀⠛⢿⣷⣄⠀⣤⠈⠻⣿⣦
⠀⠀⠀⣀⡀⠀⠀⠀⢀⡈⠻⣿⡿⢛⡛⠿⠿⠀⢀⡀⠙⢿⠇⢀⣀⠀⠈⠉
⢠⣶⣶⣿⣷⣶⣶⣶⣿⣿⣶⣶⣶⣿⣿⣶⣶⣶⣿⣿⣶⣶⣶⣾⣿⣶⣶⡄
⠈⠋⠉⠀⠈⠉⠋⠉⠁⠈⠉⠛⠉⠁⠈⠉⠛⠉⠁⠈⠉⠙⠉⠁⠀⠉⠙⠁
 """
)

# Average fare paid by passengers.
avg_fare = df["Fare"].mean()
print(f"The average fare is: ${math.floor(avg_fare)}")

# Total number of male and female passengers.
men = df["Sex"].value_counts()["male"]
woman = df["Sex"].value_counts()["female"]
print(f"Total number of men onboard: {men}")
print(f"Total number of women onboard: {woman}")

# Average age of passengers.
avg_age = df["Age"].mean()
print(f"The average passenger age is: {math.floor(avg_age)}yrs old.")

# Total number of survivors per class.

# Class 1
class1 = df.query("`Pclass` == 1")
class1_total = class1["Pclass"].sum()
class1_survivor = df.query("`Pclass` == 1 and `Survived` == 1")
class1_survivor_total = class1_survivor["Pclass"].sum()

# Class 2
class2 = df.query("`Pclass` == 2")
class2_total = class2["Pclass"].sum()
class2_survivor = df.query("`Pclass` == 2 and `Survived` == 1")
class2_survivor_total = class2_survivor["Pclass"].sum()

# Class 3
class3 = df.query("`Pclass` == 3")
class3_total = class3["Pclass"].sum()
class3_survivor = df.query("`Pclass` == 3 and `Survived` == 1")
class3_survivor_total = class3_survivor["Pclass"].sum()

survivors = [
    [class1_total, class1_survivor_total],
    [class2_total, class2_survivor_total],
    [class3_total, class3_survivor_total],
]

# Prints the survival data for each class
class_num = 1
for total, survivor in survivors:
    print(f"\nClass {class_num} Survivors:")
    print(f"Out of {total} class {class_num} passengers, {survivor} survived.")
    print(f"Class {class_num} survival rate: {survivor/total:.0%}")
    class_num += 1

# All passengers and survivors
print(
    f"\nOf {class1_total + class2_total + class3_total} passengers, only {class1_survivor_total + class2_survivor_total + class3_survivor_total} survived."
)
