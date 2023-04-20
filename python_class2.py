message = "Lorem ipsumdolar sit amet, consectetur adipiscing elit. Duis et euismod nisl. Nulla facilisi. Aliqum euismod lectus ac ipsum cursus, vel aliquam elit semper. Nullam elementum massa quis quam. "

words = message.lower().replace(".","").replace(".","").split(" ")

# dictionary = capture the key/ value  pair
wordCount ={
    "lorem" : "1",
    "ipsum" : "2",
    "dolor" : "1",
    "sit" : "1",
    "amet" : "1",
    "consectetur" : "1",
    "adipiscing" : "1",
    "elit" : "3",
    "Duis" : "1",
    "et" : "1",
    "euismod" : "2",
    "nisl" : "1",
    "nulla" : "1",
    "facilisi" : "1",
    "aliquam" : "2",
    "lectus" : "1",
    "ac" : "1",
    "cursus" : "1",
    "vel" : "1",
    "semper" : "1",
    "nullam" : "1",
    "elementum" : "1",
    "massa" : "1",
    "quis" : "1",
    "quam" : "1",
}

userInput =input('enter a word: ')

if (userInput in wordCount):
    print(wordCount.get(userInput))
else:
    print('Word not found')
    
#key = words inside of message variable
#values = number of times that word occura / loop

# if/else
# print function that will display how many times the word occured
# print function that will output a message saying the word did not occur
#)

# transform message into a dictionary
# loop through this message and count everytime a specific word ipsum
# if the user entern ipsum, the program should tell us how many times ipsum occurs
# if the word does not exist, it should tells us word is not there/ doesm't exist
 
#print(words)

