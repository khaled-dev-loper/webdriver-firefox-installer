import os
def cmd(v):
	return os.popen(v).read()
cmd("chmod +x geckodriver")
pathes = cmd("echo $PATH")
pathes = pathes.replace("\n","").replace("\n\r","").replace("\r","").split(":")
print(cmd("clear || cls"))
for loc in pathes:
	print(cmd(f"sudo cp geckodriver {loc}/geckodriver"))
print("INSTALL COMPLETED")

