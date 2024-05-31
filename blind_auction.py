

import os
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
logo='''                 ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                       .-------------.
                      /_______________\
'''


print(logo)
bids={}
bidding_finished=False

def find_highest_bidder(bidding_record):
    highest_bid=0
    for bidder in bidding_record:
        bid_amt=bidding_record[bidder]
        if bid_amt>highest_bid:
            highest_bid=bid_amt
            winner=bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")



while  not bidding_finished:
    name=input("What's your name:\n")
    bid_value=float(input("What's your bid value:\n $"))

    bids[name]=bid_value
    will_bid=input("Anyone else would like to bid?(y/n)")
    
    if(will_bid=="n"):
        bidding_finished=True
        find_highest_bidder(bids)
    elif will_bid =="y":
        clear()





