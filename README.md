# Description
This script converts human size or tallness from feet and inches to centimeters and vice versa. The user must specify a command line argument that can be either "i" or "m" for imperial and metric respectively, that will decide from which unit system the user is inputting. The second and third arguments must be either feet and inches or meters and centimeters depending on what was chosen.

# Usage
To use the script, save it to a file (e.g. "conversion.py") and run it from the terminal with the desired arguments.

    python conversion.py [i|m] feet inches|meters centimeters

# Examples
Convert 5 feet 11 inches to meters and centimeters:

    python conversion.py i 5 11

Output:

    5'11" = 1m 80cm

Convert 1 meter 80 centimeters to feet and inches:

    python conversion.py m 1 80

Output:

    1m 80cm = 5'11"

# Requirements

    Python 3.x

# Notes

    - The script will exit with an error message if invalid arguments are provided.
    - The script will only work for converting human size or tallness. It is not intended for converting other units of measurement.
