import unittest

from speciallecture.CSVPrinter import CSVPrinter

class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        printer = CSVPrinter("sample.csv")
        line = printer.read()
        print(line)
        self.assertEqual(3, len(line))

"""
Code Smellのプログラム
class TestCSVPrinter(unittest.TestCase):
    def test_read(self):
        #Magic Number / Magic String (意味不明な定数)
        file_name = "sample.csv"
        #わざと不要な変数を増やす
        expected_line_count = 3
        printer_object = CSVPrinter(file_name)
        #わざと同じ処理を何度も書く
        line1 = printer_object.read()
        line2 = printer_object.read()
        line3 = printer_object.read()

        print("読み込んだ結果:")
        print(line1)
        print(line2)
        print(line3)

        #わざと条件分岐を増やす
        if line1 is not None:
            if len(line1) == expected_line_count:
                result = True
            else:
                result = False
        else:
            result = False
        #Assertion Obscurity
        self.assertEqual(True, result)
"""