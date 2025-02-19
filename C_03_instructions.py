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


# Main Routine goes here

# Ask user if they want to see the instructions and display them if necessary

make_statement("Mini-Movie Fundraiser Program", "🍿")

print()
want_instructions = string_check("Do you want to see the instructions?")
if want_instructions == "yes":
    instructions()

print()
print("program continues...")
