print("Hi my name is Godwinn. I will try to have a conversation with you. Please answer all my question with the first letter of your answer capitalized. for example if you want to answer a question with good, please say Good")
name = input("What's your name? ")
print("Hi " + name)
feeling = input(" How are you feeling today? ")
if feeling == "Good":
  print("It's nice that you are feeling Good ")
elif feeling == "Bad" :
  print("Well That's Bad, I'll try to make your day better ")
elif feeling == "Trash":
  print("Sorry to say, you look like trash too, cut your hair. ")
elif feeling == "Ok" :
  print("Well Atleast you are not feeling bad ")
else:
  print("Well that's good for you ")

age = input("How old are you? ")
print("So you are " + age + " eh. I am artificial so I dont have an age")

friends = ["Jesus", "Allah", "Shiva"]

question1 = input("Would you like to see my friends? ")

if question1 == "Yes" :
  print(friends)
  print("As You could see I am friends with the gods so you will never be my friend")
elif question1 == "No" :
  print("Well Okay then, you dont have to be so mad. I'll never make you part of my friends list. ")

print("I am Also pretty smart, you can give me any number, with any of the four common operators and I could do the calculations in the blink of an eye. ")

num1= float(input("Enter your first number: "))
operator = input("Enter an operator: ")
num2= float(input("Enter your second number: "))

if operator == "+" :
  print(num1 + num2)
elif operator == "-" :
  print (num1-num2)
elif operator == "x" :
  print (num1 * num2)
elif operator == "/" :
  print(num1 / num2)

print("Pretty impressive right?")

question1 = [
  "What color is an Apple "
  "A)Red "
  "B)Blue "
  "C)Orange "
]

question2 = [
  "How big is a typical needle? "
  "A)Small "
  "B)Large "
  "C)Huge "
]

question3= [
  "Where is the Golden State Brige located? "
  "A)Europe "
  "B)California "
  "C)New York "
]

question4= [
  "Who is the owner of Tesla? "
  "A)Bill Gates "
  "B)Warren Buffet "
  "C)Elon Musk "
]

score = 0

start= input("Do you wanna take a 4 question multiple choice quiz? ")

if start =="Yes" :
  print("Answer all question with A B or C. lower case is not permitted")
  print(question1)
  answer1 = input("Enter your answer here: ")
elif start == "No" :
  print("You wouldn't be able to pass anyway, bye-bye ")

if answer1 == "A":
  print("Well done, you got it right!") 
  print(question2)
  score = score + 1
else:
  print("I think you picked the wrong one")
  print(question2)

answer2 = input("Enter your answer here: ")
if answer2 == "A":
  print("You just got this question right") 
  print(question3)
  score = score + 1
else:
  print("You got it wrong")
  print(question3)

answer3 = input("Enter your answer here: ")
if answer3 == "B":
  print("You got this question right! ") 
  print(question4)
  score = score + 1
else:
  print("How did you miss such an easy question. ")
  print(question4)

answer4= input("Enter your answer here: ")
if answer4 == "C":
  print("You got it! ") 
  score = score + 1
else :
  print("How do you not know who Elon Musk is. ")
print("Your score is below.")
print(score)

print("Well that's it for now, see you later, I need to go find my friend Bob. I think he got deleted")
