import psutil

stats = psutil.cpu_percent(.5)

print (stats)