import pickle

#writes to pickle file to store mildex as dictonary
#Must be in dictionary format {'Mildex' : int }
def writeIndex(newMildex):
    with open ('resources/mildex.pkl', 'wb') as f:
        pickle.dump(newMildex,f)

def ReadIndex():
    with open('resources/mildex.pkl', 'rb') as f:
        return pickle.load(f)

def resetIndex():
    zeroIndex = {'Mildex' : 0}
    with open ('resources/mildex.pkl', 'wb') as f:
        pickle.dump(zeroIndex,f)
  