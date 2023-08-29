num_of_bottles = 99

while num_of_bottles > 2:
    print(f"{num_of_bottles} of beer on the wall, {num_of_bottles} bottles of beer.")
    num_of_bottles -= 1
    print(
        f"Take one down and pass it around, {num_of_bottles} bottles of beer on the wall."
    )

print(f"{num_of_bottles} of beer on the wall, {num_of_bottles} bottles of beer.")
print("Take one down and pass it around, 1 bottle of beer on the wall.")
print("1 bottle of beer on the wall, 1 bottle of beer.")
print("Take one down and pass it around, no more bottles of beer on the wall.")
print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall.")
