import os
import sys

working_dir = sys.argv[1]
file_path = sys.argv[2]
result_path = sys.argv[3]
os.chdir(working_dir)
f_extract_check = os.system("Rscript predict.R " + working_dir + " " + file_path + " " + result_path+ " > " + result_path + "/log.txt")

if(f_extract_check!=0):
    fp = open(result_path+"/log.txt", 'r+')
    fp.write("Invalid Sequence/File. Please verify your input file!"+"\n")
    fp.close()
