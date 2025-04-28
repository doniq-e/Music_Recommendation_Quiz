print("\nWelcome to the music recommendation quiz!\nAnswer A, B, C, or type 'help' for instructions.")

p1 = 0  #A energetic  |  genres: edm
p2 = 0  #B calm
p3 = 0  #C melancholy

counter = 0

# Calls the help menu
def help_menu():
    print("\n                       ~ HELP ~\n~ We will ask you a few questions about your music interests.\n~ Type your answer to the questions by inputting A, B or C.\n~ We will then recommend music genres and music artists we think you will like!")

# Question 1 - fav mood of music? (energetic, calming, melancholy)
while True:
    q1 = input("\nHow do you like to feel when you listen to music?\na) Energetic\nb) Calm\nc) Melancholy\n")
    lq1 = q1.lower()
    if lq1 == "a":
        p1+=1
        break
    elif lq1 == "b":
        p2+=1
        break
    elif lq1 == "c":
        p3+=1
        break
    elif lq1 == "help":
        help_menu()
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")

#Question 2 - Where do you mostly listen to music? - (bus ride, gym, sleep)
while True:
    q2 = input("\nWhere do you mostly listen to music?\na) Bus/Car ride\nb) Gym\nc) Sleep\n")
    lq2 = q2.lower()
    if lq2 == "a":
        p3 += 1
        break
    elif lq2 == "b":
        p1 += 1
        break
    elif lq2 == "c":
        p2 += 1
        break
    elif lq2 == "help":
        help_menu()
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")

# Question 3 - What is your favorite comfort food? - (pizza, ice cream, mac and cheese)
while True:
    q3 = input("\nWhat is your favorite comfort food?\na) Pizza\nb) Ice Cream\nc) Mac and Cheese\n")
    lq3 = q3.lower()
    if lq3 == "a":
        p1 += 1
        break
    elif lq3 == "b":
        p3 += 1
        break
    elif lq3 == "c":
        p2 += 1
        break
    elif lq3 == "help":
        help_menu()
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")

# Question 4 - Which country do you want to visit? - (Japan, Brazil, Greece)
while True:
    q4 = input("\nWhich country do you want to visit?\na) Japan\nb) Brazil\nc) Greece\n")
    lq4 = q4.lower()
    if lq4 == "a":
        p3 += 1
        break
    elif lq4 == "b":
        p1 += 1
        break
    elif lq4 == "c":
        p2 += 1
        break
    elif lq4 == "help":
        help_menu()
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")

# Question 5 - What is your favorite type of weather? - (rain, sunny, snow)
while True:
    q5 = input("\nWhat is your favorite type of weather?\na) Rain\nb) Sun\nc) Snow\n")
    lq5 = q5.lower()
    if lq5 == "a":
        p3 += 1
        break
    elif lq5 == "b":
        p1 += 1
        break
    elif lq5 == "c":
        p2 += 1
        break
    elif lq5 == "help":
        help_menu()
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")

# Question 6 - Ideal weekend plans? - (stay at home, night out with friend, shopping)
while True:
    q6 = input("\nIdeal weekend plans?\na) Stay at Home\nb) Night out with Friends\nc) Shopping\n")
    lq6 = q6.lower()
    if lq6 == "a":
        p3 += 1
        break
    elif lq6 == "b":
        p1 += 1
        break
    elif lq6 == "c":
        p2 += 1
        break
    elif lq6 == "help":
        help_menu()
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")

# Question 7 - Favorite drink? - (water, OJ, coffee)
while True:
    q7 = input("\nFavorite drink?\na) Water\nb) Orange Juice\nc) Coffee\n")
    lq7 = q7.lower()
    if lq7 == "a":
        p3 += 1
        break
    elif lq7 == "b":
        p1 += 1
        break
    elif lq7 == "c":
        p2 += 1
        break
    elif lq7 == "help":
        help_menu()
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")

# Question 8 - Favorite leisure activity? - (gaming, sleeping, hiking)
while True:
    q8 = input("\nFavorite leisure activity?\na) Gaming\nb) Sleeping\nc) Hiking\n")
    lq8 = q8.lower()
    if lq8 == "a":
        p1 += 1
        break
    elif lq8 == "b":
        p3 += 1
        break
    elif lq8 == "c":
        p2 += 1
        break
    elif lq8 == "help":
        help_menu()
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")

# Question 9 - What time of day do you most like to listen? - (morning, afternoon, evening)
while True:
    q9 = input("\nWhat time of day do you most like to listen?\na) Morning\nb) Afternoon\nc) Evening\n")
    lq9 = q9.lower()
    if lq9 == "a":
        p2 += 1
        break
    elif lq9 == "b":
        p1 += 1
        break
    elif lq9 == "c":
        p3 += 1
        break
    elif lq9 == "help":
        help_menu()
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")

# Question 10 - Pick an animal. - (giraffe, owl, dolphin)
while True:
    q10 = input("\nPick an animal.\na) Giraffe\nb) Owl\nc) Dolphin\n")
    lq10 = q10.lower()
    if lq10 == "a":
        p1 += 1
        break
    elif lq10 == "b":
        p3 += 1
        break
    elif lq10 == "c":
        p2 += 1
        break
    elif lq10 == "help":
        help_menu()
    else:
        print("\nPlease type a valid input or type 'help' for instructions.")


# final score calculations and results
# FINISH THE RESULTSSS!!!!!!!!!!!!!
if p1 > p2 and p1 > p3:
    print("\n You should look at energetic types of music!\n\n Artists:\n- Travis Scott\n- KAYTRANADA\n- Yeat\n")
if p2 > p1 and p2 > p3:
    print("\n You should look at calm types of music!")
if p3 > p1 and p3 > p2:
    print("\n You should look at melancholy types of music!")
