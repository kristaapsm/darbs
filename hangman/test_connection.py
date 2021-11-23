import mysql.connector
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

print("Checking connection to database")
mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')

connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db,
                                     user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
assert connection.is_connected() == True
print("OK")
