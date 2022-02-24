EtoF = {'bread':'pain','wine':'vin','with':'avec','I':'Je',
        'eat':'mange','drink':'bois','John':'Jean','friends':'amis','and':'et',
        'of':'du','red':'rouge'}
FtoE = {'pain':'bread','vin':'wine','avec':'with','Je':'I',
        'mange':'eat','bois':'drink','Jean':'John','amis':'friends','et':'and',
        'du':'of','rouge':'red'}

dicts = {'EnglishToFrench':EtoF,'FrenchToEnglish':FtoE}

# Defined 3 dictionaries above with key/value pairs

def translateWord(word,dictionary):     # Function for translating the individual words
    if word in dictionary.keys():       # to check if the word is present in dictionary 
        return dictionary[word]         # if the key is present then return it's value
    elif word !='':                     # if the word isn't present 
        return '"'+word+'"'             # return the new word within quotes
    return word                         # else return the word

def translate(phrase,dicts,direction):      # function for looking the given phrase over dicts and direction i.e., from FtoE or EtoF
    UCLetters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'  # uppercase letters defined
    LCLetters='abcdefghijklmnopqrstuvwxyz'  # lowercase letters defined
    letters = UCLetters + LCLetters         # letters = containing both UC and LC
    dictionary = dicts[direction]           # we find the value from dicts given the key
    translation = ''
    word = ''
    for c in phrase:            # identifying each letter in the words of the phrase
        if c in letters:        # if the letters are mentioned in 'letters' string
            word = word+c       # we add individual letters again to form the word/phrase again
        else:                                                               # if the letters are not mentioned in 'letters' string
            translation = translation + translateWord(word,dictionary)+c    # if there's a possibility to translate then we translate it and also add 'c' to it i.e., the individual letter
            word=''
    return translation +' '+translateWord(word,dictionary)

print(translate('I drink good red wine, and eat bread 8.',dicts,'EnglishToFrench'))
print(translate('Je bois du vin rouge$.',dicts,'FrenchToEnglish'))