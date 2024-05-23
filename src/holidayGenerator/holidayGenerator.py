class HolidayGenerator:
    def __init__(self, exchange):
        self.exchange = exchange

    def generate_holidays(self, year):
        raise NotImplementedError("generate_holidays() method must be implemented in subclasses")


class NYSEHolidayGenerator(HolidayGenerator):
    def generate_holidays(self, year):
        # Generate holidays for NYSE
        # ...
        pass


class NASDAQHolidayGenerator(HolidayGenerator):
    def generate_holidays(self, year):
        # Generate holidays for NASDAQ
        # ...
        pass


class LSEHolidayGenerator(HolidayGenerator):
    def generate_holidays(self, year):
        # Generate holidays for London Stock Exchange
        # ...
        pass

class NSEHolidayGenerator(HolidayGenerator):
    def generate_holidays(self, year):
        import pandas as pd
        from jugaad_data.holidays import holidays
        return pd.bdate_range(start=f'12/01/{year}', end=f'12/31/{year}', freq='C', holidays=holidays(year, 12))

# Example usage
generator = NYSEHolidayGenerator()
holidays = generator.generate_holidays(2022)
print(holidays)