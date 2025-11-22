import sys
if len(sys.argv) != 2:
    print("ERROR: Please provide temperature in Celsius as a parameter.")
    print("Usage: python3 temp_alert.py <TEMPERATURE>")
    sys.exit(1)
temperature = float(sys.argv[1])
print("\n=== INPUT RECEIVED FROM JENKINS PARAMETERS ===")
print("Temperature (°C):", temperature)
if temperature < 15:
    alert = "Cold"
elif 15 <= temperature <= 30:
    alert = "Normal"
else:
    alert = "Hot"
print("\n===== TEMPERATURE ALERT =====")
print("Condition:", alert)
