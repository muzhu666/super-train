def fibonacci(n):
  """
  This function calculates the nth Fibonacci number.

  Args:
    n: The index of the desired Fibonacci number (starting from 0).

  Returns:
    The nth Fibonacci number.  Returns -1 if n is negative.
  """
  if n < 0:
    return -1
  elif n <= 1:
    return n
  else:
    a, b = 0, 1
    for _ in range(2, n + 1):
      a, b = b, a + b
    return b

# Example usage
if __name__ == "__main__":
  num = 10
  result = fibonacci(num)
  print(f"The {num}th Fibonacci number is: {result}")
