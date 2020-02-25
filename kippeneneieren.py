import random
secret_number1 = random.randint(0,9)
secret_number2 = random.randint(0,9)
secret_number3 = random.randint(0,9)
secret_number4 = random.randint(0,9)
secret_list = [secret_number1, secret_number2, secret_number3, secret_number4]
# for x in secret_list:
#   print(x)

given_numbers = input("Type your 4 numbers here with a space max 9: ") 
given_number1 = int(given_numbers[0])
given_number2 = int(given_numbers[2])
given_number3 = int(given_numbers[4])
given_number4 = int(given_numbers[6])
# print(given_number1)
# print(given_number2)
# print(given_number3)
# print(given_number4)

attempt = 0
chicken = 0
egg = 0

# number 1
if given_number1 == secret_number1:
  chicken += 1
elif given_number1 in secret_list:
  egg += 1

# number 2
if given_number2 == secret_number2:
  chicken += 1
elif given_number2 in secret_list:
  egg += 1

# number 3
if given_number3 == secret_number3:
  chicken += 1
elif given_number3 in secret_list:
  egg += 1

# number 4
if given_number4 == secret_number4:
  chicken += 1
elif given_number4 in secret_list:
  egg += 1

print(chicken)

while chicken < 4:
  attempt += 1
  given_numbers = input("Type your 4 numbers here with a space: ") 
  given_number1 = int(given_numbers[0])
  given_number2 = int(given_numbers[2])
  given_number3 = int(given_numbers[4])
  given_number4 = int(given_numbers[6])

  # number 1
  if given_number1 == secret_number1:
    chicken += 1
  elif given_number1 in secret_list:
    egg += 1

  # number 2
  if given_number2 == secret_number2:
    chicken += 1
  elif given_number2 in secret_list:
    egg += 1

  # number 3
  if given_number3 == secret_number3:
    chicken += 1
  elif given_number3 in secret_list:
    egg += 1

  # number 4
  if given_number4 == secret_number4:
    chicken += 1
  elif given_number4 in secret_list:
    egg += 1

  print("chickens:")
  print(chicken)
  chicken = 0
  print("Eggs:")
  print(egg)
  egg = 0

