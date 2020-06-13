from cowpy import cow
from colorama import Fore, init
import random

init(autoreset=True)
colors = [Fore.RED, Fore.GREEN, Fore.BLUE, Fore.YELLOW, Fore.LIGHTMAGENTA_EX]

# Create a cow with a dead eyes
cow1 = cow.Moose(eyes='dead')
msg = cow1.milk('Dzien dobry, wszyscy zginiemy')

random.seed()
print(colors[random.randint(0, len(colors))] + msg)

