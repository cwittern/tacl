import csv
import io
import unittest

import tacl


class TaclTestCase (unittest.TestCase):

    def _create_csv (self, data):
        fh = io.StringIO(newline='')
        writer = csv.writer(fh)
        writer.writerow(tacl.constants.QUERY_FIELDNAMES)
        for row in data:
            writer.writerow(row)
        fh.seek(0)
        return fh

    def _get_rows_from_csv (self, fh):
        rows = []
        fh.seek(0)
        reader = csv.reader(fh)
        for row in reader:
            rows.append(tuple(row))
        return rows[1:]
