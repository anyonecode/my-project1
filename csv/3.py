csvfile =[['Aditya', 'IT', '2', '9.3'],['Sagar', 'SE', '1', '9.5']]
filtered_data = []
for lst in csvfile:
    if "sagar" in lst[1]:
        filtered_data.append(lst)

# short version, checks if the word "gold" is in a particular list
filtered_data = list(filter(lambda x: "sagar" in x[1], csvfile))
print(filtered_data)
