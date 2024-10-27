def hide(card_number):
    if len(card_number)==16 and f"{card_number}".isdigit():
        return (f"{card_number[0:2]}************{card_number[12:]}")