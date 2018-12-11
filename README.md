### Idea for solving

In order to solve this problem, here is the plan that we laid out to try first.

Start by making all combinations of indexs of intersection for each corner of the molecule strings. Then, sort them by largest area. This is to ensure that we then can check for largest area combos first and work towards smaller combos. This also allows the program to terminate early if any combo is true since that will be the largest area possible.

These indexs will be stored in a tuple with the 3 item in the tuple being the area.

These tuples will then be run through a function that tests all permutations of the 4 strings and which order they can be in.

I do what I want.
