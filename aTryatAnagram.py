
#! python3

# listOfWords = ['silent', 'lent', 'nelcop', 'silents', 'silentes', 'ilents', 'xxz']
checkWord = 'silent'

with open(r'C:\Users\nope\OneDrive\Python script\2nd time\google-10000-english.txt.txt', 'r') as file:
    words = file.read()
listOfWords = words.split('\n')

for elem in listOfWords:
    # use each words exactly once
    if len(checkWord) != len(elem):
        continue
    for char in checkWord:
        if char in elem:
            continue
        else:
            break
    else:
        print(elem)
print('Finished')
