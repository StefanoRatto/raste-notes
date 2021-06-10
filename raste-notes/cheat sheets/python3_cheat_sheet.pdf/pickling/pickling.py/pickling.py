import pickle

dict1 = {"a" : 100,
        "b" : 200,
        "c" : 300}

list1 = [400,
        500,
        600]

print(dict1)
print(list1)

out_file = open("save1.pkl", "wb")

pickle.dump(dict1, out_file, pickle.HIGHEST_PROTOCOL)
pickle.dump(list1, out_file, pickle.HIGHEST_PROTOCOL)

out_file.close()

print("-------------------------")

in_file = open("save1.pkl", "rb")

dict2 = pickle.load(in_file)
list2 = pickle.load(in_file)

in_file.close()

print(dict2)
print(list2)
