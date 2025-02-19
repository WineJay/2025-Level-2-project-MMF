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

# loop for testing purposes...
while True:
    print()

    # ask user for their name
    name = not_blank("Name: ")  # replace with call to 'not blank' function!
    # ask for their age and check if it's between 12 and 120
    age = int_check("Age: ")

    # output error message / success message
    if age < 12:
        print(f"{name} is too young")
        continue
    elif age > 120:
        print(f"{name} is too old")
        continue

    else:
        pass

    # ask users for their payment method (cash/ credit/ ca/ cr)
    pay_method = string_check("Payment method: ", payment_ans, 2)
    print(f"{name} has brought a ticket ({pay_method})")
