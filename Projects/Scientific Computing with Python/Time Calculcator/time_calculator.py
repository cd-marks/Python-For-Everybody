def add_time(start, duration, day = ''):
    # Set up variables and days list
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    next_day = ''
    nextday_count = 0

    # Split each element of the start time (Hour, Minute, and AM/PM)
    start_split = start.split(':')
    start_split[1] = start_split[1].split(' ')
    start_split = start_split + start_split[1]
    del start_split[1]
    
    # Establish initial values for hour, minute and AM/PM
    start_hour = int(start_split[0])
    start_minute = int(start_split[1])
    am_pm = start_split[2]  

    # Split each element of the duration period (Hour and Minute)
    dur_split = duration.split(':')
    dur_hour = int(dur_split[0])
    dur_minute = int(dur_split[1])

    # Calculate the new hour and minute by adding duration time to initial values
    new_hour = start_hour + dur_hour
    new_minute = start_minute + dur_minute

    # Handle AM/PM changes and calculate the number of days passed by tracking the
    # number of times the clock passes 12:00AM or 12:00PM
    if new_hour > 12:
        while (new_hour / 12) > 1:
            new_hour -= 12
            if am_pm == 'AM':
                am_pm = 'PM'
                next_day = ''
            elif am_pm == 'PM':
                am_pm = 'AM'
                next_day = '(next day)'
                nextday_count += 1

    # Calculate additional hour and day changes by tracking the number of times the # # clock passes 60 minutes
    if new_minute > 60:
        while (new_minute / 60) > 1:
            new_minute -= 60
            new_hour += 1
            if new_hour == 12:
                if am_pm == 'AM':
                    am_pm = 'PM'
                    next_day = ''
                elif am_pm == 'PM':
                    am_pm = 'AM'
                    next_day = '(next day)'
                    nextday_count += 1
    
    # Add a leading zero to minute times containing just one digit
    if new_minute < 10:
        new_minute = ('0' + str(new_minute))

    # Establish initial function output (just hour, minute and AM/PM)
    new_time = str(new_hour) + ':' + str(new_minute) + ' ' + am_pm

    # Determine additional function output based on the number of added days
    if nextday_count == 1:
        new_time = new_time + ' ' + next_day
    elif nextday_count > 1:
        new_time = new_time + ' (' + str(nextday_count) + ' days later)'
    
    # If a day of the week was passed into add_time, establish the initial day ,
    # calculate the new day of the week and establish function output based on the
    # number of added days
    if day:
        day = day.lower()
        start_day = day[0].upper() + day[1:]

        # Determine the starting day's position inside the week 
        for i in days:
            if start_day == i:
                start_day_index = days.index(i)
        
        # Calculate the new day's position in the week
        new_day_index = start_day_index + nextday_count

        # If the new day is positioned during a future week, account for that by subtracting 7 from new_day_index until its within the limits of the days list
        if new_day_index > 6:
            while (new_day_index / 6) > 1:
                new_day_index -= 7

        # Establish the new day of the week based on its index within days
        new_day = days[new_day_index]

        # Establish function output based on the number of days added
        if nextday_count == 1:
            new_time = str(new_hour) + ':' + str(new_minute) + ' ' + am_pm + ', ' + new_day + ' ' + next_day
        elif nextday_count > 1:
            new_time = str(new_hour) + ':' + str(new_minute) + ' ' + am_pm + ', ' + new_day + ' (' + str(nextday_count) + ' days later)'
        else:
            new_time = str(new_hour) + ':' + str(new_minute) + ' ' + am_pm + ', ' + new_day

    return new_time
