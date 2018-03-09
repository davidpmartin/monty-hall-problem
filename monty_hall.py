# Monty Hall Problem Simulator | Created by David Martin
#
# -------------------------------------------------------
#
# Purpose: This program is to illustrate the probabilistic truth's of the Monty Hall problem.
# In this brain teaser, a contestant on a game show is presented with 3 doors, one of which hides a car, and the others
# each hide a goat. The contestant is asked to pick the door that they think hides the car.
#
# After making their choice, the host then selects one of the doors hiding a goat, reveals it to the contestant, and
# then asks them whether they would like to change their selection to the remaining door that they didn't pick.
# The conclusion presented along with this problem is that switching doors is always the statistically better choice.
#
# Most people are inclined to think that each door has equal probability throughout the entirety of the thought
# experiment, therefore the strategy of switching doors should not provide a higher change of selecting the car.
# This is in fact false; the initial odds are 1/3 for each door, but once the goat door has been revealed, the remaining
# unselected door now has a 2/3 chance, and is thus switching to it is the statistically superior choice.

# -------------------------------------------------------

from random import randint


def sim_prizedoor(nsim):
    # To simulate a prize door, randomly select from 3 values
    prize_doors = []
    for i in range(nsim):
        prize_doors.append(randint(0, 2))
    return prize_doors


def sim_guess(nsim):
    # To simulate a contestant guess, randomly select from 3 values
    guesses = []
    for i in range(nsim):
        guesses.append(randint(0, 2))
    return guesses


def goat_door(prize_doors, guesses):
    # Reveal one of the goat doors (cannot be the prize door)
    goat_doors = []
    for i in range(len(guesses)):

        # Define possible doors and remove the prize door as an option
        doors = [0,1,2]
        doors.remove(prize_doors[i])

        if not prize_doors[i] == guesses[i]:
            # If the prize door and the guess aren't the same, then also remove the guess door as an option
            doors.remove(guesses[i])
            goat_doors.append(doors[0])
        else:
            # If they are the same, both remaining doors are goat doors, so pick randomly
            goat_doors.append(doors[(randint(0, 1))])
    return goat_doors


def switch_guess(guesses, goat_doors):
    # Switch the guess to the option that isn't the original guess, or the revealed goat door
    new_guesses = []
    for i in range(len(guesses)):

        # Define possible doors, and remove the guess and revealed door as options
        guess = [0,1,2]
        guess.remove(guesses[i])
        guess.remove(goat_doors[i])

        # Guess is switched to the remaining door
        new_guesses.append(guess[0])
    return new_guesses


def win_percentage(guesses, prize_doors):
    # Calculate the win percentage (correct guesses/total guesses * 100)
    correct = 0
    for i in range(len(guesses)):
        if guesses[i] == prize_doors[i]:
            correct += 1
    return correct/len(guesses)*100


# Define the number of simulations to run
sim_num = 10000

# Randomly generate our guesses and prize doors for x simulations
prize_doors = sim_prizedoor(sim_num)
guesses = sim_guess(sim_num)

# Simulate revealing the doors, and switching to the new door.
goat_doors = goat_door(prize_doors, guesses)
new_guesses = switch_guess(guesses, goat_doors)

# Generate and display the results for both scenarios
nochange_result = win_percentage(guesses,prize_doors)
print("The probability of winning over" , sim_num, "simulations when NOT changing the door is:",'{0:.2f}'.format(nochange_result))

change_result = win_percentage(new_guesses,prize_doors)
print("The probability of winning over", sim_num, "simulations when changing door  is:",'{0:.2f}'.format(change_result))