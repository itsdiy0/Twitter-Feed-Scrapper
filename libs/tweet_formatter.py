import json

dic = {}
def checkIfQute(tweet):
    if tweet.count("@")<2:
        return True
    return False

def findTheOriginalTweet(tweet):
    second_occurrence_count = 0
    for index, item in enumerate(tweet):
        if item.startswith("@"):
            second_occurrence_count += 1
            if second_occurrence_count == 2:
                second_occurrence_index = index
                break
    return second_occurrence_index

def storeJSON(tweets):
    json_data = json.dumps(tweets, indent=2)
    file_path = "data.json"
    with open(file_path, "a") as json_file:
        json_file.write(json_data)

def outputData(data):
    ID = 0
    for i in data:
        if checkIfQute(i):
            s = i.split("\n")
            s = s[:-4]
            try:
                s.pop(3)
                s.pop(2)
            except:
                continue
            s = ['\n' if item == '' else item for item in s]
            dic.update({ID:
                    {
                    "Account name":s[0]
                    ,"Account ID":s[1],
                    "Tweet":''.join(s[2:])
                     }
                    })
        else:
            i = i.split("\n")
            qI = findTheOriginalTweet(i)
            originalTweet = i[qI-1:]
            quotedTweet = i[0:qI-1]
            try:
                quotedTweet.pop(2)
                quotedTweet.pop(2)
                originalTweet = originalTweet[:-4]
                originalTweet.pop(2)
                originalTweet.pop(2)
            except:
                continue
            dic.update({ID:{
            "Account name" : quotedTweet[0],
            "Account ID" : quotedTweet[1],
            "Qoute tweet" : ''.join(quotedTweet[2:]),
            "Qouted from" :{
                "Acount name" : originalTweet[0],
                "Account ID" : originalTweet[1],
                "Original tweet" : originalTweet[2:]
            }
        }})

        ID+=1
    storeJSON(dic)
