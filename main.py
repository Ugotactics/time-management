import operator
import calendar
from datetime import datetime, timedelta

user1 = [{"task name": "Reading Engineering math", "time needed": 30,
          "sub-time needed": 4, "restricted time": 7, "importance": 8, "urgency": 8,
          "restrictions": "Goes to fellowship by 7pm every tuesdays and thursdays", "difficulty": 7},
         {"task name": "Learn Arabic", "time needed": 365, "sub-time needed": 1, "restricted time": 7,
          "restrictions": "Goes to fellowship by 7pm every tuesdays and thursdays", "importance": 7, "urgency": 5,
          "difficulty": 3},
         {"task name": "Do yoga", "time needed": 365, "sub-time needed": 1, "restricted time": 7,
          "restrictions": "Goes to fellowship by 7pm every tuesdays and thursdays", "importance": 7, "urgency": 6,
          "difficulty": 6},
         {"task name": "Read Atomic habit", "time needed": 365, "sub-time needed": 2, "restricted time": 7,
          "restrictions": "Goes to fellowship by 7pm every tuesdays and thursdays", "importance": 6, "urgency": 5,
          "difficulty": 4}
         ]

current_time = datetime.now()


class TimeManager:
    def __init__(self, time_needed, task_name, restricted_time, importance, urgency, difficulty):
        self.time_needed = time_needed
        self.task_name = task_name
        self.restricted_time = restricted_time
        self.importance = importance
        self.urgency = urgency
        self.difficulty = difficulty
        self.current_time = current_time
        self.time_lists = []

    def task_name(self):
        return self.task_name()

    def average_priority(self):
        priority = (self.difficulty + self.urgency + self.importance) / 3
        return priority

    def allocate_time(self):
        appended_time = current_time
        appended_time = '{:%H:%M:%S}'.format(appended_time)
        return appended_time

    def divide_excess_time(self, time_list):
        while time_list > 2:
            times = 2
            time_list -= times
            self.time_lists.append(times)
        if time_list <= 2:
            self.time_lists.append(time_list)


highest_priority_time = 0
tasks = []


def prioritize_task():
    sorted_user = sorted(user1, key=operator.itemgetter("urgency", "importance", "difficulty"), reverse=True)

    print(sorted_user)
    for i in sorted_user:
        task_object = TimeManager(i["time needed"], i["task name"], i["restricted time"],
                                  i["importance"], i["urgency"], i["difficulty"])
        tasks.append(task_object)
    for i in range(len(sorted_user)):
        print(tasks[i].task_name)


def current_time_format(x, allocated_time):
    current_timer = x + timedelta(hours=(allocated_time + (1 / 12)))
    return current_timer


def split_time():
    global current_time
    tasks_length = len(tasks)
    remaining = 24
    average_sum = 0
    all_tasks_with_time = []
    for i in range(tasks_length):
        average_sum += tasks[i].average_priority()
    for n in range(tasks_length):
        allocated_time = (tasks[n].average_priority() / average_sum) * remaining
        allocated_time = round(allocated_time)
        remaining -= 2
        tasks[n].divide_excess_time(allocated_time)
        all_tasks_with_time.append((tasks[n].task_name, tasks[n].time_lists))
        tasks[n].time_needed = allocated_time
    for i in all_tasks_with_time:
        for t in i[1]:
            if t:
                current_time = current_time_format(current_time, t)
            print(i[0], current_time)



prioritize_task()
split_time()
