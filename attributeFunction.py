how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

counter = 0
for i in how_many_s:
  if hasattr(i, "count"):
    print(i)
    print(i.count("s"))
    print("======")