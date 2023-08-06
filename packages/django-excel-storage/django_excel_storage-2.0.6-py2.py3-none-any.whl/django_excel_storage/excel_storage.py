# -*- coding:utf-8 -*-

import datetime

from django.core.files.storage import default_storage
from django.db.models.query import QuerySet
from django_excel_base import (BytesIO, StringIO, as_csv, as_dict_row_merge_xls, as_list_row_merge_xls,
                               as_row_merge_xls, as_xls, is_py2)
from django_six import Support_ValuesQuerySet, ValuesQuerySet


# Min (Max. Rows) for Widely Used Excel
# http://superuser.com/questions/366468/what-is-the-maximum-allowed-rows-in-a-microsoft-excel-xls-or-xlsx
EXCEL_MAXIMUM_ALLOWED_ROWS = 65536
# Column Width Limit For ``xlwt``
# https://github.com/python-excel/xlwt/blob/master/xlwt/Column.py#L22
EXCEL_MAXIMUM_ALLOWED_COLUMN_WIDTH = 65535


def __init__(self, data, output_name='excel_data', format='%Y%m%d%H%M%S', headers=None, force_csv=False, encoding='utf-8-sig', font='', sheet_name='Sheet 1', blanks_for_none=True, auto_adjust_width=True, min_cell_width=1000, vert=0x01, horz=0x01, row_merge=False, list_row_merge=False, dict_row_merge=False, mapping=None):
    self.data = data
    self.output_name = output_name
    self.format = format
    self.headers = headers
    self.force_csv = force_csv
    self.encoding = encoding
    self.font = font
    self.sheet_name = sheet_name
    self.blanks_for_none = blanks_for_none
    self.auto_adjust_width = auto_adjust_width
    self.min_cell_width = min_cell_width
    self.file_ext = None
    # VERT_TOP     = 0x00    顶端对齐
    # VERT_CENTER  = 0x01    居中对齐（垂直方向上）
    # VERT_BOTTOM  = 0x02    底端对齐
    # HORZ_LEFT    = 0x01    左端对齐
    # HORZ_CENTER  = 0x02    居中对齐（水平方向上）
    # HORZ_RIGHT   = 0x03    右端对齐
    self.vert = vert
    self.horz = horz
    self.mapping = mapping

    if not dict_row_merge:
        if not isinstance(self.data, dict):
            self.data = {self.sheet_name: self.data}

        # Make sure we've got the right type of data to work with
        # ``list index out of range`` if data is ``[]``
        valid_data = True
        for sheet_name, sheet_data in self.data.items():
            if Support_ValuesQuerySet and isinstance(sheet_data, ValuesQuerySet):
                sheet_data = list(sheet_data)
            elif isinstance(sheet_data, QuerySet):
                sheet_data = list(sheet_data.values())
            if not hasattr(sheet_data, '__getitem__'):
                valid_data = False
                break
            if isinstance(sheet_data[0], dict):
                if headers is None:
                    headers = list(sheet_data[0].keys())
                sheet_data = [[row[col] for col in headers] for row in sheet_data]
                sheet_data.insert(0, headers)
            if not hasattr(sheet_data[0], '__getitem__'):
                valid_data = False
                break
            self.data[sheet_name] = sheet_data
        assert valid_data is True, 'ExcelStorage requires a sequence of sequences'

    self.output = StringIO() if is_py2 else BytesIO()
    if row_merge:
        _, file_ext = (self.as_row_merge_xls, 'xls')
    elif list_row_merge:
        _, file_ext = (self.as_list_row_merge_xls, 'xls')
    elif dict_row_merge:
        _, file_ext = (self.as_dict_row_merge_xls, 'xls')
    else:
        # Excel has a limit on number of rows; if we have more than that, make a csv
        use_xls = True if len(self.data) <= self.EXCEL_MAXIMUM_ALLOWED_ROWS and not self.force_csv else False
        _, file_ext = (self.as_xls, 'xls') if use_xls else (self.as_csv, 'csv')
    self.output.seek(0)

    self.file_ext = file_ext


def save(self):
    file_name_ext = '_{0}'.format(datetime.datetime.now().strftime(self.format)) if self.format else ''
    final_file_name = ('%s%s.%s' % (self.output_name, file_name_ext, self.file_ext)).replace('"', '\"')

    if default_storage.exists(final_file_name):
        default_storage.delete(final_file_name)
    default_storage.save(final_file_name, self.output)

    return final_file_name


clsdict = {
    'EXCEL_MAXIMUM_ALLOWED_ROWS': EXCEL_MAXIMUM_ALLOWED_ROWS,
    'EXCEL_MAXIMUM_ALLOWED_COLUMN_WIDTH': EXCEL_MAXIMUM_ALLOWED_COLUMN_WIDTH,
    '__init__': __init__,
    'as_xls': as_xls,
    'as_row_merge_xls': as_row_merge_xls,
    'as_list_row_merge_xls': as_list_row_merge_xls,
    'as_dict_row_merge_xls': as_dict_row_merge_xls,
    'as_csv': as_csv,
    'save': save,
}


ExcelStorage = type('ExcelStorage', (object, ), clsdict)
