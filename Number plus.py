from kivy.lang import Builder
from kivymd.app import MDApp

class CounterApp(MDApp):
    def build(self):
        return Builder.load_string("""
MDBoxLayout:
    orientation: "vertical"
    padding: "12dp"
    spacing: "12dp"

    MDToolbar:
        title: "Counter App"
        md_bg_color: app.theme_cls.primary_color
        elevation: 10

    MDLabel:
        id: counter_label
        font_size: 24
        halign: "center"
        theme_text_color: "Secondary"

    MDRaisedButton:
        text: "Count"
        on_release: app.increment_counter()
""")

    def increment_counter(self):
        counter = self.root.ids.counter_label
        counter.text = str(int(counter.text) + 1)

CounterApp().run()
