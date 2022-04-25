"""
Full Name: Francesco Lezano
Teacher: Bro. Codling
Title: 01 Checkpoint (heart_rate)
"""
# --------------------------------------------------------------------------------
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart's maximum rate.
"""

# string --> input 'x'
age = int(input("Please enter your age: "))

maximum_rate = 220 - age
range_1 = maximum_rate * 0.65
range_2 = maximum_rate * 0.85

print("When you exercise to strengthen your heart, you should keep")
print(f"your heart rate between {range_1:.0f} and {range_2:.0f} beats per minute.")