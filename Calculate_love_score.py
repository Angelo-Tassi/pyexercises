

def calculate_love_score(name1, name2):
    name_ensamble = name1+name2
    lowernames = name_ensamble.lower()
    print(lowernames)
    true = "true"
    love = "love"
    count_true = []
    count_love = []
    for letter in (true):
        if letter in lowernames :
            count_true.append(letter)
    for char in (love):
        if char in lowernames:
            count_love.append(char)

    print(f"Lovescore = {len(count_true)}{len(count_love)}")



calculate_love_score("Oronzo Cana", "Genoveffa Piluzzi")
