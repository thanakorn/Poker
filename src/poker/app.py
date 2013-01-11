'''
Created on 11/1/2013

@author: Thanakorn
'''

def poker(hands):
    "Return the best hand : poker([hand1,hand2,...]) => hand"
    return max(hands, key=hand_rank)
    
def hand_rank(hand):
    