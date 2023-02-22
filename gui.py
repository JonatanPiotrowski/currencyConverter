import PySimpleGUI as sg
import converter as c

layout = [
    [sg.Text("Amount of money:", size=(13, 1)), sg.Input("1", key="-AMOUNT-", size=(6, 1))],
    [sg.Text("Source currency:", size=(13, 1)), sg.Input("PLN", key="-FROM-", size=(6, 1))],
    [sg.Text("Target currency:", size=(13, 1)), sg.Input("USD", key="-TO-", size=(6, 1))],
    [sg.Button("Convert")],
]

window = sg.Window("Currency Converter", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Convert":
        try:
            amount = float(values["-AMOUNT-"])
        except ValueError:
            sg.popup(f"You have entered incorrect data")
            amount = 0
        from_currency = values["-FROM-"].upper()
        to_currency = values["-TO-"].upper()
        try:
            result = c.convert_currency(amount, from_currency, to_currency)
            if amount != 0:
                sg.popup(f"{amount} {from_currency} is equal {result:.2f} {to_currency}")
        except KeyError:
            sg.popup(f"{from_currency} or {to_currency} currency is not supported.")


window.close()
