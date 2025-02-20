def draw_letters():
    import random
    LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
    }
    draw_pool = []
    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
          draw_pool.append(letter)
    hand = []
    for i in range(10): # wish I had known about .sample before submitting!
        piece_index = random.randint(0,len(draw_pool)-1)
        piece = draw_pool[piece_index]
        hand.append(piece)
        draw_pool.remove(piece)
    return hand

def uses_available_letters(word, letter_bank):
    new_word = word.upper()
    copy_bank = letter_bank.copy()
    for letter in new_word:
      if letter in copy_bank:
        copy_bank.remove(letter)
      else: 
        return False
    return True

def score_word(word):
    word_dict = {
        "A" : 1, 
        "E" : 1, 
        "I" : 1, 
        "O" : 1, 
        "U" : 1, 
        "L" : 1, 
        "N" : 1, 
        "R" : 1, 
        "S" : 1, 
        "T" : 1, 
        "D" : 2, 
        "G" : 2, 
        "B" : 3, 
        "C" : 3, 
        "M" : 3, 
        "P" : 3, 
        "F" : 4, 
        "H" : 4, 
        "V" : 4, 
        "W" : 4, 
        "Y" : 4, 
        "K" : 5, 
        "J" : 8, 
        "X" : 8, 
        "Q" : 10, 
        "Z" : 10
    }
    points = 0
    new_word = word.upper()
    for letter in new_word:
        if letter.isalpha():
            points += word_dict[letter]
    if len(new_word) in range(7,11):
        points += 8
    return points

def get_highest_word_score(word_list):
    highest_word = ["",0]
    for word in word_list:
        score = score_word(word)
        if score > highest_word[1]:
            highest_word[0] = word
            highest_word[1] = score
        elif score == highest_word[1]:
            high_word = highest_word[0]
            if len(high_word) == 10:
                continue
            elif len(word) == 10 or len(word) < len(high_word):
                highest_word[0] = word
    return tuple(highest_word)