"""
CP1404 Practical
Hexadecimal Colour Lookup Program
"""

COLOUR_CODES = {
    "ALICEBLUE": "#f0f8ff",
    "ANTIQUEWHITE": "#faebd7",
    "AQUAMARINE": "#7fffd4",
    "BEIGE": "#f5f5dc",
    "BLUEVIOLET": "#8a2be2",
    "CHOCOLATE": "#d2691e",
    "CORAL": "#ff7f50",
    "DARKGREEN": "#006400",
    "FIREBRICK": "#b22222",
    "GHOSTWHITE": "#f8f8ff"
}

print("--- Hexadecimal Colour Code Lookup ---")
print("Available colours are:")
print(", ".join(COLOUR_CODES.keys()))

colour_name = input("Enter a colour name: ").upper()

while colour_name != "":
    try:
        code = COLOUR_CODES[colour_name]
        print(f"The code for {colour_name.title()} is {code}")
    except KeyError:
        print("Invalid colour name.")
    colour_name = input("Enter a colour name: ").upper()

print("Program finished.")