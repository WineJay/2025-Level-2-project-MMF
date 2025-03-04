import pandas
import random


# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    return f"{decoration * 3} {statement} {decoration * 3}"


def string_check(question, valid_answers=('yes', 'no'), num_letters=1):
    """checks that the user enter th full word
    or the first letter of a word from a list of valid response"""

    while True:

        response = input(question).lower()

        for entry in valid_answers:

            # check if the response is the entire word
            if response == entry:
                return entry

            # check if it's the first letter
            elif response == entry[:num_letters]:
                return entry

        print(f"Please choose an option from {valid_answers}")

    # main routine goes here


def instructions():
    print(make_statement("Instructions", "ℹ️"))
    """Instructions for using MMF"""

    print('''
    
For each ticket holder enter...
- Their name
- Their age
- The payment method (cash / credit)

The program will record the ticket-sale and calculate the ticket cost (and the profit).

Once you have either sold all of the tickets or entered the exit code ('xxx'), the program will display the ticket sales
information and write the data to a text file.
 
it will also choose one lucky ticket holder wins the draw (their ticket is free).

    ''')


def not_blank(question):
    """Checks that a user response is not blank"""

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again.\n")


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


def currency(x):
    """formats number as currency ($#,##)"""
    return "${:.2f}".format(x)


# Main Routine goes here

# initialise tickets numbers
MAX_TICKETS = 5
tickets_sold = 0

# initialize variable / non-default options for string checker
payment_ans = ['cash', 'credit']

# Ticket price list
CHILD_PRICE = 7.50
ADULT_PRICE = 10.50
SENIOR_PRICE = 6.50

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

# programme main heading
print(make_statement("Mini-Movie Fundraiser Program", "🍿"))

# Ask user if they want to see the instructions and display them if necessary
# Display them if necessary
print()
want_instructions = string_check("Do you want to see the instructions?")
if want_instructions == "yes":
    instructions()

print()

# loop to get name, age and payment details
while tickets_sold < MAX_TICKETS:
    print()
    # ask user for their name
    name = not_blank("Name: ")  # replace with call to 'not blank' function!

    # if name is exit code, break out of loop
    if name == "xxx" and tickets_sold > 0:
        break
    elif name == "xxx":
        print("oops, you need to sell at least one ticket")
        continue

        # ask for their age and check if it's between 12 and 120
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    # child ticket price is (7.50)
    elif age < 16:
        ticket_price = CHILD_PRICE

    # adult ticket price is (10.50)
    elif age < 65:
        ticket_price = ADULT_PRICE

    # senior citizen ticket (6.50)
    elif age < 121:
        ticket_price = SENIOR_PRICE

    else:
        print(f"{name} is too old")
        continue

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

    tickets_sold += 1

# end of the ticket loop

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

# calculate the total /table from dictionary
mini_movie_frame['Total'] = mini_movie_frame['Ticket Price'] + mini_movie_frame['Surcharge']
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# work out the total paid and total profit
total_paid = mini_movie_frame['Total'].sum()
total_profit = mini_movie_frame['Profit'].sum()

# choose random winner...
winner = random.choice(all_names)

# find index of winner (position in list)
winner_index = all_names.index(winner)

# work out the total paid and total profit
#
ticket_won = mini_movie_frame.at[winner_index, 'Total']
profit_won = mini_movie_frame.at[winner_index, 'Profit']

# currency formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)
# Print the data frame without the index

mini_movie_string = (mini_movie_frame.to_string(index=False))

total_paid_string = f"Total Paid: ${total_paid:.2f}"
total_profit_string = f"Total Profit: ${total_profit:.2f}"

# winner announcement
lucky_winner_string = f"The lucky winner is {winner}."f"Their ticket worth ${ticket_won:.2f} is free!"
final_total_paid_string = f"Total paid is now ${total_paid - ticket_won:.2f}"
final_profit_string = f"Total profit is now ${total_profit - profit_won:.2f}"

if tickets_sold == MAX_TICKETS:
    num_sold_string = make_statement(f"You have sold all the tickets - "
                                     f"ie: {MAX_TICKETS} tickets", "-")
else:
    num_sold_string = make_statement(f"You have sold {tickets_sold} / "
                                     f"{MAX_TICKETS} tickets.", "-")

# Additional strings / heading
heading_string = make_statement("Mini Movie Fundraiser", "=")
ticket_detail_heading = make_statement("Ticket Details", "-")
raffle_heading = make_statement("---Raffle Winner ---", "-")
adjusted_sales_heading = make_statement("Adjusted Sales & Profit",
                                        "-")
adjusted_explanation = (f"We have given away a ticket worth ${ticket_won:.2f}which means \n"
                        f"our sales have decreased by ${ticket_won:.2f} and our profit \n"
                        f"decreased by ${profit_won:.2f}")

# list of strings to be outputted / written to file
to_write = [heading_string, "\n",
            mini_movie_string, "\n",
            total_paid_string,
            total_profit_string, "\n",
            raffle_heading,
            lucky_winner_string, "\n",
            adjusted_sales_heading,
            adjusted_explanation, "\n",
            final_total_paid_string, "\n",
            final_profit_string, "\n",
            num_sold_string]

# Print area
print()
for item in to_write:
    print(item)

# create file to hold data (add .txt extension)
file_name = "MMF_Ticket_details"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# write the item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")
