import databaseFunctions
import re

def unicodingString(string):
    return string.encode("ascii", "ignore")
def removeURLs(string):
    return re.sub(r"(?:\@|https?\://)\S+", "", string)
def removeSpecialCharacters(string):
    return re.sub(r'([^\s\w] | [(?<!\d>)\.(?!\d)])', " ", string)
    #return re.sub(r'[^\w]', ' ', string)
def removeDates(string):
    return re.sub(r'([0-9]{1,2}[/,\-,.][0-9]{2}[/,\-,.][0-9]{2,4})', " ", string)
def stripExtraSpaces(string):
    return re.sub('\s+', " ", string).strip()
def stringLower(string):
    return string.lower()
def stringToList(string):
    return str(string).split(" ")
def cleanPrice(string):
    priceList = re.findall('(\d+(\.\d+)?)', string.split(":")[len(string.split(":")) - 1])
    try:
        price = priceList[0][0]
    except:
        price = 1
    return price
def removeExtraDots(string):
    string = re.sub(r'\.{2,}', '.', string)
    string = re.sub(r'([A-Za-z])\.([A-Za-z])', r'\1 \2', string)
    string = re.sub(r'([0-9])\.([A-Za-z])', r'\1 \2', string)
    string = re.sub(r'([A-Za-z])\.([0-9])', r'\1 \2', string)
    return string.strip(' .')
def statementLength(string):
    return len(string)
def removingNonASCII(dataFrame):
    dataFrame['tweet'] = dataFrame['tweet'].map(lambda x: unicodingString(x))
    return dataFrame
def removingURLs(dataframe):
    dataframe['tweet'] = dataframe['tweet'].map(lambda x: removeURLs(x))
    return dataframe
def removingSpecialCharacters(dataFrame):
    dataFrame['tweet'] = dataFrame['tweet'].map(lambda x: removeSpecialCharacters(x))
    return dataFrame
def removingDates(dataFrame):
    dataFrame['tweet'] = dataFrame['tweet'].map(lambda x: removeDates(x))
    return dataFrame
def stripingExtraSpaces(dataFrame):
    dataFrame['tweet'] = dataFrame['tweet'].map(lambda x: stripExtraSpaces(x))
    return dataFrame
def removingExtraDots(dataFrame):
    dataFrame['tweet'] = dataFrame['tweet'].map(lambda x: removeExtraDots(x))
    return dataFrame
def loweringString(dataFrame):
    dataFrame['tweet'] =dataFrame['tweet'].map(lambda x: stringLower(x))
    return dataFrame
def tokenizingString(dataFrame):
    dataFrame['tweet'] = dataFrame['tweet'].map(lambda x: stringToList(x))
    return dataFrame
def cleaningPrice(dataFrame):
    dataFrame['tweet'] = dataFrame['tweet'].map(lambda x: cleanPrice(x))
    return dataFrame
def calculatingStringLength(string):
    return len(string)
def removeQuotes(x):
    wordList = []
    for word in x:
        wordList.append(word.strip("'"))
    return wordList

def getCleanTweets(dataFrame):
    dataFrame = removingNonASCII(dataFrame)
    dataFrame = removingURLs(dataFrame)
    dataFrame = removingSpecialCharacters(dataFrame)
    dataFrame = removingDates(dataFrame)
    dataFrame = stripingExtraSpaces(dataFrame)
    dataFrame = removingExtraDots(dataFrame)
    dataFrame = loweringString(dataFrame)
    dataFrame = tokenizingString(dataFrame)
    dataFrame["tweet"] = dataFrame["tweet"].astype(str)
    dataFrame["tweet"] = dataFrame["tweet"].map(lambda x: x[1:len(x) - 1].split(", "))
    dataFrame["tweet"] = dataFrame["tweet"].map(lambda x: removeQuotes(x))
    dataFrame["length"] = dataFrame["tweet"].map(lambda x: calculatingStringLength(x))
    dataFrame = dataFrame[dataFrame.length <= 300]
    return dataFrame



def main():
    obj = databaseFunctions.DatabaseFunction('abc')
    df = obj.getSQLData()
    df = getCleanTweets(df)
    print(df['tweet'])

if __name__ == '__main__':
    main()