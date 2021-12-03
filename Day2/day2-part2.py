# Advent of Code 2021
# Day 2, Part 2
# December 2, 2021

file_name = "day2-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()
   val_horiz = 0
   val_depth = 0
   val_aim   = 0

   for idx in range(len(line_content)):
      curr_line = line_content[idx].rstrip()

      # split current line into command and value
      cmd1 = curr_line[0:curr_line.find(' ')]
      val1 = int(curr_line[-1])

      if cmd1 == 'forward':
         val_horiz = val_horiz + val1
         val_depth = val_depth + (val_aim * val1)
      if cmd1 == 'down':
         val_aim = val_aim + val1
      if cmd1 == 'up':
         val_aim = val_aim - val1

   answer = val_horiz * val_depth

print("\nThe final position is {}".format(answer))
