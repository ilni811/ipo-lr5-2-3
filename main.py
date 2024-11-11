filename = "text.txt"
filename1 = "output.txt"
with open(filename, "r", encoding="utf-8") as filein, open(filename1, "w", encoding="utf-8") as fileout:
  for line in filein:
    line = line.strip() 
    if len(line) > 5:
      fileout.write(line + " ") 
