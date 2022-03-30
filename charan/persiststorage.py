import time
import os
data=os.getenv("RCLONE_DATA")
app_name=os.getenv("APP_NAME")
#Config File
os.system(f'echo {data} | base64 -d > /home/coder/.config/rclone/rclone.conf')
print('config File Created')
#Download
os.system(f'rclone sync test:{app_name} ~/project/')
print('files Synced')
#upload Every 1 min
while True:
    os.system(f'rclone sync  ~/project/ test:{app_name}')
    print('Files Uploaded')
    time.sleep(60)
