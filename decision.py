temperature = float(input("Temperature? "))

# if temperature <= 60:
#     print("Wear a hat")
#     print("And a jacket")
#     # if no tab, python gets mad. SPACING IS IMPORTANT!
# else:
#     if temperature >= 90:
#         print("Wear sunscreen")
#     else:
#         if temperature == 72:
#             print("Perfect weather!")
#         else:
#             print("Wear a t-shirt")

if temperature < 60:
  print("Wear a jacket")
elif temperature > 90: #else if
  print("Wear sunscreen")
elif temperature == 72: #else if
  print("Perfect weather!")
else:
  print("Wear a t-shirt")

print("have a nice day!")