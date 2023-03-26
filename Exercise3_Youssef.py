'''
Jack Youssef
02/20/2023

Driver: Tests the modified LinkedBag class and new Ball class by creating and manipulating linked bags.
'''

from linkedbag import LinkedBag
from ball import Ball

def main():
    aBag = LinkedBag()
    anotherBag = LinkedBag()
    print(len(aBag))
    ball1 = Ball("Red", "round")
    ball2 = Ball("Blue", "oval")
    ball3 = Ball("Green", "oblong")
    ball4 = Ball("Silver", "bubble")
    myBag = LinkedBag([ball1, ball2, ball3])
    print(myBag, "with length =", str(len(myBag)))
    myBag.clear()
    myBag.add(Ball("Purple", "super"))
    anotherBag.add(ball4)
    print(myBag, "with length =", str(len(myBag)))
    print(anotherBag, "with length =", str(len(anotherBag)))
    myBag += anotherBag
    print(myBag, "with length =", str(len(myBag)))
    for bagItem in myBag:
        print(bagItem)
    if ball4 in myBag:
        print("ball4 found in bag")
    if(myBag == aBag):
        print("bags equal")
    print(len(myBag))
    myBag.clear()
    aBag.clear()
    print(len(myBag))
    if(myBag == aBag):
        print("bags equal")
    myBag.add(ball4)
    print(myBag.isEmpty())   
    myBag.remove(ball4)
    print(myBag.isEmpty())

if __name__ == '__main__':
    main()