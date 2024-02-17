class TimeCalculator:

  def __init__(self,
               start_time: str,
               duration_time: str,
               current_day: str = ''):
    self.start_hours: int = int(start_time.split(':')[0])
    self.start_minutes: int = int(start_time.split(' ')[0].split(':')[1])
    self.duration_hours: int = int(duration_time.split(':')[0])
    self.duration_minutes: int = int(duration_time.split(':')[1])
    self.ampm: str = start_time.split(' ')[1].lower()
    self.current_day: str = current_day.lower()
    self.total_hours: int = 0
    self.total_minutes: int = 0
    self.days_number: int = 0

  def set_total_hours(self) -> None:
    self.total_hours += self.start_hours + self.duration_hours

  def set_total_minutes(self) -> None:
    self.total_minutes += self.start_minutes + self.duration_minutes

  def set_total_days(self) -> None:
    self.days_number = self.total_hours // 24

  def get_days_later_string(self) -> str:
    if self.days_number == 0:
      return ''

    if self.days_number == 1:
      return '(next day)'

    dayNumberStr: str = str(self.days_number)

    return '(' + dayNumberStr + ' days later)'

  def get_new_ampm(self) -> str:
    if self.ampm == 'am':
      return 'AM'

    return 'PM'

  def get_new_minutes(self) -> str:
    new_minutes = str(self.total_minutes)

    if self.total_minutes < 10:
      new_minutes = '0' + new_minutes

    return new_minutes

  def get_new_hours(self, hours: int) -> int:
    return hours % 24

  def get_adjusted_hours(self, hours: int) -> int:
    adjusted_hours: int = hours

    if adjusted_hours >= 12:
      self.adjust_days_and_ampm()

    if adjusted_hours > 12:
      adjusted_hours -= 12

    return adjusted_hours

  def get_new_day(self) -> str:
    weekdays: list = [
        'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday'
    ]
    current_day_index: int = weekdays.index(self.current_day)
    new_day: str = weekdays[(current_day_index + self.days_number) % 7]

    return new_day.capitalize()

  def adjust_hours_and_minutes(self) -> None:
    if self.total_minutes >= 60:
      self.total_hours += 1
      self.total_minutes -= 60

  def adjust_days_and_ampm(self) -> None:
    if self.ampm == 'am':
      self.ampm = 'pm'
    else:
      self.ampm = 'am'
      self.days_number += 1

  def is_empty(self, char: str) -> bool:
    return char == ''

  def new_time(
      self,
      hours: str,
      minutes: str,
      ampm: str,
      days_later_string,
  ) -> str:
    new_time: str = ''

    if not self.is_empty(self.current_day):
      day: str = self.get_new_day()

      new_time = hours + ':' + minutes + ' ' + ampm + ', ' + day
    else:
      new_time = hours + ':' + minutes + ' ' + ampm

    if not self.is_empty(days_later_string):
      new_time += ' ' + days_later_string

    return new_time

  def calculate(self) -> str:
    self.set_total_minutes()
    self.set_total_hours()
    self.adjust_hours_and_minutes()
    self.set_total_days()

    new_hours: int = self.get_new_hours(self.total_hours)
    adjusted_hours: int = self.get_adjusted_hours(new_hours)

    new_minutes: str = self.get_new_minutes()
    new_ampm: str = self.get_new_ampm()
    days_later_string: str = self.get_days_later_string()

    new_time: str = self.new_time(str(adjusted_hours), new_minutes, new_ampm,
                                  days_later_string)

    return new_time


def add_time(start, duration, current_day: str = '') -> str:
  timeCalculator = TimeCalculator(start, duration, current_day)
  new_time: str = timeCalculator.calculate()

  return new_time