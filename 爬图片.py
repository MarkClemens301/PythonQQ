import urllib

url=r'http://cugrobot.cug.edu.cn:8188/pmh.jpg'
path = r"test.jpg"  
data = urllib.urlretrieve(url,path)
