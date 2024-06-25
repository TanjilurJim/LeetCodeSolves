def find_card_position(cards, moves, query):
    # Convert cards to a dictionary for easier access
    card_positions = {card[0]: (card[1], card[2]) for card in cards}
    card_ids = {(card[1], card[2]): card[0] for card in cards}

    for move in moves:
        card_id, from_row, from_col, to_row, to_col = move

        # Update the position in the card_positions dictionary
        if (to_row, to_col) in card_ids:
            # Move the existing card down one row
            card_ids[(to_row + 1, to_col)] = card_ids.pop((to_row, to_col))
            card_positions[card_ids[(to_row + 1, to_col)]] = (to_row + 1, to_col)

        # Move the card to the new position
        card_ids[(to_row, to_col)] = card_ids.pop((from_row, from_col))
        card_positions[card_id] = (to_row, to_col)

        # Move other cards in the original column up one row
        for row in range(from_row + 1, len(cards)):
            if (row, from_col) in card_ids:
                card_ids[(row - 1, from_col)] = card_ids.pop((row, from_col))
                card_positions[card_ids[(row - 1, from_col)]] = (row - 1, from_col)

    return list(card_positions[query])


# Example usage
cards = [[1, 1, 0], [3, 0, 0], [6, 0, 1], [4, 0, 2], [5, 2, 0], [7, 1, 1], [2, 1, 2]]
moves = [[6, 0, 1, 2, 0]]
query = 6

print(find_card_position(cards, moves, query))  # Output: [2, 0]
