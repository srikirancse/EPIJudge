def split_array(arr):
  result = {'12': 3, '14': 5, '16': 7}
  for i in range(10):
    print(next(iter(result)))
  return result

print(split_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))