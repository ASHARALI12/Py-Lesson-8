c = int(input("Whats Your Electricity Compsumption "))
if c < 50 :
    bill = (c * 2.60) + 25 
    print(bill)
elif c > 50 and c <= 100 :
    bill = (c * 3.25) + 35
    print(bill)
elif c > 100 and c <= 200 :
    bill = (c * 5.26) + 45
    print(bill)
elif c > 200 :
    bill = (c * 8.45) + 75
    print(bill)


    