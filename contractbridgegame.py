def contract_bridge_game(cards):
    suit_order = ['spades', 'hearts', 'diamonds', 'clubs']
    rank_map = {
        'ace': 'A',
        'queen': 'Q',
        'king': 'K',
        'jack': 'J'
    }
    priority = {'A': 0, 'Q': 1, 'K': 2, 'J': 3, 'x': 4}
    suits = {suit: [] for suit in suit_order}
    for rank, suit in cards:
        symbol = rank_map.get(rank, 'x')
        suits[suit].append(symbol)
    result = ""
    for suit in suit_order:
        if not suits[suit]:
            result += "-"
        else:
            suits[suit].sort(key=lambda x: priority[x])
            result += "".join(suits[suit])
    return result
