#appending in a list
list1 = [1,2,3]
list2 = [4,5,6]
for x in list2:
  list1.append(x)
print(list1)
#use set to remove duplicate values
duplist = [1,2,3,4,5,6,6,4,3,2,]
print(set(duplist))
#Dictionary
dict1 = {"firstname":"Sanjit","lastname":"Roy"}
dict1["firstname"]="anmol"
print(dict1["firstname"])
print(dict1.get("firstname"))
#Print all key names in the dictionary, one by one:
for x in dict1:
    print(x)
#Print all values in the dictionary, one by one:
for values in dict1.values():
    print(values)
#Loop through both keys and values, by using the items() function:
for key, value in dict1.items():
    print("key:{} & value:{}".format(key, value))
#Check if Key Exists