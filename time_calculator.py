class TimeCalculator:

  def __init__(self, start: str, duration: str, dayStr: str = ''):
    self.start_hours: int = int(start.split(':')[0])
    self.start_minutes: int = int(start.split(' ')[0].split(':')[1])
    self.duration_hours: int = int(duration.split(':')[0])
    self.duration_minutes: int = int(duration.split(':')[1])
    self.ampm: str = start.split(' ')[1].lower()
    self.dayStr: str = dayStr.lower()
    self.day_number: int = 0
    self.is_or_more_sixty_minutes: bool = False

  def convert_hours_to_days(self) -> None:
    while self.duration_hours >= 24:
      self.duration_hours -= 24
      self.day_number += 1

  def has_specified_day_of_week(self) -> bool:
    return self.dayStr != ''

  def get_days_later_string(self) -> str:
    if self.day_number == 1:
      return '(next day)'

    dayNumberStr: str = str(self.day_number)

    return '(' + dayNumberStr + ' days later)'

  def get_new_minutes(self) -> str:
    new_minutes: int = self.start_minutes + self.duration_minutes

    if new_minutes >= 60:
      new_minutes -= 60
      self.is_or_more_sixty_minutes = True

      if self.start_hours < 12 and self.start_hours + 1 >= 12:
        if self.ampm == 'pm':
          self.ampm = 'am'
          self.day_number += 1
        else:
          self.ampm = 'pm'

    return '0' + str(new_minutes) if new_minutes < 10 else str(new_minutes)

  def get_new_hours(self) -> str:
    new_hours: int = self.start_hours + self.duration_hours

    if self.is_or_more_sixty_minutes:
      new_hours += 1

    if new_hours >= 24:
      new_hours -= 24
      self.day_number += 1

    if new_hours > 12:
      new_hours -= 12
      if not self.is_or_more_sixty_minutes:
        if self.ampm == 'pm':
          self.ampm = 'am'
          self.day_number += 1
        else:
          self.ampm = 'pm'

    return str(new_hours)

  def get_new_ampm(self) -> str:
    return self.ampm.upper()

  def get_new_time(self) -> str:
    new_minutes: str = str(self.get_new_minutes())
    new_hours: str = str(self.get_new_hours())
    new_ampm: str = self.get_new_ampm()

    return new_hours + ':' + new_minutes + ' ' + new_ampm

  def get_new_day(self) -> str:
    weekdays: list = [
        'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday'
    ]
    current_day_index: int = weekdays.index(self.dayStr)
    new_day: str = weekdays[(current_day_index + self.day_number) % 7]

    return new_day.capitalize()

  def temp(self) -> str:
    self.convert_hours_to_days()

    new_time: str = self.get_new_time()
    new_time_info: str = new_time

    if self.has_specified_day_of_week():
      new_day: str = self.get_new_day()
      new_time_info += ', ' + new_day
    if self.day_number != 0:
      new_day_later: str = self.get_days_later_string()
      new_time_info += ' ' + new_day_later

    return new_time_info


def add_time(start, duration, dayStr: str = '') -> str:
  timeCalculator = TimeCalculator(start, duration, dayStr)
  new_time = timeCalculator.temp()

  return new_time
