#!/bin/bash

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

# Power Options - logout, reboot, shutdown 

declare -a options=("lock
logout
reboot
shutdown")

choice=$(echo -e "${options[@]}" | dmenu -l -i -p 'System:' -nb black -sb tomato -fn 'System San Francisco Display:size=10')

#'Shutdown' 'systemctl poweroff' -b 'Reboot' 'systemctl reboot' -b 'Logout' 'i3-msg exit'"

case $choice in
	lock)
		exec i3lock -c '#000000'
	;;
	logout)
		exec i3-msg exit
	;;
	reboot)
        exec i3-sensible-terminal -e systemctl reboot
	;;
	shutdown)
        exec i3-sensible-terminal -e systemctl poweroff
	;;
	*)
		exit 1
	;;
esac
