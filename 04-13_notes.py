Script of the Day
  Homework check-in
  Python Practice
  Using Functions
  Logic and Conditionals
  Writing Functions (if time)
Python Practice
    Write a script interest.py which prompts the user for:
    An initial bank balance (principle)
    An annual interest rate
    A number of years
    And then calculates the total earnings and value after that many years (when compounded monthly). 
    Use the formula: A = P(1+r/n)^(nt)
    where A = amount
          P = principal
          r = rate of interest
          n = number of times per year, interest is compounded
          t = time in years
    # example output
    Initial balance: 1000 #entered by user
    Annual interest %: 6.0 #entered by user, convert to decimal!
    Number of years: 5 #entered by user

    Interest earned in 5 years: $348.8501525493075
    Total value after 5 years: $1348.8501525493075 
    print("Hello "+name)

Importing: We can access other functions by loading modules and calling functions on them.
    import math #import the math module
    math.sqrt(3) #square root of 3
    Also check out the list of functions at: https://docs.python.org/3/library/math.html

Dot Notation: Call (execute) a function using a period between who you want to perform the function and what function to perform (module.function())
    math.sqrt(3) #square root of 3
    --> tell math module to do sqrt work
    # bad at storing floats, therefore if doing math, try to stick to ints as much as possible

  can do the same thing to different data types:
    msg = "Hello World"
    msg = msg.upper() #make msg upper case
    --> tell msg to do uppercase work (and move label to new result!)

Available Functions
    Math Functions:
        https://docs.python.org/3/library/math.html
        How can I get the cosine of 2π?
    String Methods:
        https://docs.python.org/3/library/stdtypes.html#string-methods
        How can I get the cosine of 2π?
        How can I invert the case of a String (e.g., "Hello" => "hELLO")

def Object
    A value that encapsulates both data and functions that apply to that data.
    "Things" in a computer program that we can call methods on.

Turtle Graphics: A conceptual technique for drawing pictures based on telling a (virtual) pen-dragging robot where to move. Based on work by Seymour Papert at MIT (1960s)
    https://docs.python.org/3/library/turtle.html

    # load the turtle module so we can use it
    import turtle

    # tell the turtle module to make a Screen object
    # which represents the "window" that the turtle draws on
    window = turtle.Screen()

    # tell the turtle module to make a Turtle object
    # which represents a turtle that can draw
    my_turtle = turtle.Turtle()
    type(my_turtle) #=> 'turtle.Turtle'

    # tell the turtle to move!
    my_turtle.forward(100)  #forward 100 pixels
    my_turtle.left(12)      #left 120 degrees
    my_turtle.forward(80)   #forward 80 pixels

Regex in Python:
    https://docs.python.org/3/library/re.html
    https://docs.python.org/3/library/re.html#regular-expression-objects
    https://docs.python.org/3/library/re.html#match-objects

    # load the regular expression module
    import re

    # search the string for the given regular expression
    # returns a "match" object, or None (type) if no match
    matches = re.search('((\(\d{3}\)\s)?\d{3}-\d{4})', "(206) 685-1622")
    print(matches)

    # The "match" object has its own set of methods,
    # e.g., for fetching capture groups
    print(matches.group(0))

    # tell the window to wait for the user to close it
    window.mainloop()

Booleans: 
  too_early = True
  is_monday = False

Relational Operators: 
  # greater than
  x > y

  # less than
  x < y

  # greater than or equal to
  x >= y

  # less than or equal to
  x <= y

  # equal to
  x == y # because regular "=" assigns a variable!

  # not equal to
  x != y

Conditionals:
  # general syntax
  if boolean_expression:
      statements
  if temperature < 60:
      print("Wear a hat")
      print("And a jacket")

Alternatives:
  # general syntax
  if boolean_expression:
      statements
  else:
      statements

Nesting:
  if temperature < 60:
      print("Wear a jacket")
  else:
      if temperature > 90:
          print("Wear sunscreen")
      else:
          print("Wear a t-shirt")

Else If: 
  if temperature < 60:
      print("Wear a jacket")
  elif temperature > 90: #else if
      print("Wear sunscreen")
  elif temperature == 72: #else if
      print("Perfect weather!")
  else:
      print("Wear a t-shirt")

Whats the difference? What do you do if its 40? elifs are attached to the previous statements, ifs are exclusive from one another (considered individually)
  if temperature < 30:
      print("Wear snow pants")
  elif temperature < 60:
      print("Wear a jacket")

  if temperature < 30:
      print("Wear snow pants")
  if temperature < 60:
      print("Wear a jacket")

What if temp is 20? order matters! gain a priority - first thing you check is most important when both can be true (2nd statement becomes "unreachable")
  if temperature < 60:
      print("Wear a jacket")
  elif temperature < 30:
      print("Wear snow pants")

Dont do this...(use elif for mutually exclusive statements)
  # duplicate logic...
  if temperature < 50:
      print("It is cold")
  elif temperature >= 50:
      print("It is not cold")
Do this! (easier to read and edit)
  # Much better!
  if temperature < 50:
      print("It is cold")
  else:
      print("It is not cold")

Logical Operators (and or not): 
  # conjunction
  bool_one and bool_two

  # disjunction
  bool_one or bool_two

  # negation
  not bool_one

  #combining!
  A and not B
  not A and B
  not (A and B) <--de Morgans Law
  (not A) or (not B)
  3 < x < 5 #python is amazing

Dont do this...
  # Redundant expression...
  if is_raining == True:
      print("It is raining!")
Do this!
  # Much better!
  if is_raining:
      print("It is raining!")

Which is better? (answer: depends what will fix your logic. first two are better bc only 1 variable)
  #option 1
  if not is_raining:
      print("It is not raining!")

  #option 2
  if is_raining == False
      print("It is not raining!")

  #option 3
  if is_raining != True
      print("It is not raining!")

  #option 4
  if is_not_raining:
      print("It is not raining!")