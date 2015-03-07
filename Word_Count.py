#created by Jonathan (Chia Kang) Chao
#Word Count Program

#using glob to read all the .txt files in a directory
#regular expression is mainly for eliminating punctuations
#time is for checking run time
#os for checking if a directory exists
import glob, re, time, os
start_time=time.time()
#print glob.glob('/users/JChao/Documents/Columbia/insight_data_engineering/wc_input/*.txt')
#asking for path name
#in fact, with a direct input (isntead of asking for user input)
#can reduce the run time by 5 times. This cleanup work is necessary only
#to make this program more versatile. Sacrificing efficiency for more
#of an all around work
dir_name=raw_input("Please enter the correct directory name:")
if os.path.isdir(dir_name):
	dir_name2=dir_name+'/wc_input/*.txt'
	path_name=glob.glob(dir_name2)
	#path_name=glob.glob('/users/JChao/Documents/Columbia/insight_data_engineering/wc_input/*.txt')
else:
	print ("invalid directory name")
#creating a dictionary for words to be stored
dic={}
#reading each txt file
for name in path_name:
	file_name=open(name, 'r')
	#read and split strings
	string=file_name.read()
	#since everything is in lower case in example, convert everything
	#into lower case
	string=string.lower()
	#now regular expression doesn't have to consider upperases
	string=re.sub('[^a-z\ \']+', " ", string)
	string_split=string.split()

	#if the word already exists, count goes up,
	#otherwise create the word in dictionary and set count to 1
	for word in string_split:
		if word in dic:
			dic[word]+=1
		else:
			dic[word]=1
	file_name.close()
#check if the folder wc_output exist, if not, create
out_path=os.path.join(dir_name, 'wc_output')

if not os.path.exists(out_path):
	os.makedirs(out_path)
os.chdir(out_path)
#create new .txt file to write 
out_file=open('wc_result.txt', 'w')
for word, count in dic.iteritems():
	out_file.write(word)
	out_file.write(': ')
	out_file.write(str(count))
	out_file.write('\n')
out_file.close()
print("--- %s ms ---" %((time.time()-start_time)*1000))
