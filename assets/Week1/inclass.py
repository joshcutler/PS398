def ordinalnum(number):

  last_digit = abs(number) % 10
  last_two = abs(number) % 100
  number = str(number)
  text = number + "th"
  
  if last_digit == 1 and last_two != 11:
    text = number + "st"
  elif last_digit == 2 and last_two != 12:
    text = number + "nd" 
  elif last_digit == 3 and last_two != 13:
    text = number + "rd" 
  
  return text