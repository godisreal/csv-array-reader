
import tkinter as tk
from tkinter import filedialog
from functools import partial
import re, sys, os

# Version Check
if sys.version_info[0] == 3: # Python 3
    from tkinter import *
    #from tkinter import ttk
    from tkinter.ttk import Notebook
    from tkinter.ttk import Treeview
    from tkinter.ttk import Button
    import tkinter.filedialog as tkf
else:
    # Python 2
    from Tkinter import *
    from ttk import Notebook
    from ttk import Treeview
    from ttk import Entry
    import tkFileDialog as tkf
    

class FindPopup(tk.Toplevel):
    def __init__(self, master):
        super().__init__()
        self.master = master
    
        self.title("Find in file")
        self.center_window()
        self.transient(master)
        self.matches_are_highlighted = True
    
        self.main_frame = tk.Frame(self, bg="lightgrey")
        self.button_frame = tk.Frame(self.main_frame, bg="lightgrey")
        self.find_label = tk.Label(self.main_frame, text="Find: ", bg="lightgrey", fg="black")
        self.find_entry = tk.Entry(self.main_frame, bg="white", fg="black")
        self.find_button = tk.Button(self.button_frame, text="Find All", bg="lightgrey", fg="black", command=self.find)
        self.next_button = tk.Button(self.button_frame, text="Next", bg="lightgrey", fg="black", command=self.jump_to_next_match)
        self.cancel_button = tk.Button(self.button_frame, text="Cancel", bg="lightgrey", fg="black", command=self.cancel)
    
        self.main_frame.pack(fill=tk.BOTH, expand=1)
        self.find_button.pack(side=tk.LEFT, pady=(0,10), padx=(20,20))
        self.next_button.pack(side=tk.LEFT, pady=(0,10), padx=(15,20))
        self.cancel_button.pack(side=tk.LEFT, pady=(0,10), padx=(15,0))
        self.button_frame.pack(side=tk.BOTTOM, fill=tk.BOTH)
        self.find_label.pack(side=tk.LEFT, fill=tk.X, padx=(20,0))
        self.find_entry.pack(side=tk.LEFT, fill=tk.X, expand=1, padx=(0,20))
    
        self.find_entry.focus_force()
        self.find_entry.bind("<Return>", self.jump_to_next_match)
        self.find_entry.bind("<KeyRelease>", self.matches_are_not_highlighted)
        self.bind("<Escape>", self.cancel)
    
        self.protocol("WM_DELETE_WINDOW", self.cancel)

    def find(self, event=None):
        text_to_find = self.find_entry.get()
        if text_to_find and not self.matches_are_highlighted:
            self.master.remove_all_find_tags()
        self.master.highlight_matches(text_to_find)
        self.matches_are_highlighted = True
    
    def jump_to_next_match(self, event=None):
        text_to_find = self.find_entry.get()
        if text_to_find:
            if not self.matches_are_highlighted:
                self.find()
            self.master.next_match()
    
    def cancel(self, event=None):
        self.master.remove_all_find_tags()
        self.destroy()
    
    def matches_are_not_highlighted(self, event):
    
        key_pressed = event.keysym
        if not key_pressed == "Return":
            self.matches_are_highlighted = False
    
    def center_window(self):
        master_pos_x = self.master.winfo_x()
        master_pos_y = self.master.winfo_y()
    
        master_width = self.master.winfo_width()
        master_height = self.master.winfo_height()
    
        my_width = 300
        my_height = 100
    
        pos_x = (master_pos_x + (master_width // 2)) - (my_width // 2)
        pos_y = (master_pos_y + (master_height // 2)) - (my_height // 2)
    
        geometry = "{}x{}+{}+{}".format(my_width, my_height, pos_x, pos_y)
        self.geometry(geometry)
        

class Editor(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.FONT_SIZE = 12
        self.AUTOCOMPLETE_WORDS = ["def", "import", "if", "else", "while", "for","try:", "except:", "print(", "True", "False"]
        self.WINDOW_TITLE = "Text Editor"
        self.open_file = ""
        self.title(self.WINDOW_TITLE)
        self.geometry("800x600")
        self.menubar = tk.Menu(self, bg="lightgrey", fg="black")
    
        self.file_menu = tk.Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.file_menu.add_command(label="New", command=self.file_new, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open", command=self.file_open, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Save", command=self.file_save, accelerator="Ctrl+S")
        
        self.edit_menu = tk.Menu(self.menubar, tearoff=0, bg="lightgrey", fg="black")
        self.edit_menu.add_command(label="Cut", command=self.edit_cut, accelerator="Ctrl+X")
        self.edit_menu.add_command(label="Paste", command=self.edit_paste, accelerator="Ctrl+V")
        self.edit_menu.add_command(label="Undo", command=self.edit_undo, accelerator="Ctrl+Z")
        self.edit_menu.add_command(label="Redo", command=self.edit_redo, accelerator="Ctrl+Y")
    
        self.menubar.add_cascade(label="File", menu=self.file_menu)
        self.menubar.add_cascade(label="Edit", menu=self.edit_menu)
        self.configure(menu=self.menubar)
        
        
        self.line_numbers = Text(self, bg="lightgrey", fg="black", width=6)
        self.line_numbers.insert(1.0, "1 \n")
        self.line_numbers.configure(state="disabled")
        self.line_numbers.pack(side=tk.LEFT, fill=tk.Y)

        #self.scrollbar = Scrollbar(self, orient="vertical", command=self.scroll_text_and_line_numbers)
        #self.main_text.configure(yscrollcommand=self.scrollbar.set)
        #self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        
        self.main_text = tk.Text(self, bg="white", fg="black", font=("Ubuntu Mono", self.FONT_SIZE))
        self.main_text.pack(expand=1, fill=tk.BOTH)
    
        self.main_text.bind("<space>", self.destroy_autocomplete_menu)
        self.main_text.bind("<KeyRelease>", self.display_autocomplete_menu)
        self.main_text.bind("<Tab>", self.insert_spaces)
    
        self.bind("<Control-s>", self.file_save)
        self.bind("<Control-o>", self.file_open)
        self.bind("<Control-n>", self.file_new)

    def file_new(self, event=None):
        file_name = filedialog.asksaveasfilename()
        if file_name:
            self.open_file = file_name
            self.main_text.delete(1.0, tk.END)
            self.title(" - ".join([self.WINDOW_TITLE, self.open_file]))

    def file_open(self, event=None):
        file_to_open = filedialog.askopenfilename()

        if file_to_open:
            self.open_file = file_to_open
            self.main_text.delete(1.0, tk.END)

            with open(file_to_open, "r") as file_contents:
                file_lines = file_contents.readlines()
                if len(file_lines) > 0:
                    for index, line in enumerate(file_lines):
                        index = float(index) + 1.0
                        line_t = re.sub(r',', ',\t', line)
                        self.main_text.insert(index, line_t)
                        #self.main_text.insert(index, line)
        self.title(" - ".join([self.WINDOW_TITLE, self.open_file]))

    def file_save(self, event=None):
        if not self.open_file:
            new_file_name = filedialog.asksaveasfilename()
            if new_file_name:
                self.open_file = new_file_name
            if self.open_file:
                new_contents = self.main_text.get(1.0, tk.END)
                with open(self.open_file, "w") as open_file:
                    open_file.write(new_contents)

    def select_all(self, event=None):
        self.main_text.tag_add("sel", 1.0, tk.END)
        return "break"

    def edit_cut(self, event=None):
        self.main_text.event_generate("<<Cut>>")
        return "break"

    def edit_paste(self, event=None):
        self.main_text.event_generate("<<Paste>>")
        self.on_key_release()
        self.tag_all_lines()
        return "break"

    def edit_undo(self, event=None):
        self.main_text.event_generate("<<Undo>>")
        return "break"

    def edit_redo(self, event=None):
        self.main_text.event_generate("<<Redo>>")
        return "break"

    def insert_spaces(self, event=None):
        self.main_text.insert(tk.INSERT, " ")
        return "break"

    def get_menu_coordinates(self):
        bbox = self.main_text.bbox(tk.INSERT)
        menu_x = bbox[0] + self.winfo_x() + self.main_text.winfo_x()
        menu_y = bbox[1] + self.winfo_y() + self.main_text.winfo_y() + self.FONT_SIZE + 2
        
        return (menu_x, menu_y)

    def display_autocomplete_menu(self, event=None):
        current_index = self.main_text.index(tk.INSERT)
        start = self.adjust_floating_index(current_index)

        try:
            currently_typed_word = self.main_text.get(start + " wordstart", tk.INSERT)
        except tk.TclError:
            currently_typed_word = ""
        
        currently_typed_word = str(currently_typed_word).strip()

        if currently_typed_word:
            self.destroy_autocomplete_menu()

            suggestions = []
            for word in self.AUTOCOMPLETE_WORDS:
                if word.startswith(currently_typed_word) and not currently_typed_word == word:
                    suggestions.append(word)

            if len(suggestions) > 0:
                x, y = self.get_menu_coordinates()
                self.complete_menu = tk.Menu(self, tearoff=0, bg="lightgrey", fg="black")

                for word in suggestions:
                    insert_word_callback = partial(self.insert_word, word=word, part=
                        currently_typed_word, index=current_index)
                    self.complete_menu.add_command(label=word, command=
                        insert_word_callback)

                self.complete_menu.post(x, y)
                self.main_text.bind("<Down>", self.focus_menu_item)


    def destroy_autocomplete_menu(self, event=None):
        try:
            self.complete_menu.destroy()
            self.main_text.unbind("<Down>")
            self.main_text.focus_force()
        except AttributeError:
            pass

    def insert_word(self, word, part, index):
        amount_typed = len(part)
        remaining_word = word[amount_typed:]
        remaining_word_offset = " +" + str(len(remaining_word)) + "c"
        self.main_text.insert(index, remaining_word)
        self.main_text.mark_set(tk.INSERT, index + remaining_word_offset)
        self.destroy_autocomplete_menu()
        self.main_text.focus_force()

    def adjust_floating_index(self, number):
        indices = number.split(".")
        x_index = indices[0]
        y_index = indices[1]
        y_as_number = int(y_index)
        y_previous = y_as_number - 1
        return ".".join([x_index, str(y_previous)])

    def focus_menu_item(self, event=None):
        try:
            self.complete_menu.focus_force()
            self.complete_menu.entryconfig(0, state="active")
        except tk.TclError:
            pass
    
    def tag_all_lines(self):
        final_index = self.main_text.index(tk.END)
        final_line_number = int(final_index.split(".")[0])

        for line_number in range(final_line_number):
            line_to_tag = ".".join([str(line_number), "0"])
            self.tag_keywords(None, line_to_tag)
        self.update_line_numbers()
    
    def update_line_numbers(self):
        self.line_numbers.configure(state="normal")
        self.line_numbers.delete(1.0, tk.END)
        number_of_lines = self.main_text.index(tk.END).split(".")[0]
        line_number_string = "\n".join(str(no+1) for no in range(int(number_of_lines)))
        self.line_numbers.insert(1.0, line_number_string)
        self.line_numbers.configure(state="disabled")
    
    def show_find_window(self, event=None):
        FindPopup(self)
    
    def highlight_matches(self, text_to_find):
        self.main_text.tag_remove("findmatch", 1.0, tk.END)
        self.match_coordinates = []
        self.current_match = -1
    
        find_regex = re.compile(text_to_find)
        search_text_lines = self.main_text.get(1.0, tk.END).split("\n")
    
        for line_number, line in enumerate(search_text_lines):
            line_number += 1
        for match in find_regex.finditer(line):
            start, end = match.span()
            start_index = ".".join([str(line_number), str(start)])
            end_index = ".".join([str(line_number), str(end)])
            self.main_text.tag_add("findmatch", start_index, end_index)
            self.match_coordinates.append((start_index, end_index))
    
    def next_match(self, event=None):
        try:
            current_target, current_target_end = self.match_coordinates[self.current_match]
            self.main_text.tag_remove("sel", current_target, current_target_end)
            self.main_text.tag_add("findmatch", current_target, current_target_end)
        except IndexError:
            pass
    
        try:
            self.current_match = self.current_match + 1
            next_target, target_end = self.match_coordinates[self.current_match]
        except IndexError:
            if len(self.match_coordinates) == 0:
                msg.showinfo("No Matches", "No Matches Found")
            else:
                if msg.askyesno("Wrap Search?", "Reached end of file. Continue from the top?"):
                    self.current_match = -1
                    self.next_match()
                else:
                    self.main_text.mark_set(tk.INSERT, next_target)
                    self.main_text.tag_remove("findmatch", next_target, target_end)
                    self.main_text.tag_add("sel", next_target, target_end)
                    self.main_text.see(next_target)
    
    def remove_all_find_tags(self):
        self.main_text.tag_remove("findmatch", 1.0, tk.END)
        self.main_text.tag_remove("sel", 1.0, tk.END)

if __name__ == "__main__":
    editor = Editor()
    editor.mainloop()
