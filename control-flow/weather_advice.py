#!/usr/bin/env python3

weather_condition = input("What's the weather like today? (sunny/rainy/cold): ")

sunny = "sunny"
rainy = "rainy"
cold = "cold"


if weather_condition == sunny:
   print("Wear a t-shirt and sunglasses.")
elif rainy:
   print("Don't forget your umbrella and a raincoat.")
elif cold:
   print("Make sure to wear a warm coat and a scarf.")
else:
   print("Sorry, I don't have recommendations for this weather")

