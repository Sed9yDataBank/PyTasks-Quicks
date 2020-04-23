"""
This Script Checks Whether A Website Is Live Or Not, And It Sends A Notification If The  Website Is Down
"""
import requests,os,time

SITE_URL=""
SLEEP_SEC=300
while True:
    response=requests.get(SITE_URL)
    print(response)
    if response.status_code!=200:
          os.system('notify-send "Website Down" "'+SITE_URL+'Is Down"')
          break
    time.sleep(SLEEP_SEC)