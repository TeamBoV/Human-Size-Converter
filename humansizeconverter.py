import sys

def convert_imperial_to_metric(feet, inches):
    """Converts feet and inches to meters and centimeters."""
    total_inches = feet * 12 + inches
    meters = total_inches * 0.0254
    centimeters = int(meters * 100) % 100
    meters = int(meters)
    return (meters, centimeters)

def convert_metric_to_imperial(meters, centimeters):
    """Converts meters and centimeters to feet and inches."""
    total_inches = (meters * 100 + centimeters) * 0.393701
    feet = int(total_inches // 12)
    inches = int(total_inches % 12)
    return (feet, inches)

# Parse command line arguments
if len(sys.argv) != 4:
    print("Usage: python conversion.py [i|m] feet inches|meters centimeters")
    sys.exit()

unit_system = sys.argv[1]
if unit_system == "i":
    feet = int(sys.argv[2])
    inches = int(sys.argv[3])
    (meters, centimeters) = convert_imperial_to_metric(feet, inches)
    print(f"{feet}'{inches}\" = {meters}m {centimeters}cm")
elif unit_system == "m":
    meters = int(sys.argv[2])
    centimeters = int(sys.argv[3])
    (feet, inches) = convert_metric_to_imperial(meters, centimeters)
    print(f"{meters}m {centimeters}cm = {feet}'{inches}\"")
else:
    print("Invalid unit system. Use 'i' for imperial or 'm' for metric.")
