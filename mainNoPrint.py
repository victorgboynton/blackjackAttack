import csv
import random
#from flask import Flask

listLocation = 0


#Class definition, includes a print function for testing.
class cards:
    def __init__(self,name,cValue,cValue2):
        self.name = name
        self.cValue = cValue
        self.cValue2 = cValue2

    def __repr__(self):
        return "\n"+str(self.name) + " cValue: " + str(self.cValue) + " cValue2: " + str(self.cValue2)

nCards = 52
#Initalizes the list for the cards, then fills in the list with the class opjects.
cardList = []
with open("textOfCards.csv", newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        cardList.append(cards(row[0],int(row[1]),int(row[2])))

#Shuffles the "deck"
cardList = random.sample(cardList,k=len(cardList))

class player:
    def __init__(self,hand,bank):
        self.hand = hand
        self.bank = bank
class dealer:
    def __init__(self,hand):
        self.hand = hand

# To aviod the return of "none" from a class object, external print function

def handValue(person):
    v = 0
    for x in range(len(person.hand)):
        v += person.hand[x].cValue
    return v

def deal(person):
    global listLocation
    person.hand.append(cardList[listLocation])
    listLocation += 1

def hiLow(person):
    for x in range(len(person.hand)):
        if person.hand[x].cValue == 1:
            return 1
        else:
            return 0

def checkNatural(person):
    if (person.hand[0].cValue + person.hand[0].cValue2 + person.hand[1].cValue + person.hand[1].cValue2) == 22:
        return 1
    else:
        return 0

def clearHand(player,dealer):
    player.hand = []
    dealer.hand = []



def splitCard():
    pass

def doubleDown():
    pass

def payout(person,amount):
    person.bank += amount
        
def main():
    hPlayer = player([],500)
    cDealer = dealer([])
    players = [cDealer,hPlayer]
    while hPlayer.bank != 0:
        bet = 0
        bet = int(input())
        if bet > hPlayer.bank:
            bet = int(input())
        for x in range(0,2):
            deal(hPlayer)
            deal(cDealer)

        # Goes through the options for a natural, then manages bet as required.
        if checkNatural(hPlayer) and not checkNatural(cDealer):
            payout(hPlayer,1.5*bet)
            clearHand(hPlayer,cDealer)
            continue
        elif checkNatural(cDealer) and checkNatural(hPlayer):
            payout(hPlayer,bet)
            clearHand(hPlayer,cDealer)
            continue
        elif checkNatural(cDealer):
            payout(hPlayer,-(bet))
            clearHand(hPlayer,cDealer)
            continue
        


        stand = ''
        while handValue(hPlayer) <= 21 and stand != 'stand' and stand != 'Stand':
            stand = str(input())
            if stand == 'stand' or stand =='Stand':
                pass
            elif stand == 'hit' or stand=='Hit':
                deal(hPlayer)
            else:
                continue
            if handValue(cDealer) < 17:
                deal(cDealer)
            else:
                pass

        
        pScore = 0
        cScore = 0
        if hiLow(hPlayer):
            if handValue(hPlayer)+10 <= 21:
                pScore = handValue(hPlayer) + 10
            else:
                pScore = handValue(hPlayer)
        else:
            pScore = handValue(hPlayer)

        if hiLow(cDealer):
            if handValue(cDealer)+10 <= 21:
                cScore = handValue(cDealer) + 10
            else:
                cScore = handValue(cDealer)
        else:
            cScore = handValue(cDealer)

        if pScore > 21:
            payout(hPlayer,-(bet))
        elif cScore > 21:
            payout(hPlayer,bet)
        elif cScore >= pScore:
            payout(hPlayer,-(bet))
        elif pScore > cScore:
            payout(hPlayer,bet)

        clearHand(hPlayer,cDealer)
        #Finds out if the player would like to quit
        choice = str(input())
        while choice:
            if choice == 'Yes' or choice == 'Y' or choice == 'y' or choice == 'yes': break
            elif choice =='no' or choice =='n' or choice =='No' or choice=='N':
                #Negitive walk amount
                if hPlayer.bank-500 <= 0:
                    exit()
                #Positive walk amount
                else:
                    exit()
            else: continue
            continue



        clearHand(hPlayer,cDealer)
        if hPlayer.bank == 0:
            exit()
        else:
            continue


    
    #if handValue(hPlayer)
    #print('For a total of:')
    #handValue(hPlayer)
if __name__ == '__main__':
    main()
