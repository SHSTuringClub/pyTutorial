#! /usr/bin/env python3

# This script calculates pi(π) by the Taylor series of arctan(x)
# In case you have not learnt mathematical analysis, I'll give the formula used to calculate the value.
# arctan(1) = π/4 = 1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + ...
# Please calculate π as accurate as reasonable

import math

pi_ref = math.pi
pi_cal = 0

####################################################################
# Your code begins here. Please finally store the value in pi_cal. #
####################################################################



####################################################################
# Your code ends here.                                             #
####################################################################

if math.fabs(pi_ref - pi_cal) < 0.00001:
    print('Congratulations!')
else:
    print('Oh no...')