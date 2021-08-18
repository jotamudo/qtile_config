#!/bin/bash
setxkbmap -layout br -variant abnt2 -option 'ctrl:swapcaps' -option 'numpad:microsoft' &
~/.fehbg &
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &
gnome-keyring-daemon &
picom --experimental-backend &
