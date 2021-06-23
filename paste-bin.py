#Import libararies for tkinter app
import os
import platform
from tkinterdnd2 import *
from tkinter import *
from tkinter.scrolledtext import ScrolledText

#For indicator in taskbar
import signal
#gi.require_version('Gtk', '3.0')
from gi.repository import Gtk as gtk
#gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3 as appindicator
#Use gi.require_version('Notify', '0.7')
from gi.repository import Notify as notify

APPINDICATOR_ID = 'paste-bin' #identifying tag for app

#For Indicator
def main(): # initalise indicator
    indicator = appindicator.Indicator.new(APPINDICATOR_ID, os.path.abspath('/home/jjmunso/Documents/GitHub/paste-bin/img/clipboard.png'),  appindicator.IndicatorCategory.SYSTEM_SERVICES) #requires full path (if called on outside of /paste-bin)
    indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
    indicator.set_menu(build_menu())
    notify.init(APPINDICATOR_ID)
    gtk.main()

def build_menu(): #create the menu
    menu = gtk.Menu()
    item_bin = gtk.MenuItem('paste-bin')
    item_bin.connect('activate', openPasteBin) #2nd arguement must be callable, executed on click
    menu.append(item_bin)
    item_quit = gtk.MenuItem('Quit')
    item_quit.connect('activate', quit)
    menu.append(item_quit)
    menu.show_all()
    return menu

def openPasteBin(_): #exectued on click (entire tkinter build)
    window = TkinterDnD.Tk()
    window.iconphoto(False, PhotoImage(file='/home/jjmunso/Documents/GitHub/paste-bin/img/clipboard.png')) #requires full path (if called on outside of /paste-bin) to change app icon
    window.withdraw()
    window.title('pate-bin')
    window.geometry('675x475')
    window.resizable(width=False, height=False)

    Label(window, text='Drop or type here').grid(
                        row=0, column=0)


    bin = Text(window, name='textbox', bg='white', relief='sunken',
                    bd=1, highlightthickness=1, takefocus=True)
    bin.grid(row=1, column=0, sticky='news',padx=10, pady=10)

    # make the Label a drop target:
    def drop_enter(event):
        event.widget.focus_force()
        print('Entering %s' % event.widget)
        return event.action

    def drop_position(event):
        print('Position: x %d, y %d' %(event.x_root, event.y_root))
        return event.action

    def drop_leave(event):
        print('Leaving %s' % event.widget)
        return event.action

    def drop(event):
        if event.data:
            print('Dropped data:\n', event.data)
            #print_event_info(event)

            if event.widget == bin:
                # calculate the mouse pointer's text index
                bd = bin['bd'] + bin['highlightthickness']
                x = event.x_root - bin.winfo_rootx() - bd
                y = event.y_root - bin.winfo_rooty() - bd
                index = bin.index('@%d,%d' % (x,y))
                bin.insert(index, event.data)
            else:
                print('Error: reported event.widget not known')
        return event.action

    bin.drop_target_register(DND_TEXT)
    bin.dnd_bind('<<DropEnter>>', drop_enter)
    bin.dnd_bind('<<DropPosition>>', drop_position)
    bin.dnd_bind('<<DropLeave>>', drop_leave)
    bin.dnd_bind('<<Drop>>', drop)

    bin.drag_source_register(DND_TEXT)

    window.update_idletasks()
    window.deiconify()
    window.mainloop()

def quit(_):
    notify.uninit()
    gtk.main_quit()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()

'''
window.update_idletasks()
window.deiconify()
window.mainloop()
'''
