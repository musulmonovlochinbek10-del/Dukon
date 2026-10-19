
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class DokonApp(App):
    def build(self):
        self.dona_narxi = 5000

        ekran = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=12
        )

        ekran.add_widget(Label(
            text="MINI DO'KON",
            font_size=28
        ))

        ekran.add_widget(Label(text="Ismingiz:"))
        self.ism = TextInput(
            hint_text="Ismingizni kiriting",
            multiline=False
        )
        ekran.add_widget(self.ism)

        ekran.add_widget(Label(
            text="Pulingiz (so'm):"
        ))
        self.pul = TextInput(
            hint_text="Masalan: 20000",
            input_filter="int",
            multiline=False
        )
        ekran.add_widget(self.pul)

        ekran.add_widget(Label(
            text="Mahsulot soni:"
        ))
        self.soni = TextInput(
            hint_text="Masalan: 3",
            input_filter="int",
            multiline=False
        )
        ekran.add_widget(self.soni)

        self.natija = Label(
            text="Narx: 1 dona = 5000 so'm",
            font_size=18
        )
        ekran.add_widget(self.natija)

        tugma = Button(
            text="XARIDNI HISOBLASH",
            size_hint_y=None,
            height=55
        )
        tugma.bind(on_press=self.hisobla)
        ekran.add_widget(tugma)

        return ekran

    def hisobla(self, tugma):
        try:
            pul = int(self.pul.text)
            soni = int(self.soni.text)

            if soni <= 0:
                self.natija.text = (
                    "Mahsulot sonini to'g'ri kiriting!"
                )
                return

            jami = self.dona_narxi * soni

            if jami < pul:
                self.natija.text = (
                    f"Xush kelibsiz, {self.ism.text}!\n"
                    f"Jami: {jami} so'm\n"
                    f"Qolgan pul: {pul - jami} so'm"
                )
            elif jami == pul:
                self.natija.text = (
                    f"Jami: {jami} so'm\n"
                    "Pul aynan yetadi!"
                )
            else:
                self.natija.text = (
                    f"Jami: {jami} so'm\n"
                    f"Yetmaydi: {jami - pul} so'm"
                )

        except ValueError:
            self.natija.text = (
                "Pul va mahsulot sonini kiriting!"
            )


if __name__ == "__main__":
    DokonApp().run()
