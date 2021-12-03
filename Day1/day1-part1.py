# Advent of Code 2021
# Day 1, Part 1
# December 2, 2021

file_name = "day1-input.dat"

with open(file_name) as file_contents:
   list1 = file_contents.readlines()

   prev_val = 9999999999
   counter  = 0

   for line1 in range(len(list1)):
      val1 = int(list1[line1].rstrip())
      if val1 > prev_val:
         counter = counter + 1        
      prev_val = val1

print("\nThe total number of measurements larger than the previous measurement is: {}".format(counter))
