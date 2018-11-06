import urllib.request

path = 'https://www.maine.gov/sos/cec/elec/data/absentee1116.txt'

# save website data into a HTTResponse object.
contents = urllib.request.urlopen(path)

print(type(contents))

# save file object as a list of byte literals
book = contents.readlines(1000)
print(type(book))
print(book[10])

decoded_str = book[10].decode("utf-8")
print(str(decoded_str))

seer = (decoded_str).rstrip().split('|')
print(seer, "\n")

print
for element in seer:
    print(element)
