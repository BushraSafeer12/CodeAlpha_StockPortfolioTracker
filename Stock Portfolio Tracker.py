Stocks = {
    'NVIDIA': 150,
    'Amazon': 220,
    'Netflix': 700,
    'Coca-Cola': 70
}
Total = 0
with open("portfolio.txt", "a") as file:
    file.write("\n--- New Portfolio ---\n")
    print("Available stocks:", list(Stocks.keys()))
    while True:
        stock_name = input("Enter stock name: ").strip()
        if stock_name not in Stocks:
            print("Stock not found")
        else:
            try:
                quantity = int(input("Enter quantity: "))

                if quantity > 0:
                    stock_price = Stocks[stock_name]
                    Investment = stock_price * quantity
                    print("Investment:", Investment)

                    Total = Total + Investment

                    file.write("Stock: " + stock_name + "\n")
                    file.write("Quantity: " + str(quantity) + "\n")
                    file.write("Investment: " + str(Investment) + "\n")
                else:
                    print("Quantity must be positive")
            except ValueError:
                print("Enter a valid quantity")

        choice = input("Add another stock (yes/no)? ").lower()
        if choice != "yes":
            break
    file.write("Total Investment: " + str(Total) + "\n")

print("Total Investment:", Total)
print("Portfolio saved in portfolio.txt")
