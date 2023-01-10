f = open("demofile.txt", "w")
f.write('am sreehari')
f.close()
f = open("demofile.txt", "a")
f.write('from  malappuram')
f.close()


f = open("demofile.txt", "r")
print(f.read())