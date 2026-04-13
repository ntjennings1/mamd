""" Native imports. """
import os
import asyncio
import tkinter as tk

class Helper():
    """ A class representing a Helper.

    ```
    Attributes
    ----------
    server : The Helper's server
    root : The Helper's root
    width : The wdith of the Helper's root
    height : The height of the Helper's root
    screen_width : The width of the screen
    screen_height : The height of the screen
    dir : The Helper's directory
    logo : The Helper's logo
    icon : The Helper's icon
    close_button : The Helper's close button
    bars : The Helper's bars
    section_bar : The Helper's section bar
    info_bar : The Helpers info bar
    sections : The Helper's sections
    section : The Helper's section
    section_selector : The Helper's section selector
    section_informer : The Helper's section informer

    ```
    Methods
    -------
    throw_exec : Throws a specified exception
    close : Closes the helper
    clear_info : Clears the Helper's info
    set_info : Set the Helper's info
    clear_help : Clears Helper informer
    print_help : Prints to Helper informer
    help : Runs Helper sections
    customize : Customizes the Helper
    config : Configures the Helper
    show : Shows the Helper
    """
        
    """ Initializes the class instance.
    
    @return null
    """
    def __init__(self, server):
        self.server = server
        self.root = tk.Toplevel()
        self.width = "300"
        self.height = "500"
        self.screen_width = self.get_root().winfo_screenwidth()
        self.screen_height = self.get_root().winfo_screenheight()
        self.dir = os.path.dirname(os.path.abspath(__file__))
        self.logo = None
        self.icon = None

        self.close_button = None

        self.bars = []
        self.section_bar = None
        self.info_bar = None

        self.sections = ['Select an option ...', 'Nav', 'Create', 'Games', 'Close']
        self.section = None
        self.section_selector = None
        self.section_informer = None

    """ Returns the helper's server.

    @return server : The helper's server
    @rtype server : Obj.class
    """
    def get_server(self):
        return self.server

    """ Sets the helper's server.

    @param server : A server
    @type server : Obj.class
    """
    def set_server(self, server):
        self.server = server

    """ Returns the helper's root.

    @return root : The helper's root.
    @rtype root : tk.Tk()
    """
    def get_root(self):
        return self.root

    """ Sets the helper's root.

    @oaram root : A root
    @type root : tk.Tk()
    """
    def set_root(self, root):
        self.root = root

    """ Returns the root width.

    @return width : The root width
    @rtype width : string
    """
    def get_width(self):
        return self.width

    """ Sets the root width.

    @param width : A width
    @type width : string
    """
    def set_width(self, width):
        self.width = width

    """ Returns the root height.

    @return height : The root height
    @rtype height : A height
    """
    def get_height(self):
        return self.height

    """ Sets the root height.

    @param height : A height
    @type height : string
    """
    def set_height(self, height):
        self.height = height

    """ Returns the screen width.

    @return screen_width : The screen width
    @rtype screen_width : int
    """
    def get_swidth(self):
        return self.screen_width

    """ Sets the screen width.

    @param swidth : A screen width
    @type swidth : int
    """
    def set_swidth(self, swidth):
        self.screen_width = swidth

    """ Returns the screen height.

    @return screen_height : The screen height
    @rtype screen_height : int
    """
    def get_sheight(self):
        return self.screen_height

    """ Sets the screen height.

    @param sheight : A screen height
    @type sheight : int
    """
    def set_sheight(self, sheight):
        self.screen_height = sheight

    """ Returns the helper's director.

    @return dir : The helper's directory
    @rtype dir : os.path
    """
    def get_dir(self):
        return self.dir

    """ Sets the helper's directory.

    @param di : A directory
    @type di : os.path
    '"""
    def set_dir(self, di):
        self.dir = di

    """ Returns the helper's logo.

    @return logo : The helper's logo
    @rtype logo : ImageTk.PhotoImage()
    """
    def get_logo(self):
        return self.logo

    """ Sets the helper's logo.

    @param logo : A logo
    @type logo : ImageTk.PhotoImage()
    """
    def set_logo(self, logo):
        self.logo = logo

    """ Returns the helper's icon.

    @return icon : The helper's icon
    @rtype icon : ImageTk.PhotoImage()
    """
    def get_icon(self):
        return self.icon

    """ Sets the helper's icon.

    @param icon : An icon
    @type icon : ImageTk.PhotoImage()
    """
    def set_icon(self, icon):
        self.icon = icon

    """ Returns the helper's close button.

    @return close_button : The helper's close button
    @rtype close_button : tk.Button()
    """
    def get_cbutton(self):
        return self.close_button

    """ Sets the helper's close button.

    @param cbutton : A close button
    @type cbutton : tk.Button()
    """
    def set_cbutton(self, cbutton):
        self.close_button = cbutton

    """ Returns the helper's bars.

    @return bars : The helper's bars
    @rtype bars : list
    """
    def get_bars(self):
        return self.bars

    """ Sets the helper's bars.

    @param bars : Bars
    @type bars : list
    """
    def set_bars(self, bars):
        self.bars = bars

    """ Adds a bar.

    @param bar : A bar
    @type bar : tk.Text(), tk.Label()
    """
    def add_bar(self, bar):
        self.get_bars().append(bar)

    """ Returns the helper's section bar.

    @return section_bar : The helper's section bar
    @rtype section_bar : tk.Label()
    """
    def get_sbar(self):
        return self.section_bar

    """ Sets the helper's section bar.

    @param sbar : A section bar
    @type sbar : tk.Label()
    """
    def set_sbar(self, sbar):
        self.section_bar = sbar

    """ Returns the helper's info bar.

    @return info_bar : The helper's info bar
    @rtype info_bar : tk.Text()
    """
    def get_ibar(self):
        return self.info_bar

    """ Sets the helper's info bar.

    @param ibar : An info bar
    @type ibar : tk.Text()
    """
    def set_ibar(self, ibar):
        self.info_bar = ibar

    """ Returns the helper's sections.

    @return sections : The helper's sections
    @rtype sections : list
    """
    def get_sections(self):
        return self.sections

    """ Sets the helper's sections.

    @param sections : Sections
    @type sections : list
    """
    def set_sections(self, sections):
        self.sections = sections

    """ Adds a section.

    @param section : A section
    @type section : string
    """
    def add_section(self, section):
        self.get_sections().append(section)

    """ Returns the helper's section.

    @return section : The helper's section
    @rtype section : string
    """
    def get_section(self):
        return self.section

    """ Sets the helper's current section.

    @param section : A section
    @type section : string
    """
    def set_section(self, section):
        self.section = section

    """ Returns the helper's section selector.

    @return section_selector : The helper's section selector
    @rtype section_selector : ttk.Combobox
    """
    def get_sselector(self):
        return self.section_selector

    """ Sets the helper's section selector.

    @param sselector : A section selector
    @type sselector : ttk.Combobox
    """
    def set_sselector(self, sselector):
        self.section_selector = sselector

    """ Returns the helper's section informer.

    @return section_informer : The helper's section informer
    @rtype section_informer : tk.Text()
    """
    def get_sinformer(self):
        return self.section_informer

    """ Sets the helper's section informer.

    @param sinformer : A section infomer
    @type sinformer : tk.Text()
    """
    def set_sinformer(self, sinformer):
        self.section_informer = sinformer

    """ Throws a specified exception.

    @param mes : Exception type
    @type mes : string
    """
    def throw_exec(self, mes):
        if (mes == 'config'):
            print("[!] Error configuring Helper.")
        elif (mes == 'customize'):
            print("[!] Error customizing Helper.")
        elif (mes == 'iset'):
            print("[!] Error setting info.")
        elif (mes == 'iclear'):
            print("[!] Error clearing info.")
        elif (mes == 'hprint'):
            print("[!] Error printing section help.")
        elif (mes == 'hclear'):
            print("[!] Error clearing section help.")
        elif (mes == 'close'):
            print('[!] Error closing helper.')

    """ Closes the helper.

    @return null
    """
    def close(self):
        try:
            self.get_server().set_helper(None)
            self.get_root().destroy()
        except Exception as ex:
            self.throw_exec('close')

    """ Clears helper info bar.

    @@return null
    """
    def clear_info(self):
        try:
            self.get_ibar().config(state='normal')
            self.get_ibar().delete('1.0', tk.END)
            self.get_ibar().config(state=tk.DISABLED)
        except Exception as ex:
            self.throw_exec('iclear')

    """ Sets helper info bar.

    @param mes : Helper info
    @type mes : string
    """
    def set_info(self, mes):
        try:
            self.get_ibar().config(state='normal')
            self.get_ibar().insert(tk.END, mes)
            self.get_ibar().tag_add('center', '1.0', 'end')
            self.get_ibar().config(state=tk.DISABLED)
        except Exception as ex:
            self.throw_exec('iset')

    """ Clears helper informer.

    @return null
    """
    def clear_help(self):
        try:
            self.get_sinformer().config(state='normal')
            self.get_sinformer().delete('1.0', tk.END)
            self.get_sinformer().config(state=tk.DISABLED)
        except Exception as ex:
            self.throw_exec('hclear')

    """ Prints to helper informer.

    @param mes : Helper section
    @@type mes : list
    """
    def print_help(self, mes):
        self.clear_help()
        try:
            self.get_sinformer().config(state='normal')
            for line in mes:
                self.get_sinformer().insert(tk.END, line)
            self.get_sinformer().config(state=tk.DISABLED)
        except Exception as ex:
            self.throw_exec('hprint')

    """ Config for helper section.

    @param mes : The section
    @type mes : string
    """
    def help(self, mes):

        if (mes == 'nav'):
            lines = [
                'Navigating options are simple.\n\n',
                '1. RED X to shutdown.\n\n',
                '2. GREEN arrow to proceed.\n\n',
                '3. ORANGE arrow to go back.\n\n',
                '4. YELLOW ? for this help menu.'
            ]
            self.print_help(lines)
        elif (mes == 'create'):
            lines = [
                'Here you can learn how to create your local servers...\n\n',
                'Dedicate 500 ports from a starting point.\n',
                '1. Input starting port:\n\n',
                '   a. 500 < port < 50000 \n\n',
                '2. Then proceed.'
            ]
            self.print_help(lines)
        elif (mes == 'filter'):
            lines = [
                'Filtering data happens two ways:\n\n',
                '1. Gamewise.\n',
                '   a. View each game.\n',
                '   b. Conditions, Events, etc\n\n',
                '2. Systemwise.\n',
                '   a. All servers at once.\n',
                '   b. Conditions, Errors, etc\n\n'
            ]
            self.print_help(lines)
        elif (mes == 'close'):
            lines = [
                'When you close the UI, you ...\n\n',
                '1. Stop threads.\n',
                '2. Shutdown the server.\n',
                '3. Disconnect clients.\n',
                '4. End all games.'
            ]
            self.print_help(lines)

    """ Customizes UI elements.

    @return null
    """
    def customize(self):
        from tkinter import ttk
        from PIL import Image, ImageTk
        
        try:

            """ Section select event listener.

            @param event : An event
            @type event : 
            """
            def on_select(event):
                self.help(self.get_sselector().get().lower())

            # Selector
            self.set_sselector(ttk.Combobox(self.get_root(),
                                            textvariable=self.get_section(),
                                            values=self.get_sections(),
                                            state='readonly'))
            self.get_sselector().bind("<<ComboboxSelected>>", on_select)
            self.get_sselector().current(0)
            self.get_sselector().place(x=(int(self.get_width()) / 2) - (self.get_sselector().winfo_width() / 2),
                                       y=(100 + self.get_sselector().winfo_height()),
                                       anchor='n')

            # Buttons
            self.set_cbutton(tk.Button(self.get_root(),
                                        width=4,
                                        state='active',
                                        text='X',
                                        bg='brown2',
                                        fg='black',
                                        activebackground='brown2',
                                        activeforeground='black',
                                        command=lambda:self.close()))
            self.get_cbutton().place(x=1,
                                     y=1,
                                     anchor='nw')

            # Bars
            src_dir = os.path.dirname(self.get_dir())
            im_dir = os.path.join(src_dir, "images")
            im_path = os.path.join(im_dir, "PONG_Logo.ico")
            img = Image.open(im_path)
            w, h = img.size
            scale = 0.5
            resized = img.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
            logo = ImageTk.PhotoImage(resized)
            self.set_logo(logo)

            self.set_sbar(tk.Label(self.get_root(),
                                   image=self.get_logo(),
                                   font=('Courier New', 12)))
            self.get_sbar().place(x=(int(self.get_width()) / 2),
                                y=50,
                                anchor='center')

            self.set_ibar(tk.Text(self.get_root(),
                                    wrap='word',
                                    height=2,
                                    width=20,
                                    font=('Courier New', 12),
                                    state=tk.DISABLED))
            self.get_ibar().place(x=(int(self.get_width()) / 2),
                                y=(int(self.get_height()) - 40),
                                anchor='center')
            self.get_ibar().tag_configure('center', justify='center')
            self.add_bar(self.get_sbar())
            self.add_bar(self.get_ibar())

            # Info
            self.set_sinformer(tk.Text(self.get_root(),
                                       wrap='word',
                                       width=25,
                                       height=15,
                                       font=('Courier New', 12),
                                       state=tk.DISABLED))
            self.get_sinformer().place(x=(20),
                                       y=(150),
                                       anchor='nw')
            self.set_info('Learn how to use sPONG')
            self.print_help(['This is the help tab.\n\n',
                            'Select which section you need help with above.'])

        except Exception as ex:
            self.throw_exec('customize')

    """ Configures the helper.

    @return null
    """
    def config(self):
        try:
            self.get_root().overrideredirect(True)
            self.get_root().attributes('-topmost', True)
            self.get_root().resizable(False, False)
            self.get_root().geometry(self.get_width() + "x" + self.get_height())
        except Exception as ex:
            self.throw_exec('config')

    """ Shows the helper.

    @return null
    """
    async def show(self):

        while True:
            self.get_root().update()
            await asyncio.sleep(.1)
