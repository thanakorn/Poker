'''
Created on 11/1/2013

@author: Thanakorn
'''

def poker(hands):
    "Return the best hand : poker([hand1,hand2,...]) => hand"
    return max(hands, key=hand_rank)
    
def hand_rank(hand):
    return
    
def test():
    "Test case for function poker"
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7D 7C".split()
    
    assert poker([sf,fk,fh]) == sf
    assert poker([fk,fh]) == fk
    assert poker([fh,fh]) == fh
    assert poker([sf]) == sf
    assert poker([sf] + 99*[fk]) == sf
    
    print "Test pass"
    
    
if __name__ == "__main__":
    print test()
    