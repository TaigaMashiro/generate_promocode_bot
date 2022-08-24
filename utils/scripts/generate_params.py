def output_params(text: str) -> dict[str: tuple[int, int], str: int]:
    amount_symbols = int(len(text))
    coordinate = (0, 0)
    font_size = 0
    if amount_symbols == 1:
        coordinate = (1150, 2890)
        font_size = 230

    elif amount_symbols == 2:
        coordinate = (1000, 2890)
        font_size = 230

    elif amount_symbols == 3:
        coordinate = (1000, 2890)
        font_size = 230

    elif amount_symbols == 4:
        coordinate = (850, 2900)
        font_size = 220

    elif amount_symbols == 5:
        coordinate = (825, 2900)
        font_size = 210

    elif amount_symbols == 6:
        coordinate = (800, 2900)
        font_size = 200

    elif amount_symbols == 7:
        coordinate = (750, 2900)
        font_size = 190

    elif amount_symbols == 8:
        coordinate = (700, 2900)
        font_size = 180

    elif amount_symbols == 9:
        coordinate = (650, 2900)
        font_size = 170

    elif amount_symbols == 10:
        coordinate = (600, 2900)
        font_size = 160

    elif amount_symbols == 11:
        coordinate = (570, 2900)
        font_size = 160

    elif amount_symbols == 12:
        coordinate = (450, 2900)
        font_size = 160

    elif amount_symbols == 13:
        coordinate = (440, 2900)
        font_size = 160
    if sum(map(str.isupper, text)) <= 3:
        if amount_symbols == 4:
            coordinate = (990, 2900)
            font_size = 230

        elif amount_symbols == 5:
            coordinate = (1000, 2900)
            font_size = 190

        elif amount_symbols == 6:
            coordinate = (870, 2900)
            font_size = 200

        elif amount_symbols == 9:
            coordinate = (650, 2900)
            font_size = 170

        elif amount_symbols == 10:
            coordinate = (700, 2900)
            font_size = 160

        elif amount_symbols == 11:
            coordinate = (650, 2900)
            font_size = 160

        elif amount_symbols == 12:
            coordinate = (600, 2900)
            font_size = 160

        elif amount_symbols == 13:
            coordinate = (550, 2900)
            font_size = 160

    result = {'coordinate': coordinate, 'font_size': font_size}
    return result
