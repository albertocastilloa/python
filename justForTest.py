# Write your count_first_letter function here:
def count_first_letter(names):
  letters = {}
  for i in names.keys():
    if i[0] not in letters:
      letters[i[0]] = len(names[i])
    else:
      letters[i[0]] += len(names[i])
  return letters

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}