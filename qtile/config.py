from libqtile import bar, layout, extension, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy

## stop using qtile extra...
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration
import os, subprocess

# env variables that make dolphin look right?
os.environ["XDG_CURRENT_DESKTOP"] = "KDE"
os.environ["XDG_SESSION_DESKTOP"] = "KDE"
os.environ["XDG_SESSION_VERSION"] = "5"


mod = "mod4"
terminal = "kitty"
file_manager = "dolphin"
file_manager_opt = "thunar"
browser = "thorium-browser"
browser_opt = "qutebrowser"
screen_shot = "flameshot gui"

# WALLPAPER_MAIN = wallpapers.WALLPAPER_TILES
# WALLPAPER_OPT = wallpapers.WALLPAPER_TRIANGLES_ROUNDED
WALLPAPER_MAIN = "/home/even/Pictures/wallpapers/gruvbox/anime/ign-waifu.png"
WALLPAPER_OPT = "/home/even/Pictures/wallpapers/gruvbox/anime/5m5kLI9.png"
keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window right"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "w", lazy.spawn("com.logseq.Logseq"), desc="spawn Logseq"),
    Key([mod], "k", lazy.spawn("kate"), desc="spawn kate"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key(
    #     [mod],
    #     "a",
    #     lazy.run_extension(extension.DmenuRun(dmenu_prompt=">", dmenu_lines=5, fontsize=12)),
    #     desc="spawn dmenu",
    # ),
    Key([mod], "a", lazy.spawn("dmenu_run -c -l 16 -h 28"), desc="spawn dmenu"),
    Key([mod, "shift"], "a", lazy.spawn("./.config/qtile/dmenu_scripts/dmenu_kill"), desc="spawn dmenu kill"),
    # Key([mod, "shift"], "a", lazy.spawn("./.config/qtile/dmenu_scripts/dmenu_appimage"), desc="open app image"),
    Key([mod], "r", lazy.spawncmd(), desc="spawn command using prompt"),
    Key([mod], "e", lazy.spawn(file_manager), desc="Spawn file manager"),
    Key([mod, "shift"], "e", lazy.spawn(file_manager_opt), desc="Spawn file manager opt (dolphin)"),
    Key([mod], "b", lazy.spawn(browser), desc="Spawn main web browser, qutebrowser"),
    Key([mod, "shift"], "b", lazy.spawn(browser_opt), desc="Spawn opt browser, firefox"),
    Key([mod], "s", lazy.spawn(screen_shot), desc="Take screen shot"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="toggle floating window"),
    Key([mod], "m", lazy.window.toggle_fullscreen(), desc="toggle full screen"),
    Key([mod, "shift"], "m", lazy.spawn("./.config/qtile/dmenu_scripts/dmenu_music"), desc="play work music"),
    Key([mod], "n", lazy.window.toggle_minimize(), desc="minimize screen"),
    Key([mod], "p", lazy.spawn("./.config/qtile/dmenu_scripts/dmenu_power"), desc="spawn dmenu power options"),
    Key([mod, "shift"], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc="powermenu"),
    # volume control:
    Key([mod], "Down", lazy.spawn("amixer -q sset Master 5%-"), desc="volume down"),
    Key([mod], "Up", lazy.spawn("amixer -q sset Master 5%+"), desc="volume up"),
    # copy from dt
    # Grow windows up, down, left, right.  Only works in certain layouts.
    # Works in 'bsp' and 'columns' layout.
    # tree tab
    Key(
        [mod, "shift"],
        "h",
        lazy.layout.shuffle_left(),
        lazy.layout.move_left().when(layout=["treetab"]),
        desc="Move window to the left/move tab left in treetab",
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        lazy.layout.move_right().when(layout=["treetab"]),
        desc="Move window to the right/move tab right in treetab",
    ),
    Key(
        [mod, "shift"],
        "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down().when(layout=["treetab"]),
        desc="Move window down/move down a section in treetab",
    ),
    Key(
        [mod, "shift"],
        "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up().when(layout=["treetab"]),
        desc="Move window downup/move up a section in treetab",
    ),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "space",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key(
        [mod],
        "equal",
        lazy.layout.grow_left().when(layout=["bsp", "columns"]),
        lazy.layout.grow().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left",
    ),
    Key(
        [mod],
        "minus",
        lazy.layout.grow_right().when(layout=["bsp", "columns"]),
        lazy.layout.shrink().when(layout=["monadtall", "monadwide"]),
        desc="Grow window to the left",
    ),
    # hide / show bar
    Key([mod], "z", lazy.hide_show_bar(position="bottom"), desc="Toggle bottom bar"),
    Key([mod], "x", lazy.hide_show_bar(position="top"), desc="Toggle top bar"),
    # use zenity to fix can not trigger fcitx5 issue in some app: ex steam chat
    Key([mod], "y", lazy.spawn("sh -c ~/.config/qtile/scripts/zenity_copy.sh")),
]
group_labels = ["➊", "➋", "➌", "➍", "➎", "➏", "➐", "➑", "➒"]
groups = [Group(i, label=l) for i, l in zip("123456789", group_labels)]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
        ]
    )

# define my strachpads
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown("term", "kitty --class=scratch", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
            DropDown(
                "tomato",
                "kitty --class=tomato -e tomatoshell -n 4",
                width=0.18,
                height=0.035,
                x=0.8,
                y=0.02,
                opacity=0.9,
            ),
            DropDown("ranger", "kitty --class=ranger -e ranger", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
            DropDown("volume", "kitty --class=colume -e pulsemixer", width=0.8, height=0.8, x=0.1, y=0.1, opacity=0.9),
            DropDown("clock", "kitty peaclock", width=0.6, height=0.4, x=0.2, y=0.3),
        ],
    )
)

keys.extend(
    [
        Key([mod, "shift"], "return", lazy.group["scratchpad"].dropdown_toggle("term")),
        Key([mod], "c", lazy.group["scratchpad"].dropdown_toggle("ranger")),
        Key([mod], "v", lazy.group["scratchpad"].dropdown_toggle("volume")),
        Key([mod], "d", lazy.group["scratchpad"].dropdown_toggle("clock")),
        Key([mod], "t", lazy.group["scratchpad"].dropdown_toggle("tomato")),
    ]
)

# reload colors from pywal
colors = []
cache = "/home/even/.cache/wal/colors"


def load_colors(cache):
    with open(cache, "r") as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append("#ffffff")
    lazy.reload()


load_colors(cache)

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": colors[8],
    "border_normal": colors[0],
}

layouts = [
    # layout.Max(border_width=0, margin=0),
    layout.Max(**layout_theme),
    layout.Columns(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(**layout_theme, num_stacks=2),
    # layout.Bsp(**layout_theme),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    layout.TreeTab(
        fontsize=24,
        border_width=0,
        bg_color=colors[0],
        active_bg=colors[8],
        active_fg=colors[1],
        inactive_bg=colors[1],
        inactive_fg=colors[2],
        padding_left=8,
        padding_x=8,
        padding_y=6,
        sections=[
            "TreeTab",
        ],
        section_fontsize=10,
        section_fg=colors[2],
        section_top=15,
        section_bottom=15,
        level_shift=8,
        vspace=3,
        panel_width=180,
    ),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(font="JetBrains Mono Bold", fontsize=24, padding=0, background=colors[0])
extension_defaults = widget_defaults.copy()

# use text glyph to fake rounded edge
left = ""
right = ""


# TODO: just create lighten color of core BG and send to to border and bg of left or right glyph
lbg = colors[0] + "00"
# lbg = colors[0]

top_bar_main = bar.Bar(
    [
        widget.TextBox(text=left, foreground=colors[0], background=lbg, fontsize=32),
        widget.Spacer(length=18),
        widget.CurrentLayoutIcon(foreground=colors[5], padding=0, scale=0.7),
        widget.TextBox(text="|", foreground=colors[5], padding=2, fontsize=28),
        widget.GroupBox(
            fontsize=22,
            margin_y=3,
            margin_x=4,
            padding_y=2,
            padding_x=3,
            borderwidth=3,
            active=colors[8],
            inactive=colors[5],
            rounded=False,
            highlight_color=colors[2],
            highlight_method="line",
            this_current_screen_border=colors[7],
            this_screen_border=colors[4],
        ),
        widget.TextBox(text="|", foreground=colors[5], padding=2, fontsize=28),
        widget.CurrentLayout(foreground=colors[5], padding=5),
        widget.Spacer(length=18),
        widget.TextBox(text=right, foreground=colors[0], background=lbg, fontsize=32),
        widget.Spacer(length=108, background=lbg),
        # widget.TextBox(text="|", foreground=colors[1], padding=2, fontsize=28),
        widget.TextBox(text=left, foreground=colors[0], background=lbg, fontsize=32),
        widget.Prompt(fontsize=22, foreground=colors[1]),
        widget.Spacer(),
        widget.WindowName(foreground=colors[6], max_chars=40),
        widget.Spacer(),
        widget.TextBox(text=right, foreground=colors[0], background=lbg, fontsize=32),
        widget.Spacer(length=108, background=lbg),
        widget.TextBox(text=left, foreground=colors[0], background=lbg, fontsize=32),
        # widget.TextBox(text="|", foreground=colors[1], padding=2, fontsize=28),
        # TODO: systray will alway be tranparent if bar bg is transparent...
        widget.TextBox(text="|", foreground=colors[5], padding=2, fontsize=28),
        # TODO: add a button to toggle side monitor brightness?
        widget.Clock(
            foreground=colors[6],
            format="%Y-%m-%d 󰥔 %H:%M:%S ",
        ),
        widget.TextBox(text=right, foreground=colors[0], background=lbg, fontsize=32),
        widget.WidgetBox(
            widgets=[
                widget.Systray(icon_size=32, background=lbg),
            ],
            background=lbg,
        ),
    ],
    size=36,
    background=lbg,
    opacity=1,
    margin=[4, 8, 0, 8],
)

top_bar_side = bar.Bar(
    [
        widget.TextBox(text=left, foreground=colors[0], background=lbg, fontsize=32),
        widget.Spacer(length=18),
        widget.CurrentLayoutIcon(foreground=colors[5], padding=0, scale=0.7),
        widget.TextBox(text="|", foreground=colors[5], padding=2, fontsize=28),
        widget.GroupBox(
            fontsize=22,
            margin_y=3,
            margin_x=4,
            padding_y=2,
            padding_x=3,
            borderwidth=3,
            active=colors[8],
            inactive=colors[5],
            rounded=False,
            highlight_color=colors[2],
            highlight_method="line",
            this_current_screen_border=colors[7],
            this_screen_border=colors[4],
        ),
        widget.TextBox(text="|", foreground=colors[5], padding=2, fontsize=28),
        widget.CurrentLayout(foreground=colors[5], padding=5),
        widget.Spacer(length=18),
        widget.TextBox(text=right, foreground=colors[0], background=lbg, fontsize=32),
        widget.Spacer(length=108, background=lbg),
        # widget.TextBox(text="|", foreground=colors[5], padding=2, fontsize=28),
        widget.TextBox(text=left, foreground=colors[0], background=lbg, fontsize=32),
        widget.Spacer(),
        widget.WindowName(foreground=colors[6], max_chars=40),
        widget.Spacer(),
        widget.TextBox(text=right, foreground=colors[0], background=lbg, fontsize=32),
        widget.Spacer(length=108, background=lbg),
        widget.TextBox(text=left, foreground=colors[0], background=lbg, fontsize=32),
        widget.Volume(
            foreground=colors[7],
            fmt="Vol:{}",
        ),
        widget.Spacer(length=8),
        widget.CPU(
            format="🔲 Cpu: {load_percent}%",
            mouse_callbacks={"Button1": lambda: qtile.spawn("kitty -e btop")},
            foreground=colors[4],
            # decorations=[BorderDecoration(colour=colors[4],border_width=[0, 0, 2, 0],)],
        ),
        widget.Spacer(length=8),
        widget.NvidiaSensors(
            format="GPU {temp}°C",
            mouse_callbacks={"Button1": lambda: qtile.spawn("kitty -e nvtop")},
            # decorations=[BorderDecoration(colour=colors[3], border_width=[0, 0, 2, 0])],
        ),
        widget.Spacer(length=8),
        widget.Memory(
            foreground=colors[8],
            mouse_callbacks={"Button1": lambda: qtile.spawn("kitty -e btop")},
            format="{MemUsed: .0f}{mm}",
            fmt="🖥 Mem:{}",
            # decorations=[BorderDecoration(colour=colors[8],border_width=[0, 0, 2, 0],)],
        ),
        widget.TextBox(text=right, foreground=colors[0], background=lbg, fontsize=32),
    ],
    42,
    background=lbg,
    margin=[4, 8, 0, 8],
)

bottom_bar_main = bar.Bar(
    widgets=[
        widget.Spacer(),
        widget.TaskList(max_title_width=192, txt_floating="🗗", txt_maximized="🗖", txt_minimized="🗕"),
        widget.Spacer(),
    ],
    size=36,
)

bottom_bar_side = bar.Bar(
    widgets=[
        widget.Spacer(),
        widget.TaskList(max_title_width=192, txt_floating="🗗", txt_maximized="🗖", txt_minimized="🗕"),
        widget.Spacer(),
    ],
    size=42,
)

screens = [
    Screen(
        top=top_bar_main,
        bottom=bottom_bar_main,
        wallpaper=WALLPAPER_MAIN,
        wallpaper_mode="fill",
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        x11_drag_polling_rate=60,
    ),
    Screen(
        top=top_bar_side,
        bottom=bottom_bar_side,
        wallpaper=WALLPAPER_OPT,
        wallpaper_mode="fill",
        # You can uncomment this variable if you see that on X11 floating resize/moving is laggy
        # By default we handle these events delayed to already improve performance, however your system might still be struggling
        # This variable is set to None (no cap) by default, but you can set it to 60 to indicate that you limit it to 60 events per second
        x11_drag_polling_rate=60,
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod, "mod1"],
        "Button1",
        lazy.window.set_position(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="spectacle"),
        Match(wm_class="Blender"),
        Match(wm_class="mpv"),
        Match(wm_class="UnrealEditor"),
        Match(wm_class="krita"),
        Match(wm_class="pomatez"),
        # Match(wm_class="IFCS_DEV"),  # Dev...
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "Q...Q"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/scripts/autostart.sh")
    subprocess.call([home])


@hook.subscribe.startup
def startup():
    bottom_bar_main.show(False)
    bottom_bar_side.show(False)
    top_bar_main.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)
    top_bar_side.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)
