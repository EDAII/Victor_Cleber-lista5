import time
import threading

from random import randint
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from interval_scheduling import Interval, interval_scheduling
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.graphics import Color


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
        self.myWidget = Widget(size=(0, 0), pos=(0, 0))

    def add_task(self):
        task_full = (str(self.task_name_text_input.text) + " - " + str(self.task_start_text_input.text) + " - "
                     + str(self.task_end_text_input.text))

        if int(self.task_end_text_input.text) >= self.max:
            self.max = int(self.task_end_text_input.text) + 1

        self.task_list.adapter.data.extend([task_full])

        self.task_list._trigger_reset_populate()

        self.list_I.append(Interval(self.task_name_text_input.text, int(self.task_start_text_input.text),
                                    int(self.task_end_text_input.text)))

    def show_interval_less(self, *args):
        pass

    def show_interval_more(self):
        self.remove_widget(self.myWidget)
        self.list_I = interval_scheduling(self.list_I, self.max)
        with self.myWidget.canvas:
            aux_1 = 0
            for aux in self.list_I:
                Color(float(randint(0,9))/10, float(randint(0,9))/10, float(randint(0,9))/10, 1)
                Rectangle(pos=(aux_1, 0), size=(aux.finish-aux.start, 100))
                aux_1 = aux.finish-aux.start

                # self.button = Button(background_color=[float(randint(0,9))/10, float(randint(0,9))/10, float(randint(0,9))/10, 1],
                #                      pos=(aux_1, 0), size=(aux.finish - aux.start, 100), text=aux.title)
                # self.add_widget(self.button)
                # self.list_buttons.append(self.button)

        self.add_widget(self.myWidget)

    def animate(self, instance):
        # create an animation object. This object could be stored
        # and reused each call or reused across different widgets.
        # += is a sequential step, while &= is in parallel
        animation = Animation(pos=(100, 100), t='out_bounce')
        animation += Animation(pos=(200, 100), t='out_bounce')
        animation &= Animation(size=(500, 500))
        animation += Animation(size=(100, 50))

        # apply the animation on the button, passed in the "instance" argument
        # Notice that default 'click' animation (changing the button
        # color while the mouse is down) is unchanged.
        animation.start(instance)



class EDADisplayApp(App):
    def build(self):
        return EDADisplay()


EDAApp = EDADisplayApp()
EDAApp.run()
