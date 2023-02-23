import PySimpleGUI as sg
import requests.exceptions

import converter as c

layout = [
    [sg.Text("Amount of money:", size=(13, 1)), sg.Input("1", key="-AMOUNT-", size=(6, 1))],
    [sg.Text("Source currency:", size=(13, 1)), sg.Combo(c.get_currencies_list(), key="-FROM-")],
    [sg.Text("Target currency:", size=(13, 1)), sg.Combo(c.get_currencies_list(), key="-TO-")],
    [sg.Button("Convert")],
]

window = sg.Window("Currency Converter", layout, finalize=True)
window['-AMOUNT-'].bind("<Return>", "_Enter")


def gui_support():
    try:
        amount = float(values["-AMOUNT-"])
        from_currency = values["-FROM-"]
        to_currency = values["-TO-"]
    except ValueError:
        sg.popup(f"You have entered incorrect data")
        amount = 0
        from_currency = None
        to_currency = None
    try:
        result = c.convert_currency(amount, from_currency, to_currency)
        if amount > 0:
            sg.popup(f"{amount} {from_currency} is equal {result:.2f} {to_currency}")
    except KeyError:
        sg.popup(f"{from_currency} or {to_currency} currency is not supported.")
    except requests.exceptions.JSONDecodeError:
        sg.popup(f"Incorrect data!")


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == "-AMOUNT-" + "_Enter":
        gui_support()
    elif event == "Convert":
        gui_support()

window.close()
