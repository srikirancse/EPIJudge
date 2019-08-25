from test_framework import generic_test


def search_first_of_k(A, k):
    start, end, result = 0, len(A) - 1, -1

    while start <= end:
        mid = (start + end) // 2

        if A[mid] > k:
            end = mid - 1
        elif A[mid] == k:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result


def nextGreatestLetter(letters, target):
      start, end, result = 0, len(letters) - 1, -1
      
      while start <= end:
        mid = (start + end) // 2
        
        if letters[mid] > target:
          result = letters[mid]
          end = mid - 1
        else:
          start = mid + 1
          
      return result

nextGreatestLetter(["c","f","j"], "j")

search_first_of_k([0, 1, 2, 3, 4, 5, 6, 7], 0)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "search_first_key.py", 'search_first_key.tsv', search_first_of_k))
