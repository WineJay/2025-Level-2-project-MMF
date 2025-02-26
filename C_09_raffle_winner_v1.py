import pandas
import random
# lists to hold tickets details
all_names = ["A", "B", "C", "D", "E"]
all_tickets_costs = [7.50, 7.50, 10.50, 10.50, 6.50]
all_surcharge = [0, 0, 0.53, 0.53, 0]

mini_movie_dict = {
    'Name': all_names,
    'Ticket Price': all_tickets_costs,
    'Surcharge': all_surcharge
}

# create dataframe / table from dictionary
mini_movie_frame = pandas.DataFrame(mini_movie_dict)

print(mini_movie_frame.to_string(index=False))

# choose random winner...
winner = random.choice(all_names)

# find index of winner (position in list)
winner_index = all_names.index(winner)
print("winner", winner, "list position", winner_index)

# retrieve ticket price and surcharge
winner_ticket_price = all_tickets_costs[winner_index]
winner_surcharge = all_surcharge[winner_index]

# total won
total_won = winner_ticket_price + winner_surcharge

# winner announcement
print(f"The lucky winner is {winner}. Their ticket worth ${total_won:.2f} is free!")

print()
