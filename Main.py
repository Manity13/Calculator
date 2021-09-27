print("Welcome To The Calculator")

numberOne = input("Type A Number: ")
numberTwo = input("Type Another Number: ")

enterInput = input("Type a Input A for addition, S for subtraction, M for multiplication, D for division, and E for exponents: ")

if (enterInput == "A" or "a"):
  answer = float(numberOne) + float(numberTwo)
elif (enterInput == "S" or "s"):
  answer = float(numberOne) - float(numberTwo)
elif (enterInput == "M" or "m"):
  answer = float(numberOne) * float(numberTwo)
elif (enterInput == "D" or "d"):
  answer = float(numberOne) / float(numberTwo)
elif (enterInput == "E" or "e"):
  answer = float(numberOne) ** float(numberTwo)
elif (enterInput == "Auuf" or "auuf"):
  answer = "Auuf"
elif (enterInput == "Auf" or "auf"):
  answer = "Auf"

print(answer)

close = input("Type C to close the app: ")

if (close == "C" or "c"):
  print("Bye")