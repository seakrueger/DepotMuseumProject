#!/usr/bin/env bash

systemddir=~/.local/share/systemd/user/

mkdir -p ${systemddir}
ln -s $(pwd)/exhibit.service ${systemddir} 
ln -s $(pwd)/exhibit.timer ${systemddir} 
systemctl --user enable exhibit.timer
systemctl --user daemon-reload

pip3 install -r requirements.txt