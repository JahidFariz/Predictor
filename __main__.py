def exit_app() -> None:
    app.withdraw()

    if askyesno(title="Predictor", message="Are you sure do you really want to quit?"):
        app.quit()
        print(F_GREEN + S_BRIGHT + "Bye!!")
        terminate()

    else:
        app.deiconify()
        return None


def clear_screen() -> None:
    if uname == "Linux":
        terminal(command="clear")
        return None

    elif uname == "Windows":
        terminal(command="cls")
        return None

    else:
        # Working on different operating system.
        return None


def read_database(url: str):
    try:
        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]\t{S_BRIGHT}"
            "Reading database, Please wait..."
        )
        data: read_csv = read_csv(filepath_or_buffer=url)

        return data

    except URLError as url_error:
        header_label.config(text="Welcome to Predictor")

        rb1.config(state=NORMAL)
        rb2.config(state=NORMAL)

        exit_button.config(state=NORMAL)

        minimum_value_label.config(text="0.00")
        average_value_label.config(text="0.00")
        maximum_value_label.config(text="0.00")
        delta_value_label.config(text="0.00")
        status_label.config(text="N/A")
        tomorrow_label.config(text="0.00")
        next_week_label.config(text="0.00")
        next_month_label.config(text="0.00")
        next_year_label.config(text="0.00")
        last_update_label.config(text="N/A")
        footer_label.config(
            text="Created by FOSS KINGDOM, Made with Love in Incredible India."
        )

        app.update()

        clear_screen()

        print(F_BLUE + "=" * 80)
        print(f"{S_BRIGHT}Failed to read database...")
        print(
            f"[{F_RED}{S_BRIGHT}ERROR{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]\t{S_BRIGHT}"
            f"{url_error}"
        )
        print(F_BLUE + "=" * 80)

        app.withdraw()
        showerror(title="Predictor", message=str(url_error))
        app.deiconify()

        return None


def update() -> None:
    header_label.config(text="Loading please wait...")

    rb1.config(state=DISABLED)
    rb2.config(state=DISABLED)

    exit_button.config(state=DISABLED)

    graph.cla()
    graph.grid(visible=True)

    minimum_value_label.config(text="Loading...")
    average_value_label.config(text="Loading...")
    maximum_value_label.config(text="Loading...")
    delta_value_label.config(text="Loading...")
    status_label.config(text="Loading...")
    tomorrow_label.config(text="Loading...")
    next_week_label.config(text="Loading...")
    next_month_label.config(text="Loading...")
    next_year_label.config(text="Loading...")
    last_update_label.config(text="Loading...")

    progress_bar.config(value=0)
    percentage_label.config(text="0.00%")

    footer_label.config(text="Loading please wait...")

    app.update()

    if choice.get() == 1:
        data = read_database(
            url="https://raw.githubusercontent.com/JahidFariz/ML-Training-Data/main/USD2INR.csv"
        )

        if data is None:
            return None

        x_axis = data[["sl.no"]]
        y_axis = data["price"]

        model.fit(X=x_axis.values, y=y_axis)

        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]\t{S_BRIGHT}"
            "Estimating USD Price, Please wait..."
        )
        prediction_list: list = list()
        for iteration in tqdm(range(1, len(data) + 1)):
            prediction_list.append(float(model.predict(X=[[iteration]])))

            percentage: float = round(number=iteration / len(data) * 100, ndigits=2)
            progress_bar.config(value=percentage)
            percentage_label.config(text=f"{percentage}%")
            app.update()

        total_records: int = len(data)
        min_val: float = min(data["price"])
        avg_val: float = sum(data["price"]) / total_records
        max_val: float = max(data["price"])
        delta_change: float = prediction_list[-1] - prediction_list[0]

        minimum_value_label.config(text=f"{min_val} INR")
        average_value_label.config(text=f"{round(number=avg_val, ndigits=4)} INR")
        maximum_value_label.config(text=f"{max_val} INR")
        delta_value_label.config(text=f"{round(number=delta_change, ndigits=4)} INR")

        if prediction_list[0] > prediction_list[-1]:
            status_label.config(text="BEAR")

        elif prediction_list[0] == prediction_list[-1]:
            status_label.config(text="No Change")

        else:
            status_label.config(text="BULL")

        tomorrow_value: float = float(model.predict(X=[[total_records + 1]]))
        next_week_value: float = float(model.predict(X=[[total_records + 7]]))
        next_month_value: float = float(model.predict(X=[[total_records + 30]]))
        next_year_value: float = float(model.predict(X=[[total_records + 365]]))

        fig.suptitle(t="USD to INR Currency Value Predictor")
        fig.supxlabel(t="Total no of Days")
        fig.supylabel(t="1USD to INR (₹)")

        graph.plot(x_axis, y_axis, ".", label="Actual 1USD Price")
        graph.plot(x_axis, prediction_list, "--", label="Estimated 1USD Price")

        tomorrow_label.config(text=f"{round(number=tomorrow_value, ndigits=4)} INR")
        next_week_label.config(text=f"{round(number=next_week_value, ndigits=4)} INR")
        next_month_label.config(text=f"{round(number=next_month_value, ndigits=4)} INR")
        next_year_label.config(text=f"{round(number=next_year_value, ndigits=4)} INR")
        last_update_label.config(text=list(data["date"])[-1])

    if choice.get() == 2:
        data = read_database(
            url="https://raw.githubusercontent.com/JahidFariz/ML-Training-Data/main/e-Gold.csv"
        )

        if data is None:
            return None

        x_axis = data[["sl.no"]]
        y_axis = data["price"]

        model.fit(X=x_axis.values, y=y_axis)

        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]\t{S_BRIGHT}"
            "Estimating e-Gold Price, Please wait..."
        )
        prediction_list: list = list()
        for iteration in tqdm(range(1, len(data) + 1)):
            prediction_list.append(float(model.predict(X=[[iteration]])))

            percentage: float = round(number=iteration / len(data) * 100, ndigits=2)
            progress_bar.config(value=percentage)
            percentage_label.config(text=f"{percentage}%")
            app.update()

        total_records: int = len(data)
        min_val: float = min(data["price"])
        avg_val: float = sum(data["price"]) / total_records
        max_val: float = max(data["price"])
        delta_change: float = prediction_list[-1] - prediction_list[0]

        minimum_value_label.config(text=f"{min_val} INR")
        average_value_label.config(text=f"{round(number=avg_val, ndigits=2)} INR")
        maximum_value_label.config(text=f"{max_val} INR")
        delta_value_label.config(text=f"{round(number=delta_change, ndigits=2)} INR")

        if prediction_list[0] > prediction_list[-1]:
            status_label.config(text="BEAR")

        elif prediction_list[0] == prediction_list[-1]:
            status_label.config(text="No Change")

        else:
            status_label.config(text="BULL")

        tomorrow_value: float = float(model.predict(X=[[total_records + 1]]))
        next_week_value: float = float(model.predict(X=[[total_records + 7]]))
        next_month_value: float = float(model.predict(X=[[total_records + 30]]))
        next_year_value: float = float(model.predict(X=[[total_records + 365]]))

        fig.suptitle(t="e-Gold Price Predictor")
        fig.supxlabel(t="Total no of Days")
        fig.supylabel(t="Price in INR (₹)")

        graph.plot(x_axis, y_axis, ".", label="Actual e-Gold Price")
        graph.plot(x_axis, prediction_list, "--", label="Estimated e-Gold Price")

        tomorrow_label.config(text=f"{round(number=tomorrow_value, ndigits=2)} INR")
        next_week_label.config(text=f"{round(number=next_week_value, ndigits=2)} INR")
        next_month_label.config(text=f"{round(number=next_month_value, ndigits=2)} INR")
        next_year_label.config(text=f"{round(number=next_year_value, ndigits=2)} INR")
        last_update_label.config(text=list(data["date"])[-1])

    graph.legend()
    canvas.draw()

    header_label.config(text="Welcome to Predictor")

    rb1.config(state=NORMAL)
    rb2.config(state=NORMAL)

    exit_button.config(state=NORMAL)

    progress_bar.config(value=0)
    percentage_label.config(text="0.00%")

    footer_label.config(
        text="Created by FOSS KINGDOM, Made with Love in Incredible India."
    )

    app.update()

    return None


try:
    print("[INFO]\tImporting built-in libraries, Please wait...")
    from datetime import datetime
    from os import system as terminal
    from os.path import isfile, join
    from pathlib import Path
    from platform import system as environment
    from sys import exit as terminate
    from tkinter import (
        BOTH,
        BOTTOM,
        DISABLED,
        HORIZONTAL,
        LEFT,
        NORMAL,
        RIGHT,
        TOP,
        TRUE,
        Button,
        Frame,
        IntVar,
        Label,
        LabelFrame,
        PhotoImage,
        Radiobutton,
        Tk,
        W,
        X,
    )
    from tkinter.messagebox import askyesno, showerror
    from tkinter.ttk import Notebook, Progressbar
    from urllib.error import URLError

    print(f"[INFO]\t[{datetime.now()}]\tImporting third-party modules, Please wait...")
    from colorama import Back, Fore, Style, init
    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg,
        NavigationToolbar2Tk,
    )
    from matplotlib.figure import Figure
    from pandas import read_csv
    from sklearn.linear_model import LinearRegression
    from tqdm import tqdm

    base_path: Path = Path(__file__).parent
    uname: str = environment()

    F_GREEN: str = Fore.GREEN
    F_BLUE: str = Fore.BLUE
    F_RED: str = Fore.RED

    S_BRIGHT: str = Style.BRIGHT
    S_RESET_ALL: str = Style.RESET_ALL

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]\t{S_BRIGHT}"
        f"Initializing colorama, Please wait...{S_RESET_ALL}"
    )
    init(autoreset=True)

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]\t{S_BRIGHT}"
        "Initializing linear regression model, Please wait..."
    )
    model: LinearRegression = LinearRegression()

    if not isfile(path=__file__):
        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]\t{S_BRIGHT}"
            "Importing hidden modules, Please wait..."
        )
        from PIL import _tkinter_finder
        from pyfiglet import fonts
        from sklearn.metrics._pairwise_distances_reduction import (
            _datasets_pair,
            _middle_term_computer,
        )

    theme_color = {"light": "lightsteelblue2"}

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]\t{S_BRIGHT}"
        "Loading GUI Application, Please wait..."
    )
    app: Tk = Tk()
    app.title("Predictor")
    app.resizable(width=False, height=False)

    logo_file: str = join(base_path, "./predictive-chart.png")
    logo: PhotoImage = PhotoImage(file=logo_file)

    app.iconphoto(True, logo)

    app.bind(sequence="Q", func=lambda event: exit_app())
    app.bind(sequence="q", func=lambda event: exit_app())
    app.bind(sequence="<Escape>", func=lambda event: exit_app())

    app.config(bg=theme_color["light"])

    header_label: Label = Label(
        master=app, text="Welcome to Predictor", bg="#000", fg="#FFF"
    )
    header_label.pack(side=TOP, fill=X)

    label_frame_1: LabelFrame = LabelFrame(
        master=app,
        text="What would you like to predict?",
        bg=theme_color["light"],
        fg="red",
    )
    label_frame_1.pack(fill=X, padx=10, pady=5)

    choice: IntVar = IntVar()

    rb1: Radiobutton = Radiobutton(
        master=label_frame_1,
        bg=theme_color["light"],
        activebackground=theme_color["light"],
        text="United State Dollar to India Rupees Value",
        variable=choice,
        value=1,
        command=update,
    )
    rb1.grid(row=0, column=0, sticky=W)

    rb2: Radiobutton = Radiobutton(
        master=label_frame_1,
        bg=theme_color["light"],
        activebackground=theme_color["light"],
        text="24K e-Gold Price by MMTC-PAMP",
        variable=choice,
        value=2,
        command=update,
    )
    rb2.grid(row=1, column=0, sticky=W)

    button_frame: Frame = Frame(master=app, bg=theme_color["light"])
    button_frame.pack(fill=BOTH, pady=5)

    exit_button: Button = Button(
        master=button_frame,
        text="EXIT",
        bg="#CE313A",
        fg="white",
        width=10,
        activebackground="red",
        activeforeground="white",
        command=exit_app,
    )
    exit_button.bind(sequence="<Return>", func=lambda event: exit_app())
    exit_button.pack()

    tab_view: Notebook = Notebook(master=app)
    tab_view.pack(fill=BOTH, expand=TRUE)

    graph_frame: Frame = Frame(master=tab_view, bg=theme_color["light"])
    graph_frame.pack()

    data_frame: Frame = Frame(master=tab_view, bg=theme_color["light"])
    data_frame.pack()

    tab_view.add(child=graph_frame, text="Graph")
    tab_view.add(child=data_frame, text="Data")

    fig: Figure = Figure()

    graph = fig.add_subplot()
    graph.grid(visible=TRUE)

    canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(fig, master=graph_frame)
    toolbar: NavigationToolbar2Tk = NavigationToolbar2Tk(canvas, graph_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill=BOTH, expand=TRUE)

    label_frame_2: LabelFrame = LabelFrame(
        master=data_frame, text="Statistic Data", bg=theme_color["light"], fg="red"
    )
    label_frame_2.pack(padx=10, pady=5, fill=BOTH, expand=TRUE)

    Label(master=label_frame_2, bg=theme_color["light"], text="Minimum:").grid(
        row=0, column=0, padx=10, sticky=W
    )
    minimum_value_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="0.00"
    )
    minimum_value_label.grid(row=0, column=1, padx=10, sticky=W)

    Label(master=label_frame_2, bg=theme_color["light"], text="Average:").grid(
        row=1, column=0, padx=10, sticky=W
    )
    average_value_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="0.00"
    )
    average_value_label.grid(row=1, column=1, padx=10, sticky=W)

    Label(master=label_frame_2, bg=theme_color["light"], text="Maximum:").grid(
        row=2, column=0, padx=10, sticky=W
    )
    maximum_value_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="0.00"
    )
    maximum_value_label.grid(row=2, column=1, padx=10, sticky=W)

    Label(master=label_frame_2, bg=theme_color["light"], text="Delta:").grid(
        row=3, column=0, padx=10, sticky=W
    )
    delta_value_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="0.00"
    )
    delta_value_label.grid(row=3, column=1, padx=10, sticky=W)

    Label(master=label_frame_2, bg=theme_color["light"], text="Status:").grid(
        row=4, column=0, padx=10, sticky=W
    )
    status_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="N/A"
    )
    status_label.grid(row=4, column=1, padx=10, sticky=W)

    Label(
        master=label_frame_2, bg=theme_color["light"], text="Tomorrow expected:"
    ).grid(row=5, column=0, padx=10, sticky=W)
    tomorrow_label: Label = Label(
        master=label_frame_2,
        bg=theme_color["light"],
        text="0.00",
    )
    tomorrow_label.grid(row=5, column=1, padx=10, sticky=W)

    Label(
        master=label_frame_2, bg=theme_color["light"], text="Next week expected:"
    ).grid(row=6, column=0, padx=10, sticky=W)
    next_week_label: Label = Label(
        master=label_frame_2,
        bg=theme_color["light"],
        text="0.00",
    )
    next_week_label.grid(row=6, column=1, padx=10, sticky=W)

    Label(
        master=label_frame_2, bg=theme_color["light"], text="Next month expected:"
    ).grid(row=7, column=0, padx=10, sticky=W)
    next_month_label: Label = Label(
        master=label_frame_2,
        bg=theme_color["light"],
        text="0.00",
    )
    next_month_label.grid(row=7, column=1, padx=10, sticky=W)

    Label(
        master=label_frame_2, bg=theme_color["light"], text="Next year expected:"
    ).grid(row=8, column=0, padx=10, sticky=W)
    next_year_label: Label = Label(
        master=label_frame_2,
        bg=theme_color["light"],
        text="0.00",
    )
    next_year_label.grid(row=8, column=1, padx=10, sticky=W)

    Label(master=label_frame_2, bg=theme_color["light"], text="Last Updated on:").grid(
        row=9, column=0, padx=10, sticky=W
    )
    last_update_label: Label = Label(
        master=label_frame_2, bg=theme_color["light"], text="N/A"
    )
    last_update_label.grid(row=9, column=1, padx=10, sticky=W)

    progress_frame: Frame = Frame(master=app, bg=theme_color["light"])
    progress_frame.pack(fill=X)

    progress_bar: Progressbar = Progressbar(
        master=progress_frame, orient=HORIZONTAL, mode="determinate"
    )
    progress_bar.pack(pady=10, fill=X, expand=TRUE, padx=10, side=LEFT)

    percentage_label: Label = Label(
        master=progress_frame, text="0.00%", bg=theme_color["light"]
    )
    percentage_label.pack(pady=10, padx=5, side=RIGHT)

    footer_label: Label = Label(
        master=app,
        text="Created by FOSS KINGDOM, Made with Love in Incredible India.",
        bg="#000",
        fg="#FFF",
    )
    footer_label.pack(side=BOTTOM, fill=X)

    app.mainloop()

except ModuleNotFoundError as module_not_found_error:
    print("=" * 80)
    print("Error Code: builtins.ModuleNotFoundError")
    print(
        f"[ERROR]\t[{datetime.now()}]\tSorry, an error occurred! {module_not_found_error}"
    )
    print("=" * 80)
    print("Bye!!")
