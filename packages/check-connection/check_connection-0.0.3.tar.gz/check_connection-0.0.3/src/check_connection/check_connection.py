#%%
import requests
import PySimpleGUI as sg
import datetime

sg.theme("Black")


class GUI:

    @staticmethod
    def ConnectionGUI(host="", number_of_tries=""):
        """creates GUI for input of host and number of tries"""

        centered = [
            [sg.Text('Please enter your specifications for the check:', size=(40, 2))],
            [sg.Text('Website URL', size=(15, 2)), sg.InputText(host, key='out_url', focus=True)],
            [sg.Text('Number of tries', size=(15, 2)), sg.InputText(number_of_tries, key='out_number', focus=True)],
            [sg.Button('OK', bind_return_key=True, auto_size_button=True)]
        ]

        layout = [
            [sg.VPush()],
            [sg.Push(), sg.Column(centered, element_justification="c"), sg.Push()],
            [sg.VPush()]
        ]

        window = sg.Window('Specification GUI', layout)
        (event, var) = window.Read()
        window.Close()
        if event == 'EXIT' or event is None:
            return 0
        else:
            return var


def list_mean(list):
    """Calculating arithmetic mean of list"""

    total = 0
    count = len(list)
    for item in list:
        if type(item) == int or type(item) == float:
            total = total + item
        else:
            count = count - 1
            pass
    if count == 0:
        print("No calculation possible - no item of type==int or type==float in list.")
        return ZeroDivisionError
    else:
        avg = total / count
        return avg


def check_connection(host="", number_of_tries=""):
    """ Checking how fast connection to certain host is"""

    host = host.strip()
    if host[0:4] == "www.":
        host = host[4:]

    if host and number_of_tries:
        pass
    else:
        while type(number_of_tries) != int:
            out_dict = GUI.ConnectionGUI(host, number_of_tries)
            host = out_dict["out_url"]
            number_of_tries = out_dict["out_number"]
            try:
                number_of_tries = int(number_of_tries)
            except ValueError:
                print("Wrong Input!")
            if host[0:4] == "www.":
                host = host[4:]

    time_list = []

    for x in range(number_of_tries):
        start_time = datetime.datetime.now()
        response = requests.get("https://www." + host)
        end_time = datetime.datetime.now()
        if response.status_code == 200:
            delta_time = (end_time - start_time).total_seconds()
            time_list.append(delta_time)
        else:
            print("Response failed:", response.status_code)
            return False

    avg_ping = list_mean(time_list)
    print("Average Ping:")
    print(str(avg_ping) + "s")
    return avg_ping

# %%
