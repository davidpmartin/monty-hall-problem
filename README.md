# Monty Hall Problem


### Purpose
This short program is designed to simulate both possible scenarios in the Monty Hall problem and illustrate the difference in probability.

In this brain teaser, a contestant on a game show is presented with 3 doors, one of which hides a car, and the others each hide a goat. The contestant is asked to pick the door that they think hides the car. After making their choice, the host then selects one of the doors hiding a goat, reveals it to the contestant, and then asks them whether they would like to change their selection to the remaining door that they didn't pick. The conclusion presented along with this problem is that switching doors is always the statistically better choice.

Most people are inclined to think that each door has equal probability throughout the entirety of the thought experiment, therefore the strategy of switching doors should not provide a higher chance of finding the car. This however is not correct, as it fails to account for the change in probability value for each door that occurs when host reveals the goat.


### How it works
If we present each door as A B C, and assume each have equal probably of hiding the car, we can say that at the beginning of the experiment the probably for each car is 1/3. Suppose that door A is selected, that leaves the follow possibilites:

P1: {A} = 1/3

P2: {B or C} = 2/3 (with B = 1/3, C = 1/3)

When a goat door is revealed, lets say its B, the probably of that door hiding the car drops to 0, however the probability for the set {B or C} still remains 2/3, meaning door C itself has odds of 2/3. As noted above, this means that changing to the other door will always have a greater chance of revealing the car.

This conclusion is unintuitive for many, however it becomes clear if you instead imagine there being 1000 doors to choose from, all with goats behind them except one that hides the car. The door you pick has odds of 1/1000, and if the host then reveals the goats behind 998 doors excluding your pick plus one other, it becomes obvious that the car is far more likely to be behind the other door.





