def weekday(n):
    weekdays = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
    return weekdays[(n%7)-1]
print(weekday(1))
print(weekday(4))
print(weekday(7))
print(weekday(20))