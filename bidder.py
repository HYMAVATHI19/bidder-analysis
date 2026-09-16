def find_winner(bidders):
    highest_bid = 0
    winner = ""
    for bidder in bidders:
        if bidder["bid"] > highest_bid:
            highest_bid = bidder["bid"]
            winner = bidder["name"]
    print(f"Winner is {winner} with a bid of {highest_bid}")
bidders = []
while True:
    name = input("Enter your name: ")
    bid = int(input("Enter your bid: "))
    bidders.append({"name": name, "bid": bid})
    more = input("Are there more bidders? yes/no: ").lower()
    if more == "no":
        break
find_winner(bidders)