# Paste-bin

paste-bin is a python based (tkinterdnd2) based widget for storing text. It functions with a top-menu GNOME indicator, to open and quit the program

It features drag and drop pasting in addition to normal typing and keyboard-shortcut methods

###### Dependencies:
``pip install tkinterdnd2``

``sudo apt-get install gir1.2-appindicator3-0.1``

###### Demo Gif

![Demo gif of using the paste-bin indicator][openingPasteBin]

[openingPasteBin]: demo-gifs/un-trimmed.gif "Demo of openingPasteBin"


### TODO
- Package into executable

- Test Scroll-bar
- Consider implementing multiple paste-blocks (see issue 4: https://github.com/jjmunso/paste-bin/issues/4)
- Consider implementing file hold
- Research possibility of minimise-able widget attached to top bar (expands-from top bar rather than just opening a window)
- Automatic clipboard addition to paste-bin. When user cntrl+c add that data to the paste-bin (see issue 3: https://github.com/jjmunso/paste-bin/issues/3)

### Completed
- ~~Fix Autostart Error (see issue 1: https://github.com/jjmunso/paste-bin/issues/1)~~
- ~~New line after Pastes (see issue 2: https://github.com/jjmunso/paste-bin/issues/2)~~
