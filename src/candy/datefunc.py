
import datetime

def as_datetime(dt, format:str = None):
    if not isinstance(dt, str):
        return dt
    if not format:
        columns = dt.count(':')
        if '_' in dt:
            format = '%Y-%m-%d_%H:%M:%S' if columns >= 2 else ('%Y-%m-%d_%H:%M' if columns == 1 else '%Y-%m-%d_%H')
        elif ' ' in dt:
            format = '%Y-%m-%d %H:%M:%S' if columns >= 2 else ('%Y-%m-%d %H:%M' if columns == 1 else '%Y-%m-%d %H')
        else:
            format = '%Y-%m-%d'
    
    return datetime.datetime.strptime(dt, format)


def datetime_range(start, end, interval = datetime.timedelta(days = 1), reverse:bool = False, return_as_str:bool = True):
    start_tmp = as_datetime(start)
    end_tmp = as_datetime(end)
    start_dt = min(start_tmp, end_tmp)
    end_dt = max(start_tmp, end_tmp)

    if isinstance(interval, (int, float)):
        interval = datetime.timedelta(hours = interval)

    rangedelta = end_dt - start_dt
    ret = [start_dt + interval * n for n in range(rangedelta // interval + 1)]
    ret = [dt for dt in ret if dt >= start_dt and dt <= end_dt]

    reverse0 = start_tmp > end_tmp
    reverse = reverse ^ reverse0
    if reverse:
        ret = sorted(ret, reverse = True)
    if return_as_str:
        if interval.total_seconds() % (24 * 3600) == 0:
            return [dt.strftime('%Y-%m-%d') for dt in ret]
        elif interval.total_seconds() % 3600 == 0:
            return [dt.strftime('%Y-%m-%d_%H') for dt in ret]
        else:
            return [dt.strftime('%Y-%m-%d_%H:%M:%S') for dt in ret]
    else:
        return ret
    
if __name__ == '__main__':
    import unittest
    
    class TestFixtures(unittest.TestCase):
        def setUp(self):
            pass

        def tearDown(self):
            pass

        def test_as_datetime(self):
            self.assertEqual(datetime.datetime.strptime('2019-01-01', '%Y-%m-%d'), as_datetime('2019-01-01'))
            self.assertEqual(datetime.datetime.strptime('2019-01-01 10:20', '%Y-%m-%d %H:%M'), as_datetime('2019-01-01 10:20'))
            self.assertEqual(datetime.datetime.strptime('2019-01-01 10:20:30', '%Y-%m-%d %H:%M:%S'), as_datetime('2019-01-01 10:20:30'))
            self.assertEqual(datetime.datetime.strptime('2019-01-01_10:20', '%Y-%m-%d_%H:%M'), as_datetime('2019-01-01_10:20'))
            self.assertEqual(datetime.datetime.strptime('2019-01-01_10:20:30', '%Y-%m-%d_%H:%M:%S'), as_datetime('2019-01-01_10:20:30'))

        def test_datetime_range(self):
            self.assertEqual(datetime_range('2019-01-01', '2019-01-03'), ['2019-01-01', '2019-01-02', '2019-01-03'])
            self.assertEqual(datetime_range('2019-01-01', '2019-01-03', 12), ['2019-01-01_00', '2019-01-01_12', '2019-01-02_00', '2019-01-02_12', '2019-01-03_00'])
            self.assertEqual(datetime_range('2019-01-01', '2019-01-03', reverse = True), ['2019-01-03', '2019-01-02', '2019-01-01'])
            
    unittest.main()
