def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

school_a_x = create_x(2, 0.8, 1, 5)
school_b_x = create_x(2, 0.8, 2, 5)

xxxx = zip(school_a_x, school_b_x)
print(xxxx)
middle_x =  [ (a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]

print(school_a_x)
print
print(school_b_x)
print
print(middle_x)