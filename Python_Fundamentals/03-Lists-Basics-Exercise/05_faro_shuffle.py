deck_of_cards = input().split()
count_of_shuffles = int(input())

for shuffle in range(count_of_shuffles):
    middle_of_deck = len(deck_of_cards) // 2
    left_deck = deck_of_cards[0:middle_of_deck]
    right_deck = deck_of_cards[middle_of_deck:]
    deck_after_shuffle = []
    for card_index in range(len(left_deck)):
        deck_after_shuffle.append(left_deck[card_index])
        deck_after_shuffle.append(right_deck[card_index])
    deck_of_cards = deck_after_shuffle

print(deck_of_cards)
