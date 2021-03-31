def greeting(first, last):
    def full_name():
        return "{0} {1}".format(first, last)
    print("Hello, {0}".format(full_name()))
    # interesting scope issue here!

greeting("James", "Capozzoli")

