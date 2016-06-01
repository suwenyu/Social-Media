# -*- coding: utf-8 -*-
from sys import argv
import csv
import uniout


d = {}

f = open('makeup.csv', 'r')
for row in csv.DictReader(f, ["User_ID" , "Article_ID" , "Date" , "Time" , "Device" , "Classify" , "Keyword"]):
    test = row['Keyword'][1:]


    t = d.setdefault(test)

    if t == None:
    	d[test] = 1;
    else:
    	d[test] = t + 1

    	    # print test
    # d[test] = 0
    # if len(d) == 0:
    # 	d[test] = 1
    # else:
	   #  for i in d.keys():
	   #  	# print (test , i )
	   #  	if test == i:
	   #  		# print test , i
	   #  		d[i] = d.get(i) + 1
	   #  		# print d[i]
	   #  		# print d[i]
	   #  	else :
	   #  		d[test] = 1
	   #  		# print test
	   #  # print d.values()

f.close()


# print "Value : %s" %  d.keys()
temp = d.items()

# for x in d:
    # print (x , d[x])
    # for y in d[x]:
    #     print (y,':',d[x][y])

target = open('test.csv', 'w')

for (i,j) in temp:
	target.write( i )
	target.write(",")
	target.write(str(j))
	target.write("\n")
# print len(d)
target.close()



