try:
  a=int(input("Enter an integer:"))
  if a<90 or a>120:
    raise ValueError('Abnormal condition')
  print('Valid number')
except Exception as e:
    print(e)
