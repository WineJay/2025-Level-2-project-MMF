# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")


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


def instructions():
    make_statement("Instructions", "ℹ️")
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


# Main Routine goes here

# initialise tickets numbers
MAX_TICKETS = 5
tickets_sold = 0

# initialize variable / non-default options for string checker
payment_ans = ['cash', 'credit']


# Ask user if they want to see the instructions and display them if necessary

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions?")
if want_instructions == "yes":
    instructions()

print()

while tickets_sold < MAX_TICKETS:
    print()
    # ask user for their name
    name = not_blank("Name: ")  # replace with call to 'not blank' function!

    # if name is exit code, break out of loop
    if name == "xxx":
        break
        # ask for their age and check if it's between 12 and 120
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"Sorry you are too young")
        continue
    elif age > 120:
        print(f"?? That looks like a typo (too old)")
        continue

    else:
        pass

    # ask users for their payment method (cash/ credit/ ca/ cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has brought a ticket ({pay_method})")

    tickets_sold += 1

if tickets_sold == MAX_TICKETS:
    print(f"You have sold all the tickets (ie: {MAX_TICKETS} tickets")
else:
    print(f"You have sold {tickets_sold} / {MAX_TICKETS} tickets.")
