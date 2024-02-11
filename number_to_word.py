"""

inp = input("Phone >")

number_list = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four", 
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}

output = ""

for key in inp:
    output += number_list.get(key, "i") + " "

print(output)

"""

inp = input ("Number >")

list_ing = {
    "1" : "one",
    "2" : "two",
    "3" : "three",
    "4" : "four", 
    "5" : "five",
    "6" : "six",
    "7" : "seven",
    "8" : "eight",
    "9" : "nine"
}


output = ""

for key in inp:
    output += list_ing.get(key, "i") + " "
print(output)