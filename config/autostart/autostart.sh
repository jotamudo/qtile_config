#!/bin/bash
setxkbmap -layout us -option 'ctrl:nocaps' &
~/.fehbg &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
gnome-keyring-daemon &
picom --experimental-backend &
xrandr --output DVI-D-0 --mode 1920x1080 --rate 144 &
