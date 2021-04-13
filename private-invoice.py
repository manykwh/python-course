class Invoice:
    def __init__(self, client, total):
        self.__client = client
        self.__total = total

    def formatter(self):
        return f'{self.__client} owes: ${self.__total}'

google = Invoice('Google', 100)
print(google.formatter())


