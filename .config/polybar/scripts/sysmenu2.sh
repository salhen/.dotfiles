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

about="About This Computer..."
settings="System Preferences..."
store="App Store..."
monitor="System Monitor...  Ctrl +  + Del"
restart="Restart"
shutdown="Shutdown"
sep="--------------------------------"
logout="Log Out"

cabout="kinfocenter"
csettings="systemsettings5 &"
cstore="feren-store &"
cmonitor="ksysguard &"
crestart="systemctl reboot"
cshutdown="systemctl poweroff"
clogout="i3-msg exit"

options="$about\n$sep\n$settings\n$store\n$sep\n$monitor\n$sep\n$restart\n$shutdown\n$logout"
#commands=("$cabout" "" "$csettings" "$cstore" "" "$cmonitor" "" "$crestart" "$cshutdown" "$clogout")

commands=("kinfocenter")

~/.config/polybar/scripts/rofiexec.sh "single" 0 18 "$options" "${commands[@]}"
#~/.config/polybar/scripts/rofiexec.sh "single" 0 18 "$options" "${commands[@]}"
