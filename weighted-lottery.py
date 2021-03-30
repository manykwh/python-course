import secrets

weights = { "winning": 1, "losing": 1000 }
other_weights = { "winning":1, "break_even": 2, "losing": 3}

def weighted_lottery(weights):
    win_times = weights["winning"]
    lose_times = weights["losing"]
    even_times = weights["break_even"]

    wheel_of_fortune = []
    for i in range(win_times):
        wheel_of_fortune.append("winning")

    for i in range(lose_times):
        wheel_of_fortune.append("losing")

    for i in range(even_times):
        wheel_of_fortune.append("break_even")

    return secrets.choice(wheel_of_fortune)
