s = input()
t = input()

def can(s, t):
  if s == t:
    return True
  if len(t) > 0:
    if t[-1] == 'A' and can(s, t[:-1]):
      return True
    if t[0] == 'B' and can(s, t[:0:-1]):
      return True

  return False

print(1 if can(s, t) else 0)