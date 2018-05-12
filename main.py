from random import randint

from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from interval_scheduling import Interval, interval_scheduling
from kivy.graphics import *
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App


class TaskListButton(ListItemButton):
    pass


class EDADisplay(BoxLayout):
    task_name_text_input = ObjectProperty()
    task_start_text_input = ObjectProperty()
    task_end_text_input = ObjectProperty()
    task_list = ObjectProperty()

    def __init__(self, **kwargs):
        super(EDADisplay, self).__init__(**kwargs)
        self.list_I = []
        self.max = 0
        self.myWidget = Widget(size=(100, 100))

    def add_task(self):
        task_full = (str(self.task_name_text_input.text) + " - " + str(self.task_start_text_input.text) + " - "
                     + str(self.task_end_text_input.text))

        if int(self.task_end_text_input.text) >= self.max:
            self.max = int(self.task_end_text_input.text) + 1

        self.task_list.adapter.data.extend([task_full])

        self.task_list._trigger_reset_populate()

        self.list_I.append(Interval(self.task_name_text_input.text, int(self.task_start_text_input.text),
                                    int(self.task_end_text_input.text)))

    def show_interval_more(self):
        self.list_I = interval_scheduling(self.list_I, self.max)
        self.size = Window.size
        self.add_widget(self.myWidget)

        with self.myWidget.canvas:
            aux_1 = 0
            for aux in self.list_I:
                Color(float(randint(0,9))/10, float(randint(0,9))/10, float(randint(0,9))/10, 1)
                Rectangle(pos=(aux_1, 0), size=(aux.finish-aux.start, 100))
                aux_1 = aux.finish-aux.start

    def show_interval_less(self, *args):
        pass


class EDADisplayApp(App):
    def build(self):
        return EDADisplay()


EDAApp = EDADisplayApp()
EDAApp.run()
