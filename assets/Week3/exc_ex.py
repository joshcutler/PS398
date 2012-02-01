class CustomException(Exception):
  def __init__(self, value):
    self.value = value
  
  def __str__(self):
    return self.value

def i_call_a_function_with_errors():
  try:
    print "Calling a function...."
    #function_with_generic_error()
    #function_with_custom_error()
    #function_with_unknown_error(1)
    print "Tada!"
  except CustomException as inst:
    print "Custom Error Caught! Error({0})".format(inst.value)
  except:
    print "Default Error Caught!"
  else:
    print "No error raised."
  finally:
    print "Goodbye!"
  
def function_with_generic_error():
  raise Exception, "Foo!"
  
def function_with_custom_error():
  raise CustomException, "Foo Bar!"
  
def function_with_unknown_error(foo):
  foo.bar()