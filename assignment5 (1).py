# Write a program to print numbers from 1 to 10, but stop if the number is 5.
for i in range(0, 10):
  if i == 5:
    break
  print(i)
# Write a program to skip printing even numbers from 1 to 10.
for i in range(1, 10):
  if i % 2 == 0:
    continue
  print(i)
# Write a program to print numbers from 0 to 9 using range().
range_1 = 0
for i in range(0, 9):
  range_1 = range_1 + 1
  print(range_1)
#Write a program to print multiplication tables from 1 to 5, but stop after the first table is printed for each number.
for i in range(1,6):
  for j in range(1, 11):
    print(i*j)
  print('table for', i, 'completed')
# Write a program to skip printing even numbers using a while loop.
range_2 = 0
while range_2 < 10:
  if range_2 % 2 ==0:
    range_2 += 1
    continue
  print(range_2)
  range_2 += 1
# Write a program to iterate through a list and stop when encountering a specific element.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
stop_element = 7
for i in my_list:
  if i == stop_element:
    break
  print(i)