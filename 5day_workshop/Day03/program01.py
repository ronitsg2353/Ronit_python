user_amount=int(input("please enter your amount:"))
deduced_amount=1000
Total_amount=user_amount-deduced_amount
print("1000 rs will be deduced in your accoubnt due to service charges")
print("you have in you account:",Total_amount,"RS")
if(Total_amount<1001):
    print("your amount is sufficient")
else:
    print("you should have to add more than:",Total_amount,"RS")