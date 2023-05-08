import configparser

config = configparser.ConfigParser()

config.add_section('Debug')
config.add_section('Log')
config.add_section('Gmail')

config.set('Debug', 'debug_mode', 'True')
config.set('Log', 'log_file_path', '/var/log/myapp.log')
config.set('Gmail', 'username', 'pauls.konov@gmail.com')
config.set('Gmail', 'password', '')

with open('myapp.conf', 'w') as f:
 config.write(f)

config.read('myaap.conf')

debug_mode = config.getboolean('Debug', 'debug_mode')
log_file_path = config.get('Log', 'log_file_path')
username = config.get('Gmail', 'username')
password = config.get('Gmail', 'password')

print(debug_mode)
print(log_file_path)
print(username)
print(password)
