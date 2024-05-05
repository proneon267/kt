"""
My first application
"""

import toga
from toga.style import Pack
from toga.colors import rgba


# from toga_android import native_color_from_toga_color


class HelloWorld(toga.App):
    def validate_rgba(self, value):
        try:
            parts = value.split(",")
            if len(parts) != 4:
                raise ValueError
            r, g, b, a = map(float, parts)
            if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255 and 0 <= a <= 1):
                raise ValueError
        except ValueError:
            print("Invalid RGBA string format. Example: 0,255,0,0.5")
        return None

    def do_change_place(self, widget, **kwargs):
        color_tuple = tuple(map(float, self.color_input.value.split(",")))
        self.widget_box.style.background_color = rgba(*color_tuple)

        # if getattr(self, "widgets_in_upper_box", True):
        #     self.lower_box.add(self.widget_box)
        #     self.widgets_in_upper_box = False
        # else:
        #     self.upper_box.add(self.widget_box)
        #     self.widgets_in_upper_box = True
        print(f"---------{self.image_view._impl.native.BackColor}")

    def startup(self):
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.toga_box = toga.Box(style=Pack(flex=1, direction="column"))

        self.upper_box = toga.Box(style=Pack(flex=1, background_color="red"))
        self.lower_box = toga.Box(style=Pack(flex=1, background_color="blue"))

        self.widget_box = toga.Box(
            style=Pack(
                direction="column",
                flex=1,
                # background_color=rgba(21, 21, 21, 0.6)
            )
        )
        self.button = toga.Button(
            text="Change Place",
            on_press=self.do_change_place,
            style=Pack(
                padding=10,
                padding_top=15,
                padding_right=5,
                # background_color="transparent",
            ),
        )
        self.label = toga.Label(
            text="WinForms RGBA:",
            style=Pack(
                padding_top=20,
                padding_bottom=20,
                color="white",
                background_color="transparent",
            ),
        )
        self.color_input = toga.TextInput(
            placeholder="21,21,21,0.6",
            value="21,21,21,0.6",
            validators=[self.validate_rgba],
            style=Pack(padding_top=15, padding_left=5),
        )
        self.canvas = toga.Canvas(style=Pack(height=100))
        context = self.canvas.context

        context.begin_path()
        context.move_to(20, 20)
        context.line_to(160, 20)
        context.stroke(color="orange")

        self.image_view = toga.ImageView(
            toga.Image(self.paths.app / "resources" / "kt.png")
        )

        self.widget_box.add(
            self.button,
            self.label,
            self.color_input,
            toga.DateInput(),
            toga.MultilineTextInput(),
            toga.NumberInput(),
            toga.PasswordInput(),
            toga.ProgressBar(value=50.0),
            toga.Box(style=Pack(height=20, background_color="white")),
            toga.Divider(style=Pack(height=5)),
            toga.Box(style=Pack(height=50, background_color="white")),
            toga.Selection(
                id="selection",
                items=["Alice", "Bob", "Charlie"],
                style=Pack(background_color="pink"),
            ),
            toga.Box(style=Pack(height=20, background_color="white")),
            toga.Slider(range=(-5, 10), value=7),
            toga.Switch(text="Switch"),
            toga.TimeInput(),
            toga.DetailedList(
                data=[
                    {
                        "icon": toga.Icon("icons/arthur"),
                        "title": "Arthur Dent",
                        "subtitle": "Where's the tea?",
                    },
                    {
                        "icon": toga.Icon("icons/ford"),
                        "title": "Ford Prefect",
                        "subtitle": "Do you know where my towel is?",
                    },
                    {
                        "icon": toga.Icon("icons/tricia"),
                        "title": "Tricia McMillan",
                        "subtitle": "What planet are you from?",
                    },
                ],
                style=Pack(height=200),
            ),
            self.canvas,
            self.image_view,
        )

        self.upper_box.add(self.widget_box)

        self.toga_box.add(self.upper_box, self.lower_box)
        self.web_box = toga.Box(
            style=Pack(flex=1),
            children=[
                toga.WebView(
                    url="https://proneon267.github.io/proneon267-tests/transparency-test.html",
                    style=Pack(flex=1),
                )
            ],
        )

        # self.main_window.content = toga.SplitContainer(
        #     content=[self.toga_box, self.web_box]
        # )
        self.main_window.content = toga.ScrollContainer(content=self.toga_box)
        self.main_window.show()

        self.widget_box.refresh()


def main():
    return HelloWorld()
