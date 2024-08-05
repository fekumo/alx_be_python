#!/usr/bin/env python3

FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    try:
        temp_input = input("Enter the temperature (e.g., 32F or 0C): ").strip()
        if temp_input[-1].upper() == 'F':
            temperature = float(temp_input[:-1])
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius:.2f}°C")
        elif temp_input[-1].upper() == 'C':
            temperature = float(temp_input[:-1])
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit:.2f}°F")
        else:
            raise ValueError("Invalid temperature unit. Please enter a temperature followed by 'F' or 'C'.")
    except ValueError as e:
        print(f"Invalid input. {str(e)} Please enter a numeric value for the temperature.")

if __name__ == "__main__":
    main()

