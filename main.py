from pathlib import Path

from trayapp import TrayApp

with TrayApp(name='Test',  # the little tooltip, seen when hovering over the icon
             icon_or_path=Path('res/logo/logo.png'),  # anything that can be transformed into a PIL.Image
             icon_size=(256, 256,)  # size to create the thumbnail
             ) as app:

    # create the menu shown when icon gets right-clicked here

    app.add_button(text='hello world',
                   action=print,  # method to call when clicked
                   args=('hello world',),  # arguments, optional, in a tuple
                   # determines wheter the function gets called when the icon is left-clicked
                   # optional, default to False, can be obviously only used once per app
                   default=True  
                   )

    app.add_separator()  # well...

    with app.add_submenu(text='SubMenu') as submenu:  # submenues can be created by using a context manager within

        with submenu.add_submenu(text='first subsub') as first_sub_sub:  # and recursivly as well
            first_sub_sub.add_button(text='1.1', action=print, args=('1.1',))
            first_sub_sub.add_button(text='1.2', action=print, args=('1.2',))

        with submenu.add_submenu(text='second susub') as second_sub_sub:
            second_sub_sub.add_button(text='2.1', action=print, args=('2.1',))
            second_sub_sub.add_button(text='2.2', action=print, args=('2.2',))

        # any add_button(), add_separator(), add_submenu(), add_radiobuttongroup() can be used here
        # just remember to add them to the right submenu        

    app.add_separator()

    # a RadioButtonGroup is a group of buttons which can be used to select something
    # trying it out might be the best way to understand it
    with app.add_radiobuttongroup() as rbg:  # used with a contextmanager as well
        rbg.add(text='hello')
        rbg.add(text='world', selected=True)  # selected determines the item which is selected on creation

print(1)