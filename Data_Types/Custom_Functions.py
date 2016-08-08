def celsius_converter(c):
  rate = 1.8
  suf = 32
  f = c*rate+suf
  return f
  
print(celsius_converter(25))
