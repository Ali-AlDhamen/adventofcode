def replace_j(cards):
    count = {}
    for i in set(cards):
        if i != 'J':
            count[i] = cards.count(i)
    if count == {}:
        return 'J'
    return max(count, key=count.get)

def getKind(cards):
    new_card = cards.replace('J', replace_j(cards))
    count = []
    for i in set(new_card):
        count.append(new_card.count(i))
    count.sort(reverse=True)
    if count == [1,1,1,1,1]:
        return "High card"
    elif count == [2,1,1,1]:
        return "One pair"
    elif count == [2,2,1]:
        return "Two pair"
    elif count == [3,1,1]:
        return "Three of a kind"
    elif count == [3,2]:
        return "Full house"
    elif count == [4,1]:
        return "Four of a kind"
    elif  count == [5]:
        return "Five of a kind"


def sortRanks(cards):
    strength = {
        "A": 13,
        "K": 12,
        "Q": 11,
        "J": 10,
        "T": 9,
        "9": 8,
        "8": 7,
        "7": 6,
        "6": 5,
        "5": 4,
        "4": 3,
        "3": 2,
        "2": 1,
        "J": 0
    }
    for i in range(len(cards)):
        for j in range(i+1, len(cards)):
            if cards[i][2] < cards[j][2]:
                cards[i], cards[j] = cards[j], cards[i]
            elif cards[i][2] == cards[j][2]:
                for k in range(5):
                    if strength[cards[i][0][k]] < strength[cards[j][0][k]]:
                        cards[i], cards[j] = cards[j], cards[i]
                        break
                    elif strength[cards[i][0][k]] > strength[cards[j][0][k]]:
                        break
    return cards


with open("in.txt", 'r') as f:
    kinds = {
        "Five of a kind": 10,
        "Four of a kind": 9,
        "Full house": 8,
        "Three of a kind": 7,
        "Two pair": 6,
        "One pair": 5,
        "High card": 4
    }
    
    cards_bids = [(x.split()[0], int(x.split()[1]), "no kind") for x in f.read().splitlines()]
    for i, card in enumerate(cards_bids):
        cards_bids[i] = (card[0], card[1], kinds[getKind(card[0])])
        
    ans = 0
    for rank, card in enumerate(sortRanks(cards_bids)):
        rank = len(cards_bids) - rank
        ans += rank * card[1]
    print(ans)
        
        
    

