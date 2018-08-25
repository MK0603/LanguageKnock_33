# coding: UTF-8
from LanguageKnock_30 import makeMecabPattern


class extractVersMethods:

    def loopNovel(self, novelListS):
        versAllList = []
        for sentenseListS in novelListS:
            versAllList.append(self.loopSentense(sentenseListS))
        return versAllList
    
    def loopSentense(self, sentenseListS):
        versList = []
        for sentenseList in sentenseListS:
            pos = self.extractVers(sentenseList)
            if pos != None:
                versList.append(pos)
        return versList
    
    def extractVers(self, sentenseList):
        if sentenseList["pos"] == "名詞" and sentenseList["pos1"] == "サ変接続":
            return self.extractBase(sentenseList)
    
    def extractBase(self, sentenseList):
        return sentenseList["base"]


if __name__ == '__main__':
    cal = extractVersMethods()
    novelListS = makeMecabPattern()
    ans = cal.loopNovel(novelListS)
    print (ans)
