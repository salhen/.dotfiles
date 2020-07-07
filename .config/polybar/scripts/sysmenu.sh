echo ''<<LICENSE
	The MIT License(MIT)
	Copyright(c), Tobey Peters, https://github.com/tobeypeters
	Permission is hereby granted, free of charge, to any person obtaining a copy of this software
	and associated documentation files (the "Software"), to deal in the Software without restriction,
	including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
	and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
	subject to the following conditions:
	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
	 LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
	 IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
	WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
	SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
LICENSE

# System menu - MacOS like - Just started making this.  So ... this script will change a bunch.

BORDER="#ff6347"
SEPARATOR="#1F1F1F"
FOREGROUND="#ffffff"
BACKGROUND="#ff6347"
# BACKGROUND="#546e7a"
# HIGHLIGHT_BACKGROUND="#ff9147"
HIGHLIGHT_BACKGROUND="#ffffff"
HIGHLIGHT_FOREGROUND="#000000"

about="About This Computer..."
settings="System Preferences..."
store="App Store..."
monitor="System Monitor...  Ctrl +  + Del"
restart="Restart"
shutdown="Shutdown"
sep="--------------------------------"
logout="Log Out"

options="$about\n$sep\n$settings\n$store\n$sep\n$monitor\n$sep\n$restart\n$shutdown\n$logout"

chosen="$(echo "$options" | rofi -i -p "System" -dmenu -selected-row 0 \
-hide-scrollbar true \
-location 1 \
-xoffset 0 -yoffset 18 \
-lines 10 \
-width 13 \
-padding 6 \
-font "Ubuntu Mono 10" \
-color-window "$BACKGROUND,$BORDER,$SEPARATOR" \
-color-normal "$BACKGROUND,$FOREGROUND,$BACKGROUND,$HIGHLIGHT_BACKGROUND,$HIGHLIGHT_FOREGROUND" \
-color-active "$BACKGROUND,$BACKGROUND,$BACKGROUND,$HIGHLIGHT_BACKGROUND,$HIGHLIGHT_FOREGROUND" \
-color-urgent "$BACKGROUND,$BACKGROUND,$BACKGROUND,$HIGHLIGHT_BACKGROUND,$HIGHLIGHT_FOREGROUND" \
-color-enabled true)"

case $chosen in
    $about)
    	kinfocenter
        ;;
    $settings)
    	systemsettings5 &
        ;;
    $store)
    	feren-store &
        ;;
    $monitor)
    	ksysguard &
        ;;
    $restart)
    	systemctl reboot
        ;;
    $shutdown)
    	systemctl poweroff
        ;;
    $logout)
    	 i3-msg exit
        ;;
        *)
        	exit 1
        ;;
esac
