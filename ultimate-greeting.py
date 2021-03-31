def greeting(time_of_day, *args, **kwargs):
    print(f"Hi {' '.join(args)}, I hope that you are having a good {time_of_day}.")

    if kwargs:
        print("Your tasks for the day are: ")
        for key, val in kwargs.items():
            print(f"{key}->{val}")

greeting("Morning", "James", "Capozzoli", first="Take pupper out", second="Tell pupper he is good boi", third="Reinforce pupper that is good boi")

