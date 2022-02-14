"""Write a program that takes as input the probability of a follower being a bot 
   (pbot), the probability of a bot having a username with 8 digits (p8_bot), 
   and the probability of a human having a username with 8 digits (p8_human). 
   The values for these inputs are free for you to choose, but they have to be 
   probabilitites, so they have to be between 0 and 1."""


def bot8(pbot, p8_bot, p8_human):
    p8_digits = (p8_bot * pbot) + p8_human * (1 - pbot)
    pbot_8 = (p8_bot * pbot) / p8_digits
    print(pbot_8)


# you can change these values to test your program with different values
pbot = 0.1
p8_bot = 0.8
p8_human = 0.05

bot8(pbot, p8_bot, p8_human)
