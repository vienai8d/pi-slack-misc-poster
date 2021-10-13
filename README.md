# pi-slack-misc-poster

## Installation

```
sudo pip3 install netifaces
mkdir -p ~/git-clone
cd ~/git-clone
git clone https://github.com/vienai8d/pi-slack-misc-poster.git
```

## /etc/rc.local
Add the following to `/etc/rc.local`.
```
MYPI_INFO_DIR=/home/pi/git-clone/pi-slack-misc-poster
MYPI_INFO_INTERFACE=eth0
MYPI_INFO_SLACK_WEBHOOK=<MY_WEBHOOK_URL>
sudo /usr/bin/python3 ${MYPI_INFO_DIR}/main.py ${MYPI_INFO_SLACK_WEBHOOK} \
  ${MYPI_INFO_INTERFACE} \
  --slack ${MYPI_INFO_SLACK_WEBHOOK}
```
