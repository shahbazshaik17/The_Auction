from art import logo 
print(logo)
bid_comp = False
name_list = []
bid_list = []
dict = {}
while not bid_comp:
    name = input("what's your name ?  "  )
    bid_price = int(input("what's your bid price ?  "))
    name_list.append(name)
    bid_list.append(bid_price)
    bid_i = (input("does auction comp y or n : "))
    if bid_i == "y":
        bid_comp = True
    for i in range(len(name_list)):
        dict[name_list[i]] = bid_list[i]
print(dict)
# the winner of the auction is 
winner = name_list[bid_list.index(max(bid_list))]
print("The winner is " + winner  + " with bid price of " + str(max(bid_list)))