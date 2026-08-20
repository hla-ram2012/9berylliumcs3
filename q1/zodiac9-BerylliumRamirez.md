# Chinese Zodiac Exercise
# Section: 9-Beryllium
# Name: Hugo Lian A. Ramirez
# Date: 08/21/26
# Score: _____

# Requirements:

## A. Ask the user to enter a year of birth

The program asks the user to enter a year of birth. The baseline year is 1900.

## B. Validate user input

The program validates the user inputted year, the inputted year should not be less than 1900.

## C. Invalid Year

If it's less than the year 1900, the program displays an error message and stops.

**Example input and output:**
Enter your birth year: 1800
Invalid Year, it should not be earlier than 1900

## D. Determine the Chinese Zodiac Sign

Chinese Zodiac Signs:
1. Rat (鼠 / Shǔ)
2. Ox (牛 / Niú)
3. Tiger (虎 / Hǔ)
4. Rabbit (兔 / Tù)
5. Dragon (龙 / Lóng)
6. Snake (蛇 / Shé)
7. Horse (马 / Mǎ)
8. Goat (羊 / Yáng)
9. Monkey (猴 / Hóu)
10. Rooster (鸡 / Jī)
11. Dog (狗 / Gǒu)
12. Pig (猪 / Zhū)

***Note: A zodiac sign will recur after each 12 years.***

## E. Consider only the year of birth

The program will only uses the inputted year by the user to display an output.

**Example input and output:**
Enter your birth year: 2000
Your Chinese Zodiac Sign is: Dragon (龙 / Lóng)

# Actual Code:

```python
year = int(input("Enter your birth year: "))
if year < 1900:
    print("Invalid Year, it should not be earlier than 1900")

else:
    zodiac = ["Rat (鼠 / Shǔ)", "Ox (牛 / Niú)", "Tiger (虎 / Hǔ)", "Rabbit (兔 / Tù)", "Dragon (龙 / Lóng)", "Snake (蛇 / Shé)", "Horse (马 / Mǎ)", "Goat (羊 / Yáng)", "Monkey (猴 / Hóu)", "Rooster (鸡 / Jī)", "Dog (狗 / Gǒu)", "Pig (猪 / Zhū)"]
    zodiac_sign = zodiac[(year - 1900) % 12]
    print(f'Your Chinese Zodiac Sign is:, {zodiac_sign}')
```
# Screenshots:

## Valid input
![Valid Zodiac Output](Screenshot-ValidInput-zodiac9-BerylliumRamirez.png)

## Invalid inputt
![Invalid Zodiac Output](Screenshot-InvalidInput-zodiac9-BerylliumRamirez.png)
