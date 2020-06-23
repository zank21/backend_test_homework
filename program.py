from datetime import datetime, timedelta


USD_RATE = 70
EURO_RATE = 78


class ErrorCurrency(Exception):
    def __init__(self, text):
        self.txt = text


class Record:
    def __init__(self, amount, comment, date=False):
        if not date:
            self.date = datetime.now().date()
        else:
            date_format = '%d.%m.%Y'
            self.date = datetime.strptime(date, date_format)
        self.amount = int(amount)
        self.comment = str(comment)


class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)
        print('Record Added')

    def get_today_stats(self):
        date_now = datetime.now().date()
        delta = timedelta(days=1)
        result = 0
        for record in self.records:
            if record.date < date_now + delta and record.date > date_now - delta:
                result += record.amount
        return result

    def get_week_stats(self):
        date_now = datetime.now().date()
        delta = timedelta(days=7)
        result = 0
        for record in self.records:
            if record.date > date_now - delta:
                result += record.amount
        return result


class CaloriesCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_stats(self):
        calories = super().get_today_stats()
        print(f'Колорий съедено сегодня: {calories}')

    def get_week_stats(self):
        calories = super().get_week_stats()
        print(f' Колорий съедено за последние 7 дней: {calories}')


class CashCalculator(Calculator):
    def __init__(self, limit):
        super().__init__(limit)

    def get_today_stats(self):
        cash = super().get_today_stats()
        usd = cash / USD_RATE
        euro = cash / EURO_RATE
        print(
            f'Сегодня потрачено: {cash} рублей, ИЛИ {usd} долларов, ИЛИ {euro} евро')

    def get_week_stats(self):
        cash = super().get_week_stats()
        usd = cash / USD_RATE
        euro = cash / EURO_RATE
        print(
            f'За послдение 7 дней потрачено: {cash} рублей, ИЛИ {usd} долларов, ИЛИ {euro} евро')

    def get_today_cash_remained(self, currency):
        if currency == 'rub':
            pass
        elif currency == 'usd':
            pass
        elif currency == 'eur':
            pass
        else:
            raise ErrorCurrency('Unknown currency')

if __name__ == "__main__":
    pass