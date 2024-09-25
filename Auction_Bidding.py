bidder = {}

def highest_bidder():
    max = 0
    winner = ""
    for highest in bidder:
        bid_amount = bidder[highest]
        if bid_amount > max:
            max = bid_amount
            winner = highest
    print(f"The highest bidder is {winner} with a bid of ${max}.")



while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidder[name] = bid
    user_input = input("Are there any other bidders? (yes/no): ").lower()
    if user_input == "yes":
        print("\n" * 100)
        continue

    else:
        highest_bidder()
        break


