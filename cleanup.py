def cleanTxtCIP(filePath):
########################	This first segment searches for double spaces and replaces them with single spaces #########################
								 
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
	##################### This segment deletes every single line up to the string 'DETAILED DESCRIPTION' ###########################
	########################  we do this because we aren't concerned with anything before the description	###########################

	newFile = open('upToDescription.txt','w')
	flag=0	
	with open(filePath, 'r+') as fp:
		
		#This for loop searches through the document for the 'word' var and writes all the lines of text 
		# beneath it to a new file

		lines = fp.readlines()
		for row in lines:
			
			word = 'DETAILED DESCRIPTION'
			
			if flag == 1:
				newFile.write(row)
			else:
				if row.find(word) != -1:
					#print("we found it")
					flag = 1
					if flag ==1:
						#print("Starting to write")
						newFile.write(row)
	file.close()
	fp.close()
	newFile.close()

##################################################################################
################################ I don't really remember implementing this, but ########################################
###################### apparently the strip() function removes trailing and preceding spaces and 'junk' ###################3
		
	filePath = 'upToDescription.txt'
	with open(
		filePath, 'r') as r, open(
			'stripped.txt', 'w') as o:
	
		for line in r:
			#strip() function
			if line.strip():
				o.write(line)
	
	r.close()
	o.close()

##################################################################################
############################################ This part deletes any string that is >= 6 #########################################
############### I know that it's weird, but it does yield better results because it deletes a huge portion of junk strings #####

	filePath = "stripped.txt"
	newFile = open("6charsCIP.txt",'w')	
	with open(filePath, 'r+') as fp:
		
		lines = fp.readlines()
		for row in lines:
			if len(row) > 6:
				print("len of line > 6: ",len(row))
				newFile.write(row)

			
			
	fp.close()
	newFile.close()
	




########################################################### CLEANING PARENT #########################################################
###################################### This function works EXACTLY the same as the one before #######################################
########### It just has a different name so I could call two 'different' functions for cleaning the CIP and parent ##################

def cleanTxtParent(filePath):
	
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
##################################################################################
		# opening and creating new .txt file
	filePath = 'upToDescription.txt'
	with open(
		filePath, 'r') as r, open(
			'stripped.txt', 'w') as o:
	
		for line in r:
			#strip() function
			if line.strip():
				o.write(line)
	
	r.close()
	o.close()
##################################################################################
	filePath = "stripped.txt"
	newFile = open("6charsParent.txt",'w')	
	with open(filePath, 'r+') as fp:
		
		lines = fp.readlines()
		for row in lines:
			# check if string present on a current line
			#print(row.find(word))
			# find() method returns -1 if the value is not found,
			# if found it returns index of the first occurrence of the substring
			if len(row) > 6:
				print("len of line > 6: ",len(row))
				newFile.write(row)

			
			
	fp.close()
	newFile.close()

cleanTxtCIP("childForCleaning.txt")
cleanTxtParent("parentForCleaning.txt")