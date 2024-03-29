# Write a function to convert numbers to text numerals
NUM_WORD = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

def text_numeral(num):
    '''
    converts a number into a text numeral
    
    Parameters
    ----------
    num: int
        a positive integer to be converted to a its text numeral

    Returns
    -------
    str
        text numeral of the positive integer (num)
    '''
    text_form = {}
    while num != 0:
        for i in range(len(NUM_WORD)):
            current = (list(NUM_WORD.keys()))[len(NUM_WORD)-1-i]
            if num >= current:
                num -= current
                text_form[(NUM_WORD[current])] = text_form.get(NUM_WORD[current],0)*1 +1
                break
    text = []
    for word in list(text_form.keys()):
        for i in range(text_form[word]):
            text.append(word)
    return " ".join(text)

