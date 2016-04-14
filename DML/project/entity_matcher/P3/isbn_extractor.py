import re

isbn = re.compile("(?:[0-9]{3}-)?[0-9]{1,5}-[0-9]{1,7}-[0-9]{1,6}-[0-9]")

matches = []

with open("elec_pairs_stage1.txt") as isbn_lines:
    for line in isbn_lines:
        matches.extend(isbn.findall(line))
        
print len(matches)