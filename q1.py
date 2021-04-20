#write a python function to find the max of three number.
def max(a,b,c):
    if a>b and a>c:
        print(f"a is maximum number")
    elif b>a and b>c:
        print(f"b is maximum number")
    else:
        print("c is maximum number")

max(3,8,5)

