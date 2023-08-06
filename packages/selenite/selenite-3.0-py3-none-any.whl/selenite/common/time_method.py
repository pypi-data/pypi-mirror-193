import datetime


class TimeUtils:
    DATETIME_FULL = '%Y-%m-%d %H:%M:%S'

    DATETIME_SHORT = '%Y-%m-%d %H:%M'

    DATETIME_DATE = '%Y-%m-%d'

    DATETIME_TIME = '%H:%M:%S'

    UTC_DATETIME = '%Y-%m-%dT%H:%M:%S.000Z'

    @staticmethod
    def get_timestamp() -> int:
        return int(datetime.datetime.timestamp(datetime.datetime.now()))

    @staticmethod
    def get_utc_datetime() -> datetime.datetime:
        return datetime.datetime.utcnow()

    @staticmethod
    def format_datetime(dt: datetime.datetime, time_format: str) -> str:
        return dt.strftime(time_format)

    @staticmethod
    def get_current_date():
        return datetime.datetime.now().date().isoformat()

    @staticmethod
    def add_days(date_str, days):
        date = datetime.datetime.fromisoformat(date_str)
        new_date = date + datetime.timedelta(days=days)
        return new_date.date().isoformat()
