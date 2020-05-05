
melon_cost = 1.00

def print_payment_status(payment_filename):

    payment_data = open(payment_filename)

    for line in payment_data:
        order = line.split('|')
        full_name = order[1]
        first_name = full_name.split()[0]

        melons_num = float(order[2])
        amt_paid = float(order[3])

        expected_price = melons_num * melon_cost

        print (f"{full_name} paid ${amt_paid:.2f}, expected", f"${expected_price:.2f}") 

    payment_data.close()

print_payment_status("customer-orders.txt")
