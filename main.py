def whether(temp):
  if temp > 7:
    return "Warm"
  else: 
    return "Hot"

user = float(input("enter the current temperature: "))
print(whether(user))