import os
import sys
import datetime
import random
working_dir = sys.argv[1]
sequence = sys.argv[2]
result_path = sys.argv[3]


# saving sequence to file
fileName = str(datetime.datetime.now().timestamp()).replace('.', '') + str(random.randint(1, 100000))
fp = open(working_dir + "upload/" + fileName +".fasta", 'w')
fp.close()
fp = open(working_dir+ "upload/" + fileName + ".fasta", 'r+')
fp.write(">\n"+sequence+"\n")
fp.close()


os.chdir(working_dir)

f_extract_check = os.system("Rscript predict.R " + working_dir + " " + fileName + ".fasta " + result_path + " > " + result_path + "logfile.log")

if f_extract_check != 0:
    fp = open(result_path+"/log.txt", 'w')
    fp.write("Invalid Sequence/File. Please verify your input sequence/file!"+"\n")
    fp.close()
