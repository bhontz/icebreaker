"""
    Class supporting the creation of a simple two endpoint API
"""
import json, sys, csv

class ICEBreaker():
    def __init__(self):
        self.count = -1
        self.lstNames = [] # list of player names, strings
        self.lstQuestions = [] # list of icebreaker questions, strings
        self.__populateLists()
        return

    def __del__(self):
        del self.lstNames
        del self.lstQuestions
        del self
        return

    def __populateLists(self):
        """
            Load the class lists from CSV files found within the assets folder
        """
        try:
            fp = open("assets/names.csv", "r")
        except IOError as detail:
            print("unable to open file %s for READ - details:%s" % ("assets/names.csv", detail))
            sys.exit(1)
        else:
            reader = csv.reader(fp)
            self.lstNames = list(reader)
            del reader
            fp.close()
            del fp

        try:
            fp = open("assets/questions.csv", "r")
        except IOError as detail:
            print("unable to open file %s for READ - details:%s" % ("assets/questions.csv", detail))
            sys.exit(1)
        else:
            reader = csv.reader(fp)
            self.lstQuestions = list(reader)
            del reader
            fp.close()
            del fp

        if self.lstNames != [] and self.lstQuestions != []:
            self.count = len(self.lstNames) * len(self.lstQuestions)

    def getCount(self):
        """
            Returns the count of player * question combinations.
            Allows the UI to determine the random range of selections.
        """
        return self.count

    def getQuestion(self, item):
        """
            returns a JSON structure containing a player, question, bg and fg color
            parameter 'item' has to range from 0 to self.count - 1, and determines what to return.
            Note that this assumes that the NAMES file record structure is as follows:
            name, #htmlfgcolor, #htmlbgcolor
            See the example names.csv included within the assets file of this project.
        """
        d = dict()

        if item >= 0 and item <= self.count:
            d["name"] = self.lstNames[(item // len(self.lstQuestions))][0]
            d["question"] = self.lstQuestions[(item % len(self.lstQuestions))][0]
            d["fg"] = self.lstNames[(item // len(self.lstQuestions))][1]
            d["bg"] = self.lstNames[(item // len(self.lstQuestions))][2]

        return json.dumps(d)

if __name__ == '__main__':
    """
        Some testing going on here ...
    """
    obj = ICEBreaker()
    print("count:{}".format(obj.count))
    print("len names:{}".format(len(obj.lstNames)))
    print("len questions:{}".format(len(obj.lstQuestions)))
    print(obj.lstNames)
    print(obj.lstQuestions)
    print(obj.getQuestion(14))