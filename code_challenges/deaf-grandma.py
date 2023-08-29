# Write a program which can imitate a Grandma who's hard of hearing and follows these constraints:
# If you don't input anything (just hit enter) she responds with WHAT?!
# If you ask a question with any lower-case letters, she responds with SPEAK UP, KID!
# If you talk to her in all upper-case letters, she responds with NO, NOT SINCE 1946!
# The first time you say GOODBYE! she says LEAVING SO SOON?
# The second time you say GOODBYE! she says LATER, SKATER! and the program exits.


print("HEY KID!")
speak = input().strip()
count = 1

while count < 3:
    while speak != "GOODBYE":
        if not speak.isupper():
            print("SPEAK UP, KID!")
        elif speak.isupper():
            print("NO, NOT SINCE 1946!")
        speak = input().strip()

    while speak == "GOODBYE" and count < 2:
        print("LEAVING SO SOON?")
        count += 1
        speak = input().strip()
    if speak == "GOODBYE" and count == 2:
        print("LATER, SKATER!")
        break
