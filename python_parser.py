#!/usr/bin/env python
# -*- coding: utf-8 -*-

only_sums=""

with open('input_file') as f:
   for line in f:
     #  print line
       if "sum"  in line and "param" not in line and not (("j" in line) and ("i" in line) ): 
         only_sums=only_sums+line
         #print(only_sums)
       if 'str' in line:
          break


#$$\sum_{n=1}^{\infty} 2^{-n}$$

start_on_sum="$$\sum_{"
latex_code_one_line=""
for line in only_sums:
   if("subject" in line ):
      break

   #line.replace("sum{" ,"$$\sum_{" )
   #line.replace("in", "=1}^{")
   #line.replace("[", "_")
   #line.replace("]", "]")
   #line.replace("*", " * ")
   #line.replace("+", " + ")
   #line.replace("+", "+$$")
   print(line)


