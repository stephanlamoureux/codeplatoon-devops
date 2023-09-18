def deaf_grandma():
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


deaf_grandma()
