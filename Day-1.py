"""
name and print styles

name = input("what is your name")
name = name.strip().title() capitals each words first letter
print(f"Hello, {name}", )
#print(name)


x="Hello"
y="Welcome!"
z="sam"
print(x,y,z)

x = 10
y =5
z =6
print(x,y,z)

int, float, round
x = float(input("What's x? "))
y = float(input("What's y? "))
z = x + y
print(round(z))
print(f"{z:.2f}")



 name = input("What's your name? ")

  match name: 
      case "Harry":
          print("Gryffindor")
      case "Hermione":
          print("Gryffindor")
      case "Ron": 
          print("Gryffindor")
      case "Draco":
          print("Slytherin")
      case _:
          print("Who?")




def helo(x="world"): #if helo() called with no arguments default value is addded
    print("Hey there",x)



def main():  indicates to start executing from main
    name = input("what name? ")
    helo(name.title())

    helo()


main() calling main function to execute




def main():
    x = 5; y=6
    print("its mutiplucation: ", multi(x,y))

def multi(m,n):
    return m*n
    

main()




"""
def main():
    x = int(input("a positive number: "))
    if isEven(x):
        print("Even Number")
    else:
        print("given is an Odd Number")

def isEven(value):
    if value % 2 == 0:
        return True
    else: return False

def is_even(n):
    return True if n % 2 == 0 else False

def is_even(n):
    return n % 2 == 0

main()




