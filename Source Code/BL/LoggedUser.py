

def init():
    global LoggedUserId
    LoggedUserId = None

def getLoggedUserId():
    print("GET")
    return LoggedUserId

def setLoggedUserId(val):
    print("SET")
    global LoggedUserId
    LoggedUserId = val


