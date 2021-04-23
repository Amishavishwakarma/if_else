#Rules of navgurukul where you have to take the permission from the Disco.
day=input("enter your day to go outside\n")
if day="monday" or day=="tuesday" or day=="wednesday" or day=="thursday" or day=="friday" or day=="saturday" or day=="sunday": 
    print("thusday is holiday you can go in this day\n")
    place=input("where you want to go on thursday ")
    if place=="hospital" or place=="bank" or place=="market" :
        print("you can go")
        permission=input("disco write your permission is yes or no\n")
        if permission=="yes" :
            print("you can go")
            print("masks and sanitizer are compulsary")
            work=input("you are going for personal work or ng work\n")
            if work=="personal":
                print("yes quarantine")
            else:
                print("no quarantine")
        else:
            print("you cannot go")
    else:
        print("no you cannot go on that place")


else:
    print("you entered wrong")