#import necessary packages
from PIL import Image
import cv2
from mss import mss
import numpy as np
import pytesseract
import time
import pokerUtilities as pu

#variables
threshold = 0.99

#populate deck
fullDeck = pu.getDeck()

#scan test image for each card
img_rgb = cv2.imread("test4.png")
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

holeCards = []
boardCards = []

#search the image for every card in the deck, add to respective list
for card in fullDeck:
    boardTemplate = cv2.imread(card.boardImagePath, 0)
    holeTemplate = cv2.imread(card.holeImagePath, 0)
    w, h = boardTemplate.shape[::-1] 
    x, j = holeTemplate.shape[::-1] 
    resBoard = cv2.matchTemplate(img_gray,boardTemplate,cv2.TM_CCOEFF_NORMED)
    resHole = cv2.matchTemplate(img_gray,holeTemplate,cv2.TM_CCOEFF_NORMED)
    locBoard = np.where( resBoard >= threshold)
    locHole = np.where( resHole >= threshold)

    for pt in zip(*locBoard[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
        boardCards.append(card)

    for pt in zip(*locHole[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + x, pt[1] + j), (0,255,0), 2)
        holeCards.append(card)

print("\nBOARD CARDS:")
for card in boardCards:
    print(card.name)


print("\nHOLE CARDS:")
for card in holeCards:
    print(card.name)

print("\nHAND PROBABILITIES")


#probabilities of landing any hand

cv2.imwrite("res3.png", img_rgb)


#go through array once and add to hole and board lists
#then math and thats literally it


