import tkinter
from tkinter import ttk

import data


class UI:
    screen = tkinter.Tk()
    entries = []

    screen.title("Testing")
    screen.geometry("600x700+400+10")

    ttk.Label(
            text="Tests form booking.").pack()

    def __init__(self):
        self.inputs = []

    def get_inputs_data(self, inputs):
        for entry_data in inputs:
            for key, value in entry_data.items():
                for k, v in value.items():
                     self.entries.append({key: {k:v.get()}})
        self.screen.quit()

    def fill_enries(self, test_object, elements):

        object_lable = ttk.Label(self.screen, text=test_object)
        object_lable.pack(fill='both', pady=0, padx=5, expand=False)

        for test_element in elements:

            if "input" in data.data().get_test_actions(test_object, test_element):

                if "Date" in test_element:                
                    lable = ttk.Label(self.screen, text=f"{test_element} format YYYY-MM-DD")
                else:
                    lable = ttk.Label(self.screen, text=test_element)
                                  
                entry = ttk.Entry()

                lable.pack()
                entry.pack()   
                self.inputs.append({test_object:{test_element: entry}})

        submit_btn = ttk.Button(
                text="Submit", command=lambda: self.get_inputs_data(self.inputs))

        submit_btn.pack()

        self.screen.mainloop()

        return self.entries