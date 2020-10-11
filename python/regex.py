import re
s = "Ah what a beautiful 2 AM morning at 5WoodsLake! I counted 2890 birds today."

f = open("demo.txt", "w")
f.write(s)
f.close()

s2 = "New line? How interesting."

f = open("demo.txt", "a")
f.write("\n" + s2)
f.close()


f = open("demo.txt")
for lines in f:
	print(lines)
f.close()

s3 = "Length of data: 80"

print("--------")

f = open("demo.txt", "w")
f.writelines(s+"\n"+s2+"\n"+s3)
f.close()

f = open("demo.txt")
Lines = f.readlines()
for line in Lines:
	print(line)

print("--------")

f = open("demo.txt")
for lines in f:
	m = re.findall("\d{4}", lines)
	if m:
		print(m)
	else:
		print("Skipped line. (regex 1)")
	m = re.findall("\d+", lines)
	if m:
		print(m)
	else:
		print("Skipped line. (regex 2)")
	m = re.search("Length of data:", lines)
	if m:
		print(re.split(":", lines)[1])
	else:
		print("Skipped line. (regex 3)")
	m = re.findall("\D+", lines)
	if m:
		print(m)
	else:
		print("Skipped line. (regex 4)")