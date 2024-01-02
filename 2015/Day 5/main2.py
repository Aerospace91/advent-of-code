import re

with open('input.txt', 'r') as h:
    datalines = h.readlines()

count = sum(1 for s in datalines
      if len([x for x in s if x in "aeiou"]) > 2
      and not any(x in s for x in ["ab", "cd", "pq", "xy"])
      and re.search(r"([a-z])\1", s)
 )
print(count)

count = sum(
      1 for s in datalines
      if len(re.findall(r"([a-z]{2}).*\1", s))
      and re.findall(r"([a-z]).\1", s)
 )
print(count)