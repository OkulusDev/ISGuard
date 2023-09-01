#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Intelligent Security Guard (ISG) - инструмент для шифрования, анализа сети, криптографии и работы с сетью
search_table.py - алгоритм шифрования таблицы поиска
Copyright (C) 2023  Okulus Dev
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>."""
table_en_start = str.maketrans('abcde', "01234")
table_en_end = str.maketrans('vwxyz', "56789")
table_ru_start = str.maketrans('абвгд', '01234')
table_ru_end = str.maketrans('ьъэюя', '56789')


def search_table(text: str, lang: str, table_type: str):
	if lang.lower() == 'ru':
		if table_type.lower() == 'end':
			return text.translate(table_ru_end)
		else:
			return text.translate(table_ru_start)
	else:
		if table_type.lower() == 'end':
			return text.translate(table_en_end)
		else:
			return text.translate(table_en_start)
