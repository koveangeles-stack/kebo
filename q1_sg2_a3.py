i = "Rat (鼠 / Shǔ)"
ii = "Ox (牛 / Niú)"
iii = "Tiger (虎 / Hǔ)"
iv = "Rabbit (兔 / Tù)"
v = "Dragon (龙 / Lóng)"
vi = "Snake (蛇 / Shé)"
vii = "Horse (马 / Mǎ)"
viii = "Goat (羊 / Yáng)"
ix = "Monkey (猴 / Hóu)"
x = "Rooster (鸡 / Jī)"
xi = "Dog (狗 / Gǒu)"
xii = "Pig (猪 / Zhū)"

birthyear = int(input("Enter your birth year: "))

def yearcalc():
    remainder = int(birthyear % 12)

    return remainder


if birthyear < 1900:
    print("Please input a year after 1900")

if birthyear >= 1900:
    remainder = yearcalc()
    if remainder == 1:
        print(f"Your Chinese Zodiac Sign is: {x}")
    elif remainder == 2:
        print(f"Your Chinese Zodiac Sign is: {xi}")

    elif remainder == 3:
        print(f"Your Chinese Zodiac Sign is: {xii}")

    elif remainder == 4:
        print(f"Your Chinese Zodiac Sign is: {i}")

    elif remainder == 5:
        print(f"Your Chinese Zodiac Sign is: {ii}")

    elif remainder == 6:
        print(f"Your Chinese Zodiac Sign is: {iii}")

    elif remainder == 7:
        print(f"Your Chinese Zodiac Sign is: {iv}")

    elif remainder == 8:
        print(f"Your Chinese Zodiac Sign is: {v}")

    elif remainder == 9:
        print(f"Your Chinese Zodiac Sign is: {vi}")

    elif remainder == 10:
        print(f"Your Chinese Zodiac Sign is: {vii}")

    elif remainder == 11:
        print(f"Your Chinese Zodiac Sign is: {ix}")