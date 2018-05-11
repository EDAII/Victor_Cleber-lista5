"""Add imports."""
import os
from interval_scheduling import count_sort


class Event:
    """Add events class to organizate the inverval."""

    def __init__(self, event_title, start, duration, finish):
        """Initialize the event class."""
        self.event_title = event_title
        self.start = start
        self.duration = duration
        self.finish = finish

    def __repr__(self):
        """Return developer representation."""
        yield str((self.event_title, self.time_start, self.time_finish))


def minimize_lateness(events_vector, max_length):
    """Add minimize latennes funciton."""
    vector_sorted = count_sort(events_vector, max_length)
    start_time = 0
    set_event = []
    for event in vector_sorted:
        event.start = start_time
        event.finish = start_time + event.duration
        start_time += event.duration
        set_event.append(event)
    return set_event


def add_event(list_events):
    """Add function can add events on list."""
    print("Write the name of event:")
    name = input()
    print("Write a start time:")
    start = int(input())
    print("Write a duration of the event")
    duration = int(input())
    print("Write a end time of the event")
    end = int(input())
    max_value = end
    list_events.append(Event(name, start, duration, end))
    return list_events, max_value


def print_events(list_events):
    """Add print function."""
    for event in list_events:
        print('=========================================')
        print("Name: {}\nStart: {}\nDurantion: {}\nFinish: {}".format(event.event_title, event.start, event.duration, event.finish))


if __name__ == '__main__':
    """Add main function."""
    max_value = 0
    list_events = []

    # Test with example slides in aprender.unb.br
    # list_events.append(Event('A', 1, 6, 3))
    # list_events.append(Event('B', 2, 8, 2))
    # list_events.append(Event('C', 3, 9, 1))
    # list_events.append(Event('D', 4, 9, 4))
    # list_events.append(Event('E', 5, 14, 3))
    # list_events.append(Event('F', 6, 15, 2))
    # max_value = 5

    while(1):
        print(max_value)
        print('=========================================')
        print("Choose an option:\n1: Input a task\n2: Minimizing lateness\n3: Print\n0: exit")
        ans = int(input())

        if ans == 1:
            list_events, temp_max = add_event(list_events)
            if temp_max >= max_value:
                max_value = temp_max
        if ans == 2:
            list_events = minimize_lateness(list_events, max_value)

        if ans == 3:
            print_events(list_events)

        if ans == 0:
            break
        print('=========================================')
        ans = input()
        os.system('cls' if os.name == 'nt' else 'clear')
