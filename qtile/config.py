# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# from libqtile import bar, layout, widget, hook
import colors_theme
from libqtile import bar, layout, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, ScratchPad, DropDown
from libqtile.lazy import lazy
import os, subprocess


@lazy.layout.function
def add_treetab_section(layout):
    prompt = qtile.widgets_map["prompt"]
    prompt.start_input("Section name: ", layout.cmd_add_section)


# from typing import Callable

from qtile_extras import widget

# from qtile_extras.widget.decorations import RectDecoration, PowerLineDecoration
from qtile_extras.widget.decorations import BorderDecoration
from qtile_extras.popup.toolkit import PopupRelativeLayout, PopupWidget


# colors = [
# 	      ["#282c34", "#282c34"], # panel background
#           ["#3d3f4b", "#434758"], # background for current screen tab
#           ["#ffffff", "#ffffff"], # font color for group names
#           ["#ff5555", "#ff5555"], # border line color for current tab
#           ["#74438f", "#74438f"], # border line color for 'other tabs' and color for 'odd widgets'
#           ["#4f76c7", "#4f76c7"], # color for the 'even widgets'
#           ["#e1acff", "#e1acff"], # window name
#           ["#ecbbfb", "#ecbbfb"]  # backbround for inactive screens
# ]


# colors = dict(
#     panel_bg_1="#2f343f",
#     active_group_bg="#ffffff",
#     inactive_group_bg="#848e96",
#     panel_bg_2="#3d3f4b",
#     panel_bg_3="#434758",
#     window_name_bg="#282c34",
#     active_window_frame="#74438f",
# )


mod = "mod4"
terminal = "kitty"
file_manager = "thunar"
browser = "firefox"
qutebrowser = "qutebrowser"
browser_private = "firefox -private-window"
screen_shot = "flameshot gui"

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
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
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
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "a", lazy.spawn("rofi -show combi"), desc="spawn rofi"),
    Key([mod], "r", lazy.spawncmd(), desc="spawn command using prompt"),
    Key([mod], "e", lazy.spawn(file_manager), desc="Spawn file manager"),
    Key([mod], "b", lazy.spawn(qutebrowser), desc="Spawn web browser, firefox"),
    Key([mod, "shift"], "b", lazy.spawn(browser_private), desc="Spawn qutebrowser"),
    Key([mod], "s", lazy.spawn(screen_shot), desc="Take screen shot"),
    Key([mod], "h", lazy.spawn("roficlip"), desc="clipboard"),
    Key([mod], "f", lazy.window.toggle_floating(), desc="toggle floating window"),
    Key([mod], "m", lazy.window.toggle_fullscreen(), desc="toggle full screen"),
    Key([mod], "n", lazy.window.toggle_minimize(), desc="minimize screen"),
    Key([mod], "p", lazy.spawn("sh -c ~/.config/rofi/scripts/power"), desc="powermenu"),
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
    # Treetab prompt
    Key(
        [mod, "shift"],
        "a",
        add_treetab_section,
        desc="Prompt to add new section in treetab",
    ),
    # Grow/shrink windows left/right.
    # This is mainly for the 'monadtall' and 'monadwide' layouts
    # although it does also work in the 'bsp' and 'columns' layouts.
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
    # test hide / show bar
    Key([mod], "z", lazy.hide_show_bar("bottom"), desc="Hides the bar"),
]

main_groups = [str(i) for i in range(1, 7)]
extra_group = [str(i) for i in range(7, 10)]


def go_to_group(name):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.groups_map[name].cmd_toscreen()
            return
        if name in main_groups:
            qtile.focus_screen(0)
        else:
            qtile.focus_screen(1)
        qtile.groups_map[name].cmd_toscreen()

    return _inner


def move_to_group(name, should_switch_group=False):
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_window.togroup(name, switch_group=should_switch_group)
            return
        if name in main_groups:
            qtile.current_window.togroup(name, switch_group=False)
            if should_switch_group:
                qtile.focus_screen(0)
                qtile.groups_map[name].cmd_toscreen()
        else:
            qtile.current_window.togroup(name, switch_group=False)
            if should_switch_group:
                qtile.focus_screen(1)
                qtile.groups_map[name].cmd_toscreen()

    return _inner


def move_next_group():
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_screen.cmd_next_group()
            return
        current_group = qtile.current_group.name
        if current_group in main_groups:
            if current_group != main_groups[-1]:
                qtile.current_screen.cmd_next_group()
        else:
            if current_group != extra_group[-1]:
                qtile.current_screen.cmd_next_group()

    return _inner


def move_prev_group():
    def _inner(qtile):
        if len(qtile.screens) == 1:
            qtile.current_screen.cmd_prev_group()
            return
        current_group = qtile.current_group.name
        if current_group in main_groups:
            if current_group != main_groups[0]:
                qtile.current_screen.cmd_prev_group()
        else:
            if current_group != extra_group[0]:
                qtile.current_screen.cmd_prev_group()

    return _inner


def window_to_other_screen(should_swap=False):
    def _inner(qtile):
        other = 1 - qtile.screens.index(qtile.current_screen)
        group = qtile.screens[other].group.name
        qtile.current_window.togroup(group, switch_group=should_swap)
        qtile.focues_screen(other)

    return _inner


keys.extend(
    [
        Key(
            [mod],
            "o",
            lazy.function(window_to_other_screen()),
            desc="move to other screen",
        ),
    ]
)


group_labels = ["➊", "➋", "➌", "➍", "➎", "➏"]
second_group_labels = ["➐", "➑", "➒"]
groups = [Group(i, label=n) for i, n in zip("123456", group_labels)]
groups.extend([Group(i, label=n) for i, n in zip("789", second_group_labels)])

# for i in groups:
#     keys.append(Key([mod], i.name, lazy.function(go_to_group(i.name))))

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.function(go_to_group(i.name)),
                # lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                # lazy.window.togroup(i.name, switch_group=True),
                lazy.function(move_to_group(i.name)),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            Key(
                [mod, "control"],
                i.name,
                # lazy.window.togroup(i.name, switch_group=True),
                lazy.function(move_to_group(i.name, True)),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Key([mod], "Right", lazy.screen.next_group(), desc="Switch to next group"),
            Key(
                [mod],
                "Right",
                lazy.function(move_next_group()),
                desc="Switch to next group",
            ),
            Key(
                [mod],
                "Left",
                lazy.function(move_prev_group()),
                desc="Switch to previous group",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togqtile0roup(i.name),
            #      desc="move focused window to group {}".format(i.name)),
        ]
    )


## POPUP??  based on qtile extra?
def show_graphs(qtile):
    controls = [
        PopupWidget(
            widget=widget.CPUGraph(), width=0.45, height=0.45, pos_x=0.05, pos_y=0.05
        ),
        PopupWidget(
            widget=widget.NetGraph(), width=0.45, height=0.45, pos_x=0.5, pos_y=0.05
        ),
        PopupWidget(
            widget=widget.MemoryGraph(), width=0.9, height=0.45, pos_x=0.05, pos_y=0.5
        ),
    ]

    layout = PopupRelativeLayout(
        qtile,
        width=1000,
        height=200,
        controls=controls,
        background="00000060",
        initial_focus=None,
        close_on_click=False,
    )
    layout.show(centered=True)


## scratchpads
groups.append(
    ScratchPad(
        "scratchpad",
        [
            DropDown(
                "applications",
                "nwg-drawer",
                width=0.4,
                height=0.6,
                x=0.3,
                y=0.1,
                opacity=1,
            ),
            DropDown(
                "mixer", "pavucontrol", width=0.4, height=0.6, x=0.3, y=0.1, opacity=1
            ),
            DropDown("clock", "kitty peaclock", width=0.6, height=0.4, x=0.2, y=0.3),
        ],
    )
)

keys.extend(
    [
        # Key([mod], "a", lazy.group['scratchpad'].dropdown_toggle('applications')),
        # Key([mod], "s", lazy.group['scratchpad'].dropdown_toggle('mixer')),
        Key([mod], "d", lazy.group["scratchpad"].dropdown_toggle("clock")),
    ]
)


# theming and widgets...
colors = colors_theme.tomorrow_night

layout_theme = {
    "border_width": 2,
    "margin": 8,
    "border_focus": colors[8],
    "border_normal": colors[0],
}


# layouts = [
#     # layout.Columns(border_focus_stack=["#d75f5f", "#8f3d3d"], border_width=2, margin=10),
#     layout.Tile(border_focus=colors["active_window_frame"], border_width=2, margin=10),
#     layout.MonadTall(
#         border_focus=colors["active_window_frame"], border_width=2, margin=10
#     ),
#     layout.MonadWide(
#         border_focus=colors["active_window_frame"], border_width=2, margin=10
#     ),
#     layout.VerticalTile(
#         border_width=2, margin=10, border_focus=colors["active_window_frame"]
#     ),
#     layout.TreeTab(
#         font="Cascadia Code",
#         fontsize=18,
#         section_fontsize=22,
#         sections=["Main", "Extra"],
#     ),
#     layout.Max(margin=10),
#     layout.Floating(border_focus=colors["active_window_frame"]),
#     # Try more layouts by unleashing below layouts.
#     # layout.Stack(num_stacks=2),
#     # layout.Bsp(),
#     # layout.Matrix(),
#     # layout.RatioTile(),
#     # layout.Zoomy(),
# ]

# from dt
layouts = [
    # layout.Bsp(**layout_theme),
    # layout.Floating(**layout_theme),
    # layout.RatioTile(**layout_theme),
    # layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    # layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    # layout.MonadWide(**layout_theme),
    layout.Floating(**layout_theme),
    layout.Max(
        border_width=0,
        margin=0,
    ),
    layout.Stack(**layout_theme, num_stacks=2),
    layout.Columns(**layout_theme),
    layout.TreeTab(
        font="Ubuntu Bold",
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
        sections=["ONE", "TWO", "THREE"],
        section_fontsize=10,
        section_fg=colors[2],
        section_top=15,
        section_bottom=15,
        level_shift=8,
        vspace=3,
        panel_width=240,
    ),
    # layout.Zoomy(**layout_theme),
]

widget_defaults = dict(font="Ubuntu Bold", fontsize=24, padding=0, background=colors[0])

extension_defaults = widget_defaults.copy()
main_group_box = widget.GroupBox(
    visible_groups=[str(i) for i in range(1, 7)],
    fontsize=22,
    margin_y=3,
    margin_x=4,
    padding_y=2,
    padding_x=3,
    borderwidth=3,
    active=colors[8],
    inactive=colors[1],
    rounded=False,
    highlight_color=colors[2],
    highlight_method="line",
    this_current_screen_border=colors[7],
    this_screen_border=colors[4],
)
second_group_box = widget.GroupBox(
    visible_groups=[str(i) for i in range(7, 10)],
    fontsize=22,
    margin_y=3,
    margin_x=4,
    padding_y=2,
    padding_x=3,
    borderwidth=3,
    active=colors[8],
    inactive=colors[1],
    rounded=False,
    highlight_color=colors[2],
    highlight_method="line",
    this_current_screen_border=colors[7],
    this_screen_border=colors[4],
)


def init_widgets_list():
    widgets_list = [
        widget.CurrentLayoutIcon(foreground=colors[1], padding=0, scale=0.7),
        widget.Prompt(font="Ubuntu Mono", fontsize=22, foreground=colors[1]),
        widget.TextBox(
            text="|", font="Ubuntu Mono", foreground=colors[1], padding=2, fontsize=28
        ),
        widget.CurrentLayout(foreground=colors[1], padding=5),
        widget.TextBox(
            text="|", font="Ubuntu Mono", foreground=colors[1], padding=2, fontsize=28
        ),
        widget.Spacer(),
        widget.WindowName(foreground=colors[6], max_chars=40),
        widget.Spacer(),
        widget.Systray(padding=3),
        widget.Spacer(length=8),
        widget.GenPollText(
            update_interval=300,
            func=lambda: subprocess.check_output("printf $USER", shell=True, text=True),
            foreground=colors[3],
            fmt="❤  {}",
            decorations=[
                BorderDecoration(
                    colour=colors[3],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.CPU(
            format="🔲 Cpu: {load_percent}%",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e btop")},
            foreground=colors[4],
            decorations=[
                BorderDecoration(
                    colour=colors[4],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.NvidiaSensors(
            format="GPU {temp}°C",
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e nvtop")},
            decorations=[BorderDecoration(colour=colors[3], border_width=[0, 0, 2, 0])],
        ),
        widget.Spacer(length=8),
        widget.Memory(
            foreground=colors[8],
            mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("kitty -e btop")},
            format="{MemUsed: .0f}{mm}",
            fmt="🖥  Mem: {}",
            decorations=[
                BorderDecoration(
                    colour=colors[8],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.Volume(
            foreground=colors[7],
            fmt="🕫  Vol: {}",
            decorations=[
                BorderDecoration(
                    colour=colors[7],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.Clock(
            foreground=colors[6],
            format="%Y-%m-%d  󰥔  %H:%M:%S ",
            decorations=[
                BorderDecoration(
                    colour=colors[6],
                    border_width=[0, 0, 2, 0],
                )
            ],
        ),
        widget.Spacer(length=8),
        widget.TextBox(
            text=" ",
            fontsize=24,
            mouse_callbacks={
                "Button1": lazy.spawn("sh /home/even/.config/rofi/scripts/power")
            },
        ),
        widget.Spacer(length=8),
    ]
    return widgets_list


def init_widgets_screen1():
    widgets_screen = init_widgets_list()
    widgets_screen.insert(2, main_group_box)
    return widgets_screen


def init_widgets_screen2():
    widgets_screen = init_widgets_list()
    widgets_screen.insert(2, second_group_box)
    del widgets_screen[9]  # Removes systray
    return widgets_screen


bottom_bar1 = bar.Bar(
    widgets=[
        widget.Spacer(),
        widget.TaskList(
            max_title_width=192,
            txt_floating="🗗",
            txt_maximized="🗖",
            txt_minimized="🗕"
            ),
        widget.Spacer(),
        ],
    size=36)

bottom_bar2 = bar.Bar(
    widgets=[
        widget.Spacer(),
        widget.TaskList(
            max_title_width=192,
            txt_floating="🗗",
            txt_maximized="🗖",
            txt_minimized="🗕"
            ),
        widget.Spacer(),
        ],
    size=36)

def init_screens():
    return [
        Screen(top=bar.Bar(widgets=init_widgets_screen1(), size=36), bottom=bottom_bar1),
        Screen(top=bar.Bar(widgets=init_widgets_screen2(), size=36), bottom=bottom_bar2),
    ]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen2()


# widget_defaults = dict(
#     font="Cascadia Code",
#     fontsize=24,
#     padding=6,
# )

# OUTER_GAP = 10

# decoration_group = {
#     "decorations": [PowerLineDecoration()],
#     "padding": 10,
# }

# my_clock = widget.Clock(
#     background=colors["panel_bg_1"],
#     mouse_callbacks={"Button1": lambda: qtile.cmd_spawn("gsimplecal")},
#     format="%Y-%m-%d  󰥔  %H:%M:%S ",
#     **decoration_group
# )

# main_bar = bar.Bar(
#     [
#         widget.Spacer(length=16, background=colors["panel_bg_1"]),
#         widget.CurrentLayoutIcon(
#             custom_icon_path=["/home/even/.config/qtile/icons"],
#             background=colors["panel_bg_1"],
#         ),
#         widget.GroupBox(
#             visible_groups=[str(i) for i in range(1, 7)],
#             fontsize=24,
#             borderwidth=3,
#             highlight_method="block",
#             rounded=True,
#             disable_drag=True,
#             active=colors["active_group_bg"],
#             inactive=colors["inactive_group_bg"],
#             background=colors["panel_bg_1"],
#             **decoration_group
#         ),
#         widget.TaskList(
#             background=colors["window_name_bg"], fontsize=18, margin=2, borderwidth=1
#         ),
#         widget.Spacer(background=colors["window_name_bg"], **decoration_group),
#         widget.Systray(background=colors["panel_bg_2"], **decoration_group),
#         widget.CPU(background=colors["panel_bg_3"]),
#         widget.NvidiaSensors(format="GPU {temp}°C", background=colors["panel_bg_3"]),
#         widget.Memory(
#             measure_mem="G",
#             measure_swap="G",
#             format="Mem {MemUsed:.0f}{mm}/{MemTotal:.0f}{mm}",
#             background=colors["panel_bg_3"],
#             **decoration_group
#         ),
#         # widget.Volume(fmt="   {}", background=colors["panel_bg_1"], **decoration_group),
#         widget.ALSAWidget(
#             update_interval=1,
#             mode="both",
#             theme_path="/home/even/.local/share/icons/Papirus-Dark",
#             background=colors["panel_bg_1"],
#         ),
#         my_clock,
#         # widget.Clock(format="%Y-%m-%d  󰥔  %H:%M:%S ", background=colors["panel_bg_1"], **decoration_group),
#         widget.Spacer(length=16),
#         widget.TextBox(
#             text="",
#             mouse_callbacks={
#                 "Button1": lazy.spawn("sh /home/even/.config/rofi/scripts/power")
#             },
#         ),
#         widget.Spacer(length=16),
#     ],
#     36,
#     border_width=[3, 0, 3, 0],
# )

# extra_bar = bar.Bar(
#     [
#         widget.Spacer(length=16, background=colors["panel_bg_1"]),
#         widget.CurrentLayoutIcon(
#             custom_icon_path=["/home/even/.config/qtile/icons"],
#             background=colors["panel_bg_1"],
#         ),
#         widget.GroupBox(
#             visible_groups=[str(i) for i in range(7, 10)],
#             fontsize=24,
#             borderwidth=3,
#             highlight_method="block",
#             rounded=True,
#             disable_drag=True,
#             active=colors["active_group_bg"],
#             inactive=colors["inactive_group_bg"],
#             background=colors["panel_bg_1"],
#             **decoration_group
#         ),
#         widget.TaskList(
#             background=colors["window_name_bg"], fontsize=18, margin=2, borderwidth=1
#         ),
#         widget.Spacer(
#             length=28, background=colors["window_name_bg"], **decoration_group
#         ),
#         widget.Pomodoro(background=colors["panel_bg_1"]),
#         # my_clock
#         widget.Clock(format="%Y-%m-%d  󰥔  %H:%M:%S ", background=colors["panel_bg_1"]),
#     ],
#     32,
#     border_width=[3, 0, 3, 0],
# )


# screens = [
#     Screen(
#         top=main_bar,
#         right=bar.Gap(OUTER_GAP),
#         left=bar.Gap(OUTER_GAP),
#         bottom=bar.Gap(OUTER_GAP),
#     ),
#     Screen(
#         top=extra_bar,
#         right=bar.Gap(OUTER_GAP),
#         left=bar.Gap(OUTER_GAP),
#         bottom=bar.Gap(OUTER_GAP),
#     ),
# ]

# Drag floating layouts.
## TODO add drag button1 to swap window position?
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
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
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
        Match(wm_class="blender"),
        Match(wm_class="unreal-editor"),
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
wmname = "LG3D"


@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser("~/.config/qtile/autostart.sh")
    subprocess.call([home])

# print(dir(qtile.current_group.layout))
# print(dir(qtile.current_layout.name))

# @hook.subscribe.focus_change
# def check_floating():
#     if qtile.current_group.current_layout  == 1:
#         bottom_bar.show(True)
#         # bottom_bar2.show(True)
#     else:
#         bottom_bar.show(False)
#         # bottom_bar1.show(True)

@hook.subscribe.layout_change
def check_new_floating(new_layout, new_group):
    should_decrease_height = False
    if new_group.current_layout == 1 and new_group.name in ["7", "8", "9"]:
        bottom_bar2.show(True)
        should_decrease_height = True
    elif new_group.current_layout == 1:
        bottom_bar1.show(True)
        should_decrease_height = True
    else:
        bottom_bar1.show(False)
        bottom_bar2.show(False)
    if should_decrease_height:
        for w in new_group.windows:
            w.place(w.x, w.y, w.width, w.height - 16, 2, "#ffffff")
            # with open("/home/even/qinfo.txt", "w") as f:
            #     f.write(str(dir(w)))
            #     f.write("\n......\n")
            #     f.write(f"{w.x} {w.y}")
            #     # f.write(f"{window.get_size()}/n")
            # window.toggle_floating()
            # window.place(4000, 100, 500, 300, 2, "#ffffff")
            # info = window.info()
            # w,h = window.get_size()
            # window.set_size_floating([100, 50])

@hook.subscribe.screens_reconfigured
def send_to_second_screen():
    if len(qtile.screens) > 1:
        qtile.groups_map["7"].cmd_toscreen(1, toggle=False)

@hook.subscribe.startup
def startup():
    bottom_bar1.show(False)
    bottom_bar2.show(False)

# @hook.subscribe.startup
# def match_bar_with_picom():
#     main_bar.window.window.set_property("QTILE_BAR", 1, "CARDINAL", 32)
