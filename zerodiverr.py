try:
 a=int(input("Enter the numerator:"))
 b=int(input("Enter the denominator:"))
 print('%d/%d=%f'%(a,b,a/b))
except (ZeroDivisionError,ValueError)as e:
  print(e)
else:
  print('Division successful')
