#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Intelligent Security Guard (ISG) - инструмент для шифрования, анализа сети, криптографии и работы с сетью
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
import sys
from modules.cryptography.caesar import encode_caesar, decode_caesar
from modules.cryptography.search_table import search_table

logo = '''
     _________ ______                     __
    /  _/ ___// ____/_  ______ __________/ /
    / / \\__ \\/ / __/ / / / __ `/ ___/ __  /
  _/ / ___/ / /_/ / /_/ / /_/ / /  / /_/ /
 /___//____/\\____/\\__,_/\\__,_/_/   \\__,_/
Intelligent Security Guard - (C) Okulus Dev 2023
'''


def main():
	print(logo)

	if len(sys.argv) > 1:
		if sys.argv[1] == '--help':
			print('''
Шифр Цезаря:
 --encode-caesar-ru <text> <step> - шифрование русского текста
 --encode-caesar-en <text> <step> - шифрование английского текста
 --decode-caesar-ru <text> <step> - дешифрование русского текста
 --decode-caesar-en <text> <step> - дешифрование английского текста

Таблица поиска:
 --search_table <text> <lang> <type>
				''')

		if sys.argv[1] == '--encode-caesar-ru':
			if len(sys.argv) > 3:
				result = encode_caesar(sys.argv[2], int(sys.argv[3]), 'ru')
				print(f'{sys.argv[2]} === {result}')
			else:
				print('Use: --encode-caesar-ru <text> <step>')
		elif sys.argv[1] == '--encode-caesar-en':
			if len(sys.argv) > 3:
				result = encode_caesar(sys.argv[2], int(sys.argv[3]), 'en')
				print(f'{sys.argv[2]} === {result}')
			else:
				print('Use: --decode-caesar-ru <text> <step>')
		elif sys.argv[1] == '--decode-caesar-ru':
			if len(sys.argv) > 3:
				result = decode_caesar(sys.argv[2], int(sys.argv[3]), 'ru')
				print(f'{sys.argv[2]} === {result}')
			else:
				print('Use: --decode-caesar-ru <text> <step>')
		elif sys.argv[1] == '--decode-caesar-en':
			if len(sys.argv) > 3:
				result = decode_caesar(sys.argv[2], int(sys.argv[3]), 'en')
				print(f'{sys.argv[2]} === {result}')
			else:
				print('Use: --decode-caesar-ru <text> <step>')
		elif sys.argv[1] == '--search_table':
			if len(sys.argv) > 4:
				result = search_table(sys.argv[2], sys.argv[3], sys.argv[4])
				print(f'{result}')
			else:
				print('Use: --search_table <text> <lang> <type>')
		else:
			print('Используйте с каким либо флагом (--help для справки)')


if __name__ == '__main__':
	main()
