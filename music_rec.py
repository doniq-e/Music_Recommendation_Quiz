
print("Welcome to the music recommendation questionare!")

p1 = 0  #A enegertic
p2 = 0  #B calm
p3 = 0  #C melancholy

counter = 0

while counter < 10:


    # Question 1 - fav mood of music? (energetic, calming, melancholy)
    q1 = input("\nHow do you like to feel when you listen to music?\na) Energetic\nb) Calm\nc) Melancholy\n")
    lq1 = q1.lower()
    if lq1 == "a":
        p1+=1
    elif lq1 == "b":
        p2+=1
    elif lq1 == "c":
        p3+=1
    elif lq1 == "help":
        print("\n                       ~ HELP ~\n~ We will ask you a few questions about your music interests.\n~ Type your answer to the questions by inputting A, B or C.\n~ We will then recommend music genres and music artists we think you will like!")
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")





    #Question 2 - When do you mostly listen to music? - (bus ride, gym, sleep)
    q2 = input("\nHow do you like to feel when you listen to music?\na) Energetic\nb) Calm\nc) Melancholy\n")
    lq2 = q1.lower()
    if lq2 == "a":
        p1 += 1
    elif lq2 == "b":
        p2 += 1
    elif lq2 == "c":
        p3 += 1
    elif lq2 == "help":
        print(
            "\n                       ~ HELP ~\n~ We will ask you a few questions about your music interests.\n~ Type your answer to the questions by inputting A, B or C.\n~ We will then recommend music genres and music artists we think you will like!")
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")


    #Question 3 -



    counter+=1

