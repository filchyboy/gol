# Query Builder

length = 625

# for each in range(length):
#     print(f"c{each} INT NOT NULL,")

# string = ""
# for each in range(length):
#     string = string + "c" + str(each) + ", "

# print(string)

string2 = ""
for each in range(length):
    string2 = string2 + "%s, "

print(string2)