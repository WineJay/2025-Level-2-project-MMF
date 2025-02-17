# Functions goes here
def string_check(question, valid_answers =('yes', 'no') , num_letters = 1):
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


payment_ans = ['cash', 'credit']

want_instructions = string_check("Do you want to see the instructions?")
print(f"You chose {want_instructions}")
pay_method = string_check("Payment method: ", payment_ans, 2)
print(f"You chose {pay_method}")
