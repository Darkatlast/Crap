import string


name = input("Enter you Name: ")
roll = input("Enter your Roll No: ")
iden = input("1.Boss\n2.client\n3.Servant\nEnter your Identity: ")
if name == "haziq" and roll == 31 or iden == "servant":
   print("Valid")
else:
   print("invalid")