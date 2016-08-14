#import glob2
import datetime


filenames = ["C:\Python27\Sample-Files\\file1.txt", "C:\Python27\Sample-Files\\file2.txt", "C:\Python27\Sample-Files\\file3.txt"]

with open("C:\Python27\Sample-Files\\" + datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f") + ".txt", 'w') as file:
    for filename in filenames:
        with open(filename, 'r') as f:
            file.write(f.read()+"\n")
