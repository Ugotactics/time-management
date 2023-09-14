import operator

user1 = [{"task name": "Reading Engineering math", "time needed": 30,
          "sub-time needed": 4, "restricted time": 7, "importance": 8, "urgency": 8,
          "restrictions": "Goes to fellowship by 7pm every tuesdays and thursdays"},
         {"task name": "Learn Arabic", "time needed": 365, "sub-time needed": 1, "restricted time": 7,
          "restrictions": "Goes to fellowship by 7pm every tuesdays and thursdays", "importance": 7, "urgency": 5},
         {"task name": "Do yoga", "time needed": 365, "sub-time needed": 1, "restricted time": 7,
          "restrictions": "Goes to fellowship by 7pm every tuesdays and thursdays", "importance": 7, "urgency": 6},
         {"task name": "Read Atomic habit", "time needed": 365, "sub-time needed": 2, "restricted time": 7,
          "restrictions": "Goes to fellowship by 7pm every tuesdays and thursdays", "importance": 6, "urgency": 5}
         ]


class TimeManager:
    def __init__(self, deadline, task_name, restricted_time, importance, urgency):
        self.deadline = deadline
        self.task_name = task_name
        self.restricted_time = restricted_time
        self.importance = importance
        self.urgency = urgency

    def task_name(self):
        return self.task_name()


highest_priority_time = 0
tasks = []


def prioritize_task():
    sorted_user = sorted(user1, key=operator.itemgetter("urgency", "importance"), reverse=True)

    print(sorted_user)
    for i in sorted_user:
        task_object = TimeManager(i["time needed"], i["task name"], i["restricted time"], i["importance"], i["urgency"])
        tasks.append(task_object)
    for i in range(len(sorted_user)):
        print(tasks[i].task_name)


prioritize_task()
