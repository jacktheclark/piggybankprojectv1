import tkinter as tk
from tkinter import messagebox
from pigsetup import setup

#parse the input list
def parse_coins(input_coins):
    if ", " not in input_coins:
        return [input_coins.strip()]
    else:
        coin_list = input_coins.split(", ")
        for i in range(len(coin_list)): #strip the list
            coin_list[i] = coin_list[i].strip()
        return coin_list

def save_input(entry_coins, entry_days, entry_key):
    # global label_error
    input_coins = entry_coins.get()
    coin_list = parse_coins(input_coins)
    input_days = entry_days.get()
    input_key = entry_key.get()
    print(coin_list)
    print(input_days)
    # Look through tokens, make required calls
    result_int = setup(coin_list, input_days, input_key)
    if result_int < 0:
        # label_error.pack()
        messagebox.showerror('Python Error', 'There is a formatting issue in one or more of your inputs')
    messagebox.showinfo(title=None, message='Piggybank_results.csv has been created in your current directory. It '
                                            'contains the results of your search. ')



def main():
    window = tk.Tk()
    frame_a = tk.Frame()
    greeting = tk.Label(master=frame_a, text="Welcome to Piggybank.\nPlease input your cryptocurrencies, "
                             "separated by commas and spaces. "
                             "\nFormat: BTC, ETH, SOL")
    greeting.pack()
    entry_coins = tk.Entry(master=frame_a, fg="white", bg="black", width=60)
    entry_coins.pack()

    label_total_days = tk.Label(master=frame_a, text="Enter the total days from which you want data,\n"
                                                     "with the knowledge that some coins may not have trading data"
                                                     "ranging beyond a certain date.\n"
                                                     "Format: Enter in number form (ex. 2)")
    label_total_days.pack()
    entry_days = tk.Entry(master=frame_a, fg="white", bg="black", width=60)
    entry_days.pack()

    label_key = tk.Label(master=frame_a, text="Please enter your Cryptocompare API key.\n"
                                                     "Disclaimer: I added this so I could upload this code to"
                                                     "Github without exposing my key.\n"
                                                     "Get a key for free at https://min-api.cryptocompare.com/pricing")
    label_key.pack()
    entry_key = tk.Entry(master=frame_a, fg="white", bg="black", width=60)
    entry_key.pack()

    frame_a.pack()

    tk.Button(window, text="Save and Run", width=10, command=lambda: save_input(entry_coins, entry_days, entry_key)).pack()


    window.mainloop()



if __name__ == "__main__":
    main()