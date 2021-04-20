#write a function called fizz_buzz that takes a number:
#if the number id divided by 3,it should return "fizz".
#if it is divisible by 5,it should returin "Buzz".
#if it is divsible by both 3 and 5,it should return "fizzBuzz".
#otherwise,it should return the same number.

def fizz_buzz(num):
    if num%3==0 and num%5==0:
        return "fizzBuzz"

    elif num%5==0:
        return "Buzz"
    elif num%3==0:
        return "fizz"
    else:
        print(num)
d=int(input("enter the number: "))
c=fizz_buzz(a)
print(c)
print(end of program)



