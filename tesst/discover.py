import sys
import subprocess

ip = sys.argv[1]

print("entered ip "+ip)
if not ip: 
  print("usage: discover.sh <IP>")
  sys.exit("Incorrect usage")

subprocess.run(["cd", "/root/bin/zabbix-removal"])

#output = subprocess.check_output("cat syscall_list.txt | grep f89e7000 | awk '{print $2}'", shell=True)
vmname = subprocess.check_output('/usr/bin/php /root/bin/ip2vmname.php '+ip, shell=True)
print(vmname)
#VMNAME='/usr/bin/php /root/bin/ip2vmname.php '+ip
#QUERY="update engines set vm='"+vmname+"' where ip='"+ip+"'"|MYSQL
MYSQL="mysql discover -u discover -pvmware"
QUERY="update engines set vm='"+vmname+"' where ip='"+ip+"'"

result = subprocess.check_output(QUERY|MYSQL, shell=True)

if result :
    print("Successfully executed the script")