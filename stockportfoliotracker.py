portfolio=[]
def add_stock():
	name=input("Enter the name of the stock :")
	shares=int(input("Enter the number of shares :"))
	buy_price=float(input("Enter the buying price per share :"))
	current_price=float(input("Enter the current price per share :"))
	investment=shares*buy_price
	current_value=shares*current_price
	profit_loss=current_value-investment
	stock={
	              "Name":name,
	              "Shares":shares,
	              "Buyprice":buy_price,
	              "current value":current_price,
	              "Total investment":investment,
	              "Profit/loss":profit_loss
	}
	portfolio.append(stock)
	print(f"{name} is added succesfully")
def view_stock():
			if not portfolio:
				print("portfolio is empty")
				return
			total_investment=0
			total_price=0
			total_profit=0
			print("_"*60)
			print("\n your portfolio :")
			for stock in portfolio:
			    print(f"{stock['Name']}| Shares:{stock['Shares']}| Buy:{stock['Buyprice']}| Current:{stock['current value']}|profit/loss={stock['Profit/loss']}|")
			total_investment+=stock['Total investment']
			total_price+=stock['Buyprice']
			total_profit+=stock['Profit/loss']
			print("_"*60)
			print(f"Total investment for the shares:{total_investment}")
			print(f"Total buying price :{total_price}")
			print(f"Total profit gained in the stock:{total_profit}")
			print("_"*60)
while True:
			    print("=====Stock Portfolio Tracker====")
			    print("1.add stock")
			    print("2.view stock")
			    print("3.Exit")
			    choice=input("Enter the choice :")
			    if choice=="1":
			        add_stock()
			    elif choice=="2":
			         view_stock()
			    elif choice=="3":
			         print("Bye its great time with you")
			         break
			    else:
			         print("Invalid File and doesnot exists")
