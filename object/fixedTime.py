class FixedTime:
    def __init__(self, label: str, start: int, end: int, repeat: bool, weekDay):
        self.__label = label
        self.__start = start
        self.__end = end
        self.__repeat = repeat
        self.__weekDay = weekDay

    def get_label(self):
        return self.__label

    def get_start(self):
        return self.__start

    def get_end(self):
        return self.__end

    def get_repeat(self):
        return self.__repeat

    def get_weekDay(self):
        return self.__weekDay

    def set_label(self, newLabel):
        self.__label = newLabel

    def set_start(self, newStart):
        self.__start = newStart

    def set_end(self, newEnd):
        self.__end = newEnd

    def set_repeat(self, newRepeat):
        self.__repeat = newRepeat

    def set_weekDay(self, newWeekDay):
        self.__weekDay = newWeekDay