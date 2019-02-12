# Monty Hall Problem


### Purpose
This short program is designed to demonstrate the probabilities involved in the famous montly hall problem. It does so by simulating the process for each of the possible scenarios n number of times and then presenting the probabilities of the desired outcome in each case.

In this brain teaser, a contestant on a game show is presented with three doors. Two of the doors hide joke prizes (goats) while one hides a car, and the contestent will get to keep the prize behind the door they pick. After the contestant makes their choice, the host then selects one of the doors hiding a goat, reveals it to the contestant, and then asks them whether they would like to change their selection to the other of the two remaining doors.

Most people's intuition is that each door has equal probability throughout the entirety of the thought experiment, therefore switching doors should not provide a higher chance of finding the car. This however is not correct, as it fails to account for the changing probabilities for each door that occurs when host reveals the goat.


### How it works
If we present the three doors as A, B and C, and assume that each have equal probability of hiding the car from the contestants perspective, we can say that at the beginning of the experiment the probability for each door is 1/3. Suppose that door A is selected by the contestant, that leaves the following possibilities and associated probabilities for the car:

P1 = {A} = 1/3

P2 = {B or C} = 2/3 (with B = 1/3, C = 1/3)


When a goat door is revealed, lets say its door B, the probability that B hides the car drops to 0, however the probability for the set {B or C} still remains 2/3, meaning door C itself now has odds of 2/3. Given this adjustment of probabilities, it follows that the contestent should always abandon their initial choice in favor of the remaining door as it is twice as likely to hide the car. This conclusion is unintuitive for many, as we tend to only account for the individual probabilities of B and C, rather than their collective probability. 

However, this conclusion becomes clear if we instead imagine there being 1000 doors to choose from, all with goats behind them except one that hides the car. The door initially selected has odds of 1/1000, and if the host then reveals the goats behind 998 doors excluding the selected pick plus one other, it becomes obvious that the car is far more likely to be behind the other door than the one we selected.





