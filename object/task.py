class Task:
    def __init__(self, label: str, deadline: str, hoursToFinish: int, major: bool, credit: int, breakDown: bool, priority: int):
        self.__label = label
        self.__deadline = deadline
        self.__hoursToFinish = hoursToFinish
        self.__major = major
        self.__credit = credit
        self.__breakDown = breakDown
        self.__priority = priority

    def get_label(self):
        return self.__label

    def get_deadline(self):
        return self.__deadline

    def get_hoursToFinish(self):
        return self.__hoursToFinish

    def get_major(self):
        return self.__major

    def get_credit(self):
        return self.__credit

    def get_breakDown(self):
        return self.__breakDown

    def get_priority(self):
        return self.__priority

    def set_label(self, newLabel):
        self.__label = newLabel

    def set_deadline(self, newDeadline):
        self.__deadline = newDeadline

    def set_hoursToFinish(self, newHoursToFinish):
        self.__hoursToFinish = newHoursToFinish

    def set_major(self, newMajor):
        self.__major = newMajor

    def set_credit(self, newCredit):
        self.__credit = newCredit

    def set_breakDown(self, newBreakDown):
        self.__breakDown = newBreakDown

    def set_priority(self, newPriority):
        self.__priority = newPriority
