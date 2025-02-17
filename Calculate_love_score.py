

def calculate_love_score(name1, name2):
    truelove = "truelove"
    count_letters = []
    for letter in (truelove):
        if letter in name1:
            count_letters.append(letter)
        if letter in name2:
            count_letters.append(letter)

        #print(letter)
        print(count_letters)
        #print(f"i nostri {name1} e {name2} si amano !")

calculate_love_score(name1= "giovanni", name2="giuseppina")
