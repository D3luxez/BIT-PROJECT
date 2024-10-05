def check_rightmost_set_bit(num):
  """
  Checks if the rightmost set bit in a number is 1.

  Args:
    num: The number to check.

  Returns:
    True if the rightmost set bit is 1, False otherwise.
  """
  # Check if the number is 0
  if num == 0:
    return False

  # Use bitwise AND operation to isolate the rightmost set bit
  rightmost_set_bit = num & -num

  # Check if the rightmost set bit is 1
  return rightmost_set_bit == 1

# Get the number from the user
num = int(input("Enter a number: "))

# Check the rightmost set bit
is_rightmost_set = check_rightmost_set_bit(num)

# Print the result
if is_rightmost_set:
  print("The rightmost set bit in the number is 1.")
else:
  print("The rightmost set bit in the number is not 1.")