import tkinter
from tkinter import font, messagebox

from nltk_bot import MyChat
from tools import pairs

chat_bot = MyChat(pairs=pairs)

height, width, input_height = 400, 300, 100


class ChatBotUI(object):
    """The chat bot graphical interface"""

    def __init__(self):

        # create root window
        self.window = tkinter.Tk(baseName="NLTK Bot Test")
        self.window.option_add("*tearOff", tkinter.FALSE)
        self.window.resizable(False, False)
        self.window.title("A simple chatbot with nltk. (no AI)")
        self.window.minsize(width, height)
        self.window.protocol("WM_DELETE_WINDOW", self.window.destroy)
        self.window.iconphoto(
            True, tkinter.PhotoImage(name="icon", file="./icon/favicon.png")
        )

        # add font
        self.text_font = font.Font(family="Helvetica", name="textFont", size=12)

        # add menu
        # self.menubar = tkinter.Menu(self.window)
        # self.window["menu"] = self.menubar
        # self.menu_quit = tkinter.Menu(self.menubar)
        # self.menubar.add_command(command=self.exit, label="Quitter")

        # add chat history frame
        self.history_frame = tkinter.Frame(
            self.window, width=width, height=height - input_height, bg="lightblue"
        )
        self.history_frame.pack(side=tkinter.TOP, expand=True, fill=tkinter.BOTH)
        self.history = tkinter.Text(
            self.history_frame,
            bd=0,
            bg="white",
            height="20",
            width="40",
            font=self.text_font,
        )
        self.history.config(state=tkinter.DISABLED)
        self.history_scroll = tkinter.Scrollbar(
            self.history_frame,
            command=self.history.yview,
            orient=tkinter.VERTICAL,
        )
        self.history_scroll.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        self.history_scroll["command"] = self.history.yview
        self.history.pack(fill=tkinter.BOTH, side=tkinter.LEFT, expand=True)

        # add send frame
        self.send_frame = tkinter.Frame(
            self.window, width=width, height=input_height, bg="yellow"
        )
        self.send_frame.pack(side=tkinter.BOTTOM, expand=True, fill=tkinter.BOTH)
        self.user_entry = tkinter.Text(
            self.send_frame,
            bd=0,
            bg="white",
            width="29",
            height="5",
            font=self.text_font,
        )
        self.user_entry.focus_set()
        self.user_entry.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)
        self.send_button = tkinter.Button(
            self.send_frame, text="Envoyer", command=self.send_text
        )
        self.send_button.pack(side=tkinter.RIGHT, fill=tkinter.BOTH, expand=True)

        # self.user_entry.bind("<Return>", self.send_text)
        self.send_button.bind("<Return>", self.send_text)
        self.window.bind_all("<Cancel>", self.exit)
        self.window.grid_columnconfigure(0, weight=1)
        self.window.grid_rowconfigure(0, weight=1)

        self.window.mainloop()

    def exit(self, event=None):
        """
        Exit from the program
        """
        self.window.quit()

    def send_text(self, event=None):
        text = self.user_entry.get("1.0", "end-1c").strip()
        self.user_entry.delete("0.0", tkinter.END)

        if text:
            self.history.config(
                state=tkinter.NORMAL, foreground="#000", font=self.text_font
            )
            self.history.insert(tkinter.END, "you -> " + text + "\n\n")

            response = chat_bot.respond(text)
            self.history.insert(tkinter.END, "bot -> " + response + "\n\n")

            self.history.config(state=tkinter.DISABLED)
            self.history.yview(tkinter.END)


if __name__ == "__main__":
    ChatBotUI()
