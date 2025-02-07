import calendar

def show_calendar(year, month):
    cal = calendar.TextCalendar()
    print(cal.formatmonth(year, month))

if __name__ == "__main__":
    year = int(input("表示する年を入力してください: "))
    month = int(input("表示する月を入力してください: "))
    show_calendar(year, month)