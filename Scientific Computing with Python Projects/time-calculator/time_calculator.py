def add_time(start, duration, day=''):
  days = 0
  week = ('Monday',
         'Tuesday',
         'Wednesday',
         'Thursday',
         'Friday',
         'Saturday',
         'Sunday')
  
  #conver first time to ints and 24hr
  t1, mid = start.split(' ')
  h1, m1 = t1.split(":")
  h1 = int(h1)
  m1 = int(m1)
  if mid=="PM":
    h1 += 12
  
  #convert second time to ints
  h2, m2 = duration.split(":")
  h2 = int(h2)
  m2 = int(m2)
  
  #add the time
  h_sum = h1+h2
  m_sum = m1+m2
  
  #rollover hours
  h_sum += m_sum // 60 
  m_sum %= 60
  
  #rollover days
  days = h_sum //24
  h_sum %= 24
  
  #AM or PM
  new_mid = "PM"
  if h_sum > 12:
    h_sum -= 12
  elif h_sum < 12:
    new_mid = "AM"
  if h_sum == 0:
    h_sum = 12
  
  #format new time
  new_time = f"{h_sum}:{m_sum:02} {new_mid}"
  #determine day of Week
  if day:
    day = day.title()
    i = week.index(day)
    new_day = (i+days)%7
    new_time += f", {week[new_day]}"

  #was it more than one day?
  if days:
    if days > 1:
      new_time += f" ({days} days later)"
    else:
      new_time += " (next day)"
  return new_time