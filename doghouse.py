def loop_using_while():
    dog_house = ["a","b","c","d"] # Put dog names here
    counter = 0
    while counter < len(dog_house):
        print(dog_house[counter])
        counter += 1
    
    return [dog_house, counter]
