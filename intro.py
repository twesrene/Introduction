import time

while True:
    print("What do you wanna know?")
    print("A. Name ? ")
    print("B. From ? ")
    print("C. School ? ")
    print("D. Majoring ? ")
    print("E. Languages ? ")
    print("F. Target ? ")
    print("G. My Socials?")
    print("H. Nothing Else")
    t = input("Choose what point do you wanna know? ").upper()

    if t == "A" :
        print("Hi There my name is Twesrene, Nice to meet you !")

    elif t == "B" :
        print("Hi I am from Batam, Indonesia !")

    elif t == "C" :
        print("Hi I am currently Studying in Xiamen University Malaysia year 2026!")

    elif t == "D" :
        print("Hi I am majoring in Software Engineering !")

    elif t == "E" :
        print("I can speak using Indonesia ,English ,Hokkian and currently learning Chinese(中文) and Melayu!")

    elif t == "F" :
        print("My Target right now is learning how to develop website and i am interested in Tech Company at Malaysia and Singapore  !")
    
    elif t == "G" :
        print("My Social on Instagram is @twsren and you can also contact me via email at twesrenee@gmail.com  !")

    elif t == "H" :
        print("Thank you see you next time  !")
        break
        
    else:
        print("Sorry this choice isnt available, please choose A-G, Thank you !")
        break

    time.sleep(2)

