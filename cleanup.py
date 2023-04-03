def cleanTxt(filePath):
	
	search_text = "  "
	replace_text = " "

	with open(filePath, 'r') as file:

		replaceData = file.read()

		replaceData = replaceData.replace(search_text, replace_text)

	with open(filePath, 'w') as file:

		file.write(replaceData)

	file.close()
	print("Text replaced")
	############################################################################
	newFile = open('upToDescription.txt','w')
	flag=0	
	with open(filePath, 'r+') as fp:
		
		lines = fp.readlines()
		for row in lines:
			# check if string present on a current line
			word = 'DETAILED DESCRIPTION'
			#print(row.find(word))
			# find() method returns -1 if the value is not found,
			# if found it returns index of the first occurrence of the substring
			if flag == 1:
				newFile.write(row)
			else:
				if row.find(word) != -1:
					print("we found it")
					flag = 1
					if flag ==1:
						print("Starting to write")
						newFile.write(row)
				
				
		
					

	file.close()
	fp.close()
	newFile.close()


cleanTxt("parent.txt")