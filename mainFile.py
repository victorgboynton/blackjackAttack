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
def handPrint(person):
    for x in range(len(person.hand)):
        print(person.hand[x].name)
    print('That gives a total of: ' + str(handValue(person)))
    if hiLow(person):
        print('Or, with ace high, '+ str(handValue(person)+10))

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
    print('You\'ve won ' + str(amount) + ' dollars')
        
def main():
    hPlayer = player([],500)
    cDealer = dealer([])
    players = [cDealer,hPlayer]
    while hPlayer.bank != 0:
        bet = 0
        print('You currently have '+ str(hPlayer.bank) + ' dollars.')
        print('How much would you like to bet?')
        bet = int(input())
        if bet > hPlayer.bank:
            print('You don\'t have that amount to bet, please pick again.')
            print('How much would you like to bet?')
            bet = int(input())
        print('You have bet ' + str(bet) + ' dollars, good luck.')
        for x in range(0,2):
            deal(hPlayer)
            deal(cDealer)
        print('Let\'s take a look at your hand: ')
        handPrint(hPlayer)

        # Goes through the options for a natural, then manages bet as required.
        if checkNatural(hPlayer) and not checkNatural(cDealer):
            print('That\'s a natural! You win the hand.')
            payout(hPlayer,1.5*bet)
            clearHand(hPlayer,cDealer)
            continue
        elif checkNatural(cDealer) and checkNatural(hPlayer):
            print('You and the dealer both have naturals.')
            print('You may take your chips back, and start the next hand.')
            payout(hPlayer,bet)
            clearHand(hPlayer,cDealer)
            continue
        elif checkNatural(cDealer):
            print('Looks like the dealer has a natural, sorry.')
            print('You lose your bet, and the next hand shall be dealt.')
            payout(hPlayer,-(bet))
            clearHand(hPlayer,cDealer)
            continue
        


        stand = ''
        while handValue(hPlayer) <= 21 and stand != 'stand' and stand != 'Stand':
            print("Hit or stand?")
            stand = str(input())
            if stand == 'stand' or stand =='Stand':
                print('You chose to stand')
            elif stand == 'hit' or stand=='Hit':
                deal(hPlayer)
                print('Your new hand:')
                handPrint(hPlayer)
            else:
                print('Please type hit or stand')
                continue
            if handValue(cDealer) < 17:
                deal(cDealer)
                print('Dealers new card is: ' + str(cDealer.hand[len(cDealer.hand)-1].name))
            else:
                print("The dealer stands at " + str(handValue(cDealer)))

        
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
            print('You bust')
            payout(hPlayer,-(bet))
        elif cScore > 21:
            print('The dealer has busted.')
            payout(hPlayer,bet)
        elif cScore >= pScore:
            print('The dealer has won the hand.')
            payout(hPlayer,-(bet))
        elif pScore > cScore:
            print('You\'ve won the hand!')
            payout(hPlayer,bet)

        clearHand(hPlayer,cDealer)
        print('Would you like to continue? Y/N?')
        choice = str(input())
        while choice:
            if choice == 'Yes' or choice == 'Y' or choice == 'y' or choice == 'yes': break
            elif choice =='no' or choice =='n' or choice =='No' or choice=='N':
                if hPlayer.bank-500 <= 0:
                    print('You\'ve lost '+str(abs(hPlayer.bank-500))+' dollars. Better luck next time.')
                    exit()
                else:
                    print('You\'ve won '+str(hPlayer.bank-500)+' dollars. Good job!')
                    exit()
            else: print("Please select either Y or N")
            continue



        clearHand(hPlayer,cDealer)
        if hPlayer.bank ==0:
            print('You ran out of money, goodbye.')
            exit()
        else:
            continue


    
    #if handValue(hPlayer)
    #print('For a total of:')
    #handValue(hPlayer)
if __name__ == '__main__':
    main()

