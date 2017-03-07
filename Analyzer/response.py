class Response:
    def __init__(self):
        self.text = ""
        self.vote = ""

    def changeText(self, text):
        self.text = text

    def changeVote(self, vote):
        self.vote = vote