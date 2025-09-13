name = input("What is your name? \n").strip()

if name.lower() == "tom":
    evil_status = input("Are you evil?\n").strip().lower()
    if evil_status in {"yes", "ye", "y", "yea", "yeah", "affirmative", "affirm", "aferm", "afirmativ", "aff",  "of course"}:
        print("You are not welcome here " + name  + " !! Get Out!!")
        exit()
    else:
        print("Oooh, so you are one of good " + name + "s? welcome to our community!")
else:
    print("Hello " + name + ", thank you so much for coming today!\n\n\n")