import mysql.connector
import simplejson, json

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="M0dc0mp!",
  database="aquia_drupal"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from users")

myresult = mycursor.fetchall()

my_list = []
for x in myresult:
  #append items to a list
  my_list.append(x)
encoded_str = json.dumps(my_list)
print(encoded_str)