"""
virtual G
"""

import random

def generate_player_name():
    return ''.join(random.choice(string.ascii_uppercase) for _ in range(5))

def generate_player_country():
    countries = ['USA', 'UK', 'Germany', 'France', 'Spain', 'Italy', 'Netherlands', 'Brazil', 'Argentina', 'Australia']
    return random.choice(countries)

def generate_virtual_game_info():
    player_name = generate_player_name()
    player_country = generate_player_country()
    player_credits = random.randint(1000, 10000)
    return player_name, player_country, player_credits

player_name, player_country, player_credits = generate_virtual_game_info()
print("Player Name:", player_name)
print("Player Country:", player_country)
print("Player Credits:", player_credits)
