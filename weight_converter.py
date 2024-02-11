#print ("Hello bro")

#weight_in_kg = input ("Tell me your body mass in Kilograms \n")

#weight_in_pounds = int (weight_in_kg) * 2.205 

#print ("Your body weight is " , int(weight_in_pounds))


weight = input("Enter your Weight \n")

l_or_k = input ("your mentioned weight is L or K \n")

#variable for displaying in K
K = int(weight) / 2.205
#variable for displaying in L
L = int(weight) * 2.205

if l_or_k == "l" or "L":
    print("your weight is " , round(K) , "Kgs")
elif l_or_k == "k" or "K" :
    print ("your weight is " , round(L) , "Lbs")