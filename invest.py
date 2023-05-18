import time

# input investment amount 
amount = float(input("Enter amount:N "))
# 10 percent convert to decimal
percentage = 0.10  # 10% profit per 5 minutes

while True:
    # multiply amount and percentage
    total = amount * percentage
    
    # Update the total investment amount
    amount += total
    
    # Print the current investment amount
    print(f" 10% add to amount: N{amount:,.2f}")
    
    # Wait for 5 hours
    time.sleep(20)  # 5 minutes