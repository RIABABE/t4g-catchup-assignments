first_name = "Rashida"
last_name = "Ahmed"
full_name = f"{first_name} {last_name}".title()  
cohort = "T4G"  
age = 20
favorite_topic = "Variables and f-strings".replace("Variables", "Data Types")  
current_week = 3  

weeks_left = 12 - current_week


print("=" * 40)
print(f"          PROFILE CARD")
print("=" * 40)
print(f"Name:         {full_name}")
print(f"Cohort:       {cohort}")
print(f"Age:          {age}")
print(f"Fav Topic:    {favorite_topic}")
print(f"Current Week: {current_week}")
print("-" * 40)
print(f"Weeks left:   {weeks_left} (in 12-week program)")
print("=" * 40)
