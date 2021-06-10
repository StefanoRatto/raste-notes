import pickle

from Player import Player

items = ["axe", "sword", "gun"]

my_obj = Player(1, "Jeff", 100.00, items)

print(my_obj)

with open("save2.pkl", "wb") as outfile:
    pickle.dump(my_obj, outfile, pickle.HIGHEST_PROTOCOL)
    outfile.close()

print("-----------------")

new_obj = None

with open("save2.pkl", "rb") as infile:
    new_obj = pickle.load(infile)
    infile.close()

print(new_obj)
