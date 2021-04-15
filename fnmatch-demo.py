import fnmatch
from fnmatch import fnmatchcase
import os

del list_files():
        for f in os.listdir("."):
            if fnmatch.fnmatch(f, ".txt"):
                print("Text files", f)

            if fnmatch.fnmatch(f, ".rb"):
                print("Ruby files", f)

            if fnmatch.fnmatch(f, ".yml"):
                print("Yaml files", f)

            if fnmatch.fnmatch(f, ".py"):
                print("Python files", f)

list_files()

players = ["Jose Altuve 2B", "Carlos Correa SS", "Alex Bregman 3B", "Scooter Gennett 2B"]

second_base_players = [player for player in players if fnmatchcase(player, "* 2B")]

print(second_base_players)


