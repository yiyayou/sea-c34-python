def safe_input(input):
  print("I'm a wrapper function for raw_input")
  try:
    raw_input(input)
  except EOFError:
    return None
  except KeyboardInterrupt:
    return None
    



