import random as r

def kompyuter_oylagan_son(x=10):
    random_number = r.randint(1, x)
    print("Keling o'ylangan sonni topish o'ynaymiz!")
    son = int(input(f"1 dan {x} gacha son o'yladim. Topa olasizmi:\n>>> "))
    i = 0
    while True:
        i += 1
        if son > random_number:
            son = int(input("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling:\n>>> "))
        elif son < random_number:
            son = int(input("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling:\n>>> "))
        else:
            break
    print(f"TOPDINGIZ! {random_number} sonini o'ylagan edim. {i} ta taxmin bilan topdingiz. Tabriklayman!")
    return i

def men_oylagan_son(x=10):
    print(f"1 dan {x} gacha son o'ylang. Men topishga harakat qilaman.")
    input("Son o'ylagan bo'lsangiz istalgan tugmani bosing.")
    low = 1
    high = x
    i = 0
    while True:
        i += 1
        if low != high:
            random_number = r.randint(low, high)
        else:
            random_number = low
        javob = input(f"Siz {random_number} sonini o'yladingiz: To'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-)").lower()
        if javob == "-":
            high = random_number - 1
        elif javob == "+":
            low = random_number + 1
        else:
            break
    print(f"TOPDIM! {random_number} sonini o'ylagansiz. {i} ta taxmin bilan topdim")
    return i

def play(x=10):
    javob = True
    while javob:
        taxminlar_user = kompyuter_oylagan_son(x)
        taxminlar_kompyuter = men_oylagan_son(x)
        if taxminlar_user > taxminlar_kompyuter:
            print(f"Men {taxminlar_kompyuter} ta taxmin bilan topdim va yutdim!")
        elif taxminlar_user < taxminlar_kompyuter:
            print(f"Siz {taxminlar_user} ta taxmin bilan topdingiz va yutdingiz!")
        else:
            print("Durrang!")
        javob = int(input("Yana o'ynaymizmi? Ha(1)/Yo'q(0): "))

play(20)