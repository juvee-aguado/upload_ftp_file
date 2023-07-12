import pysftp

my_hostname = "ip_host"
my_username = "user"
my_password = "password"

local_file_path ="path_local"
remote_file_path = "path_server"

def file_exists(file_path):
    srv = pysftp.Connection(host = my_hostname,username = my_username,password = my_password)
    exists = srv.exists(file_path)
    srv.close()
    return exists

def remove_file():
    sftp = pysftp.Connection(host = my_hostname,username = my_username,password = my_password)
    sftp.remove(remote_file_path)
    sftp.close()

def upload_file():
	sftp = pysftp.Connection(host = my_hostname,username = my_username,password = my_password)
	sftp.put(local_file_path, remote_file_path)
	sftp.chmod(remote_file_path,777)


if file_exists(remote_file_path):
	print("exist")
	print("delete file")
	remove_file()
	print("upload file")
	upload_file()	
else:
	print("upload file")
	upload_file()
	
