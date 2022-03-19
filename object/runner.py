from object.user import User
from object.task import Task
from object.fixedTime import FixedTime


if __name__ == '__main__':
    user1 = User("Wenhuihu@buffalo.edu", "sese112233")
    print(user1.get_email())
    user1.add_task(Task("Lab 10 (CSE306)", "03/07/2022 11:59", 3, True, 4, False, 2))
    user1.add_task(Task("Interview", "03/05/2022 11:30", 4, True, 3, False, 1))
    user1.add_task(Task("Interview google", "03/07/2022 19:30", 4, True, 3, False, 1))
    user1.add_task(Task("Interview google12", "03/05/2022 09:30", 4, True, 3, False, 1))
    user1.sort_task()
    tasks = user1.get_task()
    for task in tasks:
        #print(task.get_label())
        print(task.get_deadline())
