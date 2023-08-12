#!/bin/sh
# wall paper engine?

COLORSCHEME="doom-one"

lxsession &

numlockx on &

# exec dbus-launch --exit-with-session

picom --config /home/even/.config/picom/picom.conf -b &

xrandr --output HDMI-0 --mode 1920x1080 --pos 3840x0 --filter bilinear --scale-from 2560x1440 &

fcitx5 &

nitrogen --restore &
