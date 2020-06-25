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

# Gets a list of open windows

# window listing and focusing dialog for dmenu

IFS=$'\n' read -r -d '' -a windowlist < <( (wmctrl -l | awk '{ for(i=4; i<=NF; i++) printf "%s",$i (i==NF?ORS:OFS) }' ) | cut -c -38 && printf '\0' )

if [ ${#windowlist[@]} -eq 0 ]; then
  menu=$(echo "No windows open" | dmenu -l -i -p 'System:' -nb black -sb tomato)
else
  menu=$(printf '%s\n' "${windowlist[@]}" | dmenu  -l -i -p 'System:' -nb black -sb tomato)
  for i in "${!windowlist[@]}"; do
    if [ ! -z "$menu" ] && [[ "${windowlist[$i]}" = $menu ]]; then
      wmctrl -a $menu
    fi
  done
fi