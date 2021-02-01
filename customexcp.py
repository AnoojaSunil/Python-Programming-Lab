class LoginEx (Exception):pass
try:
  a=input("Username:")
  b=input("Password:")
  c="MCA2020"
  d="@12345"
  if a==c and b==d:
    print("Login successful")
  else:
    raise LoginEx("Invalid enter of username or password")
except LoginEx as e:
    print(e)
