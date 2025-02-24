import pandas


# functions goes here
def int_check(question):
    """checks that the user enter an integer. """

    error = "Oops - please enter an integer. "

    while True:
        try:
            # Return the response if it's an integer
            response = int(input(question))
            return response

        except ValueError:
            print(error)


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """checks that the user enter th full word
        or the first letter of a word from a list of valid response"""

    while True:

        response = input(question).lower()

        for item in valid_answers:

            # check if the response is the entire word
            if response == item:
                return item

            # check if it's the first letter
            elif response == item[:num_letters]:
                return item

        print(f"Please choose an option from {valid_answers}")

    # main routine goes here


# main routine starts here

# initialize variable / non-default options for string checker
payment_ans = ['cash', 'credit']

# Ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

# tickets total sold
tickets_sold = 0
# Credit card surcharge (currently 5%)
CREDIT_SURCHARGE = 0.05

# lists to hold tickets details
all_names = []
all_tickets_costs = []
all_surcharge = []

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_tickets_costs,
    'Surcharge': all_surcharge
}

# loop for testing purposes...
while True:
    print()

    # ask user for their name
    name = not_blank("Name: ")  # replace with call to 'not blank' function!
    # if name is exit code, break out of loop

    if name == "xxx" and tickets_sold > 0:
        break
    elif name == "xxx":
        print("You need to sell at least one ticket")
        continue

    # ask for their age and check if it's between 12 and 120
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    # child ticket price is (7.50)
    elif 12 <= age < 16:
        ticket_price = CHILD_PRICE

    # adult ticket price is (10.50)
    elif 16 <= age < 65:
        ticket_price = ADULT_PRICE

    # senior citizen ticket (6.50)
    elif 65 <= age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

    tickets_sold += 1

    # ask users for their payment method (cash/ credit/ ca/ cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)

    if pay_method == "cash":
        surcharge = 0

    # if paying with credit, calculate surcharge
    else:
        surcharge = ticket_price * CREDIT_SURCHARGE

    # add name, ticket cost and surcharge
    all_names.append(name)
    all_tickets_costs.append(ticket_price)
    all_surcharge.append(surcharge)

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate the total /table from dictionary
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# work out the total paid and total profit
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()
# Print the data frame without the index
mini_movie_frame = mini_movie_frame.set_index('Name')
print(mini_movie_frame)
print()
print(f"Total Paid: ${total_paid:.2f}")
print(f"Total Profit: ${total_profit:.2f}")
