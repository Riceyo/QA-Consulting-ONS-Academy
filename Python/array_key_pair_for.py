array = {"tom": "London", "dick": "Cardiff", "harry": "Manchester"}

for loop in array:
    print(array[loop])

array["dick"] = "Newport" # update value in the "dick" index

print("")

for loop in array:
    print(array[loop])
