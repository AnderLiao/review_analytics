# read the file
# 1. Initialize
# 2. Try to print out the list
# 3. Show the progress by print out the length of list
# 4. Only shows the progress every 10K counts

data = []
with open('reviews.txt', 'r') as file: # open and read review.txt
	count = 0
	for line in file:
		data.append(line.strip()) # remove '/n' sign
		count += 1
		if count % 10000 == 0:
			print('Processing...' + str(len(data)))
print(len(data))
print(data[0]) # Print out the 1st review in data list