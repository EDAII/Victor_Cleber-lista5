from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from interval_scheduling import Interval

class TaskListButton(ListItemButton):
    pass


class EDADisplay(BoxLayout):
    task_name_text_input = ObjectProperty()
    task_start_text_input = ObjectProperty()
    task_end_text_input = ObjectProperty()
    task_list = ObjectProperty()
    max = 0
    list = []

    def add_task(self):
        task_full = (str(self.task_name_text_input.text) + " - " + str(self.task_start_text_input.text) + " - "
                     + str(self.task_end_text_input.text))

        self.task_list.adapter.data.extend([task_full])

        self.task_list._trigger_reset_populate()

        list.append(Interval(self.task_name_text_input.text, self.task_start_text_input.text, self.task_end_text_input.text))

    def show_interval_more(self, *args):
        pass

    def show_interval_less(self, *args):
        pass


class EDADisplayApp(App):
    def build(self):
        return EDADisplay()


EDAApp = EDADisplayApp()
EDAApp.run()
