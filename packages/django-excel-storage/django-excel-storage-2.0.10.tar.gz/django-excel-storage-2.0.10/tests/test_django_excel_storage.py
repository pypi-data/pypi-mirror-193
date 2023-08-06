# -*- coding: utf-8 -*-

from django_excel_storage import ExcelStorage


class TestDjangoExcelStorageCommands(object):

    def setup_class(self):
        self.data1 = [{
            'Column 1': 1,
            'Column 2': 2,
        }, {
            'Column 1': 3,
            'Column 2': 4,
        }]
        self.data2 = [
            ['Column 1', 'Column 2'],
            [1, 2],
            [3, 4]
        ]
        self.data3 = [
            ['Column 1', 'Column 2'],
            [1, [2, 3]],
            [3, 4]
        ]

        self.content_type_csv = 'text/csv'
        self.content_type_xls = 'application/vnd.ms-excel'

        self.sheet_name1 = 'Sheet Name 1'
        self.sheet_name2 = 'Sheet Name 2'
        self.sheet_name3 = 'Sheet Name 3'

        self.sheet_data1 = {'Sheet Name 1': {'data': [['Column 1', 'Column 2'], [1, 2], [3, 4]]}}
        self.sheet_data2 = {'Sheet Name 1': {'data': [['Column 1', 'Column 2'], [1, [2, 3]], [3, 4]]}}

        self.headers = ['Column 1', 'Column 2', 'Column 3', 'Column 4', 'Column 5']
        self.mapping = {
            'field_key': 'Column 1',
            'data_key': 'Children 1',
            'next': {
                'field_key': 'Column 2',
                'data_key': 'Children 2',
                'next': {
                    'field_key': ['Column 3', 'Column 4'],
                    'data_key': 'Children 3',
                    'next': {
                        'field_key': 'Column 5',
                    }
                }
            }
        }
        self.rawdata = [{
            'Column 1': 'Value 1',
            'Column 11': 'Value 11',
            'Children 1': [{
                'Column 2': 'Value 2 Row 1',
                'Column 22': 'Value 22 Row 1',
                'Children 2': [{
                    'Column 3': 'Value 3',
                    'Column 4': 'Value 4',
                    'Children 3': {
                        'Column 5': 'Value 5',
                    }
                }]
            }, {
                'Column 2': 'Value 2 Row 2',
                'Column 22': 'Value 22 Row 2',
                'Children 2': [{
                    'Column 3': 'Value 3 Row 1',
                    'Column 4': 'Value 4 Row 1',
                    'Children 3': {
                        'Column 5': 'Value 5 Row 1',
                    }
                }, {
                    'Column 3': 'Value 3 Row 2',
                    'Column 4': 'Value 4 Row 2',
                    'Children 3': {
                        'Column 5': 'Value 5 Row 2',
                    }
                }]
            }]
        }]
        self.preprocesseddata = [['Value 1', [['Value 2 Row 1', [['Value 3', 'Value 4', [['Value 5']]]]], ['Value 2 Row 2', [['Value 3 Row 1', 'Value 4 Row 1', [['Value 5 Row 1']]], ['Value 3 Row 2', 'Value 4 Row 2', [['Value 5 Row 2']]]]]]]]

    def test_as_csv(self):
        csv1 = ExcelStorage(self.data1, 'my_data', force_csv=True, font='name SimSum')
        assert isinstance(csv1, ExcelStorage)

        csv2 = ExcelStorage(self.data2, 'my_data', force_csv=True, font='name SimSum')
        assert isinstance(csv2, ExcelStorage)

        csv3 = ExcelStorage(self.data3, 'my_data', force_csv=True, font='name SimSum')
        assert isinstance(csv3, ExcelStorage)

    def test_as_xls(self):
        xls1 = ExcelStorage(self.data1, 'my_data', font='name SimSum')
        assert isinstance(xls1, ExcelStorage)

        xls2 = ExcelStorage(self.data2, 'my_data', font='name SimSum')
        assert isinstance(xls2, ExcelStorage)

        # xls3 = ExcelResponse(self.data3, 'my_data', font='name SimSum')
        # assert isinstance(xls3, ExcelStorage)

        xls11 = ExcelStorage({
            self.sheet_name1: {'data': self.data1},
        }, 'my_data', font='name SimSum')
        assert isinstance(xls11, ExcelStorage)

        xls22 = ExcelStorage({
            self.sheet_name2: {'data': self.data2},
        }, 'my_data', font='name SimSum')
        assert isinstance(xls22, ExcelStorage)

    def test_as_row_merge_xls(self):
        xls1 = ExcelStorage(self.data1, 'my_data', font='name SimSum', merge_type='row_merge')
        assert isinstance(xls1, ExcelStorage)

        xls2 = ExcelStorage(self.data2, 'my_data', font='name SimSum', merge_type='row_merge')
        assert isinstance(xls2, ExcelStorage)

        xls3 = ExcelStorage(self.data3, 'my_data', font='name SimSum', merge_type='row_merge')
        assert isinstance(xls3, ExcelStorage)

        xls11 = ExcelStorage({
            self.sheet_name1: {'data': self.data1},
        }, 'my_data', font='name SimSum', merge_type='row_merge')
        assert isinstance(xls11, ExcelStorage)

        xls22 = ExcelStorage({
            self.sheet_name2: {'data': self.data2},
        }, 'my_data', font='name SimSum', merge_type='row_merge')
        assert isinstance(xls22, ExcelStorage)

        xls33 = ExcelStorage({
            self.sheet_name3: {'data': self.data3},
        }, 'my_data', font='name SimSum', merge_type='row_merge')
        assert isinstance(xls33, ExcelStorage)

    def test_as_list_row_merge_xls(self):
        xls1 = ExcelStorage(self.preprocesseddata, 'my_data', font='name SimSum', merge_type='list_row_merge')
        assert isinstance(xls1, ExcelStorage)

        xls2 = ExcelStorage(self.preprocesseddata, 'my_data', font='name SimSum', merge_type='list_row_merge', headers=self.headers)
        assert isinstance(xls2, ExcelStorage)

        xls11 = ExcelStorage({
            self.sheet_name1: {'data': self.preprocesseddata},
        }, 'my_data', font='name SimSum', merge_type='list_row_merge')
        assert isinstance(xls11, ExcelStorage)

        xls22 = ExcelStorage({
            self.sheet_name2: {'data': self.preprocesseddata},
        }, 'my_data', font='name SimSum', merge_type='list_row_merge', headers=self.headers)
        assert isinstance(xls22, ExcelStorage)

    def test_as_dict_row_merge_xls(self):
        xls1 = ExcelStorage(self.rawdata, 'my_data', font='name SimSum', merge_type='dict_row_merge', mapping=self.mapping)
        assert isinstance(xls1, ExcelStorage)

        xls2 = ExcelStorage(self.rawdata, 'my_data', font='name SimSum', merge_type='dict_row_merge', mapping=self.mapping, headers=self.headers)
        assert isinstance(xls2, ExcelStorage)

        xls11 = ExcelStorage({
            self.sheet_name2: {
                'data': self.rawdata,
                'mapping': self.mapping,
                'headers': self.headers,
            },
        }, 'my_data', font='name SimSum', merge_type='dict_row_merge')
        assert isinstance(xls11, ExcelStorage)

        xls22 = ExcelStorage({
            self.sheet_name2: {
                'data': self.rawdata,
                'mapping': self.mapping,
                'headers': self.headers,
            },
        }, 'my_data', font='name SimSum', merge_type='dict_row_merge', headers=self.headers)
        assert isinstance(xls22, ExcelStorage)
