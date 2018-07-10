import os

def redup():
    return

def reddown():
    return

def greenup():
    return

def greendown():
    return

def blueup():
    return

def bluedown():
    return

def cclear():
    return

def restart():
    return

def action():
    return

K = {
    273 : redup, # Up / 2
    274 : reddown, # Down / 3
    276 : greendown , # Left / 4
    275 : greenup , # Right / 5
    97 : restart , # A / 6
    49 : blueup , # 1 / 7
    50 : bluedown , # 2 / 6
    51 : action , # 3 / 6
    52 : action , # 4 / 6
    53 : cclear , # 5 / 6
    54 : action , # 6 / 6
    55 : action , # 7 / 6
    56 : action , # 8 / 6
    57 : action , # 9 / 6
}

key = 0
works = ''
should = ''

while key < 300:
    if key in K.keys():
        print( str(key) + ' is avalible and runs ' + str(K[key]) + '()' )
        works = works + str(key) + ', '
    else:
        print( str(key) + ' is not in dictionary')
    key = key + 1

for value in K:
    should = should + str(value) + ', '

print(works)
print(should)
