import os
import datetime

# get the date
today = datetime.date.today()
day = today.day
year = today.year

# go to the year folder
os.chdir(str(year))

# create the files
for i in range(0, day):
    folder_name = str(i+1).zfill(2)
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        os.chdir(folder_name)
        python_file = open(f'{folder_name}.py', 'w')
        python_file.write("input = open('input.txt', 'r')\n")
        python_file.write("lines = input.readlines()\n")
        python_file.close()
        open(f'input.txt', 'w').close()


        
