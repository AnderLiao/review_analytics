# read the file
# r = read; w = write
# open the file and check the content
# with = close來結束掉檔案佔用的狀態
with open('food.txt', 'r') as file: 
	for line in file:
		print(line.strip()) # stirp去掉換行(/n)符號