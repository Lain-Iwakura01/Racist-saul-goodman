import shutil

columns = shutil.get_terminal_size().columns
print(" ")
print("Saul Goodman - attorney in law, how can i help you :".center(columns))
print("-Please fill this following form : ")
race = input("Your race : (Black/White/Brown/Asian): ").lower()
crime = input("Your crime : (Theft/Slavery/Terrorism/Edging) : ").lower()
race_list = ["asian", "white", "black", "brown"]
crime_list = ["theft", "slavery", "terrorism", "edging"]
# theft (aka average black nigger crime)
if crime not in crime_list and race not in race_list:
    print("Invalid crime and race")
elif crime == "theft":
    if race == "black":
        print("Well well well, the usual suspects.")
        print("Even Saul cant defend you")
    elif race == "white":
        print("How? thats impossible!")
        print("Saul will make sure to free you from your sentence")
    elif race == "brown":
        print("I expected you to do a Kaboom crime instead.")
        print("Maybe Saul can manage to do something for you")
    elif race == "asian":
        print("Theft? stick to math and eating rice")
    else:
        print("Invalid race")
# Terrorism
elif crime == "terrorism":
    if race == "brown":
        print("EVACUATE THE LAW FIRM ASAP !!!")
    elif race == "black":
        print("Not stereotyping but did you steal the bomb ?")
    elif race == "white" or race == "asian":
        print("You must have been framed by these kaboom people")
        print("Dont worry about it Saul is Here !")
    else:
        print("Invalid race")
# Edging
elif crime == "edging":
    if race in race_list:
        print("Edging isnt meta anymore, Saul invites you to skibidi goon instead")
    else:
        print("Invalid race")
# Slavery
elif crime == "slavery":
    if race == "white":
        print("back to old habits arent we?")
        print("thats gonna be difficult to defend on court")
    elif race == "black":
        print("Poor guy")
    elif race == "brown":
        print("Thought you were mexican for a while")
        print("they like to put these guys in factories")
    elif race == "asian":
        print("they cant just put you in rice fields like that")
        print("ill manage it, just call saul")
    else:
        print("Invalid race")
else:
    print("Invalid crime")
