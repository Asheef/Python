print ("Are you ready to control the status of a car ? \n")

control = ""
started = False
 

while control != "exit":
    control = input("--> ").lower()

    if (control == "start"):
        if started:
            print("Car is started already")
        else:
            started = True
            print("Engine Starts..........................")
            
    
    elif (control == "stop"):
        if not started:
            print("car is stopped already..!")
        else:
            started = False
            print ("Car Stopped")
            

    elif (control == "exit"):
        break

    else:
        print("unknown command")

        

        

