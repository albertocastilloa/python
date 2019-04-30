love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

print(love_maybe_lines)
love_maybe_lines_stripped = []

for i in range(len(love_maybe_lines)):
  love_maybe_lines_stripped.append(love_maybe_lines[i].strip())

love_maybe_full = '\n'.join(love_maybe_lines_stripped)
print(love_maybe_full)