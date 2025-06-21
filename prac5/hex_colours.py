# Constant dictionary mapping color names to hexadecimal codes
COLOR_TO_HEX = {
    "crimson": "#dc143c",
    "coral": "#ff7f50",
    "darkorchid": "#9932cc",
    "deepskyblue": "#00bfff",
    "forestgreen": "#228b22",
    "gold": "#ffd700",
    "hotpink": "#ff69b4",
    "indigo": "#4b0082",
    "khaki": "#f0e68c",
    "lavender": "#e6e6fa"
}
# Prompt user for color name and convert input to lowercase for case-insensitive comparison
color_name = input("Enter color name: ").lower()
while color_name != "":
    if color_name in COLOR_TO_HEX:
        # Print the color name in title case and its corresponding hex code
        print(f"{color_name.title()} is {COLOR_TO_HEX[color_name]}")
    else:
        # Handle invalid color name input gracefully
        print("Invalid color name")
    # Prompt for the next input
    color_name = input("Enter color name: ").lower()