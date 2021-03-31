def greeting(**kwargs):
    if(kwargs):
        print(f"Hi {kwargs['first']} {kwargs['last']}, have a great day!")
    else:
        print("Hi Guest!")

greeting(first = "James", last = "Capozzoli")

