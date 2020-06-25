#	The MIT License(MIT)
#	Copyright(c), Tobey Peters, https://github.com/tobeypeters
#	Permission is hereby granted, free of charge, to any person obtaining a copy of this software
#	and associated documentation files (the "Software"), to deal in the Software without restriction,
#	including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense,
#	and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so,
#	subject to the following conditions:
#	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT
#	 LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#	 IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#	WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#	SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import i3ipc
import re
import getpass
import sys

def get_window_info(e):
    focused_window = i3.get_tree().find_focused()
    
    if focused_window.window_class is None:
        return ''
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'application':
            return to_camelcase(focused_window.window_class)
    
    title = focused_window.name
    
    title_len = len(title)    
    title = stripclassnameoff(title, '-')
    
    if len(title) == title_len:
    	title = stripclassnameoff(title, '—')
    
    title = title.replace('/home/{}'.format(user), '~')
    title = re.sub(r'@.*:', ':', title)
    
    if len(sys.argv) > 1:
        if sys.argv[1] == 'title':
            return title
    else:
        return to_camelcase(focused_window.window_class) + ': ' + title

def stripclassnameoff(str, character):
	idx = None
	for i in range(len(str)): 
	    if character == str[i]: 
	        idx = i 
	buffer = str[:idx] 
		
	return buffer

def to_camelcase(str):
    return ' '.join([t.title() for t in str.split()])

def on_window_title(i3, e):
    print(get_window_info(e))
    
i3 = i3ipc.Connection()

user = getpass.getuser()

i3.on("window::focus", on_window_title)
i3.on("window::title", on_window_title)
i3.on("window::close", on_window_title)
i3.on("workspace", on_window_title)

i3.main()
