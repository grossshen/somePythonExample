import json

def testJson():
    data=[1,1,1,1,1,12,2]
    jsonObject=json.dumps(data)
    print(jsonObject)
def main():
    testJson()
if __name__=='__main__':
    main()
