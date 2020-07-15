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

# Arguments
#
# application - Tells the script we just want the foreground windows "application" classname
# title - Tells the script we just want the foreground windows' title minus it's classname
#
# if neither is given, it should just default to returning "application" + title 
#
# Now, I need to add OPTIONAL color arguments. Up to 4 different ones.  Polybar allows you to add
# formatting text to the label you want to display.  Right now, I have the application text
# and window text different colors.
#
# background    foreground  background  foreground
# #ff9147       #ffffff     #e69e6e     #ffffff

def get_window_info(e):
#    Test returning formatted text
#    return "%{F#f00} red text %{F-}"

    focused_window = i3.get_tree().find_focused()
    
    if (focused_window.window_class is None): return ''
    
    if (len(sys.argv) > 1) and (sys.argv[1] == 'application'):
    	return to_CamelCase(focused_window.window_class)
    
    title = stripClassFromTitle(focused_window.window_title)
    
    if (len(sys.argv) > 1) and (sys.argv[1] == 'title'): return title

    return to_CamelCase(focused_window.window_class) + ': ' + title

def stripClassFromTitle(title):    
	idx = None
	
	for i in range(len(title)): 
	    if (title[i] in ['-','—']): idx = i
	    	        
	return title[:idx]

def to_CamelCase(str):
    return ' '.join([t.title() for t in str.split()])

def on_window_title(i3, e):
    print(get_window_info(e))
    
i3 = i3ipc.Connection()

i3.on("window::focus", on_window_title)
i3.on("window::title", on_window_title)
i3.on("window::close", on_window_title)
i3.on("workspace", on_window_title)

i3.main()
