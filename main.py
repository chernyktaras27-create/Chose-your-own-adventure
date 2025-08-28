name = input("Type your name: ")
print("Welcome,", name + ", to Middle-earth! Your journey begins...")

print("\nYou are a simple hobbit of the Shire. One day, you find the One Ring in your pocket. "
      "It whispers to you with dark power...")
answer = input("Do you KEEP the Ring, SEEK Gandalf, or IGNORE it? (keep/seek/ignore): ").lower()

if answer == "keep":
    print("\nYou clutch the Ring tightly, feeling its power...")
    answer = input("Soon, Black Riders appear in the Shire. Do you HIDE or FIGHT them? (hide/fight): ").lower()

    if answer == "hide":
        print("\nYou hide in Bag End, but the Riders burn the Shire searching for you. You are captured. You lose.")
    elif answer == "fight":
        answer = input("\nYou bravely fight, but the Riders are too strong. Strider arrives to help you. "
                       "Do you TRUST him or ESCAPE from him? (trust/escape): ").lower()
        if answer == "trust":
            answer = input("\nStrider takes you to Rivendell. At Elrond’s council, the Fellowship is formed. "
                           "Do you VOLUNTEER to carry the Ring or REFUSE? (volunteer/refuse): ").lower()
            if answer == "volunteer":
                answer = input("\nYou march with the Fellowship. At Moria, Gandalf faces the Balrog. "
                               "Do you STAY and fight with him or RUN with the others? (stay/run): ").lower()
                if answer == "stay":
                    print("\nYou fall into the abyss with Gandalf. A noble but tragic end. You lose.")
                elif answer == "run":
                    answer = input("\nYou escape Moria and reach Mordor after a long journey. At Mount Doom, "
                                   "you stand at the edge of the fire. Do you DESTROY the Ring or CLAIM it? (destroy/claim): ").lower()
                    if answer == "destroy":
                        print("\n🔥 You throw the Ring into the fire! Middle-earth is saved. You WIN!")
                    elif answer == "claim":
                        print("\nThe Ring corrupts you. Sauron rises again. Darkness covers Middle-earth. You lose.")
                    else:
                        print("Not a valid option. You lose.")
                else:
                    print("Not a valid option. You lose.")
            elif answer == "refuse":
                print("\nBoromir takes the Ring, and you return to the Shire. But soon, Sauron’s armies find you. You lose.")
            else:
                print("Not a valid option. You lose.")
        elif answer == "escape":
            print("\nYou run from Strider, but without his guidance, the Riders catch you. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

elif answer == "seek":
    print("\nYou seek Gandalf, who warns you of the Ring’s danger.")
    answer = input("He tells you to go to Rivendell. Do you TRAVEL alone or ASK friends to join? (alone/friends): ").lower()

    if answer == "alone":
        print("\nThe road is dangerous, and you are captured by Orcs. You lose.")
    elif answer == "friends":
        answer = input("\nYour friends Sam, Merry, and Pippin join you. You reach Rivendell safely. "
                       "At the council, you must choose: Do you GIVE the Ring to Aragorn or BEAR it yourself? (give/bear): ").lower()
        if answer == "give":
            print("\nAragorn takes the Ring, but is soon corrupted. Gondor falls, and Sauron wins. You lose.")
        elif answer == "bear":
            print("\nYou carry the Ring bravely. With Sam at your side, you reach Mount Doom. "
                  "Do you THROW the Ring into the fire or KEEP it? (throw/keep): ").lower()
            if answer == "throw":
                print("\n🔥 The Ring is destroyed. Middle-earth is saved. You WIN!")
            elif answer == "keep":
                print("\nThe Ring corrupts you at the last moment. Gollum bites off your finger and falls into the fire. "
                      "The Ring is destroyed, but you die. A bittersweet ending.")
            else:
                print("Not a valid option. You lose.")
        else:
            print("Not a valid option. You lose.")
    else:
        print("Not a valid option. You lose.")

elif answer == "ignore":
    print("\nYou ignore the Ring, hoping life will remain peaceful in the Shire...")
    answer = input("But soon, the Ringwraiths arrive. Do you FLEE to the mountains or SURRENDER the Ring? (flee/surrender): ").lower()
    if answer == "flee":
        print("\nYou hide in the mountains, living in fear until the world falls to Sauron. A sad, quiet ending.")
    elif answer == "surrender":
        print("\nYou give the Ring to the Riders. Sauron regains his full power. Middle-earth is lost. You lose.")
    else:
        print("Not a valid option. You lose.")

else:
    print("Not a valid option. You lose.")

print("\nThank you for playing,", name + "! May your choices be remembered in the songs of Middle-earth.")
