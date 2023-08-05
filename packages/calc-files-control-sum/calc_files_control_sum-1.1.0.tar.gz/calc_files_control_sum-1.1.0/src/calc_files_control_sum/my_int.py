"""реализация интернационализации.
Если что, я знаю про gettext"""
import csv


def _get_fields_by_names(csv_filename: str, column_names: [tuple, list], delimiter: str = ',') -> tuple:
    """Итератор, который возвращает за каждый вызов кортеж из полей csv файла, имена которых (первая строка),
    в виде строк, содержит последовательность field_names"""
    with open(csv_filename, mode='r', newline='') as csv_file:
        row_reader = csv.reader(csv_file, delimiter=delimiter)
        _b = True
        for _row in row_reader:
            if _b:
                column_indexes = tuple([_row.index(column_name) for column_name in column_names])
                _b = False
            yield tuple([_row[_index] for _index in column_indexes])


class Internationalization:
    """Моя реализация интернационализации. Если что, я знаю про gettext"""
    def __init__(self, csv_filename: str, lang: str, default_lang="EN"):
        self._filename = csv_filename
        self._lang = lang
        self._def_lang = default_lang     # язык по умолчанию
        # ключи-имена строк в файлах проекта. значения - содержимое строк на разных языках
        self._str_and_vals = dict()
        # заполнение словаря
        try:
            for fields in _get_fields_by_names(csv_filename, ("strID", lang.upper())):
                self._str_and_vals[fields[0]] = fields[1]
        except IndexError:
            pass
        except LookupError:
            pass
        except ValueError:
            pass
        else:
            return  # исключения не было!
        # было исключение, возможно задан неверный язык локализации
        self._str_and_vals.clear()
        # последняя попытка с языком по умолчанию
        for fields in _get_fields_by_names(csv_filename, ("strID", default_lang)):
            self._str_and_vals[fields[0]] = fields[1]

    def __call__(self, key: str) -> str:
        return self._str_and_vals[key]
