print("Hello I'll be calculating your tip percentage today.")
bill = input("How much was your food?") 
percent = input("What percentage do you want to tip?")

new_percent = float(percent) / 100

new_bill = int(bill) *  float(new_percent)
print(new_bill)








