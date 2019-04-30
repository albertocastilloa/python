authors = "Audre Lorde, William Carlos Williams, Gabriela Mistral, Jean Toomer, An Qi, Walt Whitman, Shel Silverstein, Carmen Boullosa, Kamala Suraiyya, Langston Hughes, Adrienne Rich, Nikki Giovanni"

author_names = authors.split(',')
print(author_names)
print("----")



author_last_names = []
a = [] 

for i in range(len(author_names)):
  a.append(author_names[i].split(" "))

for x in a:
  for y in x:
    if x[-1] not in author_last_names:
      author_last_names.append(x[-1])

print(author_last_names)