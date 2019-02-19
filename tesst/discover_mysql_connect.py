import mysql.connector
import sys
import subprocess

ip = sys.argv[1]

print("entered ip is "+ip)
if not ip: 
  print("usage: discover.sh <IP>")
  sys.exit("Incorrect usage")

vmname = subprocess.check_output('/usr/bin/php /root/bin/ip2vmname.php '+ip, shell=True)
print(vmname)

""" UPDATEQUERY="update engines set vm='"+vmname+"'"
WHERE = "where ip='"+ip+"'"
#print(UPDATEQUERY+' '+WHERE)

UPDATE= "ON DUPLICATE KEY "+ UPDATEQUERY+' '+WHERE """

INSERT= "INSERT into engines (ip, vm, sfe_config_name, sfe_config_version, sfe_config_release, sfe_proxy_instance, sfe_template_type, sfe_template_version) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON DUPLICATE KEY UPDATE vm='"+vmname.strip()+"'"
val = (ip, vmname.strip(), 'no package provides sfe-proxy', 'no package provides sfe-proxy', 'no package provides sfe-proxy', 0, 'CentOS6.7-64bit-wax-RAT-H9', '2.1')

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="123123",
  database="discover"
)

mycursor = mydb.cursor()
mycursor.execute(INSERT, val)
