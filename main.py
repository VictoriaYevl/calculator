from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.size = 260, 420

class Container(GridLayout):
    def clear(self):
        self.display.text = ''

    def dot(self):
        calc_input = self.display.text
        num_list = calc_input.split("+")

        if "+" in calc_input and "." not in num_list[-1]:
            calc_input = f'{calc_input}.'
            self.display.text = calc_input
        elif "." in calc_input:
            pass
        else:
            calc_input = f'{calc_input}.'
            self.display.text = calc_input


    def calculate(self, calculation):
        if calculation:
            try:
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Ошибка"

class CalcApp(MDApp):
    def __init__(self, **kwargs):
        self.title = "Калькулятор"

        super().__init__(**kwargs)
    def build (self):
        return Container()

if __name__=="__main__":
    CalcApp().run()