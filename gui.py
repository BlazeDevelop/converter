import tkinter as tk
from converter import convert_currency, get_currencies

class CurrencyConverter:
    def __init__(self, master):
        self.master = master
        master.title("Currency Converter")

        currencies = get_currencies()

        # Currency from
        self.from_label = tk.Label(master, text="From:")
        self.from_label.grid(row=0, column=0)

        self.from_var = tk.StringVar(master)
        self.from_var.set(currencies[0])
        self.from_menu = tk.OptionMenu(master, self.from_var, *currencies)
        self.from_menu.grid(row=0, column=1)

        # Currency to
        self.to_label = tk.Label(master, text="To:")
        self.to_label.grid(row=1, column=0)

        self.to_var = tk.StringVar(master)
        self.to_var.set(currencies[1])
        self.to_menu = tk.OptionMenu(master, self.to_var, *currencies)
        self.to_menu.grid(row=1, column=1)

        # Amount
        self.amount_label = tk.Label(master, text="Amount:")
        self.amount_label.grid(row=2, column=0)

        self.amount_entry = tk.Entry(master)
        self.amount_entry.grid(row=2, column=1)

        # Result
        self.result_label = tk.Label(master, text="")
        self.result_label.grid(row=3, column=0, columnspan=2)

        # Convert button
        self.convert_button = tk.Button(master, text="Convert", command=self.convert)
        self.convert_button.grid(row=4, column=0, columnspan=2)

        # Made by label
        self.made_by_label = tk.Label(master, text="Сделано чатгпт", font=("Arial", 8))
        self.made_by_label.place(x=10, y=165)

    def convert(self):
        amount = self.amount_entry.get()
        currency_from = self.from_var.get()
        currency_to = self.to_var.get()
        result = convert_currency(amount, currency_from, currency_to)
        self.result_label.config(text=result)

root = tk.Tk()
currency_converter = CurrencyConverter(root)
root.mainloop()
