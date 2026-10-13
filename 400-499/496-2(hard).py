t = int(input())
for values in range(t):
    x = int(input())
    y = 0.1
    if x*y > 100:
        print(int(x*y))
    elif x*y <= (100):
        print("100")


#need to think about percentage questions properly. If it says flat discount of rs 100 of any price it means that it will deduct 100 rupees no matter what, and if it says 10% discount off price, then it means it multiply the price by 0.1 and subtract it by the answer it gives. For example for 1300 , 10 percent discount meant 1300*0.1 = 130 and, therefore it will deduct 130 compared to the flat discount of 100, which means it will deduct 100 only regardless.