__all__ = ['divide_by']

def divide2(number) :
   number = str(number)
   if (number[-1] == '0' or number[-1] == '2' or number[-1] == '4' or number[-1] == '6' or number[-1] == '8') :
      return True
   else :
      return False   

#function to check if a large number is divisible by 3:
def divide3(number) :
   number = str(number)
   n = len(number)
   sum = 0
   for i in range(0,n) :
      sum = sum + ((int)(number[i]))
   return (sum % 3 == 0)


def divide5(number) :
   number = str(number)
   if (number[-1] == '0' or number[-1] == '5') :
      return True
   else :
      return False

#function to check if a large number is divisible by 7:
def divide7(number) :
   number = str(number)
   n = len(number)
   last3 = 0
   if (n < 3) :
      last3 = (int)(number)
   else :
      last3 = (int)(number[n-3:n])
   return (last3 % 7 == 0)


def divide11(number) :
   number = str(number)
   n = len(number)
   oddDigSum = 0
   evenDigSum = 0
   for i in range(0,n) :
      if (i % 2 == 0) :
         oddDigSum = oddDigSum + ((int)(number[i]))
      else:
         evenDigSum = evenDigSum + ((int)(number[i]))
   return ((oddDigSum - evenDigSum) % 11 == 0)
 

#function to check if a large number is divisible by 13:
def divide13(number) :
   number = str(number)
   n = len(number)
   last4 = 0
   if (n < 4) :
      last4 = (int)(number)
   else :
      last4 = (int)(number[n-4:n])
   return (last4 % 13 == 0)


#function to check if a large number is divisible by 17:
def divide17(number) :
    number = str(number)
    n = len(number)
    last3 = 0
    if (n < 3) :
        last3 = (int)(number)
    else :
        last3 = (int)(number[n-3:n])
    return (last3 % 17 == 0)

#function to check if a large number is divisible by 19:
def divide19(number) :
    number = str(number)
    n = len(number)
    last2 = 0
    if (n < 2) :
        last2 = (int)(number)
    else :
        last2 = (int)(number[n-2:n])
    return (last2 % 19 == 0)

# def divide17(number) : 
#    while(number // 100) :
#       last_digit = number % 10
#       number //= 10
#       number -= last_digit * 5
#    return (number % 17 == 0)

# def divide19(number) :
#    while(number // 100) :
#       last_digit = number % 10
#       number //= 10
#       number += last_digit * 2
#    return (number % 19 == 0)









divide_by = {
   '2': divide2,
   '3': divide3,
   '5': divide5,
   '7': divide7,
   '11': divide11,
   '13': divide13,
   '17': divide17,
   '19': divide19,
}