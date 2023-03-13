"""
Author: Mohamed Fariz
Version: 20230313
Application Name: Predictor

It is a supervised machine learning algorithm to predict the future data.
"""

# pylint: disable=C0302


def special_day_banner(msg: str):
    """
    This special_day_banner function is used to display about the event of the day
    """

    special_day_label: Label = Label(master=app, text=msg, bg="yellow")
    special_day_label.pack(fill="x")


def exit_app() -> None:
    """
    This exit_app function used to exit the tkinter application
    """

    app.withdraw()

    if askyesno(title="Predictor", message="Are you sure do you really want to quit?"):
        app.quit()
        clear_cache()
        print(F_GREEN + S_BRIGHT + "Bye!!")
        terminate()

    else:
        app.deiconify()
        return None


def clrscr() -> None:
    """
    This clear_screen function is used to clear the console screen
    """

    if uname == "Linux":
        terminal(command="clear")

    if uname == "Windows":
        terminal(command="cls")


def clear_cache() -> None:
    """
    This clear_cache function is used to delete the pycache folder
    """

    cache_dir: str = join(base_path, "__pycache__")

    if isdir(s=cache_dir):
        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}Clearing cache files, Please wait..."
        )
        rmtree(path=cache_dir)


def figlet_banner(font: str) -> None:
    """
    This figlet_banner function is used to print the figlet text on console
    """

    print()
    print(S_BRIGHT + figlet_format(text="Predictor", font=font))
    print(f"Figlet Font: {font}")


def loading_ui() -> None:
    """
    This loading_ui function is used to load the user interface.
    """

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Loading please wait..."
    )

    header_label.config(text="Loading please wait...")

    rb1.config(state="disabled")
    rb2.config(state="disabled")

    exit_button.config(state="disabled")

    fig.suptitle("Loading...")
    fig.supxlabel(t="Loading...")
    fig.supylabel(t="Loading...")

    graph.cla()
    graph.grid(visible=True)
    canvas.draw()

    minimum_value_label.config(text="Loading...")
    average_value_label.config(text="Loading...")
    maximum_value_label.config(text="Loading...")
    delta_value_label.config(text="Loading...")
    tomorrow_label.config(text="Loading...")
    next_week_label.config(text="Loading...")
    next_month_label.config(text="Loading...")
    next_year_label.config(text="Loading...")
    coefficient_label.config(text="Loading...")
    intercept_label.config(text="Loading...")
    status_label.config(text="Loading...")
    last_update_label.config(text="Loading...")

    source_button.config(text="Loading...", state="disabled")

    progress_bar.config(value=0)
    percentage_label.config(text="0.00%")

    footer_label.config(text="Loading please wait...")

    app.update()


def predict_values(data, x_axis, y_axis, prediction_lst) -> None:
    """
    This predict_values function is used to predict values from the data
    """

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Estimating Values, Please wait..."
    )

    model.fit(X=x_axis.values, y=y_axis)

    for iteration in tqdm(range(1, len(data) + 1)):
        prediction_lst.append(float(model.predict(X=[[iteration]])))

        percentage: float = round(number=iteration / len(data) * 100, ndigits=2)
        progress_bar.config(value=percentage)
        percentage_label.config(text=f"{percentage}%")

        app.update()


def draw_graph(x_axis, y_axis, prediction_lst):
    """
    This draw_graph function is used to plot the graph on application
    """

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]"
        f"\t{S_BRIGHT}Plotting Graph, Please wait..."
    )

    if choice.get() == 1:
        fig.suptitle(t="USD to INR Currency Value Predictor")
        fig.supxlabel(t="Total no of Days")
        fig.supylabel(t="1USD to INR (₹)")

        graph.plot(x_axis, y_axis, ".", label="Actual 1USD Price")
        graph.plot(x_axis, prediction_lst, "--", label="Estimated 1USD Price")

    else:
        fig.suptitle(t="e-Gold Price Predictor")
        fig.supxlabel(t="Total no of Days")
        fig.supylabel(t="Price in INR (₹)")

        graph.plot(x_axis, y_axis, ".", label="Actual e-Gold Price")
        graph.plot(x_axis, prediction_lst, "--", label="Estimated e-Gold Price")

    graph.legend()
    canvas.draw()

    app.update()


def display_data(data, prediction_lst):
    """
    This display_data function is used to display the data to the application.
    """

    total_records: int = len(data)
    min_val: float = min(data["price"])
    avg_val: float = sum(data["price"]) / total_records
    max_val: float = max(data["price"])

    minimum_value_label.config(text=f"{min_val} INR")
    average_value_label.config(text=f"{round(number=avg_val, ndigits=2)} INR")
    maximum_value_label.config(text=f"{max_val} INR")
    delta_value_label.config(
        text=f"{round(number=prediction_lst[-1] - prediction_lst[0], ndigits=2)} INR"
    )

    tomorrow_label.config(
        text=f"{round(number=float(model.predict(X=[[total_records + 1]])), ndigits=2)} INR"
    )
    next_week_label.config(
        text=f"{round(number=float(model.predict(X=[[total_records + 7]])), ndigits=2)} INR"
    )
    next_month_label.config(
        text=f"{round(number=float(model.predict(X=[[total_records + 30]])), ndigits=2)} INR"
    )
    next_year_label.config(
        text=f"{round(number=float(model.predict(X=[[total_records + 365]])), ndigits=2)} INR"
    )

    coefficient_label.config(text=f"{float(model.coef_)}")
    intercept_label.config(text=f"{model.intercept_}")

    if prediction_lst[0] > prediction_lst[-1]:
        status_label.config(text="BEAR")

    elif prediction_lst[0] == prediction_lst[-1]:
        status_label.config(text="No Change")

    else:
        status_label.config(text="BULL")

    last_update_label.config(text=list(data["date"])[-1])

    if choice.get() == 1:
        source_button.config(
            command=lambda: browser(url="https://www.google.com/finance/quote/USD-INR"),
        )

    else:
        source_button.config(
            command=lambda: browser(url="https://www.mmtcpamp.com/"),
        )


def reset_ui():
    """
    This reset_ui function is used to reset the user interface
    """

    header_label.config(text="Welcome to Predictor")

    rb1.config(state="normal")
    rb2.config(state="normal")

    choice.set(value=0)

    exit_button.config(state="normal")

    fig.suptitle("Graph Area")
    fig.supxlabel(t="X-Axis")
    fig.supylabel(t="Y-Axis")

    graph.cla()
    graph.grid(visible=True)
    canvas.draw()

    minimum_value_label.config(text="0.00")
    average_value_label.config(text="0.00")
    maximum_value_label.config(text="0.00")
    delta_value_label.config(text="0.00")
    tomorrow_label.config(text="0.00")
    next_week_label.config(text="0.00")
    next_month_label.config(text="0.00")
    next_year_label.config(text="0.00")
    coefficient_label.config(text="0.00")
    intercept_label.config(text="0.00")
    status_label.config(text="N/A")
    last_update_label.config(text="N/A")

    source_button.config(text="Source", state="disabled")

    footer_label.config(
        text="Created by FOSS KINGDOM, Made with Love in Incredible India."
    )

    app.update()


def usd_to_inr():
    """
    This usd_to_inr function is used to predict the USD to INR value
    """

    choice.set(value=1)

    update(
        url="https://raw.githubusercontent.com/JahidFariz/ML-Training-Data/main/USD2INR.csv"
    )


def e_gold_24k():
    """
    This e_gold_24 function is used to predict the 24K e-Gold Price
    """

    choice.set(value=2)

    update(
        url="https://raw.githubusercontent.com/JahidFariz/ML-Training-Data/main/e-Gold.csv"
    )


def update(url) -> None:
    """
    This update function is used to update the graph and data when the radio button is clicked.
    """

    loading_ui()

    try:
        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}Reading database, Please wait..."
        )
        with urlopen(url, timeout=10) as response:
            data: read_csv = read_csv(filepath_or_buffer=response, encoding="utf-8")
            response.close()

    except URLError as url_error:
        reset_ui()
        clrscr()

        print(F_BLUE + "=" * 80)
        figlet_banner(font=selected_figlet_font)
        print(F_BLUE + "=" * 80)
        print(f"{S_BRIGHT}Failed to read database...")
        print(f"{S_BRIGHT}Error Code: urllib.error.URLError")
        print(
            f"[{F_RED}{S_BRIGHT}ERROR{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}{url_error}"
        )
        print(F_BLUE + "=" * 80)

        app.withdraw()
        showerror(title="Predictor", message=str(url_error))
        app.deiconify()

        return None

    prediction_lst: list = []
    x_axis = data[["sl.no"]]
    y_axis = data["price"]

    predict_values(data, x_axis, y_axis, prediction_lst)
    draw_graph(x_axis, y_axis, prediction_lst)
    display_data(data, prediction_lst)

    # Update User Interface

    header_label.config(text="Welcome to Predictor")

    rb1.config(state="normal")
    rb2.config(state="normal")

    exit_button.config(state="normal")

    source_button.config(text="Source", state="normal")

    progress_bar.config(value=0)
    percentage_label.config(text="0.00%")

    footer_label.config(
        text="Created by FOSS KINGDOM, Made with Love in Incredible India."
    )

    app.update()

    return None


try:
    print("[INFO]\tImporting libraries, Please wait...")
    from datetime import datetime
    from os import system as terminal
    from os.path import isdir, join
    from pathlib import Path
    from platform import system as environment
    from random import choice
    from shutil import rmtree
    from sys import exit as terminate
    from tkinter import (
        Button,
        Frame,
        IntVar,
        Label,
        LabelFrame,
        Menu,
        PhotoImage,
        Radiobutton,
        TclError,
        Tk,
    )
    from tkinter.messagebox import askyesno, showerror
    from tkinter.ttk import Notebook, Progressbar
    from urllib.error import URLError
    from urllib.request import urlopen
    from webbrowser import open as browser

    today: datetime = datetime.today()
    base_path: Path = Path(__file__).parent
    uname: str = environment()
    __version__: str = "v.20230313"

    print(f"[INFO]\t[{datetime.now()}]\tImporting third-party modules, Please wait...")
    from colorama import init
    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg,
        NavigationToolbar2Tk,
    )
    from matplotlib.figure import Figure
    from pandas import read_csv
    from pyfiglet import FigletFont, figlet_format
    from sklearn.linear_model import LinearRegression
    from tqdm import tqdm

    selected_figlet_font: str = choice(FigletFont.getFonts())

    print(f"[INFO]\t[{datetime.now()}]\tImporting constants module, Please wait...")
    from constants import F_BLUE, F_GREEN, F_RED, S_BRIGHT, S_RESET_ALL

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Initializing colorama, Please wait...{S_RESET_ALL}"
    )
    init(autoreset=True)

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Initializing linear regression model, Please wait..."
    )
    model: LinearRegression = LinearRegression()

    theme_color = {"light": "lightsteelblue2"}

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Loading GUI Application, Please wait..."
    )

    print(F_BLUE + "=" * 80)
    figlet_banner(font=selected_figlet_font)
    print(F_BLUE + "=" * 80)

    app: Tk = Tk()
    app.title(string=f"Predictor {__version__}")
    app.resizable(width=False, height=False)

    logo_file: str = join(base_path, "./predictive-chart.png")
    logo: PhotoImage = PhotoImage(file=logo_file)

    app.iconphoto(True, logo)

    app.bind(sequence="Q", func=lambda event: exit_app())
    app.bind(sequence="q", func=lambda event: exit_app())
    app.bind(sequence="<Escape>", func=lambda event: exit_app())

    menu_bar: Menu = Menu(master=app)

    app.config(bg=theme_color["light"], menu=menu_bar)

    # File Menu
    file_menu: Menu = Menu(master=menu_bar, tearoff=False)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", accelerator="(Ctrl+O)")
    predict_menu: Menu = Menu(master=file_menu, tearoff=False)
    file_menu.add_cascade(label="Predict", menu=predict_menu)
    predict_menu.add_command(label="USD to INR", command=usd_to_inr)
    predict_menu.add_command(label="24K e-Gold", command=e_gold_24k)
    predict_menu.add_separator()
    predict_menu.add_command(label="Custom")
    goto_menu: Menu = Menu(master=file_menu, tearoff=False)
    file_menu.add_cascade(label="Goto", menu=goto_menu)
    goto_menu.add_command(label="Graph", command=lambda: tab_view.select(tab_id=0))
    goto_menu.add_command(label="Data", command=lambda: tab_view.select(tab_id=1))
    file_menu.add_separator()
    file_menu.add_command(label="Exit", accelerator="(Ctrl+Q)", command=exit_app)

    # Links Menu
    links_menu: Menu = Menu(master=menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Links", menu=links_menu)
    links_menu.add_command(label="License")
    links_menu.add_command(label="Video")
    links_menu.add_command(label="Source Code")
    links_menu.add_command(label="Issues")
    links_menu.add_command(label="Translation")
    links_menu.add_command(label="Changelog")
    links_menu.add_command(label="Website")
    links_menu.add_command(label="E-Mail Author")

    # Help Menu
    help_menu: Menu = Menu(master=menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(
        label="About",
        accelerator="(\u2139\ufe0f)",
        command=lambda: browser(url="https://github.com/JahidFariz/Predictor#readme"),
    )
    help_menu.add_command(
        label="Make a donation",
        accelerator="($)",
        command=lambda: browser(url="https://paypal.me/jahidfariz"),
    )

    header_label: Label = Label(
        master=app, text="Welcome to Predictor", bg="#000", fg="#FFF"
    )
    header_label.pack(side="top", fill="x")

    if today.month == 1:
        if today.day == 1:
            special_day_banner(msg="Today is New Year's Day")

        if today.day == 26:
            special_day_banner(msg="Today is India Republic Day")

    if today.month == 2:
        if today.day == 4:
            special_day_banner(msg="Today is Sri Lanka Independence Day")

        if today.day == 6:
            special_day_banner(msg="Today is Waitangi Day")

        if today.day == 14:
            special_day_banner(msg="Today is Valentine's Day")

        if today.day == 15:
            special_day_banner(msg="Today is Serbia National Day")

        if today.day == 16:
            special_day_banner(msg="Today is Lithuania Independence Day")

        if today.day == 24:
            special_day_banner(msg="Today is Estonia Independence Day")

        if today.day == 25:
            special_day_banner(msg="Today is Kuwait National Day")

        if today.day == 27:
            special_day_banner(msg="Today is Dominican Republic Independence Day")

    if today.month == 3:
        if today.day == 1:
            special_day_banner(msg="Today is St. David's Day")

        if today.day == 3:
            special_day_banner(msg="Today is Bulgaria Liberation Day")

        if today.day == 6:
            special_day_banner(msg="Today is Ghana Independence Day")

        if today.day == 8:
            special_day_banner(msg="Today is International Women's Day")

        if today.day == 15:
            special_day_banner(msg="Today is Hungary National Day")

        if today.day == 20:
            special_day_banner(msg="Today is Tunisia National Day")

        if today.day == 25:
            special_day_banner(msg="Today is Greece National Day")

        if today.day == 26:
            special_day_banner(msg="Today is Bangladesh Independence Day")

    if today.month == 4:
        if today.day == 4:
            special_day_banner(msg="Today is Senegal Independence Day")

        if today.day == 22:
            special_day_banner(msg="Today is Earth Day")

        if today.day == 23:
            day_list: list = [
                "Today is National Sovereignty and Children's Day",
                "Today is St. George's Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if today.day == 27:
            day_list: list = [
                "Today is King's Day",
                "Today is South Africa Freedom Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

    if today.day == 5:
        if today.day == 5:
            special_day_banner(msg="Today is Israel Independence Day")

        if today.day == 17:
            special_day_banner(msg="Today is Norway Constitution Day")

        if today.day == 25:
            special_day_banner(msg="Today is Jordan Independence Day")

        if today.day == 26:
            special_day_banner(msg="Today is Georgia Independence Day")

    if today.month == 6:
        if today.day == 2:
            special_day_banner(msg="Today is Italy Republic Day")

        if today.day == 5:
            special_day_banner(msg="Today is Denmark Constitution Day")

        if today.day == 6:
            special_day_banner(msg="Today is Sweden National Day")

        if today.day == 10:
            special_day_banner(msg="Today is Portugal National Day")

        if today.day == 12:
            special_day_banner(msg="Today is Philippines Independence Day")

        if today.day == 17:
            special_day_banner(msg="Today is Iceland National Day")

        if today.day == 25:
            special_day_banner(msg="Today is Slovenia National Day")

        if today.day == 27:
            special_day_banner(msg="Today is Djibouti Independence Day")

    if today.month == 7:
        if today.day == 1:
            special_day_banner(msg="Today is Canada Day")

        if today.day == 4:
            special_day_banner(msg="Today is Fourth of July")

        if today.day == 5:
            day_list: list = [
                "Today is Algeria Independence Day",
                "Today is Venezuela Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if today.day == 9:
            special_day_banner(msg="Today is Argentina Independence Day")

        if today.day == 14:
            special_day_banner(msg="Today is Bastille Day")

        if today.day == 20:
            special_day_banner(msg="Today is Colombia Independence Day")

        if today.day == 21:
            special_day_banner(msg="Today is Belgium National Day")

        if today.day == 28:
            special_day_banner(msg="Today is Peru Independence Day")

    if today.month == 8:
        if today.day == 1:
            special_day_banner(msg="Today is Switzerland National Day")

        if today.day == 6:
            day_list: list = [
                "Today is Bolivia Independence Day",
                "Today is Jamaica Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if today.day == 9:
            special_day_banner(msg="Today is Singapore National Day")

        if today.day == 10:
            special_day_banner(msg="Today is Ecuador Independence Day")

        if today.day == 11:
            special_day_banner(msg="Today is Mountain Day")

        if today.day == 14:
            special_day_banner(msg="Today is Pakistan Independence Day")

        if today.day == 15:
            day_list: list = [
                "Today is National Liberation Day of Korea",
                "Today is India Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if today.day == 17:
            special_day_banner(msg="Today is Indonesia Independence Day")

        if today.day == 24:
            special_day_banner(msg="Today is Ukraine Independence Day")

        if today.day == 25:
            special_day_banner(msg="Today is Uruguay Independence Day")

        if today.day == 27:
            special_day_banner(msg="Today is Republic of Moldova Independence Day")

        if today.day == 31:
            day_list: list = [
                "Today is Hari Merdeka",
                "Today is Trinidad & Tobago Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

    if today.month == 9:
        if today.day == 1:
            special_day_banner(msg="Today is Uzbekistan Independence Day")

        if today.day == 2:
            special_day_banner(msg="Today is Vietnam National Day")

        if today.day == 7:
            special_day_banner(msg="Today is Brazil Independence Day")

        if today.day == 15:
            day_list: list = [
                "Today is Costa Rica Independence Day",
                "Today is El Salvador Independence Day",
                "Today is Guatemala Independence Day",
                "Today is Honduras National Day",
                "Today is Nicaragua Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if today.day == 16:
            special_day_banner(msg="Today is Mexico Independence Day")

        if today.day == 19:
            special_day_banner(msg="Today is Respect for the Aged Day")

        if today.day == 21:
            special_day_banner(msg="Today is Armenia Independence Day")

        if today.day == 23:
            special_day_banner(msg="Today is Saudi Arabia National Day")

    if today.month == 10:
        if today.day == 1:
            special_day_banner(msg="Today is Nigeria Independence Day")

        if today.day == 3:
            special_day_banner(msg="Today is German Unity Day")

        if today.day == 9:
            day_list: list = ["Today is Hangul Day", "Today is Uganda Independence Day"]
            special_day_banner(msg=choice(seq=day_list))

        if today.day == 18:
            special_day_banner(msg="Today is Azerbaijan Independence Day")

        if today.day == 26:
            special_day_banner(msg="Today is Austria National Day")

        if today.day == 29:
            special_day_banner(msg="Today is Turkey National Day")

    if today.month == 11:
        if today.day == 3:
            special_day_banner(msg="Today is Panama Independence Day")

        if today.day == 9:
            special_day_banner(msg="Today is Cambodia Independence Day")

        if today.day == 11:
            day_list: list = ["Today is Poland National Day", "Today is Veterans Day"]
            special_day_banner(msg=choice(seq=day_list))

        if today.day == 17:
            day_list: list = [
                "Today is Czech Republic Freedom and Democracy Day",
                "Today is Slovakia Freedom and Democracy Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if today.day == 18:
            day_list: list = [
                "Today is Oman National Day",
                "Today is Latvia Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if today.day == 22:
            special_day_banner(msg="Today is Lebanon Independence Day")

        if today.day == 25:
            special_day_banner(msg="Today is Bosnia & Herzegovina Statehood Day")

        if today.day == 28:
            special_day_banner(msg="Today is Albania Independence Day")

        if today.day == 30:
            special_day_banner(msg="Today is St. Andrew's Day")

    if today.month == 12:
        if today.day == 1:
            special_day_banner(msg="Today is Great Union Day")

        if today.day == 2:
            special_day_banner(msg="Today is UAE National Day")

        if today.day == 6:
            special_day_banner(msg="Today is Finland Independence Day")

        if today.day == 9:
            special_day_banner(msg="Today is Tanzania Independence Day")

        if today.day == 12:
            special_day_banner(msg="Today is Kenya Independence Day")

        if today.day == 16:
            day_list: list = [
                "Today is Kazakhstan Independence Day",
                "Today is Bahrain National Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if today.day == 18:
            special_day_banner(msg="Today is Qatar National Day")

        if today.day == 31:
            special_day_banner(msg="Today is New Year's Eve")

    label_frame_1: LabelFrame = LabelFrame(
        master=app,
        text="What would you like to predict?",
        bg=theme_color["light"],
        fg="red",
    )
    label_frame_1.pack(fill="x", padx=10, pady=5)

    choice: IntVar = IntVar()

    rb1: Radiobutton = Radiobutton(
        master=label_frame_1,
        bg=theme_color["light"],
        activebackground=theme_color["light"],
        text="United State Dollar to India Rupees Value",
        variable=choice,
        value=1,
        command=usd_to_inr,
    )
    rb1.grid(row=0, column=0, sticky="w")

    rb2: Radiobutton = Radiobutton(
        master=label_frame_1,
        bg=theme_color["light"],
        activebackground=theme_color["light"],
        text="24K e-Gold Price by MMTC-PAMP",
        variable=choice,
        value=2,
        command=e_gold_24k,
    )
    rb2.grid(row=1, column=0, sticky="w")

    tab_view: Notebook = Notebook(master=app)
    tab_view.pack(fill="both", expand=True)

    graph_frame: Frame = Frame(master=tab_view, bg=theme_color["light"])
    graph_frame.pack()

    data_frame: Frame = Frame(master=tab_view, bg=theme_color["light"])
    data_frame.pack()

    tab_view.add(child=graph_frame, text="Graph")
    tab_view.add(child=data_frame, text="Data")

    fig: Figure = Figure()
    fig.suptitle("Graph Area")
    fig.supxlabel(t="X-Axis")
    fig.supylabel(t="Y-Axis")

    graph = fig.add_subplot()
    graph.grid(visible=True)

    canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(fig, master=graph_frame)
    toolbar: NavigationToolbar2Tk = NavigationToolbar2Tk(canvas, graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    label_frame_2: LabelFrame = LabelFrame(
        master=data_frame, text="Statistic Data", bg=theme_color["light"], fg="red"
    )
    label_frame_2.pack(padx=10, pady=5, fill="both", expand=True)

    Label(master=label_frame_2, bg=theme_color["light"], text="Minimum:").grid(
        row=0, column=0, padx=10, sticky="w"
    )
    minimum_value_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="0.00"
    )
    minimum_value_label.grid(row=0, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=theme_color["light"], text="Average:").grid(
        row=1, column=0, padx=10, sticky="w"
    )
    average_value_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="0.00"
    )
    average_value_label.grid(row=1, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=theme_color["light"], text="Maximum:").grid(
        row=2, column=0, padx=10, sticky="w"
    )
    maximum_value_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="0.00"
    )
    maximum_value_label.grid(row=2, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=theme_color["light"], text="Delta:").grid(
        row=3, column=0, padx=10, sticky="w"
    )
    delta_value_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="0.00"
    )
    delta_value_label.grid(row=3, column=1, padx=10, sticky="w")

    Label(
        master=label_frame_2, bg=theme_color["light"], text="Tomorrow expected:"
    ).grid(row=4, column=0, padx=10, sticky="w")
    tomorrow_label: Label = Label(
        master=label_frame_2,
        bg=theme_color["light"],
        text="0.00",
    )
    tomorrow_label.grid(row=4, column=1, padx=10, sticky="w")

    Label(
        master=label_frame_2, bg=theme_color["light"], text="Next week expected:"
    ).grid(row=5, column=0, padx=10, sticky="w")
    next_week_label: Label = Label(
        master=label_frame_2,
        bg=theme_color["light"],
        text="0.00",
    )
    next_week_label.grid(row=5, column=1, padx=10, sticky="w")

    Label(
        master=label_frame_2, bg=theme_color["light"], text="Next month expected:"
    ).grid(row=6, column=0, padx=10, sticky="w")
    next_month_label: Label = Label(
        master=label_frame_2,
        bg=theme_color["light"],
        text="0.00",
    )
    next_month_label.grid(row=6, column=1, padx=10, sticky="w")

    Label(
        master=label_frame_2, bg=theme_color["light"], text="Next year expected:"
    ).grid(row=7, column=0, padx=10, sticky="w")
    next_year_label: Label = Label(
        master=label_frame_2,
        bg=theme_color["light"],
        text="0.00",
    )
    next_year_label.grid(row=7, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=theme_color["light"], text="Coefficient:").grid(
        row=8, column=0, padx=10, sticky="w"
    )
    coefficient_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="0.00"
    )
    coefficient_label.grid(row=8, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=theme_color["light"], text="Intercept:").grid(
        row=9, column=0, padx=10, sticky="w"
    )
    intercept_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="0.00"
    )
    intercept_label.grid(row=9, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=theme_color["light"], text="Status:").grid(
        row=10, column=0, padx=10, sticky="w"
    )
    status_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="N/A"
    )
    status_label.grid(row=10, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=theme_color["light"], text="Last Updated:").grid(
        row=11, column=0, padx=10, sticky="w"
    )
    last_update_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="N/A"
    )
    last_update_label.grid(row=11, column=1, padx=10, sticky="w")

    source_button: Button = Button(
        master=label_frame_2,
        text="Source",
        bg="#CE313A",
        fg="white",
        activebackground="red",
        activeforeground="white",
        width=10,
        state="disabled",
    )
    source_button.grid(row=12, column=0, padx=10, pady=5, sticky="w")

    bottom_frame: Frame = Frame(master=app, bg=theme_color["light"])
    bottom_frame.pack(fill="x", pady=5)

    progress_bar: Progressbar = Progressbar(
        master=bottom_frame, orient="horizontal", mode="determinate"
    )
    progress_bar.pack(fill="x", expand=True, padx=10, side="left")

    percentage_label: Label = Label(
        master=bottom_frame, text="0.00%", bg=theme_color["light"]
    )
    percentage_label.pack(side="left")

    exit_button: Button = Button(
        master=bottom_frame,
        text="EXIT",
        bg="#CE313A",
        fg="white",
        width=10,
        activebackground="red",
        activeforeground="white",
        command=exit_app,
    )
    exit_button.bind(sequence="<Return>", func=lambda event: exit_app())
    exit_button.pack(padx=10, side="left")

    footer_label: Label = Label(
        master=app,
        text="Created by FOSS KINGDOM, Made with Love in Incredible India.",
        bg="#000",
        fg="#FFF",
    )
    footer_label.pack(side="bottom", fill="x")

    app.mainloop()

except TclError as tcl_error:
    clrscr()

    print(F_BLUE + "=" * 80)

    figlet_banner(font="standard")

    print(F_BLUE + "=" * 80)

    print(S_BRIGHT + "Error Code: tkinter.TclError")
    print(
        f"[{F_RED}{S_BRIGHT}ERROR{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]"
        f"\t{S_BRIGHT}Sorry, an error occurred! {tcl_error}"
    )

    print(F_BLUE + "=" * 80)

    print(F_GREEN + S_BRIGHT + "Bye!!")

except ModuleNotFoundError as module_not_found_error:
    clrscr()

    print("=" * 80)

    print("Error Code: builtins.ModuleNotFoundError")
    print(
        f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {module_not_found_error}"
    )

    print("=" * 80)

    print("Bye!!")
