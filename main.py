import time
import threading
from random import randint

from interval_scheduling import Interval, interval_scheduling
from scheduling_to_minimize_maximum_lateness import Event, minimize_lateness

from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.animation import Animation
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

buildKV = Builder.load_file("edadisplay.kv")


class ListButtons:
    def __init__(self, button, pos_x, size_x):
        self.button = button
        self.pos_x = pos_x
        self.size_x = size_x

    def __repr__(self):
        return str((self.button, self.pos_x, self.size_x))


class TaskListButton(ListItemButton):
    pass


class EDADisplayMore(Screen):
    task_name_text_input = ObjectProperty()
    task_start_text_input = ObjectProperty()
    task_end_text_input = ObjectProperty()
    task_list = ObjectProperty()

    def __init__(self, **kwargs):
        super(EDADisplayMore, self).__init__(**kwargs)
        self.list_I = []
        self.max = 0
        self.myWidget = Widget()
        self.list_buttons = []
        self.button = Button()

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
        self.remove_widget(self.myWidget)
        self.myWidget = Widget()
        self.size = Window.size

        self.list_I = interval_scheduling(self.list_I, self.max)

        aux_1 = 0
        aux_2 = 0
        for aux in self.list_I:
            self.button = Button(text=aux.title, pos=(aux_2, 200), size=(100, 100), font_size=12,
                                 background_color=[float(randint(0, 9)) / 10, float(randint(0, 9)) / 10,
                                                   float(randint(0, 9)) / 10, 1])

            self.myWidget.add_widget(self.button)
            self.list_buttons.append(ListButtons(self.button, aux_1, (aux.finish - aux.start)*self.size[0]/24))
            aux_1 = aux_1 + (aux.finish - aux.start)*self.size[0]/24
            aux_2 = aux_2 + 100

        print(self.list_buttons)
        self.add_widget(self.myWidget)
        self.animetionstart()

    def animetionstart(self):
        t = threading.Thread(target=self.animation)  # initiate the thread
        t.daemon = True  # daemon thread so it terminates when stopping the main thread
        t.start()

    def animation(self):
        for these_labels in self.list_buttons:
            anim = Animation(x=these_labels.pos_x, y=0, size=(these_labels.size_x, 100), t='in_quad')
            anim.start(these_labels.button)
            time.sleep(1.5)


# The ScreenManager controls moving between screens
screen_manager = ScreenManager()

# Add the screens to the manager and then supply a name
# that is used to switch screens
screen_manager.add_widget(EDADisplayMore(name="edadisplaymore"))
screen_manager.add_widget(EDADisplayLess(name="edadisplayless"))

class EDADisplayApp(App):
    def build(self):
        return screen_manager

EDAApp = EDADisplayApp()
EDAApp.run()
