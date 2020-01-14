class Token:
    tokenIndex = 1
    authorID = ""
    publicationID = ""
    participation = 0
    pubParticipation = 0
    value = 0

    def __init__(self, autorID, publicationID, participation, pubParticipation, value):
        self.tokenIndex = Token.tokenIndex
        Token.tokenIndex += 1
        self.authorID = autorID
        self.publicationID = publicationID
        self.participation = participation
        self.pubParticipation = pubParticipation
        self.value = value

    def __str__(self):
        return 'ID: ' + str(self.tokenIndex) + ', author: ' + self.authorID + ', publication: ' + self.publicationID
