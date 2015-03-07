#created by Jonathan Chao
import glob, os, numpy, re
#the first part, which is reading the files from directories, is the
#same as the word_count problem
dir_name=raw_input("Please enter the correct directory name:")

if os.path.isdir(dir_name):
	dir_name2=dir_name+'/wc_input/*.txt'
	path_name=glob.glob(dir_name2)
	
else:
	print ("invalid directory name")
#initialize the place keepers for word count for each line
#running average, and temperary average for calculation
line_store, running_avg=[], []
temp_avg=0
#count for words
count=0
#sort the list of file names to read it in alphabetical order
for name in sorted(path_name):
	
	with open(name, 'r') as file_name:
	
		for string in file_name:
			line=string.split()
			#for every word in a line, count goes up	
			for word in line:
				count+=1
			line_store.append(count)
			#need to sort the elements
			line_store=sorted(line_store)
			count=0
			#2 cases for the median, one is odd number of element:
			#just find the middle element of the list
			#the other is even element, find the two middle elements
			#then average them.
			if len(line_store)%2==1:
				temp_avg=line_store[((len(line_store)+1)/2)-1]
			elif len(line_store)%2==0:
				
				lower_v=line_store[len(line_store)/2-1]
				upper_v=line_store[len(line_store)/2]
				temp_avg=(float(lower_v+upper_v))/2
			
			running_avg.append(temp_avg)
						
		file_name.close()


#writing the running average into txt file in wc_output
out_path=os.path.join(dir_name, 'wc_output')
print out_path
if not os.path.exists(out_path):
	os.makedirs(out_path)
os.chdir(out_path)
#create new .txt file to write 
out_file=open('med_result.txt', 'w')
for med in running_avg:
	out_file.write(str(med))
	out_file.write('\n')
out_file.close()
#print("--- %s ms ---" %((time.time()-start_time)*1000))
