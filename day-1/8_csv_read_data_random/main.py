import random
import csv

fruits = [
    "apple", "banana", "cherry", "date", "fig",
    "grape", "kiwi", "lemon", "mango", "nectarine",
    "orange", "papaya", "peach", "pear", "pineapple",
    "plum", "pomegranate", "raspberry", "strawberry", "watermelon"
]


prices = [12.99, 5.49, 23.75, 8.30, 15.00, 3.99, 19.45, 7.25, 11.60, 29.99]

fruit_with_prices = []

for fruit in fruits:
    fruit_with_price = (fruit, random.choice(prices))
    fruit_with_prices.append(fruit_with_price)

with open("fruits.csv", "w", newline="") as file:
    writer = csv.writer(file)

    for fruit_with_price in fruit_with_prices:
        writer.writerow(fruit_with_price)



