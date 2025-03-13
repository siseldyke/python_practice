# slicing = creatre a substring by extracting elements from another string
# indexing[] or slice()
#[start:stop:step]

# name = "Stefan I"
# first index[0] is inclusive, will always contain the first, the stoping [for example 2 just does ST] is exculsive, will excule what is at said index
# python wil always assume the starting point is zero if you type things like [:3]
# first_name = name[:6]
# can do the opposite as well [6:] will provide all after the start
# last_name = name[6:]
# funky_name = name [0:8:2]
# step method prints IE every first character with one, every second with 2 etc can leave start and stop empty [::2] must provide colons though
# reversed_name = name[::-1]
# print(reversed_name)

website1 = "http://google.com"
website2="http://wikipedia.com"
# everything has positive positions, starting with zero, and negative, starting with -1
slice = slice(7,-4)

print(website1[slice])
print(website2[slice])