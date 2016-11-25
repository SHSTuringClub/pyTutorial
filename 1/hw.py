#! /usr/bin/env python3

# Think about an unfortunate circumstance, where you are on a ship but caught by pirates.
# The pirates decided that all the 1000 passengers should stand in one row (not a ring!).
# First, the passengers are numbered 1-1000, and those whose number is dividable by 3 will die.
# Then, the alive ones are re-numbered (1-what? I don't know!). Now those whose number is dividable
# by 5 are the unlucky ones.
#
# No, I'm not to let you choose a good seat. Just suppose that all the passengers are "stored" in a
# list like [{"name": "Xingjian Di", "alive": True}, {"name": "Xuelin Sun", "alive": True},
# {"name": "Ruiqi Lin", "alive": True}, ...]. Please set the unlucky ones' property "alive" to false,
# and print a list of their name.

import json
passengers = json.load(open('data.json')) # Remember to download "data.json" in the folder

####################################################################
# Your code begins here.                                           #
####################################################################



####################################################################
# Your code ends here.                                             #
####################################################################


# For reference, here's how the test data are generated.

"""
import random
import json
import codecs

first_name = ['雪', '琳', '睿', '祺', '天', '乐', '文', '鑫', '嘉', '祺', '行', '健',
              '驰', '方', '翔', '洵', '婧', '常', '箐', '翊', '旭', '亮', '乐', '萌']

last_name = ['孙', '林', '郑', '于', '狄', '姚', '魏', '滕', '陈', '胡']

c = random.choice
out = []

for i in range(1000):
    tmp = {"name": "{l}{f1}{f2}".format(l=c(last_name),
           f1=c(first_name), f2=c(first_name)), "alive": True}

    out.append(tmp)

with codecs.open('data.json', 'w', 'utf-8') as fp:
    fp.write(json.dumps(out))
"""
