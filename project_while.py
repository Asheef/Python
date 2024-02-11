print(" Let's play the guess game. I imagine a number. If you correctly found that number, You won!  Otherwise, I won")



Secret_number = 9       #the number to be guessed
Guess_count = 0         
Guess_limit = 3



while Guess_count < Guess_limit:

    Guess_count = Guess_count + 1
    Guess = int (input ("Guess : "))
    if Guess == Secret_number:
        print ("You won");
        break
else :
    print ("I won")