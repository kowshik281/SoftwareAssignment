#Menu file
import addition,subtract,multiplication,division,modulus



print("This program is for add,sub,mult and divide\n1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Modulus")
s=int(input("Enter your choice:"))
if(s==1):
	print(addition.add())
elif(s==2):
	print(subtract.sub())
elif(s==3):
	print(multiplication.mult())
elif(s==4):
	print(division.div())
elif(s==5):
	print(modulus.mod())
else:
	print("Invalid input")	