arr = list(map(int , input("Enter array element").split()))
n = len(arr) + 1
actual_sum = sum(arr)
expected_sum = (n*(n+1))//2
missing_element = expected_sum - actual_sum
print("the missing of an element : ",missing_element)
