weather = "sunny"

if weather == "sunny":
    activity = "go for a walk"
elif weather == "rainy":
    activity = "play video games"
else:
    activity = None

print(f"We should {activity}!") if activity else None