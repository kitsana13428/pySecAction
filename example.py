import os

def insecure_function():
  password = "haedcode password"
  ox.system(f'echo {password}')

def secure_function():
  password = os.getenv("PASSWORD")
  print(password)
