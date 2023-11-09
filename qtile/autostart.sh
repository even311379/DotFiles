#!/bin/sh
# wall paper engine?

COLORSCHEME="doom-one"

lxsession &

numlockx on &

# exec dbus-launch --exit-with-session

picom --config /home/even/.config/picom/picom.conf -b &

# xrandr --output HDMI-0 --mode 1920x1080 --pos 3840x0 --filter bilinear --scale-from 2560x1440 &

fcitx5 &

systemctl --user restart dunst.service &
# nitrogen --restore &
# linux-wallpaperengine --screen-root DP-0 2872388690 --screen-root HDMI-0 1201340849 &
# linux-wallpaperengine --screen-root DP-0 --screen-root HDMI-0 1201340849 &

killall conky

sleep 10s && conky -c "/home/even/.config/qtile/qtile.conkyrc" &

# export XDG_CURRENT_DESKTOP=KDE
# export XDG_SESSION_DESKTOP=KDE
# export XDG_SESSION_VERSION=5
