import datetime as dt
import calendar


class UtilsClass:
    def __init__(self):
        self.today = dt.date.today()
        self.__year = ''
        self.__month = ''
        self.__dayName = ''
        self.make()

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__month

    @property
    def dayName(self):
        return self.__dayName

    def convertDayOfWeek(self, jaWeekName):
        weekList = {
            '月': 'Monday',
            '火': 'Tuesday',
            '水': 'Wednesday',
            '木': 'Thursday',
            '金': 'Friday',
            '土': 'Saturday',
            '日': 'Sunday'
        }
        return weekList[jaWeekName]

    def make(self):
        self.__year = self.today.year
        self.__dayName = calendar.day_name[self.today.weekday()]
        if self.today.month < 10:
            month = f'0{self.today.month}'
        else:
            month = self.today.month
        self.__month = month
