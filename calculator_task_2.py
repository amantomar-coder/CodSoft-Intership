def calculator():
  print("Simple Calculator")
  try:
      num1 = float(input("Enter first number: "))
      operation = input("Enter operation (+, -, *, /): ")
      num2 = float(input("Enter second number: "))

      if operation == '+':
          print(f'Result: {num1 + num2}')
      elif operation == '-':
          print(f'Result: {num1 - num2}')
      elif operation == '*':
          print(f'Result: {num1 * num2}')
      elif operation == '/':
          if num2 != 0:
              print(f'Result: {num1 / num2}')
          else:
              print("Error: Division by zero")
      else:
          print("Invalid operation.")
  except ValueError:
      print("Invalid input.")

if __name__ == "__main__":
  calculator()
