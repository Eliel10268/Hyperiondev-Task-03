
#This will ask the client/user to enter their full namee
name = input("Please Enter Your Full name: ")

# This will check they are blank spaces or empty name

if not name.strip():
    print("You have not Entered Anything. Please Enter Your Full Name. ")

#This will check they are less than Four Characters in the name entered by the user

elif len(name) < 4:
    print("You have entered less than 4 Characters. Please make sure that you have entered your name and surname.")

#This will check if the name entered is more than 25 characters

elif len(name) > 25:
    print("You have entered more than 25 characters. Please make sure that you have only entered your full name.")

#Or else; Your name is legitimate
else:
    print("Thank you for entering your name.")
