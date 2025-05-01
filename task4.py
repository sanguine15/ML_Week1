# Simple Average Temperature Calculator

temperatures = []

for i in range(5):
    temp = float(input(f"Enter temperature for day {i+1}: "))
    temperatures.append(temp)

average = sum(temperatures) / 5

print(f"\nAverage Temperature: {average:.2f}°C")
