from urllib2 import *

f=urlopen("http://cugrobot.cug.edu.cn:8188/index1.html")
g=f.read()
print g
outfile = open("output.txt","w")
outfile.write(g)
outfile.close()
