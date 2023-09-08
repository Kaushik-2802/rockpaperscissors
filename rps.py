import random
list=['rock','paper','scissor']
p=random.choice(list)
while(1):
   q=input("enter rock/paper/scissor:")
   if p=='rock':
      if q=='paper':
        print("you win congratulations\n")
        print("computer's choice:",p)
        break
      if q=='scissor':
        print("you lost try again\n")
        print("computer's choice:",p)
        continue
      if q=='rock':
        print("it's a tie \n")
        print("computer's choice:",p)
        continue
   if p=='paper':
      if q=='paper':
        print("it's a tie\n")
        print("computer's choice:",p)
        continue
      if q=='scissor':
        print("you win congratulations\n")
        print("computer's choice:",p)
        break
      if q=='rock':
        print("you lost try again\n")
        print("computer's choice:",p)
        continue
   if p=='scissor':
      if q=='paper':
        print("you lot try again\n")
        print("computer's choice:",p)
        continue
      if q=='scissor':
        print("it's a tie\n")
        print("computer's choice:",p)
        continue
      if q=='rock':
        print("you win congratulations\n")
        print("computer's choice:",p)
        break
