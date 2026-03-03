def main():
    # Initialize stock prices
    stock_prices = {
        "AAPL":180,
        "TSLA":250,
        "GOOG":140,
        "MSFT":300,
    }

    # Initialize portfolio and total investment
    portfolio = {}
    total_investment = 0

    print("welcome to Stock portfoli tracker. Type 'done' to finish.\n")

    #  running Input loop
    while True:
        stock = input("Enter stock symbol (AAPL, TSLA, GOOG, MSFT): ").upper()  #initialize the  stock symbol

        if stock == "DONE":  # Stop condition
            break

        if stock not in stock_prices:
            print("Stock not available in our price list.\n")
            continue

        # Quantity input with error handling
        try:
            # ENTER THE  quantity of  stock
            quantity = int(input("Enter quantity: "))
            if quantity <= 0:
                print("Quantity must be positive.\n")
                continue
        except ValueError:
            #  if  the  user type  invalid number  here to user  request to  ask the  valid  number type
            print("Please enter a valid number.\n")
            continue

        #Update portfolio and calculate value
        #update the  portfolio
        portfolio[stock] = portfolio.get(stock, 0) + quantity     # update the portfolio dictionary 
        value = stock_prices[stock] * quantity
        total_investment += value  #calculate the value of update portfolio

#print the confirmation message whenever the user adds a stock
        print(f"Added: {stock} x {quantity} shares = ${value}\n") #user adds a stock if they want

    # display porfolio summary
    print("\n*********************DISPLAY SUMMARY*****************")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        print(f"{stock}: {qty} shares x ${price} = ${value}")#Print stock summary for example 5share x$180=$900

    print(f"\nTotal Investment Value: ${total_investment}") #print the total investment value of each stock detail

    # save to file
   #open file in portfolio.txt
    with open("portfolio.txt", "w") as file:  # create a file portfolio.txt
       #heading portfolio summary
        file.write("Portfolio Summary\n")   
        file.write("-----------------\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            file.write(f"{stock}: {qty} shares x ${price} = ${value}\n")# write  each stock summary into the file
        file.write(f"\nTotal Investment Value: ${total_investment}")# total investment  value to the  file

    print("\nPortfolio saved to portfolio.txt")   #saved the  stock portfoli tracker to portfolio.txt


if __name__ == "__main__":   # python file is being run 
    main()