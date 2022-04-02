print("Welcome to Donells tip calculator project!")


print("My Tip Calculator")
while True:
        try:
            ticket_input = float(input("what is the total amount of your bill"))
            tip_total = float(input("what is the total amount of your bill? $")) 
            break
        except ValueError:
            print("Please use numbers and try again.")
            break

while True:
        try:
            gratuity_input = float(input("what percentage of gratuity will you leave today? % "))
            gratuity_total = (gratuity_input)
            break
        except ValueError:
            print("Please use numbers and try again")
            
while True:
    try:
        split_input = float(input("how many people are splitting the bill?"))
        split_total = float(split_input)
        break
    except ValueError:
        print("Please use numbers and try again.")

tax = 0.10
taxed_bill = (ticket_input * tax) + ticket_input
gratuity = taxed_bill * (gratuity_input/100)
grand_total = taxed_bill + gratuity 
each_person_pays = grand_total / split_total

# Final print statement with output stating the grand total of the bill times tax with gratuity.




