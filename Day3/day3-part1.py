# Advent of Code 2021
# Day 3, Part 1
# December 3, 2021

# I acknowledge this is a terrible, long-winded way to do this :)

file_name = "day3-input.dat"

with open(file_name) as file_contents:
   line_content = file_contents.readlines()
   gamma   = "000000000000"
   epsilon = "000000000000"
   power   = 0

   pos000  = 0
   pos001  = 0
   pos010  = 0
   pos011  = 0
   pos020  = 0
   pos021  = 0
   pos030  = 0
   pos031  = 0
   pos040  = 0
   pos041  = 0
   pos050  = 0
   pos051  = 0
   pos060  = 0
   pos061  = 0
   pos070  = 0
   pos071  = 0
   pos080  = 0
   pos081  = 0
   pos090  = 0
   pos091  = 0
   pos100  = 0
   pos101  = 0
   pos110  = 0
   pos111  = 0

   for idx in range(len(line_content)):
      curr_line = line_content[idx].rstrip()

      for pos in range(len(curr_line)):
         if pos == 0:
            if curr_line[pos] == "1":
               pos001 = pos001 + 1
            else:
               pos000 = pos000 + 1
         
         if pos == 1:
            if curr_line[pos] == "1":
               pos011 = pos011 + 1
            else:
               pos010 = pos010 + 1

         if pos == 2:
            if curr_line[pos] == "1":
               pos021 = pos021 + 1
            else:
               pos020 = pos020 + 1
  
         if pos == 3:
            if curr_line[pos] == "1":
               pos031 = pos031 + 1
            else:
               pos030 = pos030 + 1

         if pos == 4:
            if curr_line[pos] == "1":
               pos041 = pos041 + 1
            else:
               pos040 = pos040 + 1

         if pos == 5:
            if curr_line[pos] == "1":
               pos051 = pos051 + 1
            else:
               pos050 = pos050 + 1

         if pos == 6:
            if curr_line[pos] == "1":
               pos061 = pos061 + 1
            else:
               pos060 = pos060 + 1

         if pos == 7:
            if curr_line[pos] == "1":
               pos071 = pos071 + 1
            else:
               pos070 = pos070 + 1

         if pos == 8:
            if curr_line[pos] == "1":
               pos081 = pos081 + 1
            else:
               pos080 = pos080 + 1

         if pos == 9:
            if curr_line[pos] == "1":
               pos091 = pos091 + 1
            else:
               pos090 = pos090 + 1

         if pos == 10:
            if curr_line[pos] == "1":
               pos101 = pos101 + 1
            else:
               pos100 = pos100 + 1

         if pos == 11:
            if curr_line[pos] == "1":
               pos111 = pos111 + 1
            else:
               pos110 = pos110 + 1

   if pos001 > pos000:
      gamma = "1"
   else:
      gamma = "0"

   if pos011 > pos010:
      gamma = gamma + "1"
   else:
      gamma = gamma + "0"

   if pos021 > pos020:
      gamma = gamma + "1"
   else:
      gamma = gamma + "0"

   if pos031 > pos030:
      gamma = gamma + "1"
   else:
      gamma = gamma + "0"

   if pos041 > pos040:
      gamma = gamma + "1"
   else:
      gamma = gamma + "0"

   if pos051 > pos050:
      gamma = gamma + "1"
   else:
      gamma = gamma + "0"

   if pos061 > pos060:
      gamma = gamma + "1"
   else:
      gamma = gamma + "0"

   if pos071 > pos070:
      gamma = gamma + "1"
   else:
      gamma = gamma + "0"

   if pos081 > pos080:
      gamma = gamma + "1"
   else:
      gamma = gamma + "0"

   if pos091 > pos090:
      gamma = gamma + "1"
   else:
      gamma = gamma + "0"

   if pos101 > pos100:
      gamma = gamma + "1"
   else:
      gamma = gamma + "0"

   if pos111 > pos110:
      gamma = gamma + "1"
   else:
      gamma = gamma + "0"

   # invert gamma to get epsilon
   epsilon = gamma
   epsilon = epsilon.replace("1", "2")
   epsilon = epsilon.replace("0", "1")
   epsilon = epsilon.replace("2", "0")
   
   print("Gamma  : {} ({})".format(gamma, int(gamma, 2)))
   print("Epsilon: {} ({})".format(epsilon, int(epsilon, 2)))
      
   power = int(gamma, 2) * int(epsilon, 2)

print("\nThe power consumption is {}".format(power))
