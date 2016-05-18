import urllib
import MySQLdb

finalList=[]
db = MySQLdb.connect("localhost","root","paul6627","sampleDB")
cursor = db.cursor()
sql = "INSERT INTO firstTable VALUES ('%s')"

#Include a try statement here 

for count in range(0,5):

	sock=urllib.urlopen("http://getcomics.info/category/dc/page/"+str(count)+"/")
	htmlSource=sock.read()
	count=0
	tempList=[]
	length = len(htmlSource) 
	length= length -4
	fileNew= open('fileNew.txt','w')
	listCount=0
	beg=0
	end=0
	i=0
	while i<length:
		'''fileNew.write( htmlSource[i:i+4]+'\n')'''
		if htmlSource[i:i+3] == '<h1':
			beg=i
			while htmlSource[i:i+5] != '</h1>':
				i=i+1
			tempList.append(htmlSource[beg:i])
			listCount=listCount+1
		i=i+1
	length  = len(tempList)
	for i in range(1,length):
		iLength=len(tempList[i])-2
		while tempList[i][iLength]!='<':
			iLength = iLength-1
		end=iLength 
		while tempList[i][iLength]!='>'  :
			iLength=iLength -1 
	
		tempList[i]= tempList[i][iLength+1:end]


	
	for i in range(1,length):
		finalList.append(tempList[i])

for value in finalList:
	cursor.execute(sql % (value)  )
	db.commit()		
				
		

