def add_time(start, duration, day=''):

  # Destructuring parameters
  startTime, meridiem = start.split()
  startHours, startMinutes = startTime.split(':')
  durationHours, durationMinutes = duration.split(':')
  
  # Add the duration time to the start time
  # Get new hour, minutes and meridiem
  addHours, newMinutes = divmod(int(startMinutes) + int(durationMinutes), 60)
  totalHours = int(startHours) + int(durationHours) + addHours
  newMeridiem, newHours = divmod(totalHours, 12)
  
  if newHours == 0:
    newHours = '12'

  if newMinutes < 10:    
    newMinutes = '0' + str(newMinutes)

  if newMeridiem % 2 == 0:
    newMeridiem = meridiem
  elif meridiem == 'AM':
    newMeridiem = 'PM'
  else:
    newMeridiem = 'AM'    
  
  new_time = str(newHours) + ':' + str(newMinutes) + ' ' + str(newMeridiem)

  # Check if the result will be the next day or more than one day later
  if (meridiem == 'AM' and totalHours > 24 and totalHours < 48) or (meridiem == 'PM' and totalHours > 12 and totalHours < 36):
    new_time += getDayOfWeek(day, 1)
    new_time += ' (next day)'
  elif (meridiem == 'AM' and totalHours >= 48):
    new_time += getDayOfWeek(day, totalHours // 24)
    new_time += ' (' + str((totalHours // 24)) + ' days later)'
  elif (meridiem == 'PM' and totalHours >= 36):
    new_time += getDayOfWeek(day, (totalHours + 12) // 24)
    new_time += ' (' + str((totalHours + 12) // 24) + ' days later)'
  else:
    new_time += getDayOfWeek(day, 0)

  return new_time

def getDayOfWeek(day, daysLater):

  days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

  # Check if the output should display the day of the week of the result
  if day.title() in days:
    newDay = (days.index(day.title()) + daysLater) % 7
    return ', ' + days[newDay]

  return ''