# Copyright (c) 2013-2022 khal contributors
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


dark = [
    ('header', 'white', 'black'),
    ('footer', 'white', 'black'),
    ('line header', 'black', 'white', 'bold'),
    ('alt header', 'white', '', 'bold'),
    ('bright', 'dark blue', 'white', 'bold,standout'),
    ('list', 'black', 'white'),
    ('list focused', 'white', 'light blue', 'bold'),
    ('edit', 'black', 'white'),
    ('edit focus', 'white', 'light blue', 'bold'),
    ('button', 'black', 'dark cyan'),
    ('button focused', 'white', 'light blue', 'bold'),

    ('reveal focus', 'black', 'light gray'),
    ('today focus', 'white', 'dark magenta'),
    ('today', 'dark gray', 'dark green',),

    ('date header', 'light gray', 'black'),
    ('date header focused', 'black', 'white'),
    ('date header selected', 'dark gray', 'light gray'),

    ('dayname', 'light gray', ''),
    ('monthname', 'light gray', ''),
    ('weeknumber_right', 'light gray', ''),
    ('alert', 'white', 'dark red'),
    ('mark', 'white', 'dark green'),
    ('frame', 'white', 'black'),
    ('frame focus', 'light red', 'black'),
    ('frame focus color', 'dark blue', 'black'),
    ('frame focus top', 'dark magenta', 'black'),

    ('eventcolumn', '', '', ''),
    ('eventcolumn focus', '', '', ''),
    ('calendar', '', '', ''),
    ('calendar focus', '', '', ''),

    ('editbx', 'light gray', 'dark blue'),
    ('editcp', 'black', 'light gray', 'standout'),
    ('popupbg', 'white', 'black', 'bold'),
    ('popupper', 'white', 'dark cyan'),
    ('caption', 'white', '', 'bold'),
]
light = [
    ('header', 'black', 'white'),
    ('footer', 'black', 'white'),
    ('line header', 'black', 'white', 'bold'),
    ('alt header', 'black', '', 'bold'),
    ('bright', 'dark blue', 'white', 'bold,standout'),
    ('list', 'black', 'white'),
    ('list focused', 'white', 'light blue', 'bold'),
    ('edit', 'black', 'white'),
    ('edit focus', 'white', 'light blue', 'bold'),
    ('button', 'black', 'dark cyan'),
    ('button focused', 'white', 'light blue', 'bold'),

    ('reveal focus', 'black', 'dark cyan', 'standout'),
    ('today focus', 'white', 'dark cyan', 'standout'),
    ('today', 'black', 'light gray'),

    ('date header', '', 'white'),
    ('date header focused', 'white', 'dark gray', 'bold,standout'),
    ('date header selected', 'dark gray', 'light cyan'),

    ('dayname', 'dark gray', 'white'),
    ('monthname', 'dark gray', 'white'),
    ('weeknumber_right', 'dark gray', 'white'),
    ('alert', 'white', 'dark red'),
    ('mark', 'white', 'dark green'),
    ('frame', 'dark gray', 'white'),
    ('frame focus', 'light red', 'white'),
    ('frame focus color', 'dark blue', 'white'),
    ('frame focus top', 'dark magenta', 'white'),

    ('eventcolumn', '', '', ''),
    ('eventcolumn focus', '', '', ''),
    ('calendar', '', '', ''),
    ('calendar focus', '', '', ''),

    ('editbx', 'light gray', 'dark blue'),
    ('editcp', 'black', 'light gray', 'standout'),
    ('popupbg', 'white', 'black', 'bold'),
    ('popupper', 'black', 'light gray'),
    ('caption', 'black', '', ''),
]

themes: dict[str, list[tuple[str, ...]]] = {'light': light, 'dark': dark}
