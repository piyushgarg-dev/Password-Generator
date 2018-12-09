print("Password Generator \n")

fname=input("Please Enter Your First Name: ")
lname=input("Please Enter Your Last Name: ")
mobile=input("Contact No: ")
Password="@"+fname[0:5]+lname+mobile[-3:]
print("Your Password --> \t"+Password)
