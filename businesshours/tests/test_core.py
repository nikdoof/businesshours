from datetime import datetime
import unittest

from businesshours import calc_business_hours


class TestCalcBusinessHours(unittest.TestCase):

        def run_tests(self, tests):
            for res, dt1, dt2 in tests:
                self.assertEqual(calc_business_hours(dt1, dt2,), res)

        def test_invalid_arguments(self):
            self.assertRaises(ValueError, calc_business_hours, datetime(2014, 1, 2), datetime(2014, 1, 1))

        def test_simple_day(self):
            self.run_tests([
                (60, datetime(2013, 8, 1, 9, 0, 0), datetime(2013, 8, 1, 9, 1, 0)),
                (600, datetime(2013, 8, 1, 9, 0, 0), datetime(2013, 8, 1, 9, 10, 0)),  # Simple multiday
                (36000, datetime(2013, 8, 1, 9, 0, 0), datetime(2013, 8, 2, 9, 0, 0)),
                (72000, datetime(2013, 8, 5, 9, 0, 0), datetime(2013, 8, 7, 9, 0, 0)),
            ])

        def test_multiday_out_of_hours(self):
            self.run_tests([
                (68400, datetime(2013, 8, 5, 9, 0, 0), datetime(2013, 8, 7, 0, 1, 0)),
                (72000, datetime(2013, 8, 5, 7, 0, 0), datetime(2013, 8, 7, 8, 0, 0)),
                (72000, datetime(2013, 8, 5, 6, 0, 0), datetime(2013, 8, 7, 8, 0, 0)),
            ])

        def test_weekend_single_day(self):
            self.run_tests([
                (0, datetime(2013, 8, 24, 9, 0, 0), datetime(2013, 8, 24, 9, 1, 0)),
                (0, datetime(2013, 8, 25, 9, 0, 0), datetime(2013, 8, 25, 9, 10, 0)),  # Multiday during weekend
                (0, datetime(2013, 8, 3, 7, 0, 0), datetime(2013, 8, 4, 9, 0, 0)),
            ])

        def test_weekend_early_monday(self):
            self.run_tests([
                (0, datetime(2014, 4, 6, 23, 59, 59), datetime(2014, 4, 7, 0, 0, 59)),
                (59, datetime(2014, 4, 6, 23, 59, 59), datetime(2014, 4, 7, 8, 0, 59)),
                (0, datetime(2014, 4, 4, 23, 59, 59), datetime(2014, 4, 5, 8, 0, 59))
            ])