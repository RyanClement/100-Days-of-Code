"""
Created: May 4, 2021
@author: Ryan Clement
Day #9: Project: Secret Auction.
"""
from secret_auction_art import logo

def winner(bid_list):
    max_bid = 0
    winner = ''
    for bidder in bid_list:
        bid = bidder['bid']
        if  bid > max_bid:
            winner = bidder['name']
            max_bid = bid
    print(f"\nThe winner is {winner} with a bid of ${max_bid}.")
    
print(logo)
print("Welcome to the secret auction program.")
new_bidder = True
bidder_list = []
while new_bidder:
    dic = {}
    dic['name'] = input("What is your name?: ")
    dic['bid'] = int(input("What is your bid?: $"))
    bidder_list.append(dic)
    others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
    if others == 'no':
        new_bidder = False
winner(bidder_list)