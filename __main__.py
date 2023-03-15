"""
Author: Mohamed Fariz
Version: 20230315
Application Name: Predictor

It is a supervised machine learning algorithm to predict the future data.
"""

# pylint: disable=C0302


def special_day_banner(msg: str):
    """
    This special_day_banner function is used to display about the event of the day
    """

    print(f"{F_YELLOW}{S_BRIGHT}Tody is {msg}")

    special_day_label: Label = Label(master=app, text=f"Today is {msg}", bg="yellow")
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
    print(F_RED + S_BRIGHT + figlet_format(text="Predictor", font=font))
    print(f"{F_BLUE}Figlet Font: {font}")


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

    clear_button.config(state="disabled")
    exit_button.config(state="disabled")

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

    for _ in tqdm(range(1, len(data) + 1)):
        prediction_lst.append(float(model.predict(X=[[_]])))

        percentage: float = round(number=_ / len(data) * 100, ndigits=2)
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

    clear_button.config(state="normal")
    exit_button.config(state="normal")

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

    source_button.config(text="Source", state="normal")

    progress_bar.config(value=0)
    percentage_label.config(text="0.00%")

    clear_button.config(state="normal")
    exit_button.config(state="normal")

    footer_label.config(
        text="Created by FOSS KINGDOM, Made with Love in Incredible India."
    )

    app.update()

    return None


try:
    print("[INFO]\tImporting libraries, Please wait...")
    from datetime import datetime
    from getpass import getuser
    from os import system as terminal
    from os.path import isdir, join
    from pathlib import Path
    from platform import system as environment
    from random import choice
    from shutil import rmtree
    from sys import exit as terminate
    from tkinter import Button, Frame, IntVar, Label, LabelFrame, Menu
    from tkinter import PhotoImage as TkPhotoImage
    from tkinter import Radiobutton, TclError, Tk
    from tkinter.messagebox import askyesno, showerror
    from tkinter.ttk import Notebook, Progressbar
    from urllib.error import URLError
    from urllib.request import urlopen
    from webbrowser import open as browser

    whoami: str = getuser()
    today: datetime = datetime.today()
    base_path: Path = Path(__file__).parent
    uname: str = environment()
    __version__: str = "v.20230315"

    print(f"[INFO]\t[{datetime.now()}]\tImporting third-party modules, Please wait...")
    from colorama import init
    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg,
        NavigationToolbar2Tk,
    )
    from matplotlib.figure import Figure
    from pandas import read_csv
    from PIL.Image import open as img_open
    from PIL.ImageTk import PhotoImage as PILPhotoImage
    from pyfiglet import FigletFont, figlet_format
    from sklearn.linear_model import LinearRegression
    from tqdm import tqdm

    selected_figlet_font: str = choice(FigletFont.getFonts())

    print(f"[INFO]\t[{datetime.now()}]\tImporting constants module, Please wait...")
    from constants import F_BLUE, F_GREEN, F_RED, F_YELLOW, S_BRIGHT, S_RESET_ALL

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
    x_axis_resolution: int = app.winfo_screenwidth()
    y_axis_resolution: int = app.winfo_screenheight()
    app.maxsize(width=x_axis_resolution, height=y_axis_resolution)
    app.resizable(width=False, height=False)

    logo_file: str = join(base_path, "./assets/predictive-chart.png")
    logo_image: TkPhotoImage = TkPhotoImage(file=logo_file)

    app.iconphoto(True, logo_image)

    for _ in ["Q", "q", "<Escape>"]:
        app.bind(sequence=_, func=lambda event: exit_app())

    menu_bar: Menu = Menu(master=app)

    app.config(bg=theme_color["light"], menu=menu_bar)

    # <a href="https://www.flaticon.com/free-icons/money" title="money icons">
    # Money icons created by vectorsmarket15 - Flaticon
    # </a>
    # https://www.flaticon.com/free-icon/money_2704332?term=dollar&page=1&position=8&origin=search&related_id=2704332
    money_ico: PILPhotoImage = PILPhotoImage(
        img_open(join(base_path, "./assets/money.png")).resize(size=(20, 20))
    )

    # <a href="https://www.flaticon.com/free-icons/gold" title="gold icons">
    # Gold icons created by photo3idea_studio - Flaticon
    # </a>
    # https://www.flaticon.com/free-icon/ingots_1473504?term=gold&page=1&position=1&origin=search&related_id=1473504
    gold_ico: PILPhotoImage = PILPhotoImage(
        img_open(join(base_path, "./assets/ingots.png")).resize(size=(20, 20))
    )

    # <a href="https://www.flaticon.com/free-icons/profit" title="profit icons">
    # Profit icons created by Pixel perfect - Flaticon
    # </a>
    # https://www.flaticon.com/free-icon/bar-chart_893214?term=graph&page=1&position=48&origin=search&related_id=893214
    graph_ico: PILPhotoImage = PILPhotoImage(
        img_open(join(base_path, "./assets/bar-chart.png")).resize(size=(20, 20))
    )

    # <a href="https://www.flaticon.com/free-icons/statistics" title="statistics icons">
    # Statistics icons created by Freepik - Flaticon
    # </a>
    # https://www.flaticon.com/free-icon/statistics_2920349?term=data&page=1&position=6&origin=search&related_id=2920349
    statistic_ico: PILPhotoImage = PILPhotoImage(
        img_open(join(base_path, "./assets/statistics.png")).resize(size=(20, 20))
    )

    # File Menu
    file_menu: Menu = Menu(master=menu_bar, tearoff=False)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", accelerator="(Ctrl+O)")
    predict_menu: Menu = Menu(master=file_menu, tearoff=False)
    file_menu.add_cascade(label="Predict", menu=predict_menu)
    predict_menu.add_command(
        label="USD to INR", image=money_ico, compound="left", command=usd_to_inr
    )
    predict_menu.add_command(
        label="24K e-Gold", image=gold_ico, compound="left", command=e_gold_24k
    )
    predict_menu.add_separator()
    predict_menu.add_command(label="Custom")
    goto_menu: Menu = Menu(master=file_menu, tearoff=False)
    file_menu.add_cascade(label="Goto", menu=goto_menu)
    goto_menu.add_command(
        label="Graph",
        image=graph_ico,
        compound="left",
        command=lambda: tab_view.select(tab_id=0),
    )
    goto_menu.add_command(
        label="Data",
        image=statistic_ico,
        compound="left",
        command=lambda: tab_view.select(tab_id=1),
    )
    file_menu.add_separator()
    file_menu.add_command(label="Exit", accelerator="(Ctrl+Q)", command=exit_app)

    license_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/license.png")).resize(size=(20, 20))
    )

    # <a href="https://www.flaticon.com/free-icons/play-button" title="play button icons">
    # Play button icons created by Freepik - Flaticon
    # </a>
    # https://www.flaticon.com/free-icon/play_2377793?term=video&page=1&position=46&origin=search&related_id=2377793
    video_ico: PILPhotoImage = PILPhotoImage(
        img_open(join(base_path, "./assets/play.png")).resize(size=(20, 20))
    )

    source_code_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/programming.png")).resize(
            size=(20, 20)
        )
    )
    issues_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/bug-report.png")).resize(size=(20, 20))
    )

    # <a href="https://www.flaticon.com/free-icons/translate" title="translate icons">
    # Translate icons created by icon wind - Flaticon
    # </a>
    # https://www.flaticon.com/free-icon/translate_9628122?term=translation&page=1&position=22&origin=search&related_id=9628122
    translation_ico: PILPhotoImage = PILPhotoImage(
        img_open(join(base_path, "./assets/translate.png")).resize(size=(20, 20))
    )

    # <a href="https://www.flaticon.com/free-icons/notepad" title="notepad icons">
    # Notepad icons created by Freepik - Flaticon
    # </a>
    # https://www.flaticon.com/free-icon/notepad_686234?term=notepad&page=1&position=1&origin=search&related_id=686234
    changelog_ico: PILPhotoImage = PILPhotoImage(
        img_open(join(base_path, "./assets/notepad.png")).resize(size=(20, 20))
    )

    website_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/web-link.png")).resize(size=(20, 20))
    )

    # <a href="https://www.flaticon.com/free-icons/email" title="email icons">
    # Email icons created by Fathema Khanom - Flaticon
    # </a>
    # https://www.flaticon.com/free-icon/mail_9068642?term=email&page=1&position=25&origin=search&related_id=9068642
    email_ico: PILPhotoImage = PILPhotoImage(
        img_open(join(base_path, "./assets/mail.png")).resize(size=(20, 20))
    )

    # Links Menu
    links_menu: Menu = Menu(master=menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Links", menu=links_menu)
    links_menu.add_command(
        label="License (GPL-v3.0)", image=license_ico, compound="left"
    )
    links_menu.add_command(label="Video (YouTube)", image=video_ico, compound="left")
    links_menu.add_command(
        label="Source Code (GitHub)", image=source_code_ico, compound="left"
    )
    links_menu.add_command(label="Issues", image=issues_ico, compound="left")
    links_menu.add_command(label="Translation", image=translation_ico, compound="left")
    links_menu.add_command(label="Changelog", image=changelog_ico, compound="left")
    links_menu.add_command(label="Website", image=website_ico, compound="left")
    links_menu.add_command(label="E-Mail Author", image=email_ico, compound="left")

    donation_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/donation.png")).resize(size=(20, 20))
    )

    # Help Menu
    help_menu: Menu = Menu(master=menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(
        label="About Predictor",
        accelerator="(\u2139\ufe0f)",
        command=lambda: browser(url="https://github.com/JahidFariz/Predictor#readme"),
    )
    help_menu.add_separator()
    help_menu.add_command(
        label="Make a donation",
        accelerator="($)",
        command=lambda: browser(url="https://paypal.me/jahidfariz"),
        image=donation_ico,
        compound="left",
    )

    header_label: Label = Label(
        master=app,
        text=f"Hello {whoami.title()}, Welcome to Predictor",
        bg="#000",
        fg="#FFF",
    )
    header_label.pack(side="top", fill="x")

    print(f"{F_GREEN}{S_BRIGHT}Hello {whoami.title()}, Welcome to Predictor")

    month: int = today.month
    day: int = today.day

    if month == 1:
        if day == 1:
            special_day_banner(msg="New Year's Day")

        if day == 26:
            special_day_banner(msg="India Republic Day")

    if month == 2:
        if day == 4:
            special_day_banner(msg="Sri Lanka Independence Day")

        if day == 6:
            special_day_banner(msg="Waitangi Day")

        if day == 14:
            special_day_banner(msg="Valentine's Day")

        if day == 15:
            special_day_banner(msg="Serbia National Day")

        if day == 16:
            special_day_banner(msg="Lithuania Independence Day")

        if day == 24:
            special_day_banner(msg="Estonia Independence Day")

        if day == 25:
            special_day_banner(msg="Kuwait National Day")

        if day == 27:
            special_day_banner(msg="Dominican Republic Independence Day")

    if month == 3:
        if day == 1:
            special_day_banner(msg="St. David's Day")

        if day == 3:
            special_day_banner(msg="Bulgaria Liberation Day")

        if day == 6:
            special_day_banner(msg="Ghana Independence Day")

        if day == 8:
            special_day_banner(msg="International Women's Day")

        if day == 15:
            special_day_banner(msg="Hungary National Day")

        if day == 20:
            special_day_banner(msg="Tunisia National Day")

        if day == 25:
            special_day_banner(msg="Greece National Day")

        if day == 26:
            special_day_banner(msg="Bangladesh Independence Day")

    if month == 4:
        if day == 4:
            special_day_banner(msg="Senegal Independence Day")

        if day == 22:
            special_day_banner(msg="Earth Day")

        if day == 23:
            day_list: list = [
                "National Sovereignty and Children's Day",
                "St. George's Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 27:
            day_list: list = [
                "King's Day",
                "South Africa Freedom Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

    if day == 5:
        if day == 5:
            special_day_banner(msg="Israel Independence Day")

        if day == 17:
            special_day_banner(msg="Norway Constitution Day")

        if day == 25:
            special_day_banner(msg="Jordan Independence Day")

        if day == 26:
            special_day_banner(msg="Georgia Independence Day")

    if month == 6:
        if day == 2:
            special_day_banner(msg="Italy Republic Day")

        if day == 5:
            special_day_banner(msg="Denmark Constitution Day")

        if day == 6:
            special_day_banner(msg="Sweden National Day")

        if day == 10:
            special_day_banner(msg="Portugal National Day")

        if day == 12:
            special_day_banner(msg="Philippines Independence Day")

        if day == 17:
            special_day_banner(msg="Iceland National Day")

        if day == 25:
            special_day_banner(msg="Slovenia National Day")

        if day == 27:
            special_day_banner(msg="Djibouti Independence Day")

    if month == 7:
        if day == 1:
            special_day_banner(msg="Canada Day")

        if day == 4:
            special_day_banner(msg="Fourth of July")

        if day == 5:
            day_list: list = [
                "Algeria Independence Day",
                "Venezuela Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 9:
            special_day_banner(msg="Argentina Independence Day")

        if day == 14:
            special_day_banner(msg="Bastille Day")

        if day == 20:
            special_day_banner(msg="Colombia Independence Day")

        if day == 21:
            special_day_banner(msg="Belgium National Day")

        if day == 28:
            special_day_banner(msg="Peru Independence Day")

    if month == 8:
        if day == 1:
            special_day_banner(msg="Switzerland National Day")

        if day == 6:
            day_list: list = [
                "Bolivia Independence Day",
                "Jamaica Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 9:
            special_day_banner(msg="Singapore National Day")

        if day == 10:
            special_day_banner(msg="Ecuador Independence Day")

        if day == 11:
            special_day_banner(msg="Mountain Day")

        if day == 14:
            special_day_banner(msg="Pakistan Independence Day")

        if day == 15:
            day_list: list = [
                "National Liberation Day of Korea",
                "India Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 17:
            special_day_banner(msg="Indonesia Independence Day")

        if day == 24:
            special_day_banner(msg="Ukraine Independence Day")

        if day == 25:
            special_day_banner(msg="Uruguay Independence Day")

        if day == 27:
            special_day_banner(msg="Republic of Moldova Independence Day")

        if day == 31:
            day_list: list = [
                "Hari Merdeka",
                "Trinidad & Tobago Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

    if month == 9:
        if day == 1:
            special_day_banner(msg="Uzbekistan Independence Day")

        if day == 2:
            special_day_banner(msg="Vietnam National Day")

        if day == 7:
            special_day_banner(msg="Brazil Independence Day")

        if day == 15:
            day_list: list = [
                "Costa Rica Independence Day",
                "El Salvador Independence Day",
                "Guatemala Independence Day",
                "Honduras National Day",
                "Nicaragua Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 16:
            special_day_banner(msg="Mexico Independence Day")

        if day == 19:
            special_day_banner(msg="Respect for the Aged Day")

        if day == 21:
            special_day_banner(msg="Armenia Independence Day")

        if day == 23:
            special_day_banner(msg="Saudi Arabia National Day")

    if month == 10:
        if day == 1:
            special_day_banner(msg="Nigeria Independence Day")

        if day == 3:
            special_day_banner(msg="German Unity Day")

        if day == 9:
            day_list: list = ["Hangul Day", "Uganda Independence Day"]
            special_day_banner(msg=choice(seq=day_list))

        if day == 18:
            special_day_banner(msg="Azerbaijan Independence Day")

        if day == 26:
            special_day_banner(msg="Austria National Day")

        if day == 29:
            special_day_banner(msg="Turkey National Day")

    if month == 11:
        if day == 3:
            special_day_banner(msg="Panama Independence Day")

        if day == 9:
            special_day_banner(msg="Cambodia Independence Day")

        if day == 11:
            day_list: list = ["Poland National Day", "Veterans Day"]
            special_day_banner(msg=choice(seq=day_list))

        if day == 17:
            day_list: list = [
                "Czech Republic Freedom and Democracy Day",
                "Slovakia Freedom and Democracy Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 18:
            day_list: list = [
                "Oman National Day",
                "Latvia Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 22:
            special_day_banner(msg="Lebanon Independence Day")

        if day == 25:
            special_day_banner(msg="Bosnia & Herzegovina Statehood Day")

        if day == 28:
            special_day_banner(msg="Albania Independence Day")

        if day == 30:
            special_day_banner(msg="St. Andrew's Day")

    if month == 12:
        if day == 1:
            special_day_banner(msg="Great Union Day")

        if day == 2:
            special_day_banner(msg="UAE National Day")

        if day == 6:
            special_day_banner(msg="Finland Independence Day")

        if day == 9:
            special_day_banner(msg="Tanzania Independence Day")

        if day == 12:
            special_day_banner(msg="Kenya Independence Day")

        if day == 16:
            day_list: list = [
                "Kazakhstan Independence Day",
                "Bahrain National Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 18:
            special_day_banner(msg="Qatar National Day")

        if day == 31:
            special_day_banner(msg="New Year's Eve")

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

    tab_view.add(child=graph_frame, text="Graph", image=graph_ico, compound="left")
    tab_view.add(child=data_frame, text="Data", image=statistic_ico, compound="left")

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

    redirect_icon: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=join(base_path, "./assets/share.png")).resize(size=(15, 15))
    )

    source_button: Button = Button(
        master=label_frame_2,
        text="Source",
        bg="#CE313A",
        fg="#FFF",
        activebackground="red",
        activeforeground="#FFF",
        state="disabled",
        compound="right",
        image=redirect_icon,
        width=80,
    )
    source_button.grid(row=12, column=0, padx=10, pady=5, sticky="w")

    bottom_frame: Frame = Frame(master=app, bg=theme_color["light"])
    bottom_frame.pack(fill="x", pady=5)

    progress_bar: Progressbar = Progressbar(
        master=bottom_frame, orient="horizontal", mode="determinate"
    )
    progress_bar.pack(fill="x", expand=True, padx=(10, 5), side="left")

    percentage_label: Label = Label(
        master=bottom_frame, text="0.00%", bg=theme_color["light"]
    )
    percentage_label.pack(padx=(5, 5), side="left")

    clear_icon: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/clear.png")).resize(size=(16, 16))
    )

    clear_button: Button = Button(
        master=bottom_frame,
        text="CLEAR",
        bg="orange",
        fg="#FFF",
        activeforeground="#FFF",
        compound="left",
        image=clear_icon,
        width=60,
        command=reset_ui,
    )
    clear_button.bind(sequence="<Return>", func=lambda event: reset_ui())
    clear_button.pack(padx=(5, 5), side="left")

    refresh_button: Button = Button(
        master=bottom_frame,
        text="REFRESH",
        bg="orange",
        fg="#FFF",
        activeforeground="#FFF",
    )
    refresh_button.pack(padx=(5, 5), side="left")

    exit_icon: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=join(base_path, "./assets/logout.png")).resize(size=(16, 16))
    )

    exit_button: Button = Button(
        master=bottom_frame,
        text="EXIT",
        bg="#CE313A",
        fg="#FFF",
        width=60,
        activebackground="red",
        activeforeground="#FFF",
        image=exit_icon,
        compound="left",
        command=exit_app,
    )
    exit_button.bind(sequence="<Return>", func=lambda event: exit_app())
    exit_button.pack(padx=(5, 10), side="left")

    footer_label: Label = Label(
        master=app,
        text="Created by FOSS Kingdom / Made with Love in Incredible India.",
        bg="#000",
        fg="#FFF",
    )
    footer_label.pack(side="bottom", fill="x")

    print(
        f"{F_GREEN}{S_BRIGHT}Created by FOSS Kingdom / Made with Love in Incredible India."
    )

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
