# Advent of Code 2021
# Day 1, Part 2
# December 2, 2021

file_name = "day1-input.dat"

with open(file_name) as file_contents:
   list1 = file_contents.readlines()
   line_range = range(len(list1))
   line_count = len(list1)

   prev_sum = 9999999999
   counter  = 0

   for line1 in line_range:
      if line1 < (line_count - 2):
         sum1 = int(list1[line1]) + int(list1[line1 + 1]) + int(list1[line1 + 2])
         if sum1 > prev_sum:
            counter = counter + 1        
         prev_sum = sum1

print("\nThe total number of sliding window sums than the previous sum is: {}".format(counter))
