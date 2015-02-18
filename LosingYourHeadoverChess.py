"""I was reading this book "Introduction to Computer Science Using Python: A Computational Problem-Solving Focus by Charles Dierbach" and one of the program development problems discussed is
Losing Your Head over Chess.
The game of chess is generally believed to have been invented in India in the sixth century for a ruling king by one of his subjects. The king was supposedly very delighted with teh game and
asked the subject what he wanted in return. The subject, being clever, asked for one grain of wheat on the first square, two grains of wheat on the second square, four grains of wheat on the
third square, and so forth, doubling the amount on each next square. The king thought that this was a modest reward for such an invention. However, the total amount of wheat would have been
more than 1000 times the current world production.
Develop and test a Python Program that calculates how much wheat would be in pounds, using the fact that a grain of wheat weighs approximately 1/7000 of a pound."""

# I thought this is interesting so I checked the current wheat production and am going to compare the weight of reward to world's current wheat production.

#using for loop
def calculate_grains_for():
    grains = 1
    for i in range(1, 64):
        grains *= 2
    return grains

#using while looop
def calculate_grains_while():
    grains = 1
    squares_left = 63
    while squares_left > 0:
        grains *= 2
        squares_left -= 1
    return grains

