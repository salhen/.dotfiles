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

# Get the Application "classname", Title or both, of the current foreground window and
# return the info back to polybar.

# Arguments - ALL OPTIONAL
#
# argument #1:
#   Specified: application or title
# Description:
#              application - Tells the script we just want the foreground windows "application" classname
#              title - Tells the script we just want the foreground windows' title minus it's classname
#     Default: if neither option is specified, application + title is returned.
#
# argument #2:
#   Specified: application_colors
# Description: The windows application "classname", will be displayed in polybar with the specified colors.
#              
#        Note: Both background and foreground colors must be provided. directly after applicaton_colors.
#              Colors must be provide in hex format.
#
# argument #3:
#   Specified: title_colors
# Description: The windows title, will be displayed in polybar with the specified colors.
#        Note: Both background and foreground colors must be provided, directly after title_colors.
#              Colors must be provide in hex format.
#
#       Usage:
#              window_info.py application application_colors #ffffff #000000 title_colors #00ff00 #ffffff
#              window_info.py title application_colors #ffffff #000000 title_colors #00ff00 #ffffff
#              window_info.py application_colors #ffffff #000000 title_colors #00ff00 #ffffff
#              window_info.py title_colors #00ff00 #ffffff
#              window_info.py
#
#              etc ...
#
# Example output : https://github.com/tobeypeters/.dotfiles/blob/master/images/currentdesktop3.png

def get_window_info(e):
    focused_window = i3.get_tree().find_focused()

    if (focused_window.window_class is None): return ''

    showApplication = ('application' in sys.argv)
    showTitle = ('title' in sys.argv)

    # Following .index() calls are safe, because the if statement makes sure it's there.
    if ('application_colors' in sys.argv):
        application_text = formatText(to_CamelCase(focused_window.window_class), sys.argv.index('application_colors'))

    if ('title_colors' in sys.argv):
        title_text = formatText(stripClassFromTitle(focused_window.window_title), sys.argv.index('title_colors'))

    if (showApplication): return application_text
    if (showTitle): return title_text
    
    return ''.join([application_text, title_text])

# Strip the classname from the end of window titles
# Instead of "New Tab - Google-Chrome", we just want "New Tab"
def stripClassFromTitle(title):
	idx = None
	
	for i in range(len(title)): 
	    if (title[i] in ['-','—']): idx = i
	    	        
	return title[:idx]

# Make sure a specified string is in CamelCase format
def to_CamelCase(str):
    return ''.join([t.title() for t in str.split()])

# Add background & foreground color formatting, to a specified string
def formatText(str, argoffset):
    return ''.join(['%{B',
                    sys.argv[argoffset + 1],
                    '}',
                    '%{F',
                    sys.argv[argoffset + 2],
                    '}',
                    ' ',
                    str,
                    ' ',
                    '%{B- F-}'
                   ])

def on_window_title(i3, e):
    print(get_window_info(e))
    
i3 = i3ipc.Connection()

i3.on("window::focus", on_window_title)
i3.on("window::title", on_window_title)
i3.on("window::close", on_window_title)
i3.on("workspace", on_window_title)

i3.main()
