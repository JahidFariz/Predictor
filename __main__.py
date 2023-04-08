"""

Author: Mohamed Fariz
Version: 20230408
Application Name: Predictor

It is a supervised machine learning algorithm to predict the future data.


Sound Effect by
<a href="https://pixabay.com/users/universfield-28281460/?utm_source=link-attribution&amp; \
    utm_medium=referral&amp; \
    utm_campaign=music&amp; \
    utm_content=129258">
UNIVERSFIELD
</a>
from
<a href="https://pixabay.com//?utm_source=link-attribution&amp; \
    utm_medium=referral&amp; \
    utm_campaign=music&amp; \
    utm_content=129258">
Pixabay
</a>


a href="https://www.flaticon.com/free-icons/money" title="money icons">
Money icons created by vectorsmarket15 - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/gold" title="gold icons">
Gold icons created by photo3idea_studio - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/profit" title="profit icons">
Profit icons created by Pixel perfect - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/statistics" title="statistics icons">
Statistics icons created by Freepik - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/information" title="information icons">
Information icons created by Freepik - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/play-button" title="play button icons">
Play button icons created by Freepik - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/translate" title="translate icons">
Translate icons created by icon wind - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/notepad" title="notepad icons">
Notepad icons created by Freepik - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/email" title="email icons">
Email icons created by Fathema Khanom - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/direct-download" title="direct download icons">
Direct download icons created by Pixel perfect - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/google-play" title="google play icons">
Google play icons created by Pixel perfect - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/google" title="google icons">
Google icons created by Freepik - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/copy" title="copy icons">
Copy icons created by Freepik - Flaticon
</a>


<a href="https://www.flaticon.com/free-icons/speaker" title="speaker icons">
Speaker icons created by Freepik - Flaticon
</a>

"""

# pylint: disable=C0302


def special_day_banner(msg: str) -> None:
    """
    This special_day_banner function is used to display about the event of the day
    """

    print(f"{F_YELLOW}{S_BRIGHT}Today is {msg}")

    special_day_label: Label = Label(master=app, text=f"Today is {msg}", bg="yellow")
    special_day_label.pack(fill="x")


def exit_app() -> None:
    """
    This exit_app function used to exit the tkinter application
    """

    music.stop()

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

    if uname == "posix":
        terminal(command="clear")

    if uname == "nt":
        terminal(command="cls")


def set_title() -> None:
    """
    This set_title function is used to set the title name in CLI console.
    """

    if uname == "posix":
        stat: int = terminal(command=f"xtitle Predictor {__version__}")

        if stat == 32512:
            # sh: 1: xtitle: not found
            # 32512

            print(f"{F_RED}{S_BRIGHT}Use the following command to install xtitle:")
            print(f"{F_BLUE}{S_BRIGHT}sudo apt update && sudo apt install xtitle -y")

    if uname == "nt":
        terminal(command="title Predictor")


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


def load_tab_1() -> None:
    """
    This load_tab_1 function is used to load the graph tab view
    """

    fig.suptitle(t="Loading...")
    fig.supxlabel(t="Loading...")
    fig.supylabel(t="Loading...")

    graph.cla()
    graph.grid(visible=True)
    canvas.draw()


def load_tab_2() -> None:
    """
    This load_tab_2 function is used to load the data tab view
    """

    tot_data_label.config(text="Loading...")
    min_val_label.config(text="Loading...")
    avg_val_label.config(text="Loading...")
    max_val_label.config(text="Loading...")
    coef_label.config(text="Loading...")
    intercept_label.config(text="Loading...")
    tomorrow_label.config(text="Loading...")
    next_week_label.config(text="Loading...")
    next_month_label.config(text="Loading...")
    next_year_label.config(text="Loading...")
    status_label.config(text="Loading...")
    last_update_label.config(text="Loading...")

    source_button.config(state="disabled")
    google_play_button.config(state="disabled")

    for _ in ["<Left>", "<Right>", "<Return>"]:
        source_button.unbind(sequence=_)
        google_play_button.unbind(sequence=_)


def load_tab_3() -> None:
    """
    This load_tab_3 function is used to load the info tab view
    """

    text_box.config(state="normal")
    text_box.delete(index1=1.0, index2="end")
    text_box.insert(index=1.0, chars="Loading, Please wait...")
    text_box.config(state="disabled")

    for _ in ["<Button-3>", "<Control-C>", "<Control-c>"]:
        text_box.unbind(_)

    copy_button.config(state="disabled")
    read_aloud_button.config(state="disabled")

    for _ in ["<Left>", "<Right>", "<Return>"]:
        copy_button.unbind(sequence=_)
        read_aloud_button.unbind(sequence=_)


def loading_ui(value: int) -> None:
    """
    This loading_ui function is used to load the user interface.
    """

    music.stop()

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Loading, Please wait..."
    )

    for _ in ["<Control-R>", "<Control-r>", "<Control-S>", "<Control-s>"]:
        app.unbind(sequence=_)

    # 1 = Predict
    # 4 = Clear
    # 5 = Refresh
    # 6 = Download CSV
    # 8 = Exit

    for _ in [1, 4, 5, 6, 8]:
        file_menu.entryconfig(index=_, state="disabled")

    header_label.config(text="Loading, Please wait...")

    choice.set(value)
    rb1.config(state="disabled")
    rb2.config(state="disabled")

    clear_button.config(state="disabled")
    refresh_button.config(state="disabled")
    download_button.config(state="disabled")
    exit_button.config(state="disabled")

    for _ in ["<Right>", "<Left>"]:
        clear_button.unbind(sequence=_)
        refresh_button.unbind(sequence=_)
        download_button.unbind(sequence=_)
        exit_button.unbind(sequence=_)

    load_tab_1()
    load_tab_2()
    load_tab_3()

    progress_bar.config(value=0)
    percentage_label.config(text="0.00%")

    footer_label.config(text="Loading, Please wait...")

    app.update()


def predict_values(prediction_lst: list, total_records: int) -> None:
    """
    This predict_values function is used to predict the linear line between the data.
    """

    for _ in tqdm(range(1, total_records + 1)):
        prediction_lst.append(float(model.predict(X=[[_]])))
        percentage: float = round(number=_ / total_records * 100, ndigits=2)
        progress_bar.config(value=percentage)
        percentage_label.config(text=f"{percentage}%")
        progress_bar.update()


def draw_graph(x_axis, y_axis, prediction_lst: list) -> None:
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

    if choice.get() == 2:
        fig.suptitle(t="e-Gold Price Predictor")
        fig.supxlabel(t="Total no of Days")
        fig.supylabel(t="Price in INR (₹)")

        graph.plot(x_axis, y_axis, ".", label="Actual e-Gold Price")
        graph.plot(x_axis, prediction_lst, "--", label="Estimated e-Gold Price")

    graph.legend()
    canvas.draw()

    app.update()


def display_data(data, total_records: int) -> None:
    """
    This display_data function is used to display the data to the application.
    """

    min_val: float = min(data["price"])
    avg_val: float = sum(data["price"]) / total_records
    max_val: float = max(data["price"])
    coef_val: float = float(model.coef_)
    intercept_val: float = float(model.intercept_)
    tomorrow_val: float = coef_val * (total_records + 1) + intercept_val
    next_week_val: float = coef_val * (total_records + 7) + intercept_val
    next_month_val: float = coef_val * (total_records + 30.4375) + intercept_val
    next_year_val: float = coef_val * (total_records + 365.25) + intercept_val
    last_update_val: str = list(data["date"])[-1]

    tot_data_label.config(text=total_records)
    min_val_label.config(text=f"₹ {min_val}")
    max_val_label.config(text=f"₹ {max_val}")

    if coef_val < 0:
        status_label.config(text=f"BEAR {DOWN_ARROW}")

    if coef_val == 0:
        status_label.config(text="No Change")

    if coef_val > 0:
        status_label.config(text=f"BULL {UP_ARROW}")

    last_update_label.config(text=last_update_val)

    if choice.get() == 1:
        avg_val_label.config(text=f"₹ {round(number=avg_val, ndigits=4)}")
        coef_label.config(text=round(number=coef_val, ndigits=4))
        intercept_label.config(text=round(number=intercept_val, ndigits=4))
        tomorrow_label.config(text=f"₹ {round(number=tomorrow_val, ndigits=4)}")
        next_week_label.config(text=f"₹ {round(number=next_week_val, ndigits=4)}")
        next_month_label.config(text=f"₹ {round(number=next_month_val, ndigits=4)}")
        next_year_label.config(text=f"₹ {round(number=next_year_val, ndigits=4)}")

        source_button.config(
            state="normal",
            command=lambda: browser(url="https://www.google.com/finance/quote/USD-INR"),
        )
        source_button.bind(
            sequence="<Return>",
            func=lambda event: browser(
                url="https://www.google.com/finance/quote/USD-INR"
            ),
        )
        google_play_button.config(state="disabled")

        for _ in ["<Left>", "<Right>"]:
            source_button.unbind(sequence=_)
            google_play_button.unbind(sequence=_)

    if choice.get() == 2:
        avg_val_label.config(text=f"₹ {round(number=avg_val, ndigits=2)}")
        coef_label.config(text=round(number=coef_val, ndigits=2))
        intercept_label.config(text=round(number=intercept_val, ndigits=2))
        tomorrow_label.config(text=f"₹ {round(number=tomorrow_val, ndigits=2)}")
        next_week_label.config(text=f"₹ {round(number=next_week_val, ndigits=2)}")
        next_month_label.config(text=f"₹ {round(number=next_month_val, ndigits=2)}")
        next_year_label.config(text=f"₹ {round(number=next_year_val, ndigits=2)}")

        source_button.config(
            state="normal",
            command=lambda: browser(url="https://www.mmtcpamp.com/"),
        )
        source_button.bind(
            sequence="<Return>",
            func=lambda event: browser(url="https://www.mmtcpamp.com/"),
        )
        google_play_button.config(
            state="normal",
            command=lambda: browser(
                url="https://play.google.com/store/apps/details?id=com.mmtcpamp.app"
            ),
        )
        google_play_button.bind(
            sequence="<Return>",
            func=lambda event: browser(
                url="https://play.google.com/store/apps/details?id=com.mmtcpamp.app"
            ),
        )

        for _ in ["<Left>", "<Right>"]:
            source_button.bind(
                sequence=_, func=lambda event: google_play_button.focus()
            )
            google_play_button.bind(
                sequence=_, func=lambda event: source_button.focus()
            )

    app.update()


def display_info() -> None:
    """
    This display_info function is used to display the information on the text widget.
    """

    if choice.get() == 1:
        with open(
            file=join(base_path, "./docs/USD_2_INR.txt"), mode="r", encoding="utf-8"
        ) as file:
            content: str = file.read()
            file.close()

    if choice.get() == 2:
        with open(
            file=join(base_path, "./docs/24k_e-Gold.txt"), mode="r", encoding="utf-8"
        ) as file:
            content: str = file.read()
            file.close()

    text_box.config(state="normal")
    text_box.delete(index1=1.0, index2="end")
    text_box.insert(index=1.0, chars=content)
    text_box.config(state="disabled")
    text_box.bind(
        sequence="<Button-3>",
        func=lambda event: popup_menu.tk_popup(x=event.x_root, y=event.y_root),
    )

    for _ in ["<Control-C>", "<Control-c>"]:
        text_box.bind(sequence=_, func=lambda event: copy_to_clipboard())

    copy_button.config(state="normal")
    read_aloud_button.config(state="normal")

    copy_button.bind(sequence="<Return>", func=lambda event: copy_to_clipboard())
    read_aloud_button.bind(sequence="<Return>", func=lambda event: read_aloud())

    for _ in ["<Left>", "<Right>"]:
        copy_button.bind(sequence=_, func=lambda event: read_aloud_button.focus())
        read_aloud_button.bind(sequence=_, func=lambda event: copy_button.focus())

    app.update()


def reset_tab_1() -> None:
    """
    This reset_tab_1 function is used to reset the graph tab view
    """
    fig.suptitle(t="Graph Area")
    fig.supxlabel(t="X-Axis")
    fig.supylabel(t="Y-Axis")

    graph.cla()
    graph.grid(visible=True)
    canvas.draw()


def reset_tab_2() -> None:
    """
    This reset_tab_2 function is used to teset the data tab view
    """

    tot_data_label.config(text="0")
    min_val_label.config(text="0.00")
    avg_val_label.config(text="0.00")
    max_val_label.config(text="0.00")
    coef_label.config(text="0.00")
    intercept_label.config(text="0.00")
    tomorrow_label.config(text="0.00")
    next_week_label.config(text="0.00")
    next_month_label.config(text="0.00")
    next_year_label.config(text="0.00")
    status_label.config(text="N/A")
    last_update_label.config(text="N/A")

    source_button.config(state="disabled")
    google_play_button.config(state="disabled")

    for _ in ["<Left>", "<Right>", "<Return>"]:
        source_button.unbind(sequence=_)
        google_play_button.unbind(sequence=_)


def reset_tab_3() -> None:
    """
    This reset_tab_3 function is used to reset the info tab view
    """

    text_box.config(state="normal")
    text_box.delete(index1=1.0, index2="end")
    text_box.insert(index=1.0, chars="No information available...")
    text_box.config(state="disabled")

    for _ in ["<Button-3>", "<Control-C>", "<Control-c>"]:
        text_box.unbind(sequence=_)

    copy_button.config(state="disabled")
    read_aloud_button.config(state="disabled")

    for _ in ["<Left>", "<Right>", "<Return>"]:
        copy_button.unbind(sequence=_)
        read_aloud_button.unbind(sequence=_)


def reset_ui():
    """
    This reset_ui function is used to reset the user interface
    """

    music.stop()

    for _ in ["<Control-R>", "<Control-r>", "<Control-S>", "<Control-s>"]:
        app.unbind(sequence=_)

    # 1 = Predict
    # 4 = Clear
    # 5 = Refresh
    # 6 = Download CSV
    # 8 = Exit

    file_menu.entryconfig(index=1, state="normal")
    file_menu.entryconfig(index=4, state="disabled")
    file_menu.entryconfig(index=5, state="disabled")
    file_menu.entryconfig(index=6, state="disabled")
    file_menu.entryconfig(index=8, state="normal")

    header_label.config(text=f"Hello {whoami.title()}, Welcome to Predictor")

    rb1.config(state="normal")
    rb2.config(state="normal")
    choice.set(value=0)

    clear_button.config(state="disabled")
    refresh_button.config(state="disabled", text="Refresh")
    download_button.config(state="disabled")
    exit_button.config(state="normal")

    for _ in ["<Right>", "<Left>"]:
        clear_button.unbind(sequence=_)
        refresh_button.unbind(sequence=_)
        download_button.unbind(sequence=_)
        exit_button.unbind(sequence=_)

    reset_tab_1()
    reset_tab_2()
    reset_tab_3()

    footer_label.config(
        text="Created by FOSS KINGDOM, Made with Love in Incredible India."
    )

    app.update()


def usd_to_inr() -> None:
    """
    This usd_to_inr function is used to predict the USD to INR value
    """

    loading_ui(value=1)
    read_database(url=USD2INR)


def e_gold_24k() -> None:
    """
    This e_gold_24 function is used to predict the 24K e-Gold Price
    """

    loading_ui(value=2)
    read_database(url=E_GOLD)


def read_database(url: str) -> None:
    """
    This read_database function is used to read the csv file from the internet.
    """

    try:
        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}Reading database, Please wait..."
        )
        with urlopen(url, timeout=10) as response:
            data: read_csv = read_csv(filepath_or_buffer=response, encoding="utf-8")
            response.close()
            update(data)

            return None

    except URLError as url_error:
        clrscr()
        reset_ui()

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

        play(path=join(base_path, "./mp3/error-call-to-attention-129258.mp3"))

        app.withdraw()
        showerror(
            title="Predictor", message=f"Failed to read database...\n{str(url_error)}"
        )
        app.deiconify()

        return None


def update(data) -> None:
    """
    This update function is used to predict, plot, and display the results
    """

    prediction_lst: list = []
    x_axis = data[["sl.no"]]
    y_axis = data["price"]
    total_records: int = len(data)

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Estimating Values, Please wait..."
    )

    model.fit(X=x_axis.values, y=y_axis)

    predict_values(prediction_lst, total_records)
    draw_graph(x_axis, y_axis, prediction_lst)
    display_data(data, total_records)
    display_info()

    update_ui()


def update_ui() -> None:
    """
    This update function is used to update the graph and data when the radio button is clicked.
    """

    for _ in ["<Control-R>", "<Control-r>"]:
        app.bind(sequence=_, func=lambda event: refresh())

    for _ in ["<Control-S>", "<Control-s>"]:
        app.bind(sequence=_, func=lambda event: download_csv())

    # 1 = Predict
    # 4 = Clear
    # 5 = Refresh
    # 6 = Download CSV
    # 8 = Exit

    for _ in [1, 4, 5, 6, 8]:
        file_menu.entryconfig(index=_, state="normal")

    header_label.config(text=f"Hello {whoami.title()}, Welcome to Predictor")

    rb1.config(state="normal")
    rb2.config(state="normal")

    clear_button.config(state="normal")
    refresh_button.config(state="normal", text="Refresh")
    download_button.config(state="normal")
    exit_button.config(state="normal")

    clear_button.bind(sequence="<Right>", func=lambda event: refresh_button.focus())
    clear_button.bind(sequence="<Left>", func=lambda event: exit_button.focus())

    refresh_button.bind(sequence="<Right>", func=lambda event: download_button.focus())
    refresh_button.bind(sequence="<Left>", func=lambda event: clear_button.focus())

    download_button.bind(sequence="<Right>", func=lambda event: exit_button.focus())
    download_button.bind(sequence="<Left>", func=lambda event: refresh_button.focus())

    exit_button.bind(sequence="<Right>", func=lambda event: clear_button.focus())
    exit_button.bind(sequence="<Left>", func=lambda event: download_button.focus())

    progress_bar.config(value=0)
    percentage_label.config(text="0.00%")

    footer_label.config(
        text="Created by FOSS KINGDOM, Made with Love in Incredible India."
    )

    app.update()


def refresh() -> None:
    """
    This refresh function is used to refresh the graph and data.
    """

    refresh_button.config(text="Refreshing...", state="disabled")
    refresh_button.update()

    if choice.get() == 1:
        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}Refreshing, Please wait..."
        )

        usd_to_inr()

    if choice.get() == 2:
        print(
            f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}Refreshing, Please wait..."
        )

        e_gold_24k()


def download_csv() -> None:
    """
    This download_csv function is used to download the CSV model.
    """

    download_button.config(state="disabled", text="Downloading...")
    download_button.update()

    try:
        if choice.get() == 1:
            content: str = get(url=USD2INR, timeout=10).content.decode(encoding="utf-8")

        if choice.get() == 2:
            content: str = get(url=E_GOLD, timeout=10).content.decode(encoding="utf-8")

        app.withdraw()
        file_location: str = asksaveasfilename(
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")],
            defaultextension=".csv",
        )

        if file_location:
            with open(file=file_location, mode="w", encoding="utf-8") as file:
                file.write(content)
                file.close()

                print(
                    f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
                    f"{S_RESET_ALL}]\t{S_BRIGHT}CSV file downloaded successfully..."
                )
                showinfo(
                    title="Predictor", message="CSV file downloaded successfully..."
                )

        app.deiconify()

    except RequestsConnectionError as requests_connection_error:
        print(F_BLUE + "=" * 80)
        figlet_banner(font=selected_figlet_font)
        print(F_BLUE + "=" * 80)
        print(f"{S_BRIGHT}Failed to download CSV file...")
        print(f"{S_BRIGHT}Error Code: requests.exceptions.ConnectionError")
        print(
            f"[{F_RED}{S_BRIGHT}ERROR{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
            f"{S_RESET_ALL}]\t{S_BRIGHT}{requests_connection_error}"
        )
        print(F_BLUE + "=" * 80)

        play(path=join(base_path, "./mp3/error-call-to-attention-129258.mp3"))

        app.withdraw()
        showerror(
            title="Predictor",
            message=f"Failed to download CSV file...\n\n{str(requests_connection_error)}",
        )
        app.deiconify()

    download_button.config(state="normal", text="Download CSV")
    download_button.update()


def copy_to_clipboard() -> None:
    """
    This copy_to_clipboard function is used to copy the text from the textbox widget
    """

    app.clipboard_clear()

    try:
        app.clipboard_append(string=text_box.selection_get())

    except TclError:
        app.clipboard_append(string=text_box.get(index1=1.0, index2="end"))

    app.withdraw()
    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Successfully, copied to clipboard!!"
    )
    showinfo(title="Predictor", message="Successfully, copied to clipboard!!")
    app.deiconify()


def play(path: str) -> None:
    """
    This play function is used to play the sounds and music
    """

    music.load(filename=path)
    music.play(loops=0)


def read_aloud() -> None:
    """
    This read_aloud function is used to read the text using TTS engines.
    """

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Reading the text..."
    )

    if choice.get() == 1:
        play(path=join(base_path, "./mp3/USD_2_INR.mp3"))

    if choice.get() == 2:
        play(path=join(base_path, "./mp3/24k_e-Gold.mp3"))


try:
    print("=" * 80)
    print("[INFO]\tImporting built-in libraries, Please wait...")

    print("[INFO]\tImporting datetime, Please wait...")
    from datetime import datetime

    print("[INFO]\tImporting getpass, Please wait...")
    from getpass import getuser

    print("[INFO]\tImporting os, Please wait...")
    from os import name
    from os import system as terminal
    from os.path import isdir, join

    print("[INFO]\tImporting pathlib, Please wait...")
    from pathlib import Path

    print("[INFO]\tImporting random, Please wait...")
    from random import choice

    print("[INFO]\tImporting shutil, Please wait...")
    from shutil import rmtree

    print("[INFO]\tImporting sys, Please wait...")
    from sys import exit as terminate

    print("[INFO]\tImporting tkinter, Please wait...")
    from tkinter import Button, Frame, IntVar, Label, LabelFrame, Menu
    from tkinter import PhotoImage as TkPhotoImage
    from tkinter import Radiobutton, TclError, Tk
    from tkinter.filedialog import asksaveasfilename
    from tkinter.messagebox import askyesno, showerror, showinfo
    from tkinter.scrolledtext import ScrolledText
    from tkinter.ttk import Notebook, Progressbar

    print("[INFO]\tImporting urllib, Please wait...")
    from urllib.error import URLError
    from urllib.request import urlopen

    print("[INFO]\tImporting webbrowser, Please wait...")
    from webbrowser import open as browser

    print("=" * 80)

    whoami: str = getuser()
    today: datetime = datetime.today()
    base_path: Path = Path(__file__).parent
    uname: str = name
    __version__: str = "v.20230408"

    print(f"[INFO]\t[{datetime.now()}]\tImporting third-party modules, Please wait...")

    print(f"[INFO]\t[{datetime.now()}]\tImporting colorama, Please wait...")
    from colorama import init as colorama_init

    print(f"[INFO]\t[{datetime.now()}]\tImporting matplotlib, Please wait...")
    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg,
        NavigationToolbar2Tk,
    )
    from matplotlib.figure import Figure

    print(f"[INFO]\t[{datetime.now()}]\tImporting pandas, Please wait...")
    from pandas import read_csv

    print(f"[INFO]\t[{datetime.now()}]\tImporting pillow, Please wait...")
    from PIL.Image import open as img_open
    from PIL.ImageTk import PhotoImage as PILPhotoImage

    print(f"[INFO]\t[{datetime.now()}]\tImporting pyfiglet, Please wait...")
    from pyfiglet import FigletFont, figlet_format

    # https://www.youtube.com/watch?v=djDcVWbEYoE
    print(f"[INFO]\t[{datetime.now()}]\tImporting pygame, Please wait...")
    from pygame.mixer import init as pygame_init
    from pygame.mixer import music

    print(f"[INFO]\t[{datetime.now()}]\tImporting requests, Please wait...")
    from requests import get
    from requests.exceptions import ConnectionError as RequestsConnectionError

    print(f"[INFO]\t[{datetime.now()}]\tImporting scikit-learn, Please wait...")
    from sklearn.linear_model import LinearRegression

    print(f"[INFO]\t[{datetime.now()}]\tImporting tqdm, Please wait...")
    from tqdm import tqdm

    selected_figlet_font: str = choice(FigletFont.getFonts())

    print("=" * 80)

    print(f"[INFO]\t[{datetime.now()}]\tImporting constants module, Please wait...")

    print(f"[INFO]\t[{datetime.now()}]\tImporting constants, Please wait...")
    from constants import (
        ALB,
        ARG,
        ARM,
        AUT,
        AZE,
        BEATING_HEART,
        BEL,
        BGD,
        BGR,
        BHR,
        BIH,
        BOL,
        BRA,
        CAN,
        CHE,
        COL,
        CRI,
        DEU,
        DJI,
        DNK,
        DOM,
        DOWN_ARROW,
        DZA,
        E_GOLD,
        ECU,
        EST,
        F_BLUE,
        F_GREEN,
        F_RED,
        F_YELLOW,
        FIN,
        GEO,
        GHA,
        GRC,
        GTM,
        HND,
        HUN,
        IDN,
        IND,
        ISL,
        ISR,
        ITA,
        JAM,
        JOR,
        KAZ,
        KEN,
        KHM,
        KWT,
        LBN,
        LKA,
        LTU,
        LVA,
        MDA,
        MEX,
        MOUNTAIN,
        NGA,
        NIC,
        NOR,
        OMN,
        PAK,
        PAN,
        PER,
        PHL,
        POL,
        PRT,
        QAT,
        S_BRIGHT,
        S_RESET_ALL,
        SAU,
        SEN,
        SGP,
        SLV,
        SRB,
        SVK,
        SVN,
        SWE,
        THEME_COLOR,
        TTO,
        TUN,
        TUR,
        TZA,
        UAE,
        UGA,
        UKR,
        UP_ARROW,
        URY,
        USA,
        USD2INR,
        UZB,
        VEN,
        VNM,
        ZAF,
    )

    print(F_BLUE + "=" * 80 + S_RESET_ALL)

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Initializing colorama, Please wait...{S_RESET_ALL}"
    )
    colorama_init(autoreset=True)

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Initializing linear regression model, Please wait..."
    )
    model: LinearRegression = LinearRegression()

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Initializing pygame.mixer, Please wait..."
    )
    pygame_init()

    print(
        f"[{F_GREEN}{S_BRIGHT}INFO{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}"
        f"{S_RESET_ALL}]\t{S_BRIGHT}Loading GUI Application, Please wait..."
    )

    print(F_BLUE + "=" * 80)
    figlet_banner(font=selected_figlet_font)
    print(F_BLUE + "=" * 80)

    app: Tk = Tk()

    app.title(string=f"Predictor {__version__}")
    set_title()

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

    app.config(bg=THEME_COLOR["light"], menu=menu_bar)

    money_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/money.png")).resize(size=(16, 16))
    )

    gold_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/ingots.png")).resize(size=(16, 16))
    )

    graph_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/bar-chart.png")).resize(size=(16, 16))
    )

    statistic_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/statistics.png")).resize(size=(16, 16))
    )

    info_ico: PILPhotoImage = PILPhotoImage(
        img_open(fp=join(base_path, "./assets/information.png")).resize(size=(16, 16))
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
        accelerator="(Alt+1)",
        command=lambda: tab_view.select(tab_id=0),
    )
    goto_menu.add_command(
        label="Data",
        image=statistic_ico,
        compound="left",
        accelerator="(Alt+2)",
        command=lambda: tab_view.select(tab_id=1),
    )
    file_menu.add_separator()
    file_menu.add_command(label="Clear", state="disabled", command=reset_ui)
    file_menu.add_command(
        label="Refresh", accelerator="(Ctrl+R)", state="disabled", command=refresh
    )
    file_menu.add_command(
        label="Download CSV",
        accelerator="(Ctrl+S)",
        state="disabled",
        command=download_csv,
    )
    file_menu.add_separator()
    file_menu.add_command(label="Exit", accelerator="(Ctrl+Q)", command=exit_app)

    license_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/license.png")).resize(size=(16, 16))
    )

    video_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/play.png")).resize(size=(16, 16))
    )

    source_code_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/programming.png")).resize(
            size=(16, 16)
        )
    )
    issues_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/bug-report.png")).resize(size=(16, 16))
    )

    translation_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/translate.png")).resize(size=(16, 16))
    )

    changelog_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/notepad.png")).resize(size=(16, 16))
    )

    website_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/web-link.png")).resize(size=(16, 16))
    )

    email_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/mail.png")).resize(size=(16, 16))
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
        image=img_open(join(base_path, "./assets/donation.png")).resize(size=(16, 16))
    )

    # Help Menu
    help_menu: Menu = Menu(master=menu_bar, tearoff=False)
    menu_bar.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(
        label="About Predictor",
        accelerator="(\u2139\ufe0f)",
        image=info_ico,
        compound="left",
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

    # https://carpedm20.github.io/emoji/
    if month == 1:
        if day == 1:
            special_day_banner(msg="New Year's Day")

        if day == 26:
            special_day_banner(msg=f"India {IND} Republic Day")

    if month == 2:
        if day == 4:
            special_day_banner(msg=f"Sri Lanka {LKA} Independence Day")

        if day == 6:
            special_day_banner(msg="Waitangi Day")

        if day == 14:
            special_day_banner(msg=f"Valentine's Day {BEATING_HEART}")

        if day == 15:
            special_day_banner(msg=f"Serbia {SRB} National Day")

        if day == 16:
            special_day_banner(msg=f"Lithuania {LTU} Independence Day")

        if day == 24:
            special_day_banner(msg=f"Estonia {EST} Independence Day")

        if day == 25:
            special_day_banner(msg=f"Kuwait {KWT} National Day")

        if day == 27:
            special_day_banner(msg=f"Dominican Republic {DOM} Independence Day")

    if month == 3:
        if day == 1:
            special_day_banner(msg="St. David's Day")

        if day == 3:
            special_day_banner(msg=f"Bulgaria {BGR} Liberation Day")

        if day == 6:
            special_day_banner(msg=f"Ghana {GHA} Independence Day")

        if day == 8:
            special_day_banner(msg="International Women's Day")

        if day == 15:
            special_day_banner(msg=f"Hungary {HUN} National Day")

        if day == 20:
            special_day_banner(msg=f"Tunisia {TUN} National Day")

        if day == 25:
            special_day_banner(msg=f"Greece {GRC} National Day")

        if day == 26:
            special_day_banner(msg=f"Bangladesh {BGD} Independence Day")

    if month == 4:
        if day == 4:
            special_day_banner(msg=f"Senegal {SEN} Independence Day")

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
                f"South Africa {ZAF} Freedom Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

    if day == 5:
        if day == 5:
            special_day_banner(msg=f"Israel {ISR} Independence Day")

        if day == 17:
            special_day_banner(msg=f"Norway {NOR} Constitution Day")

        if day == 25:
            special_day_banner(msg=f"Jordan {JOR} Independence Day")

        if day == 26:
            special_day_banner(msg=f"Georgia {GEO} Independence Day")

    if month == 6:
        if day == 2:
            special_day_banner(msg=f"Italy {ITA} Republic Day")

        if day == 5:
            special_day_banner(msg=f"Denmark {DNK} Constitution Day")

        if day == 6:
            special_day_banner(msg=f"Sweden {SWE} National Day")

        if day == 10:
            special_day_banner(msg=f"Portugal {PRT} National Day")

        if day == 12:
            special_day_banner(msg=f"Philippines {PHL} Independence Day")

        if day == 17:
            special_day_banner(msg=f"Iceland {ISL} National Day")

        if day == 25:
            special_day_banner(msg=f"Slovenia {SVN} National Day")

        if day == 27:
            special_day_banner(msg=f"Djibouti {DJI} Independence Day")

    if month == 7:
        if day == 1:
            special_day_banner(msg=f"Canada {CAN} Day")

        if day == 4:
            special_day_banner(msg=f"Fourth of July USA {USA}")

        if day == 5:
            day_list: list = [
                f"Algeria {DZA} Independence Day",
                f"Venezuela {VEN} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 9:
            special_day_banner(msg=f"Argentina {ARG} Independence Day")

        if day == 14:
            special_day_banner(msg="Bastille Day")

        if day == 20:
            special_day_banner(msg=f"Colombia {COL} Independence Day")

        if day == 21:
            special_day_banner(msg=f"Belgium {BEL} National Day")

        if day == 28:
            special_day_banner(msg=f"Peru {PER} Independence Day")

    if month == 8:
        if day == 1:
            special_day_banner(msg=f"Switzerland {CHE} National Day")

        if day == 6:
            day_list: list = [
                f"Bolivia {BOL} Independence Day",
                f"Jamaica {JAM} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 9:
            special_day_banner(msg=f"Singapore {SGP} National Day")

        if day == 10:
            special_day_banner(msg=f"Ecuador {ECU} Independence Day")

        if day == 11:
            special_day_banner(msg=f"Mountain {MOUNTAIN} Day")

        if day == 14:
            special_day_banner(msg=f"Pakistan {PAK} Independence Day")

        if day == 15:
            day_list: list = [
                "National Liberation Day of Korea",
                f"India {IND} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 17:
            special_day_banner(msg=f"Indonesia {IDN} Independence Day")

        if day == 24:
            special_day_banner(msg=f"Ukraine {UKR} Independence Day")

        if day == 25:
            special_day_banner(msg=f"Uruguay {URY} Independence Day")

        if day == 27:
            special_day_banner(msg=f"Republic of Moldova {MDA} Independence Day")

        if day == 31:
            day_list: list = [
                "Hari Merdeka",
                f"Trinidad & Tobago {TTO} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

    if month == 9:
        if day == 1:
            special_day_banner(msg=f"Uzbekistan {UZB} Independence Day")

        if day == 2:
            special_day_banner(msg=f"Vietnam {VNM} National Day")

        if day == 7:
            special_day_banner(msg=f"Brazil {BRA} Independence Day")

        if day == 15:
            day_list: list = [
                f"Costa Rica {CRI} Independence Day",
                f"El Salvador {SLV} Independence Day",
                f"Guatemala {GTM} Independence Day",
                f"Honduras {HND} National Day",
                f"Nicaragua {NIC} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 16:
            special_day_banner(msg=f"Mexico {MEX} Independence Day")

        if day == 19:
            special_day_banner(msg="Respect for the Aged Day")

        if day == 21:
            special_day_banner(msg=f"Armenia {ARM} Independence Day")

        if day == 23:
            special_day_banner(msg=f"Saudi Arabia {SAU} National Day")

    if month == 10:
        if day == 1:
            special_day_banner(msg=f"Nigeria {NGA} Independence Day")

        if day == 3:
            special_day_banner(msg=f"German {DEU} Unity Day")

        if day == 9:
            day_list: list = ["Hangul Day", f"Uganda {UGA} Independence Day"]
            special_day_banner(msg=choice(seq=day_list))

        if day == 18:
            special_day_banner(msg=f"Azerbaijan {AZE} Independence Day")

        if day == 26:
            special_day_banner(msg=f"Austria {AUT} National Day")

        if day == 29:
            special_day_banner(msg=f"Turkey {TUR} National Day")

    if month == 11:
        if day == 3:
            special_day_banner(msg=f"Panama {PAN} Independence Day")

        if day == 9:
            special_day_banner(msg=f"Cambodia {KHM} Independence Day")

        if day == 11:
            day_list: list = [f"Poland {POL} National Day", "Veterans Day"]
            special_day_banner(msg=choice(seq=day_list))

        if day == 17:
            day_list: list = [
                "Czech Republic Freedom and Democracy Day",
                f"Slovakia {SVK} Freedom and Democracy Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 18:
            day_list: list = [
                f"Oman {OMN} National Day",
                f"Latvia {LVA} Independence Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 22:
            special_day_banner(msg=f"Lebanon {LBN} Independence Day")

        if day == 25:
            special_day_banner(msg=f"Bosnia & Herzegovina {BIH} Statehood Day")

        if day == 28:
            special_day_banner(msg=f"Albania {ALB} Independence Day")

        if day == 30:
            special_day_banner(msg="St. Andrew's Day")

    if month == 12:
        if day == 1:
            special_day_banner(msg="Great Union Day")

        if day == 2:
            special_day_banner(msg=f"UAE {UAE} National Day")

        if day == 6:
            special_day_banner(msg=f"Finland {FIN} Independence Day")

        if day == 9:
            special_day_banner(msg=f"Tanzania {TZA} Independence Day")

        if day == 12:
            special_day_banner(msg=f"Kenya {KEN} Independence Day")

        if day == 16:
            day_list: list = [
                f"Kazakhstan {KAZ} Independence Day",
                f"Bahrain {BHR} National Day",
            ]
            special_day_banner(msg=choice(seq=day_list))

        if day == 18:
            special_day_banner(msg=f"Qatar {QAT} National Day")

        if day == 31:
            special_day_banner(msg="New Year's Eve")

    label_frame_1: LabelFrame = LabelFrame(
        master=app,
        text="What would you like to predict?",
        bg=THEME_COLOR["light"],
        fg="red",
    )
    label_frame_1.pack(fill="x", padx=10, pady=5)

    choice: IntVar = IntVar()

    rb1: Radiobutton = Radiobutton(
        master=label_frame_1,
        bg=THEME_COLOR["light"],
        activebackground=THEME_COLOR["light"],
        text="United State Dollar to India Rupees Value",
        variable=choice,
        value=1,
        command=usd_to_inr,
    )
    rb1.bind(sequence="<Up>", func=lambda event: rb2.focus())
    rb1.bind(sequence="<Down>", func=lambda event: rb2.focus())
    rb1.grid(row=0, column=0, sticky="w")

    rb2: Radiobutton = Radiobutton(
        master=label_frame_1,
        bg=THEME_COLOR["light"],
        activebackground=THEME_COLOR["light"],
        text="24K e-Gold Price by MMTC-PAMP",
        variable=choice,
        value=2,
        command=e_gold_24k,
    )
    rb2.bind(sequence="<Up>", func=lambda event: rb1.focus())
    rb2.bind(sequence="<Down>", func=lambda event: rb1.focus())
    rb2.grid(row=1, column=0, sticky="w")

    buttons_frame_1: Frame = Frame(master=app, bg=THEME_COLOR["light"])
    buttons_frame_1.pack(pady=5)

    clear_icon: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/clear.png")).resize(size=(16, 16))
    )

    clear_button: Button = Button(
        master=buttons_frame_1,
        text="Clear",
        bg="#00f",
        fg="#FFF",
        activeforeground="#FFF",
        activebackground="#3333ff",
        compound="left",
        state="disabled",
        image=clear_icon,
        width=110,
        command=reset_ui,
    )
    clear_button.bind(sequence="<Return>", func=lambda event: reset_ui())
    clear_button.pack(padx=5, side="left")

    refresh_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/refresh.png")).resize(size=(16, 16))
    )

    refresh_button: Button = Button(
        master=buttons_frame_1,
        text="Refresh",
        bg="green",
        fg="#FFF",
        activeforeground="#FFF",
        activebackground="#009a00",
        image=refresh_ico,
        compound="left",
        state="disabled",
        width=110,
        command=refresh,
    )
    refresh_button.bind(sequence="<Return>", func=lambda event: refresh())
    refresh_button.pack(padx=5, side="left")

    download_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/direct-download.png")).resize(
            size=(16, 16)
        )
    )

    download_button: Button = Button(
        master=buttons_frame_1,
        text="Download CSV",
        bg="orange",
        fg="#FFF",
        activeforeground="#FFF",
        activebackground="#ffbe00",
        image=download_ico,
        compound="left",
        state="disabled",
        width=110,
        command=download_csv,
    )
    download_button.bind(sequence="<Return>", func=lambda event: download_csv())
    download_button.pack(padx=5, side="left")

    exit_icon: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=join(base_path, "./assets/logout.png")).resize(size=(16, 16))
    )

    exit_button: Button = Button(
        master=buttons_frame_1,
        text="Exit",
        bg="#CE313A",
        fg="#FFF",
        width=110,
        activebackground="red",
        activeforeground="#FFF",
        image=exit_icon,
        compound="left",
        command=exit_app,
    )
    exit_button.bind(sequence="<Return>", func=lambda event: exit_app())
    exit_button.pack(padx=5, side="left")

    tab_view: Notebook = Notebook(master=app)
    tab_view.pack(fill="both", expand=True)

    graph_frame: Frame = Frame(master=tab_view, bg=THEME_COLOR["light"])
    graph_frame.pack()

    data_frame: Frame = Frame(master=tab_view, bg=THEME_COLOR["light"])
    data_frame.pack()

    info_frame: Frame = Frame(master=tab_view, bg=THEME_COLOR["light"])
    info_frame.pack()

    tab_view.add(child=graph_frame, text="Graph", image=graph_ico, compound="left")
    tab_view.add(child=data_frame, text="Data", image=statistic_ico, compound="left")
    tab_view.add(child=info_frame, text="Info", image=info_ico, compound="left")

    app.bind(sequence="<Alt-KeyPress-1>", func=lambda event: tab_view.select(tab_id=0))
    app.bind(sequence="<Alt-KeyPress-2>", func=lambda event: tab_view.select(tab_id=1))
    app.bind(sequence="<Alt-KeyPress-3>", func=lambda event: tab_view.select(tab_id=2))

    fig: Figure = Figure(facecolor=THEME_COLOR["light"])
    fig.suptitle(t="Graph Area")
    fig.supxlabel(t="X-Axis")
    fig.supylabel(t="Y-Axis")

    graph = fig.add_subplot()
    graph.grid(visible=True)

    canvas: FigureCanvasTkAgg = FigureCanvasTkAgg(fig, master=graph_frame)
    toolbar: NavigationToolbar2Tk = NavigationToolbar2Tk(canvas, graph_frame)
    toolbar.pack()
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)

    label_frame_2: LabelFrame = LabelFrame(
        master=data_frame, text="Statistic Data", bg=THEME_COLOR["light"], fg="red"
    )
    label_frame_2.pack(padx=10, pady=5, fill="both")

    Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="Total Records (n):"
    ).grid(row=0, column=0, padx=10, sticky="w")
    tot_data_label: Label = Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="0"
    )
    tot_data_label.grid(row=0, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=THEME_COLOR["light"], text="Minimum:").grid(
        row=1, column=0, padx=10, sticky="w"
    )
    min_val_label: Label = Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="0.00"
    )
    min_val_label.grid(row=1, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=THEME_COLOR["light"], text="Average:").grid(
        row=2, column=0, padx=10, sticky="w"
    )
    avg_val_label: Label = Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="0.00"
    )
    avg_val_label.grid(row=2, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=THEME_COLOR["light"], text="Maximum:").grid(
        row=3, column=0, padx=10, sticky="w"
    )
    max_val_label: Label = Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="0.00"
    )
    max_val_label.grid(row=3, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=THEME_COLOR["light"], text="Coefficient (m):").grid(
        row=4, column=0, padx=10, sticky="w"
    )
    coef_label: Label = Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="0.00"
    )
    coef_label.grid(row=4, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=THEME_COLOR["light"], text="Intercept (b):").grid(
        row=5, column=0, padx=10, sticky="w"
    )
    intercept_label: Label = Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="0.00"
    )
    intercept_label.grid(row=5, column=1, padx=10, sticky="w")

    Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="Tomorrow expected:"
    ).grid(row=6, column=0, padx=10, sticky="w")
    tomorrow_label: Label = Label(
        master=label_frame_2,
        bg=THEME_COLOR["light"],
        text="0.00",
    )
    tomorrow_label.grid(row=6, column=1, padx=10, sticky="w")

    Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="Next week expected:"
    ).grid(row=7, column=0, padx=10, sticky="w")
    next_week_label: Label = Label(
        master=label_frame_2,
        bg=THEME_COLOR["light"],
        text="0.00",
    )
    next_week_label.grid(row=7, column=1, padx=10, sticky="w")

    Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="Next month expected:"
    ).grid(row=8, column=0, padx=10, sticky="w")
    next_month_label: Label = Label(
        master=label_frame_2,
        bg=THEME_COLOR["light"],
        text="0.00",
    )
    next_month_label.grid(row=8, column=1, padx=10, sticky="w")

    Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="Next year expected:"
    ).grid(row=9, column=0, padx=10, sticky="w")
    next_year_label: Label = Label(
        master=label_frame_2,
        bg=THEME_COLOR["light"],
        text="0.00",
    )
    next_year_label.grid(row=9, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=THEME_COLOR["light"], text="Status:").grid(
        row=10, column=0, padx=10, sticky="w"
    )
    status_label: Label = Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="N/A"
    )
    status_label.grid(row=10, column=1, padx=10, sticky="w")

    Label(master=label_frame_2, bg=THEME_COLOR["light"], text="Last Updated:").grid(
        row=11, column=0, padx=10, sticky="w"
    )
    last_update_label: Label = Label(
        master=label_frame_2, bg=THEME_COLOR["light"], text="N/A"
    )
    last_update_label.grid(row=11, column=1, padx=10, sticky="w")

    buttons_frame_2: Frame = Frame(master=data_frame, bg=THEME_COLOR["light"])
    buttons_frame_2.pack(pady=5)

    redirect_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=join(base_path, "./assets/share.png")).resize(size=(14, 14))
    )

    source_button: Button = Button(
        master=buttons_frame_2,
        text="Source",
        bg="#CE313A",
        fg="#FFF",
        activebackground="red",
        activeforeground="#FFF",
        state="disabled",
        compound="right",
        image=redirect_ico,
        width=100,
    )
    source_button.pack(padx=5, side="left")

    google_play_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(join(base_path, "./assets/google-play.png")).resize((16, 16))
    )

    google_play_button: Button = Button(
        master=buttons_frame_2,
        text="Google Play",
        bg="#00f",
        fg="#fff",
        activeforeground="#fff",
        activebackground="#3333ff",
        state="disabled",
        compound="left",
        width=100,
        image=google_play_ico,
    )
    google_play_button.pack(padx=5, side="left")

    label_frame_3: LabelFrame = LabelFrame(
        master=data_frame, text="Powered by", bg=THEME_COLOR["light"], fg="red"
    )
    label_frame_3.pack(padx=10, pady=5, fill="both", expand=True)

    google_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=join(base_path, "./assets/search.png")).resize(size=(80, 80))
    )

    mmtc_pamp_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=join(base_path, "./assets/header-logo.png")).resize(
            size=(80, 80)
        )
    )

    Label(master=label_frame_3, image=google_ico, bg=THEME_COLOR["light"]).grid(
        row=0, column=0, padx=5, pady=5
    )
    Label(master=label_frame_3, image=mmtc_pamp_ico, bg=THEME_COLOR["light"]).grid(
        row=0, column=1, padx=5, pady=5
    )

    text_box: ScrolledText = ScrolledText(master=info_frame, wrap="word")
    text_box.insert(index=1.0, chars="No information available...")
    text_box.config(state="disabled")
    text_box.pack(fill="both", expand=True)

    # https://www.youtube.com/watch?v=KRuUtNxOb_k&t=466s
    popup_menu: Menu = Menu(master=text_box, tearoff=False)
    popup_menu.add_command(
        label="Copy", accelerator="(Ctrl+C)", command=copy_to_clipboard
    )
    popup_menu.add_command(label="Read Aloud", command=read_aloud)
    popup_menu.add_separator()
    popup_menu.add_command(label="Select All", accelerator="(Ctrl+A)")

    buttons_frame_3: Frame = Frame(master=info_frame, bg=THEME_COLOR["light"])
    buttons_frame_3.pack(pady=5)

    copy_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=join(base_path, "./assets/copy.png")).resize(size=(16, 16))
    )

    copy_button: Button = Button(
        master=buttons_frame_3,
        text="Copy",
        bg="orange",
        fg="#fff",
        activeforeground="#fff",
        activebackground="#ffbe00",
        compound="left",
        state="disabled",
        width=100,
        image=copy_ico,
        command=copy_to_clipboard,
    )
    copy_button.pack(padx=5, side="left")

    megaphone_ico: PILPhotoImage = PILPhotoImage(
        image=img_open(fp=join(base_path, "./assets/megaphone.png")).resize(
            size=(16, 16)
        )
    )

    read_aloud_button: Button = Button(
        master=buttons_frame_3,
        text="Read Aloud",
        bg="#00f",
        fg="#fff",
        activebackground="#3333ff",
        activeforeground="#fff",
        compound="left",
        state="disabled",
        width=100,
        image=megaphone_ico,
        command=read_aloud,
    )
    read_aloud_button.pack(padx=5, side="left")

    progress_frame: Frame = Frame(master=app, bg=THEME_COLOR["light"])
    progress_frame.pack(fill="x", pady=5)

    Label(master=progress_frame, text="Job:", bg=THEME_COLOR["light"]).pack(
        padx=(10, 5), side="left"
    )

    progress_bar: Progressbar = Progressbar(
        master=progress_frame, orient="horizontal", mode="determinate"
    )
    progress_bar.pack(fill="x", expand=True, padx=5, side="left")

    percentage_label: Label = Label(
        master=progress_frame, text="0.00%", bg=THEME_COLOR["light"]
    )
    percentage_label.pack(padx=(5, 10), side="left")

    footer_msg: str = (
        f"Created by FOSS Kingdom / "
        f"Made with Love {BEATING_HEART} in Incredible India {IND}"
    )

    footer_label: Label = Label(
        master=app,
        text=footer_msg,
        bg="#000",
        fg="#FFF",
    )
    footer_label.pack(side="bottom", fill="x")

    print(f"{F_GREEN}{S_BRIGHT}{footer_msg}")
    print(F_BLUE + "=" * 80)

    app.mainloop()

except TclError as tcl_error:
    clrscr()

    print(F_BLUE + "=" * 80)
    figlet_banner(font=selected_figlet_font)
    print(F_BLUE + "=" * 80)
    print(S_BRIGHT + "Error Code: tkinter.TclError")
    print(
        f"[{F_RED}{S_BRIGHT}ERROR{S_RESET_ALL}]\t[{F_BLUE}{S_BRIGHT}{datetime.now()}{S_RESET_ALL}]"
        f"\t{S_BRIGHT}{tcl_error}"
    )
    print(F_BLUE + "=" * 80)
    print(F_GREEN + S_BRIGHT + "Bye!!")

    terminate()

except ModuleNotFoundError as module_not_found_error:
    clrscr()

    print("=" * 80)
    print("Error Code: builtins.ModuleNotFoundError")
    print(f"[ERROR]\t[{datetime.now()}]\t{module_not_found_error}")
    print("=" * 80)
    print("Bye!!")

    terminate()
