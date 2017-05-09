import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

height = 30
width = 120

def calculateFeatureVector(filename):
    img = loadAndResizeImg(filename)

    return getFeatureVector(img)


def loadAndResizeImg(filename):
    img = Image.open(filename)
    img_resized = img.resize((int(img.width/(1.3*(img.height/height))), height))
    if img_resized.width > width:
        img_resized = img_resized.resize((width, height))

    G = np.full((height,width), True, dtype=bool)
    npImg = np.asarray(img_resized)

    # Where we set the RGB for each pixel
    G[npImg > 0.5] = True  # white pixels
    G[npImg <= 0.5] = False  # black pixels

    return G


def getLowerContur(column):
    for i in range(len(column)):
        if column[i] == False:
            return i
    return 0


def getUpperContur(column):
    for i in reversed(range(len(column))):
        if column[i] == False:
            return i
    return height-1


def getBWTransitions(column):
    counter = 0
    for i in range(len(column)-1):
        if column[i] != column[i+1]:
            counter = counter +1

    return counter


def getFractionOfBlackPxInWindow(column):
    counter = 0
    for i in range(len(column)):
        if column[i] == False:
            counter = counter +1

    return counter/len(column)


def getFractionOfBlackPxBtwLcAndUc(column, lc, uc):
    if lc == None or uc == None:
        return None
    counter = 0
    upperBound = uc + 1 if uc +1 <=height else height
    for i in range(lc,upperBound):
        if column[i] == False:
            counter = counter +1

    return counter/len(range(lc,upperBound))


def getGradientDifferenceLcUc(column):
    pass


def calculateFeatures(column):
    features = []
    #Slides from Exercise 7 slides , slide 14
    features.append(getLowerContur(column))
    features.append(getUpperContur(column))
    features.append(getBWTransitions(column)/7)
    features.append(getFractionOfBlackPxInWindow(column))
    features.append(getFractionOfBlackPxBtwLcAndUc(column, features[0], features[1]))
    features[0] = float(features[0]/(height-1))
    features[1] = float(features[1]/(height-1))

    return features
    # features.append(getGradientDifferenceLcUc(column))


def getFeatureVector(a):
    featureList = list()
    for i in range(width):
        featureList.append(calculateFeatures(a[:,i]))
    return featureList


