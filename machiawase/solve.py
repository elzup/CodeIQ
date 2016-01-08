# -*- coding: utf-8 -*-
import math

# # debug input
# chiper_nums = [169, 147, 161, 173, 145, 161, 67, 159,
#                149, 67, 171, 133, 153, 133, 161, 169,
#                133, 159, 67, 137, 147, 161, 173, 151,
#                161, 173, 67, 139, 141]

import fileinput
chiper_nums = map(int, (fileinput.input()[0]).split(" "))

# hint: 2x + 3
comp_nums = [int(math.floor((c - 3) / 2)) for c in chiper_nums]
# print(comp_nums)
comp_strs = map(chr, comp_nums)
print("".join(comp_strs))
