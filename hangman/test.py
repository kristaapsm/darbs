import os
import mysql.connector
from configparser import ConfigParser


print("Configuration file test")
print("Checking if config file exists")
assert os.path.isfile("config.ini") == True
print("OK")
print("-----------------")

config = ConfigParser()
config.read('config.ini')


print("Checking if config has MYSQL related options")
assert config.has_option('mysql_config','mysql_host') == True
assert config.has_option('mysql_config','mysql_db') == True
assert config.has_option('mysql_config','mysql_user') == True
assert config.has_option('mysql_config','mysql_pass') == True
print("OK")
print("-----------------")


print("Checking connection to database")
mysql_config_mysql_host = config.get('mysql_config', 'mysql_host')
mysql_config_mysql_db = config.get('mysql_config', 'mysql_db')
mysql_config_mysql_user = config.get('mysql_config', 'mysql_user')
mysql_config_mysql_pass = config.get('mysql_config', 'mysql_pass')

connection = mysql.connector.connect(host=mysql_config_mysql_host, database=mysql_config_mysql_db,
                                    user=mysql_config_mysql_user, password=mysql_config_mysql_pass)
assert connection.is_connected() == True
print("OK")
print("-----------------")

print("Checking if directory log exists")
assert os.path.isdir("log")
print("OK")
print("-----------------")

print("Checking if migration logging configuration file exists")
assert os.path.isfile("log_migrate_db.yaml")
print("OK")
print("-----------------")


print("Checking if directory migration exists")
assert os.path.isdir("migration")
print("OK")
print("-----------------")
print("Test completed, Everything is OK")

