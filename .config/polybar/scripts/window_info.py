#	The MIT License(MIT)
#	Copyright(c), Tobey Peters, https://github.com/tobeypeters
#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software
#	and associated documentation files (the "Software"), to deal in the Software without restriction,
#	including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
#	and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
#	subject to the following conditions:
#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
#	LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#	IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#	WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#	SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import i3ipc
import re
import sys
import argparse

# Gets the foreground windows' Application/classname, Title or both <default> of them and returns it
# to our polybar module.

# Arguments:
#              --application - Tells the script we just want the foreground windows "application" classname
#              --title - Tells the script we just want the foreground windows' title minus it's classname
#
#              --application_colors - The Application will be displayed with the specified colors, both of which MUST be provided.
#              --title_colors - The Title will be displayed with the specified colors, both of which MUST be provided.
#
#       Usage:
#              window_info.py --application --application_colors #ffffff #000000 --title_colors #00ff00 #ffffff
#              window_info.py --title application_colors #ffffff #000000 --title_colors #00ff00 #ffffff
#              window_info.py --application_colors #ffffff #000000 --title_colors #00ff00 #ffffff
#              window_info.py --title_colors #00ff00 #ffffff
#              window_info.py
#
#   args_gist: https://gist.github.com/strager/e86e355cf8b9d60a0ff9b785506a34f9
#
# Example output : https://github.com/tobeypeters/.dotfiles/blob/master/images/currentdesktop3.png

def get_window_info(e):
    focused_window = i3.get_tree().find_focused()

    if (focused_window.window_class is None): return ''

    if not args.title:
        application_text = f' {to_CamelCase(focused_window.window_class)} '
        colors = args.application_colors
        if (colors):
            application_text = formatText(application_text, colors)

    if not args.application:
        title_text = f' {stripClassFromTitle(focused_window.window_title)} '
        colors = args.title_colors        
        if (colors):
            title_text = formatText(title_text, colors)
            
    if (args.application): return application_text
    if (args.title): return title_text
    
    return f'{application_text}{title_text}'

# Strip the classname from the end of window titles
# Instead of "New Tab - Google-Chrome", we just want "New Tab"
def stripClassFromTitle(title = str):
	idx = None
	
	for i in range(len(title)): 
	    if (title[i] in ['-','—']): idx = i
	    	        
	return title[:idx]

# Make sure a specified string is in CamelCase format
def to_CamelCase(camelStr = str):
   return ''.join([t.title() for t in camelStr.split()])

# Add background & foreground color formatting, to a specified string
def formatText(formatStr = str, formatColors = []):
    return f'%{{B{formatColors[0]}}}%{{F{formatColors[1]}}}{formatStr}%{{B- F-}}'

def on_window_title(i3, e):
    print(get_window_info(e))

parser = argparse.ArgumentParser()
parser.add_argument("--application", action="store_true", help="Displays ONLY the foreground windows' Application name.")
parser.add_argument("--title", action="store_true", help="Displays ONLY the foreground windows' Title.")
parser.add_argument("--application_colors", nargs=2, help="Override the background & foreground colors, of the displayed text.  Colors must be specified in hex format.")
parser.add_argument("--title_colors", nargs=2, help="Override the background & foreground colors, of the displayed text.  Colors must be specified in hex format.")
args = parser.parse_args()
    
i3 = i3ipc.Connection()

i3.on("window::focus", on_window_title)
i3.on("window::title", on_window_title)
i3.on("window::close", on_window_title)
i3.on("workspace", on_window_title)

i3.main()
