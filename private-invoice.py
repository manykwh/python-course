class Invoice:
    def __init__(self, client, total):
        self.__client = client
        self.__total = total

    def formatter(self):
        return f'{self.__client} owes: ${self.__total}'

    @property
    def client(self):
        return self.__client

    @client.setter
    def client(self, client):
        self._client = client

    @property
    def total(self):
        return self.__total


google = Invoice("Google", 100)

print(google.formatter())
print(google.client)
google.client = "Yahoo"
print(google.client)
# notice how the client has not actually changed, it's still google
google.client("Yahoo")
print(google.client)

