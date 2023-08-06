from datetime import datetime, timedelta
import pytz
import typing
import copy

from rich.console import Console, ConsoleOptions, RenderResult
from rich.table import Table, Column
from rich.text import Text
from rich.style import Style
from rich.panel import Panel
from rich.color import Color
from rich.box import Box

DEFAULT_COLOR_MAP = [
    "rgb(0,140,255)",
    "rgb(0,175,255)",
    "rgb(0,215,255)",
    "rgb(0,255,255)",
    "rgb(0,255,195)",
    "rgb(0,255,145)",
    "rgb(0,255,0)",
    "rgb(75,255,0)",
    "rgb(125,255,0)",
    "rgb(175,255,0)",
    "rgb(215,255,0)",
    "rgb(255,255,0)",
    "rgb(255,215,0)",
    "rgb(255,175,0)",
    "rgb(255,135,95)",
    "rgb(255,95,0)",
    "rgb(255,0,0)",
]
DEFAULT_WEEK_DAYS = {
    "Mon": "Mon",
    "Tue": "Tue",
    "Wed": "Wed",
    "Thu": "Thu",
    "Fri": "Fri",
    "Sat": "Sat",
    "Sun": "Sun"
}
_DAYS_NAMES = list(DEFAULT_WEEK_DAYS.keys())

MYBOX: Box = Box(
    """\
┌─\x00┐
│ \x00│
├─\x00┤
│ \x00│
├─\x00┤
├─\x00┤
│ \x00│
└─\x00┘
"""
)

def convert_to_datetime(
    item: typing.Any
) -> datetime:
    if isinstance(item, datetime):
        return item
    elif isinstance(item, str):
        if item.isdigit():
            item = int(item)
    if isinstance(item, (float, int)):
        return datetime.fromtimestamp(item)
    else:
        raise TypeError()

def calculate_color(
    colors: list[Color], _min: int, _max: int, current: int
) -> Color:
    x = (current - _min) * (len(colors) - 1) / ((_max - _min) or 1)
    return colors[int(x)]

class TimezoneGuesser(dict[int, int]):
    """
        `TimezoneGuesser` allows to guess the timezone based on the input
        hours and amount of activity per each. The dictionnary should be
        looking like:
        ```py
        {   
            # Hour in the day as the key
            # Amount of activities found at this hour as the value
            0: 89,
            1: 57,
            2: 43,
            ...
            # And we stop at hour 23, DO NOT PUT HOUR 24
            23: 9
        }
        ```
    """
    _night_lenght_in_hours: int = 10
    _going_to_sleep_hour: int = 0

    @property
    def night_lenght_in_hours(self) -> int:
        return self._night_lenght_in_hours

    @night_lenght_in_hours.setter
    def night_lenght_in_hours(self, value: typing.Any) -> None:
        assert isinstance(value, int), "Night lenght value must be an `int`"
        assert 4 <= value <= 16, "Night lenght must be between `4` and `16`"
        self._night_lenght_in_hours = value

    @property
    def going_to_sleep_hour(self) -> int:
        return self._going_to_sleep_hour

    @going_to_sleep_hour.setter
    def going_to_sleep_hour(self, value: typing.Any) -> None:
        assert isinstance(value, int), "Sleeping hour value must be an `int`"
        assert 0 <= value <= 23, "Sleeping hour must be between `0` and `23`"
        self._going_to_sleep_hour = value

    def lowest_activity_hours(self) -> list[int]:
        """
            Returns the list of hours on which the activity is the lowest. The
            amount of hours returned is `self.night_lenght_in_hours`.
        """
        return sorted([
            key for key, value in sorted(
                self.items(),
                key=lambda items: items[1]
            )
        ][:self.night_lenght_in_hours])

    def has_gap(self, hours_list: list[int]) -> tuple[bool, int]:
        """
            Tells if the hour list contains a gap, which is a sign of someone 12h
            off UTC+00:00.
        """
        has_gap = False
        #   Here we are checking for a gap. Since all the timestamps should be on tz
        # UTC+00:00, some `hours_list`, instead of being [7, 8, 9, 10, 11, 12, 13, 14
        # 15, 16], could be [0, 1, 2, 3, 4, 19, 20, 21, 22, 23] and having an anormal
        # space between two hours (4 to 19 here).
        #   The gap is being detected by checking if the current hour added to half
        # of sleep time is lower than the next hour. If it is the case, we break.
        for index, hour in enumerate(hours_list):
            try:
                if has_gap:
                    break
                else:
                    has_gap = (hour + (self.night_lenght_in_hours / 2)) < hours_list[index + 1]
            except IndexError:
                index += 1
                break
        return has_gap, index

    def guess_tz(self) -> int:
        """
            Will guess the timezone, and will return it as an `int` that might
            be negative.
        """
        lowest_activity_hours = self.lowest_activity_hours()
        has_gap, index = self.has_gap(hours_list=lowest_activity_hours)

        #   Here we are adding 24 to the part before the gap ([0, 1, 2, 3, 4]), then
        # add it to the part after the gap ([19, 20, 21, 22, 23]), so we obtain a
        # list such as [19, 20, 21, 22, 23, 24, 25, 26, 27, 28], as a full night.
        on_48_hours = [
            *lowest_activity_hours[index:],
            *[n + 24 for n in lowest_activity_hours[:index]]
        ]

        return 24 - (on_48_hours[0] - self.going_to_sleep_hour)

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        yield Panel(f"Timezone guessed: {self.guess_tz()}", expand=False)

class WeekActivity(list[datetime]):
    """
        Prints out the activity off the input datetimes.
    """
    _colors: list[Color]
    _day_names: dict[str: str]

    @property
    def colors(self) -> list[Color]:
        return self._colors

    @colors.setter
    def colors(self, value: list[str, Color]) -> None:
        self._colors = [ color if isinstance(color, Color) else Color.parse(color)
                         for color in value ]

    @property
    def day_names(self) -> dict[str: str]:
        return self._day_names

    @day_names.setter
    def day_names(self, value: dict[str: str]) -> None:
        assert set(value.keys()) == set(_DAYS_NAMES), f"Keys of day names dict must be {_DAYS_NAMES}"
        assert all([isinstance(v, str) for v in value.values()]), "All values of day names must be `str`"
        self._day_names = value

    def edit_timezone(self, timezone: int = 0) -> None:
        delta = timedelta(hours=timezone)
        for index, item in enumerate(self):
            self[index] = item + delta

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        days: list[str] = _DAYS_NAMES
        empty_week_per_hour: dict[int: list[int]] = { hour: [ 0 for day in days ] for hour in range(24) }
        empty_week_per_days: dict[str: list[int]] = { day: [0] * 24 for day in days }
        for item in self:
            week_day = item.strftime("%a")
            empty_week_per_hour[item.hour][days.index(week_day)] += 1
            empty_week_per_days[week_day][item.hour] += 1

        all_hours: list[int] = []
        for day_activities in empty_week_per_hour.values():
            all_hours += day_activities
        min_hours = min(all_hours)
        max_hours = max(all_hours)

        all_days: list[int] = []
        for hour_activites in empty_week_per_days.values():
            all_days.append(sum(hour_activites))
        min_days = min(all_days)
        max_days = max(all_days)

        columns: list[Column] = []
        for day_name, activities in empty_week_per_days.items():
            style = Style(bgcolor=calculate_color(self.colors, min_days, max_days, sum(activities)))
            columns.append(Column(
                self._day_names[day_name],
                header_style=style,
                justify="center"
            ))

        activity_table = Table("  ", *columns, title="Activity table", caption="Made with Malfratools")

        for hour, activities in enumerate(empty_week_per_hour.values()):
            row = []
            for activity in activities:
                style = Style(bgcolor=calculate_color(self.colors, min_hours, max_hours, activity))
                row.append(Text(str(activity), style))
            activity_table.add_row(*[str(hour).zfill(2), *row])

        yield activity_table

# class Timeline(list[datetime]):
#     width: int = None
#     height: int = None

#     @property
#     def first_date(self) -> datetime:
#         return min(self)

#     @property
#     def last_date(self) -> datetime:
#         return max(self)
    
#     def __rich_console__(
#         self, console: Console, options: ConsoleOptions
#     ) -> RenderResult:
#         width = (self.width or options.max_width) - 27
#         height = self.height or (options.max_height - 3)

#         first_ts = self.first_date.timestamp()
#         last_ts = self.last_date.timestamp()
#         total_space = last_ts - first_ts
#         s_between_groups = total_space / height

#         border = first_ts + s_between_groups

#         groups: dict[datetime, list[datetime]] = {}
#         for date in sorted(self):
#             while True:
#                 if border not in groups:
#                     groups[border] = []
#                 if date.timestamp() <= border:
#                     groups[border].append(date)
#                     break
#                 else:
#                     border += s_between_groups
#         group_activites = [len(group) for group in groups.values()]
#         max_group_activies = max(group_activites)
#         min_group_activies = min(group_activites)

#         width -= len(str(max_group_activies))

#         rows: list[list[str, str, str]] = []
#         for group_base, group_activity in zip(groups.keys(), group_activites):
#             rows.append([
#                 datetime.fromtimestamp(group_base).strftime("%b %d %Y - %Hh"),
#                 str(group_activity),
#                 "=" * int(group_activity * width / max_group_activies)
#             ])

#         recap = Table(
#             "", "", "",
#             show_header=False
#         )
#         for row in rows:
#             recap.add_row(*row)

#         yield recap

class TimesAnalyzis(list[datetime]):
    colors = DEFAULT_COLOR_MAP

    def append_timestamp(
        self, *tss: tuple[typing.Any]
    ) -> None:
        for ts in tss:
            self.append(convert_to_datetime(item=ts))

    @property
    def earliest_time(self) -> datetime:
        return min(self)

    @property
    def latest_time(self) -> datetime:
        return max(self)

    @property
    def total_times(self) -> datetime:
        return len(self)

    def guess_timezone(
        self,
        night_lenght_in_hours: int = 10,
        going_to_sleep_hour: int = 0,
    ) -> TimezoneGuesser:
        tzgs = TimezoneGuesser([(hour, 0) for hour in range(24)])
        for time in self:
            tzgs[time.hour] += 1

        tzgs.night_lenght_in_hours = night_lenght_in_hours
        tzgs.going_to_sleep_hour = going_to_sleep_hour

        return tzgs

    def week_activity(
        self,
        timezone: int = 0,
        colors: list[str] = None,
        day_names: typing.Annotated[dict[str, str], 7] = None
    ) -> WeekActivity:
        datetimes = copy.deepcopy(list(self))
        new_datetimes: list[datetime] = []
        for date in datetimes:
            new_datetimes.append(date + timedelta(hours=timezone))

        result = WeekActivity(new_datetimes)
        result.colors = colors or self.colors
        result.day_names = day_names or DEFAULT_WEEK_DAYS

        return result

    # def timeline(
    #     self
    # ) -> Timeline:
    #     tml = Timeline()
    #     for date in self:
    #         tml.append(date)
    #     return tml

    def __rich_console__(
        self, console: Console, options: ConsoleOptions
    ) -> RenderResult:
        yield self.guess_timezone()
        yield self.week_activity()
        # yield self.timeline()