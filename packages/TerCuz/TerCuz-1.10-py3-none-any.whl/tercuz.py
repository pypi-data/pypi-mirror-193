import os
import sys
import cv2
import atexit
import random
import pathlib
import pyfiglet
import numpy as np
from PIL import Image
from time import sleep
os.system('')

# THIS FUCNTION IS USED TO CLEAR THE SCREEN EVERY TIME THE PROGRAM HAS EXITED.
def exit_handler():

    if Terminal.Exit_Mode:
        sys.stdout.write(Terminal.End)
        Terminal.Cursor.Clear()

atexit.register(exit_handler)

# THIS CLASS CONTAINS ALL BG NAD FR COLOR VALUES.
class Colors:  # ESC [ <n> m	SGR	Set Graphics Rendition	Set the format of the screen and text as specified by <n>


    # BACKGROUND NORMAL COLORS

    BG_Black = '\x1b[40m'
    BG_Red = '\x1b[41m'
    BG_Green = '\x1b[42m'
    BG_Yellow = '\x1b[43m'
    BG_Blue = '\x1b[44m'
    BG_Magenta = '\x1b[45m'
    BG_Cyan = '\x1b[46m'
    BG_White = '\x1b[47m'

    Bg_Reset = '\x1b[49m'

    BG_B_Black = "\x1b[100m"
    BG_B_Red = "\x1b[101m"
    BG_B_Green = "\x1b[102m"
    BG_B_Yellow = "\x1b[103m"
    BG_B_Blue = "\x1b[104m"
    BG_B_Magenta = "\x1b[105m"
    BG_B_Cyan = "\x1b[106m"
    BG_B_White = "\x1b[107m"

    # FOREGROUND COLORS FOR TEXT

    FR_Black = "\x1b[30m"
    FR_Red = "\x1b[31m"
    FR_Green = "\x1b[32m"
    FR_Yellow = "\x1b[33m"
    FR_Blue = "\x1b[34m"
    FR_Magenta = "\x1b[35m"
    FR_Cyan = "\x1b[36m"
    FR_White = "\x1b[37m"

    Reset_Fr = '\x1b[39m'

    # TEXT BRIGHT COLORS
    FR_B_Black = "\x1b[90m"
    FR_B_Red = "\x1b[91m"
    FR_B_Green = "\x1b[92m"
    FR_B_Yellow = "\x1b[93m"
    FR_B_Blue = "\x1b[94m"
    FR_B_Magenta = "\x1b[95m"
    FR_B_Cyan = "\x1b[96m"
    FR_B_White = "\x1b[97m"

# THIS CLASS IS USED TO CONTROL VARIOUS PARAMETERS LIKE COLOR CURSOR AND FONTS
class Terminal:

    ### mode con:cols=80 lines=100 ### from windows screen

    Main_Win_Bg_Color = '\x00'
    Main_Txt_Bg_Color = '\x00'
    Main_Txt_Fr_Color = '\x00'

    Null = '\x00'
    End = f'\x1b[0m'
    SYS_Reset = '\x1b[!p'

    Exit_Mode=True

    Verbose = True
    Title = lambda title: sys.stdout.write(f'\x1b]0;{title}\x07')
    Prefix = lambda  : sys.stdout.write(Terminal.End+Terminal.Main_Win_Bg_Color)

    BG_array = []
    FR_array = []

    format = Main_Win_Bg_Color + \
             Main_Txt_Bg_Color + \
             Main_Txt_Fr_Color

    class Cursor:

        Save = lambda : sys.stdout.write(f'\x1b[s')
        Restore = lambda : sys.stdout.write( f'\x1b[u')
        Del = lambda line: f'\x1b[{line}M'


        Clear = lambda : sys.stdout.write(f'\x1b[2J')
        Hide  = lambda : sys.stdout.write(f'\x1b[?25l')
        Show  = lambda : sys.stdout.write(f'\x1b[?25h')
        Origin = lambda: sys.stdout.write(f'\x1b[H')

        class Shape:

            # Cursor_Shape  # 'ESC[<n> q'
            Default = lambda : sys.stdout.write('\033[0 q')
            Binking_block = lambda : sys.stdout.write( '\033[1 q')
            Steady_block = lambda : sys.stdout.write( '\033[2 q')
            Blinking_underline = lambda : sys.stdout.write( '\033[3 q')
            Steady_underline = lambda : sys.stdout.write( '\033[4 q')
            Blinking_bar = lambda : sys.stdout.write('\033[5 q')
            Steady_bar = lambda : sys.stdout.write('\033[6 q')

        class Move:  # SYS_COMMNDS

            Up       = lambda line=0: sys.stdout.write(f'\033[{line}A')
            Down     = lambda line=0: sys.stdout.write(f'\033[{line}B')
            Forward  = lambda line=0: sys.stdout.write(f'\033[{line}C')
            Backward = lambda line=0: sys.stdout.write(f'\033[{line}D')
            Nxt_Line = lambda line=0: sys.stdout.write(f'\033[{line}E')
            Pre_Line = lambda line=0: sys.stdout.write(f'\033[{line}f')
            Position = lambda line=0, column=0: sys.stdout.write(f'\033[{line};{column}H')

            Scroll_Up   = lambda line=1: Terminal.write(f'\x1b[{int(line)}T')
            Scroll_Down = lambda line=1: Terminal.write(f'\x1b[{int(line)}S')

    class Text:

        # Decorations
        Bold = '\x1b[1m'
        Italic = '\x1b[3m'
        Underline = '\x1b[4m'
        Blink = '\x1b[5m'

        Swap = lambda: sys.stdout.write('\x1b[7m')  # \x1b[0m

    class Font:

        m_L ='\x1b(0\x6a\x1b(B'        # ┘
        fm_L ='\x1b(0\x6b\x1b(B'       # ┐
        f_L ='\x1b(0\x6c\x1b(B'        # ┌
        L ='\x1b(0\x6d\x1b(B'          # └
        x ='\x1b(0\x6e\x1b(B'          # ┼
        __ ='\x1b(0\x71\x1b(B'         # ─
        le_T ='\x1b(0\x74\x1b(B'       # ├
        ri_T ='\x1b(0\x75\x1b(B'       # ┤
        re_T ='\x1b(0\x76\x1b(B'       # ┴
        T ='\x1b(0\x77\x1b(B'          # ┬
        line ='\x1b(0\x78\x1b(B'       # │

    @staticmethod  # NOT FOR USER
    def Error(error=Null, name=Null,exit_=False):

        if Terminal.Verbose:
            Th = Colors.BG_Black + Colors.FR_Red + Terminal.Text.Underline
            err = f"{Th}: {name} : Error : {error} :{Terminal.End}{Terminal.Main_Win_Bg_Color}"
            Terminal.write(err)

            if exit_:
                Terminal.Exit_Mode=False
                exit()

    @staticmethod  # NOT FOR USER
    def Message(message=Null, name=Null):
        if Terminal.Verbose:
            Th = Colors.BG_Black + Colors.FR_B_Green +  Terminal.Text.Underline
            msg = f"{Th}: {name} : Message : {message} :{Terminal.End}{Terminal.Main_Win_Bg_Color}"
            Terminal.write(msg)

    @staticmethod
    def Reset():

        Terminal.Main_Bg_Color='\x00'
        Terminal.Main_Fr_Color='\x00'
        Terminal.Cursor.Shape.Default()
        sys.stdout.write('\x1b[0m')
        os.system('cls') #REMEBER TO CORRECT
        Terminal.Message(message=f"Terminal Reset Done",name="Terminal")

    @staticmethod #improve this method by reducing num of opreation
    def Show_Colors(show=True):

        x = vars(Colors)
        ignore_keys = ['__module__', 'Main_Bg_Color', 'Main_Fr_Color', 'Swap', '__dict__', '__weakref__', '__doc__']
        keys = []
        for i in x:
            if i not in ignore_keys:
                keys.append(i)

        if len(Terminal.BG_array) == 0 and len(Terminal.FR_array) == 0:
            for i in keys:
                if "BG" in i:
                    Terminal.BG_array.append(x[i])
                elif "FR" in i:
                    Terminal.FR_array.append(x[i])
        if show:
            Terminal.Message(message="All this Colors can can be used by their respected attribute", name="Show_Colors")
            for i in keys:
                print(f"Terminal.Colors.{i} = " + x[i] + "+----+" + Terminal.End)

    @staticmethod #LINUX ADDKARVA NU CHE AJU
    def Set_Window_Bg_Color(color):

        x = color.replace("\x1b[", " ")
        x = x.replace("m", " ")
        if int(x) in list(range(40, 48)) + list(range(100, 108)):
            sys.stdout.write(color)
            Terminal.Main_Win_Bg_Color = color

        if os.name == 'nt':
            Terminal.Cursor.Clear()
            Terminal.Message(message=f"Terminal Background Color Set to {color}||||",name="Set_terminal_color")
        elif os.name == "posix":
            os.system('clear')
            Terminal.Message(message=f"Terminal Background Color Set to {color}||||", name="Set_terminal_color")

        else:
            Terminal.Error(error=f"Enter A valid color which has word 'BG' in it .", name="Set_Window_Bg_Color")

    @staticmethod
    def Set_Text_Bg_Color(color):
        x=color.replace("\x1b[", " ")
        x=x.replace("m"," ")
        if int(x) in list( range(40,48)) + list(range(100,108)):
            Terminal.Main_Txt_Bg_Color=color
            Terminal.Message(message=f"Text BG color Set to {Terminal.Main_Txt_Bg_Color}||||",name="Set_Text_Bg_Color")
        else:
            Terminal.Error(error=f"Enter A valid color which has word 'BG' in it .",name="Set_Text_Bg_Color")

    @staticmethod
    def Set_Text_Fr_Color(color):
        x = color.replace("\x1b[", " ")
        x = x.replace("m", " ")
        if int(x) in list(range(30, 38)) + list(range(90, 98)):
            Terminal.Main_Txt_Fr_Color = color
            Terminal.Message(message=f"Text FR color Set to {Terminal.Main_Txt_Fr_Color}||||{Terminal.End}", name="Set_Text_Fr_Color")
        else:
            Terminal.Error(error=f"Enter A valid color which has word 'FR' in it .", name="Set_Text_Fr_Color")

    @staticmethod
    def write(string="",new_line=True,theme='\x00'):

        if new_line:
            sys.stdout.write(f'{Terminal.format}{theme}{string}{Terminal.End}{Terminal.Main_Win_Bg_Color}\n')
            sys.stdout.flush()

        else:
            sys.stdout.write(f'{Terminal.format}{theme}{string}{Terminal.End}{Terminal.Main_Win_Bg_Color}')
            sys.stdout.flush()

# THIS CLASS IS USED TO WRITE TEXT IN ASCII FONTS
class Ascii_Font:

    Font_array = None
    _Last_Font_ = None
    _Font_ = None
    status=True

    @staticmethod  # NOT FOR USER
    def List_fonts():

        if Ascii_Font.Font_array is None:

            mod_path = pyfiglet.__file__.replace("__init__.py", "fonts")
            fonts = os.listdir(mod_path)

            fonts = [f for f in fonts if f.endswith('.flf') or f.endswith('.flc')]
            fonts = [f.replace('.flf', '') for f in fonts]
            fonts = [f.replace('.flc', '') for f in fonts]

            Ascii_Font.Font_array = fonts
            return Ascii_Font.Font_array

        else:
            return Ascii_Font.Font_array

    @staticmethod
    def Show_fonts():
        name = Ascii_Font.Show_fonts.__name__
        if Ascii_Font.Font_array is not None:

            num = 1
            for i in Ascii_Font.Font_array:
                print(f"{num} : {i}\n")
                try:
                    print(pyfiglet.figlet_format(f"{i}", font=i))
                    sleep(0.25)
                except pyfiglet.FontNotFound:
                    Terminal.Error(error="Sorry Unable to load This font !!! (File might be missing or corrupted) ",
                                   name=name)
                    sleep(0.50)
                num += 1
        else:
            Ascii_Font.Font_array = Ascii_Font.List_fonts()
            Ascii_Font.Show_fonts()

    @staticmethod  # NOT FOR USER
    def chk_font(font):
        name = Ascii_Font.chk_font.__name__
        try:
            pyfiglet.figlet_format("FONT", font=font)
            return True
        except pyfiglet.FontNotFound:

            Terminal.Error(error="Sorry Unable to load This font !!! (File might be missing or corrupted", name=name)
            return False

    @staticmethod
    def Set_Font(val):

        name = Ascii_Font.Set_Font.__name__
        if Ascii_Font.Font_array is not None:

            if type(val) is int:
                if val > len(Ascii_Font.Font_array):
                    Terminal.Error(error=f"Select from range 0 to {len(Ascii_Font.Font_array)}", name=name)
                else:
                    if Ascii_Font.chk_font(Ascii_Font.Font_array[val]):
                        Ascii_Font._Last_Font_ = Ascii_Font._Font_
                        Ascii_Font._Font_ = Ascii_Font.Font_array[val]
                        Ascii_Font.status = True

                        Terminal.Message(message=f"Font Set to {Ascii_Font.Font_array[val]}", name=name)

            elif type(val) is str:

                if val in Ascii_Font.Font_array:

                    if Ascii_Font.chk_font(val):
                        Ascii_Font._Last_Font_ = Ascii_Font._Font_
                        Ascii_Font._Font_ = val
                        Ascii_Font.status = True
                        Terminal.Message(message=f"Font Set to {val}", name=name)

                elif val == "off":
                    Ascii_Font.status = False
                    Terminal.Message(message=f"Font {Ascii_Font._Font_} Set to Off", name=name)

                elif val is None and Ascii_Font._Last_Font_ is None:
                    Ascii_Font._Last_Font_ = Ascii_Font._Font_
                    Ascii_Font._Font_ = val
                    Ascii_Font.status = True
                    Terminal.Message(message=f"Font Set to {val}", name=name)

                else:
                    Terminal.Error(error=f"Unable to find font {val} ", name=name)

            elif val == Ascii_Font._Last_Font_:
                if val is None:
                    Ascii_Font._Font_ = val
                    Ascii_Font.status = False
                    Terminal.Message(message=f"Font Set to {val} and Art mode is off", name=name)
                else:
                    Ascii_Font._Font_ = val
                    Terminal.Message(message=f"Font Set to {val}", name=name)
            else:
                Terminal.Error(error=f"Unable to find font {val} ", name=name)

        else:
            Ascii_Font.Font_array = Ascii_Font.List_fonts()
            Ascii_Font.Set_Font(val)

    @staticmethod
    def write(string,new_line=True,theme='\x00'):

        string=string.upper()

        if Ascii_Font.status and Ascii_Font._Font_ is not None:
            string = pyfiglet.figlet_format(f"{string}", font=Ascii_Font._Font_)
            Terminal.write(string, new_line=new_line,theme=theme)

        else:
            Terminal.Error(error="Oops! You called Ascii_Font class but no font has been selected or status is false",name="Ascii_Font.write")

# THIS CLASS IS USED TO PERFORM ANIMATION ON A GIVEN TEXT STRING.
class Animations:

    Loop = False
    Speed = 0.25
    Override = False
    ascii_fonts = True  #marck we need to add this method to enable ascii fonts in animations

    @staticmethod
    def Fall(string, speed=Speed, loop=Loop, font=None,theme=Colors.BG_Black+Colors.FR_Yellow):

        if font is not None and Ascii_Font.status:
            Ascii_Font.Set_Font(font)
            class_=Ascii_Font
        else:
            class_=Terminal


        x = ([*string])
        Terminal.Cursor.Hide()

        for i in x:
            class_.write(string=i, new_line=True,theme=theme)
            sleep(speed)

        Terminal.Cursor.Show()
        sys.stdout.write('\n')

        if loop or Animations.Loop:
            while True:
                Animations.Fall(string=x)

    @staticmethod
    def Play(string, speed=0.35, loop=Loop, font=None,theme=Colors.BG_Red+Colors.FR_Yellow):

        if font is not None and Ascii_Font.status:
            Ascii_Font.Set_Font(font)
            class_=Ascii_Font
        else:
            class_=Terminal

        x = ([*string])
        for i in x:
            Terminal.Cursor.Save()
            class_.write(string=i, new_line=False,theme=theme)
            Terminal.Cursor.Restore()
            sleep(speed)

        Terminal.Cursor.Restore()
        class_.write(string="    ", new_line=True,theme=theme)

        Terminal.Cursor.Show()
        Ascii_Font.Set_Font(Ascii_Font._Last_Font_)

        if loop or Animations.Loop:
            while True:
                Animations.Play(string=x)

    @staticmethod
    def Erase_Line(string, speed=Speed, loop=Loop, replace=" ", move="<"):

        x = ([*string])
        Terminal.Cursor.Hide()
        if move == "<":
            Terminal.write(string, new_line=False)
            num = 1
            for i in x:
                sleep(speed)
                Terminal.Cursor.Move.Backward(num)
                Terminal.write(replace, new_line=False)
                num = 2
            Terminal.Cursor.Show()

        elif move == ">":

            num = len(x)
            Terminal.Cursor.Move.Backward(num)
            Terminal.write(string, new_line=False)
            Terminal.Cursor.Move.Backward(num)
            for i in x:
                sleep(speed)
                Terminal.Cursor.Move.Forward(1)
                Terminal.Cursor.Move.Backward(1)
                Terminal.write(replace)
            Terminal.Cursor.Show()

        else:
            Terminal.Error(error="Invalid move detected parameter move can be either '<' or '>'",
                           name="Animations.Erase_Line")
            return None

        if loop or Animations.Loop:
            while True:
                Animations.Erase_Line(string=string, move=move, replace=replace)

    @staticmethod
    def Blink(string,font=None,times=0, speed=0.10, loop=Loop, override=False):

        Terminal.write()
        x = ([*string])
        if override:
            string = string
        else:
            string = Colors.BG_Black + Colors.FR_B_Green + string + Terminal.End

        if times != 0:
            if times > 50:
                time = 50
                Terminal.Error(
                    error=f": Times has benn set to Max {str(time)} : Invalid Time Value Detected. Input must be >= 50)",
                    name="Animations.Blink")
            elif times < 5:
                time = 5
                Terminal.Error(
                    error=f": Times has been set to Min {str(time)} : Invalid Time Value Detected. Input must be >= 5)",
                    name="Animations.Blink")
            else:
                time = times
        else:
            time = int(len(string) / 2)
            Terminal.Error(
                error=f": Time has been set to Default {str(time)} : Invalid Time Value Detected. Note times value "
                      "should be int only. (preferred value greater than 5 and smaller than 50 )",
                name="Animations.Blink")

        Terminal.Cursor.Save()
        Terminal.Cursor.Hide()
        for i in range(1, time):
            Terminal.write(string, new_line=False)
            sleep(speed)
            Terminal.Cursor.Restore()
            Terminal.write(Colors.BG_Black + " " * (len(x)), new_line=False)
            Terminal.Cursor.Restore()
            sleep(speed)

        Terminal.Cursor.Show()
        if loop or Animations.Loop:
            while True:
                Animations.Blink(string=string, speed=speed)

    @staticmethod
    def Slide_Colors(string, font=None,loop=Loop):

        if font is not None and Ascii_Font.status:
            Ascii_Font.Set_Font(font)
            class_=Ascii_Font
        else:
            class_=Terminal

        Terminal.write()
        speed = 0.0001
        Terminal.Show_Colors(show=False)
        Terminal.Cursor.Hide()
        x = ([*string])

        Terminal.Cursor.Save()
        Terminal.write(string, new_line=False)
        Terminal.Cursor.Restore()
        num = 0
        for txt_color in Terminal.FR_array:

            z = txt_color.replace("\x1b[", "")
            z = z.replace("m", "")
            if int(z) in [30, 37, 90, 97]:
                continue
            for i in x:
                sleep(speed)
                Terminal.Cursor.Move.Forward(1)
                Terminal.Cursor.Move.Backward(1)
                Terminal.write(i, new_line=False,theme=Colors.BG_Black + txt_color)

            Terminal.Cursor.Restore()
        Terminal.Cursor.Show()

        if loop or Animations.Loop:
            while True:
                Animations.Slide_Colors(string=string)

    @staticmethod
    def Random_Colors(string, font=None, speed=0.10, loop=Loop):

        if font is not None and Ascii_Font.status:
            Ascii_Font.Set_Font(font)
            class_ = Ascii_Font
        else:
            class_ = Terminal

        Terminal.Show_Colors(show=False)
        x = ([*string])

        Terminal.Cursor.Hide()
        Terminal.Cursor.Save()
        class_.write(string, new_line=False)
        Terminal.Cursor.Restore()

        for txt_color in Terminal.FR_array:
            z = txt_color.replace("\x1b[", "")
            z = z.replace("m", "")
            if int(z) in [30, 37, 90, 97]:
                continue
            sleep(speed)
            class_.write( string, new_line=False,theme=Colors.BG_Black + txt_color)
            Terminal.Cursor.Restore()
            Terminal.Cursor.Save()

        txt_color = random.choice(Terminal.FR_array)
        class_.write( string, new_line=False,theme=Colors.BG_Black + txt_color)
        Terminal.Cursor.Show()

        if loop or Animations.Loop:
            while True:
                Animations.Random_Colors(string=string)

    @staticmethod
    def Loading(message="Loading...", fill="_", replace="|", length=100, bar_color='\x1b[100m'):

        speed = 0.05
        Terminal.write()
        Terminal.Cursor.Hide()
        th = Colors.FR_B_Green + Terminal.Text.Underline

        if type(length) is int and length in range(20, 211):
            length = length
            Terminal.Message(message=f"Length set to Custom {length}",
                             name="Animations.Loading")
        else:
            length = 100
            Terminal.Error(error=f": Length set to Default {length} : Note length must be a int between 20 to 210 "
                           , name="Animations.Loading")

        if len(Terminal.BG_array) == 0:
            Terminal.Show_Colors(show=False)

        if bar_color in Terminal.BG_array:
            bar_color = bar_color
            Terminal.Message(message=f"bar_color set to Custom Background Color",
                             name="Animations.Loading")

        elif bar_color is None:
            if Terminal.Main_Txt_Bg_Color == '\x00':
                bar_color = Colors.BG_Black
                Terminal.Message(message="bar_color set to None", name="Animations.Loading")
            else:
                bar_color = Terminal.Main_Txt_Bg_Color
                Terminal.Message(message="bar_color set to None", name="Animations.Loading")

        else:
            Terminal.Error(
                error=f": Bar_Color set to Defalut : Please Select A valid Foreground_Color from Terminal.Colors.FR_*",
                name="Animations.Loading")
            bar_color = '\x1b[100m'

        if type(message) and type(replace) and type(fill) is not str:
            message = "Loading..."
            replace = "_"
            fill = "|"
            Terminal.Error(
                error=": Using Defaluts for message, replace, fill :Note values message, replace and fill should be string or any Ascii Value",
                name="Animations.Loading")
        else:
            message = message
            replace = replace
            fill = fill
            Terminal.Message(
                message=f" Values : Message='{message}', Replace='{replace}', Fill='{fill}' : Set Successfully",
                name="Animation.Loading")

        Terminal.write(th + message + '\n')
        Terminal.write(th + fill * length + Terminal.End, new_line=False)
        Terminal.Cursor.Move.Backward(length)
        Terminal.Cursor.Move.Backward(length)
        sleep(speed)
        for i in range(length):
            sleep(speed)
            Terminal.Cursor.Move.Forward(1)
            Terminal.Cursor.Move.Backward(1)
            Terminal.write(th + bar_color + replace, new_line=False)
        Terminal.Cursor.Show()

# THIS IS A SUPPORTING SYSTEM CLASS
class Main:

    Mode = "print"
    Out_File = None
    Default_Ext = ".aplay"

    Allowed_VF = ['.mp4', '.mkv']
    Allowed_IF = ['.jpg', '.png', '.jpeg','.bmp']

    Video_File = False
    Write_Header = False
    Save_location="Aplay/Saved/"

    MoreLevels = True
    Camera_Gscale = False

    # 70 levels of gray
    gscale1 = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    # 10 levels of gray
    gscale2 = r'@%#*+=-:. '
    # 21 levels of gray for cam
    gscale3 = r"?-_+~<>i!lI;:,\"^`'. "

# THIS CLASS IS USED TO PLAY VIDEOS AND IMAGES INTO ASCII.
class Ascii_Display:

    @staticmethod
    def convert(img):

        if Main.Video_File:
            image = Image.fromarray(img).convert('L')
        else:
            image = Image.open(img).convert('L')

        W, H = image.size
        cols = 150
        scale = 0.43
        w = W / cols
        h = w / scale
        rows = int(H / h)

        if cols > W or rows > H:
            print("")
            Terminal.Error(error="Image too small for specified cols!",name="Ascii_Display.convert",exit_=True)

        def getAverageL(image):

            im = np.array(image)
            w, h = im.shape
            return np.average(im.reshape(w * h))

        aimg = []
        for j in range(rows):
            y1 = int(j * h)
            y2 = int((j + 1) * h)
            if j == rows - 1:
                y2 = H
            aimg.append("")

            for i in range(cols):
                x1 = int(i * w)
                x2 = int((i + 1) * w)
                if i == cols - 1:
                    x2 = W
                img = image.crop((x1, y1, x2, y2))
                avg = int(getAverageL(img))

                if Main.MoreLevels:
                    gsval = Main.gscale1[int((avg * 69) / 255)]
                elif Main.Camera_Gscale:
                    gsval = Main.gscale3[int((avg * len(Main.gscale3) - 1) / 255)]
                else:
                    gsval = Main.gscale2[int((avg * 9) / 255)]

                aimg[j] += gsval

        if Main.Mode == "print":
            Terminal.write('\x1b[H', new_line=False)
            for row in aimg:
                Terminal.write(f"{row}\n", new_line=False)
            # Terminal.write('\b', new_line=False)

        elif Main.Mode == "save":

            if Main.Write_Header:
                with open(Main.Out_File, 'w') as file:
                    file.write(f"row{rows}:col{cols}:scale{scale}\n")
                    Main.Write_Header = False

            with open(Main.Out_File, "a") as file:
                file.write('\x1b[H')
                for row in aimg:
                    file.write(f"{row}\n")

    # Function to extract frames
    @staticmethod
    def Video_(vid):

        Main.Video_File=True

        vidObj = cv2.VideoCapture(vid)
        total_frames = int(vidObj.get(cv2.CAP_PROP_FRAME_COUNT))

        for i in range(int(total_frames)):
            vidObj.set(cv2.CAP_PROP_POS_FRAMES, i)
            success, frame = vidObj.read()
            if success:
                Ascii_Display.convert(img=frame)
                Main.Write_Header = False

        Main.Video_File = False

    @staticmethod
    def Camera_():

        Terminal.Cursor.Move.Position(line=49,column=170)
        Terminal.write(": Press 'q' to stop :")

        vidObj = cv2.VideoCapture(0)

        success = 1
        while success:
            success, frame = vidObj.read()
            if success:
                Ascii_Display.convert(img=frame)
                Main.Write_Header = False

                key = cv2.waitKey(1)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        Main.Video_File = False
        Main.MoreLevels = True

    @staticmethod
    def Play(file, speed=0.05):

        if os.path.isfile(file) and (file).split('.')[-1] == "aplay":
            with open(file, 'r') as file:
                x = file.readlines()
                header = x[0]
                rows = int(header.split(':')[0].replace('row', ''))
        else:
            Terminal.Error(error=f"The given soruce '{file}' is Invalid or it's not supproted format.",
                           name="Ascii_Display.Play")
        last_row = 1
        row = rows
        for i in range(int(len(x) / rows)):
            strx = x[last_row:row]
            strx = ' '.join(strx)
            Terminal.write(string=f"{strx}", new_line=False)
            last_row = row
            row += rows
            sleep(speed)

    @staticmethod
    def Media(soruce, mode="print"):

        if mode is not None and type(mode) == str and mode in ["print", "save"]:
            Main.Mode = mode
            if Main.Mode == "save":
                Main.Write_Header=True
                Main.Out_File = f"{os.path.basename(soruce).split('/')[-1].split('.')[0]}{Main.Default_Ext}"
        else:
            Terminal.Error(error=f"Mode {mode} is Invalid. Using Default mode 'print'", name="img2ascii.Play",
                           exit_=True)

        if type(soruce) is str:

            if soruce == "camera":
                Main.Video_File = True
                Ascii_Display.Camera_()

            elif os.path.isfile(soruce):
                if pathlib.Path(soruce).suffix.lower() in Main.Allowed_IF:
                    Ascii_Display.convert(img=soruce)

                elif pathlib.Path(soruce).suffix.lower() in Main.Allowed_VF:
                    Main.Video_File=True
                    Ascii_Display.Video_(vid=soruce)
        else:
            Terminal.Error(error=f"The given soruce '{soruce}' is Invalid or it's not supproted format.",
                           name="Ascii_Display.Play", exit_=True)