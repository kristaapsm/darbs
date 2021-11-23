import os
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

