# bill_amt=float(input("Enter the total amount of bill"))
# tip_amt=float(input("how much tip percentaage of total amount?"))
# total_bill=(floatbill_amt+(tip_amt/100*bill_amt))
# print(total_bill)
# no_of_persons=print("Whats the no of persons in which bill need to be split?")
# individual_bill=float(total_bill/no_of_persons)
# print("Each person has to pay "+individual_bill)


net_bill=input("Enter the amount of bill \n")
net_bill1=float(net_bill)
tip=input("whats the percent of net bill as tip \n")
tip1=float(tip)
total_bill=net_bill1*(1+(tip1/100))
print(total_bill)
no_of_person=int (input("What's the no of persons? \n"))

individual_bill=total_bill/no_of_person
print(f"Each person has to pay {individual_bill} \n")
