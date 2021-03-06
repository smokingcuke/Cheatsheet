import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('python', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'python'
meta = {
	'title': 'Python3 Cheatsheet',
	'description': 'String Methods · Random Module · File Methods · List Methods · Sets · Dictionary Methods · Math · Powers & Logarithms · Trigonometry · File Attributes · Numbers',
	'keywords': 'python2, python3, python, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/Python/',

	'opengraph_title': 'Python Cheatsheet',
	'opengraph_description': 'String Methods · Random Module · File Methods · List Methods · Sets · Dictionary Methods · Math · Powers & Logarithms · Trigonometry · File Attributes · Numbers',
	'opengraph_image': 'opengraph_python.png',
	'opengraph_url': 'https://www.cheatsheet.wtf/python/',

	'twitter_title': 'Python Cheatsheet',
	'twitter_description': 'String Methods · Random Module · File Methods · List Methods · Sets · Dictionary Methods · Math · Powers & Logarithms · Trigonometry · File Attributes · Numbers',
	'twitter_image': 'twitter_card_python.png',
}
information = {
	'tool': 'Python',
	'title': 'Python Cheatsheet',
	'subtitle': 'This site is a reference for Python',
	'description': 'Python started as a hobby project by Guido Van Rossum and was first released in 1991, as a successor to the ABC programming language. Python\'s design philosophy emphasizes code readability with its notable use of significant whitespace. It aims to help programmers write clear, logical code for small and large-scale projects. Popular frameworks include Django, Flask, Numpy, Scipy',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Python',
			[
				helper.characteristics.get('general-purpose'),
				helper.characteristics.get('object-oriented-programming'),
				helper.characteristics.get('web-development'),
				helper.characteristics.get('scripting-language'),
				helper.characteristics.get('compiled-language'),
			])
	],
	'topic_uris': [
		'general-purpose',
		'object-oriented-programming',
		'web-development',
		'scripting-language',
		'compiled-language',
	],
}
general_info_text = ''
general_info_text_lead = ''
general_info_links = {}
general_info = [
]
general_info_flag = False
see_also = [
	{
	},
]
code_cards = [{
}]
# TODO: Make regex for links (find links at: https://overapi.com/jquery)
cheatsheet = [
	{
		'heading': helper.set_folder('String Methods'),
		'subtitle': '',
		'description': 'Used to manipulate or retrieve information on strings',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '5eee9467c27e44deaec60e1a03aac120',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('cb45cbb007be47149cbd5404f31be46d')[0]),
					'flag': helper.set_entry_command_string('capitalize()'),
					'description': [
						Markup('Return a copy of the string with its first character capitalized and the rest lowercased'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.capitalize',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6b9143367c6a4ff0a3699c2c5554c327')[0]),
					'flag': helper.set_entry_command_string('center(width[, fillchar])'),
					'description': [
						Markup('Return centered in a string of length width. Padding is done using the specified fillchar (default is a space)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.center',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a54fa56129974f12a3d1cc6aa43fb84d')[0]),
					'flag': helper.set_entry_command_string('count(sub[, start[, end]])'),
					'description': [
						Markup('Return the number of non-overlapping occurrences of substring sub in the range [start, end]'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.count',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f2373c3653f04483a11141276d3a7fec')[0]),
					'flag': helper.set_entry_command_string('decode'),
					'description': [
						Markup('Decodes the string using the codec registered for encoding'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.decode',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8660899f357949aca51bcff26a25c720')[0]),
					'flag': helper.set_entry_command_string('encode([encoding[, errors]])'),
					'description': [
						Markup('Return an encoded version of the string.  Default encoding is the current default string encoding'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.encode',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1ee34d1fb22b49d082019a337c72653b')[0]),
					'flag': helper.set_entry_command_string('endswith(suffix[, start[, end]])'),
					'description': [
						Markup('Return True if the string ends with the specified suffix, otherwise return False'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.endswith',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('eb3e05977d34467f8a98d99db5f71ba0')[0]),
					'flag': helper.set_entry_command_string('expandtabs([tabsize])'),
					'description': [
						Markup('Return a copy of the string where all tab characters are replaced by one or more spaces, depending on the current column and the given tab size'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.expandtabs',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('69eb80de5e434a6e9dc770116be35547')[0]),
					'flag': helper.set_entry_command_string('find(sub[, start[, end]])'),
					'description': [
						Markup('Return the lowest index in the string where substring sub is found, such that sub is contained in the slice s[start:end]'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.find',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f3763a0353cf4968a3787bd5a7464cc1')[0]),
					'flag': helper.set_entry_command_string('format(*args, **kwargs)'),
					'description': [
						Markup('Perform a string formatting operation'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.format',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1d061af159b94d779f5a914e1b483b09')[0]),
					'flag': helper.set_entry_command_string('index(sub[, start[, end]])'),
					'description': [
						Markup('Like find(), but raise ValueError when the substring is not found'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.index',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('03c787ab3f9a46f1ac8d4cf1ebf23293')[0]),
					'flag': helper.set_entry_command_string('isalnum()'),
					'description': [
						Markup('Return true if all characters in the string are alphanumeric and there is at least one character, false otherwise'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.isalnum',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dd96d06fb1ec4441b1bc12f833bdf5ec')[0]),
					'flag': helper.set_entry_command_string('isalpha()'),
					'description': [
						Markup('Return true if all characters in the string are alphabetic and there is at least one character, false otherwise'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.isalpha',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f53c42d71c584313bc40e2b0ffe314e0')[0]),
					'flag': helper.set_entry_command_string('isdigit()'),
					'description': [
						Markup('Return true if all characters in the string are digits and there is at least one character, false otherwise'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.isdigit',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a72e60b975084f49990c4cdb50a96f67')[0]),
					'flag': helper.set_entry_command_string('islower()'),
					'description': [
						Markup('Return true if all cased characters in the string are lowercase and there is at least one cased character, false otherwise'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.islower',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d2baf4108d294b12bb8295fe62971ca1')[0]),
					'flag': helper.set_entry_command_string('isspace()'),
					'description': [
						Markup('Return true if there are only whitespace characters in the string and there is at least one character, false otherwise'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.isspace',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('defefbed482d4b38bc8397c0d20ea215')[0]),
					'flag': helper.set_entry_command_string('istitle()'),
					'description': [
						Markup('Return true if the string is a titlecased string and there is at least one character, for example uppercase characters may only follow uncased characters and lowercase characters only cased ones'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.istitle',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('63374df5f5f34690a25b1e49df138648')[0]),
					'flag': helper.set_entry_command_string('isupper()'),
					'description': [
						Markup('Return true if all cased characters in the string are uppercase and there is at least one cased character, false otherwise'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.isupper',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3addc4aa9798469da8fe4887b5ef98e6')[0]),
					'flag': helper.set_entry_command_string('join(iterable)'),
					'description': [
						Markup('Return a string which is the concatenation of the strings in the iterable iterable'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.join',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8cc2742bcf8d489d9be9bae15040b878')[0]),
					'flag': helper.set_entry_command_string('ljust(width[, fillchar])'),
					'description': [
						Markup('Return the string left justified in a string of length width'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.ljust',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3e92c5bac33843b2ad828001f445dcdf')[0]),
					'flag': helper.set_entry_command_string('lower()'),
					'description': [
						Markup('Return a copy of the string converted to lowercase'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.lower',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8883a831dd694e17b993903e8b2ddfdf')[0]),
					'flag': helper.set_entry_command_string('lstrip([chars])'),
					'description': [
						Markup('Return a copy of the string with leading characters removed'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.lstrip',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('95b92854dcb44af7b5d75a86412bf82e')[0]),
					'flag': helper.set_entry_command_string('partition(sep)'),
					'description': [
						Markup('Split the string at the first occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.partition',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('945c4bb45d6b49e3adee5fd0be4053d0')[0]),
					'flag': helper.set_entry_command_string('replace(old, new[, count])'),
					'description': [
						Markup('Return a copy of the string with all occurrences of substring old replaced by new'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.replace',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f9d17e739ded46b59acd2a9315dbfe74')[0]),
					'flag': helper.set_entry_command_string('rfind(sub[, start[, end]])'),
					'description': [
						Markup('Return the highest index in the string where substring sub is found, such that sub is contained within s[start:end]'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.rfind',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0afa40818a4c49babf27c4c5d723c901')[0]),
					'flag': helper.set_entry_command_string('rindex(sub[, start[, end]])'),
					'description': [
						Markup('Like rfind() but raises ValueError when the substring sub is not found'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.rindex',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f44181f79d3343f2919a6f15f5553d19')[0]),
					'flag': helper.set_entry_command_string('rjust(width[, fillchar])'),
					'description': [
						Markup('Return the string right justified in a string of length width'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.rjust',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1e79c7a98847408983009985c1f02d0a')[0]),
					'flag': helper.set_entry_command_string('rpartition(sep)'),
					'description': [
						Markup('Split the string at the last occurrence of sep, and return a 3-tuple containing the part before the separator, the separator itself, and the part after the separator'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.rpartition',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bcc15a3f336c4d29a25b1729ff7d175d')[0]),
					'flag': helper.set_entry_command_string('rsplit([sep[, maxsplit]])'),
					'description': [
						Markup('Return a list of the words in the string, using sep as the delimiter string'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.rsplit',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1d0274ab74764049ad038c302107dd6b')[0]),
					'flag': helper.set_entry_command_string('rstrip([chars])'),
					'description': [
						Markup('Return a copy of the string with trailing characters removed'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.rstrip',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b38b63f50b4b49f382b3ba8831c9ab4c')[0]),
					'flag': helper.set_entry_command_string('split([sep[, maxsplit]])'),
					'description': [
						Markup('Return a list of the words in the string, using sep as the delimiter string'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.split',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('caef72af15d246d7a28df3c2e56d50fa')[0]),
					'flag': helper.set_entry_command_string('splitlines([keepends])'),
					'description': [
						Markup('Return a list of the lines in the string, breaking at line boundaries'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.splitlines',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('72a18d16121b4258a87f0e1e51e40084')[0]),
					'flag': helper.set_entry_command_string('startswith(prefix[, start[, end]])'),
					'description': [
						Markup('Return True if string starts with the prefix, otherwise return False'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.startswith',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3b79be4a9915415ba13fcf345b8f1a0c')[0]),
					'flag': helper.set_entry_command_string('strip([chars])'),
					'description': [
						Markup('Return a copy of the string with the leading and trailing characters removed'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.strip',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1999ae2403554608930dd58045490a97')[0]),
					'flag': helper.set_entry_command_string('swapcase'),
					'description': [
						Markup('Return a copy of the string with uppercase characters converted to lowercase and vice versa'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.swapcase',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d700c622fe4f460ea25bfd3869ff0dee')[0]),
					'flag': helper.set_entry_command_string('title()'),
					'description': [
						Markup('Return a titlecased version of the string where words start with an uppercase character and the remaining characters are lowercase'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.title',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9ecf3f9e24404198881bee7758857f0d')[0]),
					'flag': helper.set_entry_command_string('translate(table[, deletechars])'),
					'description': [
						Markup('Return a copy of the string where all characters occurring in the optional argument deletechars are removed, and the remaining characters have been mapped through the given translation table, which must be a string of length 256'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.translate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2b5206556ade49ed99be4787c884fbb3')[0]),
					'flag': helper.set_entry_command_string('upper()'),
					'description': [
						Markup('Return a copy of the string converted to uppercase'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.upper',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5e24c0c73cf84198a9856898729e7dcb')[0]),
					'flag': helper.set_entry_command_string('zfill(width)'),
					'description': [
						Markup('Return the numeric string left filled with zeros in a string of length width'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#str.zfill',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2442d5f7c9d745bb923a8064ca39ad80')[0]),
					'flag': helper.set_entry_command_string('isnumeric()'),
					'description': [
						Markup('Return True if there are only numeric characters in S, False otherwise. Numeric characters include digit characters, and all characters that have the Unicode numeric value property, e.g. U+2155, VULGAR FRACTION ONE FIFTH'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#unicode.isnumeric',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f596de7b9def4459bd372c8bd0d93060')[0]),
					'flag': helper.set_entry_command_string('isdecimal()'),
					'description': [
						Markup('Return True if there are only decimal characters in S, False otherwise'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#unicode.isdecimal',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Random'),
		'subtitle': 'Use randomly generated numbers',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '25e4c6858fb04035a57a4f7e58218512',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('9cc508a38fdd441e9bbddb652910b105')[0]),
					'flag': helper.set_entry_command_string('seed([x])'),
					'description': [
						Markup('Initialize the basic random number generator'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.seed',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b4438a9c5be540afb854c66654d8f18d')[0]),
					'flag': helper.set_entry_command_string('getstate()'),
					'description': [
						Markup('Return an object capturing the current internal state of the generator'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.getstate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('40d1a2b48d4a481d9b986750b0d3a2d6')[0]),
					'flag': helper.set_entry_command_string('setstate(state)'),
					'description': [
						Markup('State should have been obtained from a previous call to getstate(), and setstate() restores the internal state of the generator to what it was at the time setstate() was called'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.setstate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4bc9e2b2400242c28e47aba78e619f0e')[0]),
					'flag': helper.set_entry_command_string('jumpahead(n)'),
					'description': [
						Markup('Change the internal state to one different from and likely far away from the current state'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.jumpahead',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bded0c0c55d44f53ad987c361990a8b1')[0]),
					'flag': helper.set_entry_command_string('getrandbits(k)'),
					'description': [
						Markup('Returns a python long int with k random bits'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.getrandbits',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4469977a88224ef8a61dd42a6e44e0a0')[0]),
					'flag': helper.set_entry_command_string('randrange([start], stop[, step])'),
					'description': [
						Markup('Return a randomly selected element from range(start, stop, step)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.randrange',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e680c9d0412041358fc5bfd4dfddd190')[0]),
					'flag': helper.set_entry_command_string('randint(a,b)'),
					'description': [
						Markup('Return a random integer N such that a <= N <= b'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.randint',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('de865953f451465a8b66f84c7fe85bd6')[0]),
					'flag': helper.set_entry_command_string('choice(seq)'),
					'description': [
						Markup('Return a random element from the non-empty sequence seq'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.choice',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1f241d43d6c240cda94980fce0b3e9c9')[0]),
					'flag': helper.set_entry_command_string('shuffle(x[,random])'),
					'description': [
						Markup('Shuffle the sequence x in place'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.shuffle',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b0861c74ff664f699fe18e8df73da43f')[0]),
					'flag': helper.set_entry_command_string('sample(population,k)'),
					'description': [
						Markup('Return a k length list of unique elements chosen from the population sequence'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.sample',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5394d4271f274f1e82c43ed7a2d7089b')[0]),
					'flag': helper.set_entry_command_string('random()'),
					'description': [
						Markup('Return the next random floating point number in the range [0.0, 1.0)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.random',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('511f7594e9764df8adcc6e00c91a8abf')[0]),
					'flag': helper.set_entry_command_string('uniform(a,b)'),
					'description': [
						Markup('Return a random floating point number N such that a <= N <= b for a <= b and b <= N <= a for b < a'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.uniform',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d0b0ac61cac348639b1c2a01d104d13b')[0]),
					'flag': helper.set_entry_command_string('triangular(low,high,mode)'),
					'description': [
						Markup('Return a random floating point number N such that low <= N <= high and with the specified mode between those bounds'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.triangular',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3060270889fe493c92f5b4fd2204552a')[0]),
					'flag': helper.set_entry_command_string('betavariate(alpha,beta)'),
					'description': [
						Markup('Beta distribution'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.betavariate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1aca1c5dafc6448fb801de4ea05295d7')[0]),
					'flag': helper.set_entry_command_string('expovariate(lambd)'),
					'description': [
						Markup('Exponential distribution'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.expovariate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c93dfc04db614e5dbb267b7ce2c57153')[0]),
					'flag': helper.set_entry_command_string('gammavariate(alpha,beta)'),
					'description': [
						Markup('Gamma distribution'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.gammavariate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5596571311f24b688a31b8185633f36b')[0]),
					'flag': helper.set_entry_command_string('gauss(mu,sigma)'),
					'description': [
						Markup('Gaussian distribution'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.gauss',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('755085b8200e478381f1ce42998f4a01')[0]),
					'flag': helper.set_entry_command_string('lognormvariate(mu,sigma)'),
					'description': [
						Markup('Log normal distribution'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.lognormvariate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b308a61db795458994a0946e5e01f639')[0]),
					'flag': helper.set_entry_command_string('normalvariate(mu,sigma)'),
					'description': [
						Markup('Normal distribution'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.normalvariate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e4a39e44d31f44f5847ae26db56fc655')[0]),
					'flag': helper.set_entry_command_string('vonmisesvariate(mu,kappa)'),
					'description': [
						Markup('Mu is the mean angle, expressed in radians between 0 and 2*pi, and kappa is the concentration parameter, which must be greater than or equal to zero'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.vonmisesvariate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c2904b89b9924305ae03c7e89dd74d34')[0]),
					'flag': helper.set_entry_command_string('paretovariate(alpha)'),
					'description': [
						Markup('Pareto distribution'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.paretovariate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3a90416cc623424cbaf64514b03d77fa')[0]),
					'flag': helper.set_entry_command_string('weibullvariate(alpha,beta)'),
					'description': [
						Markup('Weibull distribution'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/random.html#random.weibullvariate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Numbers'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '53f4e28546e84fd0b1f293dc4bc33f29',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('8e1b2be9f68e4186a9cd0d8dfc860ab6')[0]),
					'flag': helper.set_entry_command_string('ceil(x)'),
					'description': [
						Markup('Return the ceiling of x as a float, the smallest integer value greater than or equal to x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.ceil',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('30fa974e2e844a7bb24795c2976e62a5')[0]),
					'flag': helper.set_entry_command_string('copysign(x,y)'),
					'description': [
						Markup('Return x with the sign of y'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.copysign',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c766f4abb4f845a380e478f350e21f30')[0]),
					'flag': helper.set_entry_command_string('fabs(x)'),
					'description': [
						Markup('Return the absolute value of x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.fabs',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bfadab7453234e979a24aff28beec963')[0]),
					'flag': helper.set_entry_command_string('factorial(x)'),
					'description': [
						Markup('Return x factorial'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.factorial',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('41ca96a1d2fb4713a1287c7ea982c733')[0]),
					'flag': helper.set_entry_command_string('floor(x)'),
					'description': [
						Markup('Return the floor of x as a float, the largest integer value less than or equal to x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.floor',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9eb2c92ecba14012b5a083b2e5a71060')[0]),
					'flag': helper.set_entry_command_string('fmod(x,y)'),
					'description': [
						Markup('Return fmod(x, y), as defined by the platform C library'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.fmod',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('66d924fec76a48868fbe5bc3cb369c3c')[0]),
					'flag': helper.set_entry_command_string('frexp(x)'),
					'description': [
						Markup('Return the mantissa and exponent of x as the pair (m, e)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.frexp',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fe7a12ddc805451e9d1e604abdc30f8f')[0]),
					'flag': helper.set_entry_command_string('fsum(iterable)'),
					'description': [
						Markup('Return an accurate floating point sum of values in the iterable'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.fsum',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('290a8b90a5e84ceaa633aa08415dd4e0')[0]),
					'flag': helper.set_entry_command_string('isinf(x)'),
					'description': [
						Markup('Check if the float x is positive or negative infinity'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.isinf',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1e3d342835e546ea81c42c36fc83788c')[0]),
					'flag': helper.set_entry_command_string('isnan(x)'),
					'description': [
						Markup('Check if the float x is a NaN (not a number)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.isnan',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8cf00b28a01d45beb3b066ef127b23db')[0]),
					'flag': helper.set_entry_command_string('ldexp(x,i)'),
					'description': [
						Markup('Return x * (2**i)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.ldexp',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('aa7b9d168e5b4694ac0080eb3636e95d')[0]),
					'flag': helper.set_entry_command_string('modf()'),
					'description': [
						Markup('Return the fractional and integer parts of x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.modf',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3fc7e9f8c2804d23862ca86c0f16dc36')[0]),
					'flag': helper.set_entry_command_string('trunc()'),
					'description': [
						Markup('Return the Real value x truncated to an Integral (usually a long integer)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.trunc',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Powers and Logarithms'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '41341efc68184d5e96a45c2cc30cc2b8',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('200aa23efd8c48c680cbf62666935648')[0]),
					'flag': helper.set_entry_command_string('exp(x)'),
					'description': [
						Markup('Return e**x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.exp',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a5c51ddf3115487ab2d50a4e84587cd1')[0]),
					'flag': helper.set_entry_command_string('log(x[,base])'),
					'description': [
						Markup('With one argument, return the natural logarithm of x (to base e)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.log',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f6dbacbb11fe44e2b648268313252f5d')[0]),
					'flag': helper.set_entry_command_string('log1p(x)'),
					'description': [
						Markup('Return the natural logarithm of 1+x (base e)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.log1p',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bab3f9e38a414646a884eab00a95d0a8')[0]),
					'flag': helper.set_entry_command_string('log10(x)'),
					'description': [
						Markup('Return the base-10 logarithm of x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.log10',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ffbf5166645f48e4bbb42cfa50ea4b4a')[0]),
					'flag': helper.set_entry_command_string('pow(x,y)'),
					'description': [
						Markup('Return x raised to the power y'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.pow',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('906e51d07ced438899b3f4db599c2735')[0]),
					'flag': helper.set_entry_command_string('sqrt(x)'),
					'description': [
						Markup('Return the square root of x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.sqrt',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Trigonometry'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'c1f18506648a4b4ab4a3626d506438c0',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('9befcc6763984e18ae1d05c003fbeaee')[0]),
					'flag': helper.set_entry_command_string('acos(x)'),
					'description': [
						Markup('Return the arc cosine of x, in radians'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.acos',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('93c6d117c1d34437a927e85b45f97b5d')[0]),
					'flag': helper.set_entry_command_string('asin(x)'),
					'description': [
						Markup('Return the arc sine of x, in radians'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.asin',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f08c6041883044ee8387cb95676cd496')[0]),
					'flag': helper.set_entry_command_string('atan(x)'),
					'description': [
						Markup('Return the arc tangent of x, in radians'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.atan',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ef6c1fd2f1734b3aa9d73952a17be80e')[0]),
					'flag': helper.set_entry_command_string('atan2(y,x)'),
					'description': [
						Markup('Return atan(y / x), in radians'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.atan2',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8adb4f4c4a2a4f4e8f4c7051397f8648')[0]),
					'flag': helper.set_entry_command_string('cos(x)'),
					'description': [
						Markup('Return the cosine of x radians'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.cos',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('11158201355d4f3188aef7fdfc0069ec')[0]),
					'flag': helper.set_entry_command_string('hypot(x,y)'),
					'description': [
						Markup('Return the Euclidean norm, sqrt(x*x + y*y)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.hypot',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('122d63a501054957bf160e0d3fbc166a')[0]),
					'flag': helper.set_entry_command_string('sin(x)'),
					'description': [
						Markup('Return the sine of x radians'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.sin',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a9a8a08e63634f2ca8b2bc2c021e7c7c')[0]),
					'flag': helper.set_entry_command_string('tan(x)'),
					'description': [
						Markup('Return the tangent of x radians'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.tan',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('268cd563f4f94d509dc176d7b7a9346a')[0]),
					'flag': helper.set_entry_command_string('degrees(x)'),
					'description': [
						Markup('Converts angle x from radians to degrees'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.degrees',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('44363325f245420e828e9cfcd5960e68')[0]),
					'flag': helper.set_entry_command_string('radians(x)'),
					'description': [
						Markup('Converts angle x from degrees to radians'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.radians',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('44e43e60d629417cb040f1f4a49e2b9d')[0]),
					'flag': helper.set_entry_command_string('acosh(x)'),
					'description': [
						Markup('Return the inverse hyperbolic cosine of x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.acosh',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e0a46947864b44949551f5d311aab6a8')[0]),
					'flag': helper.set_entry_command_string('asinh(x)'),
					'description': [
						Markup('Return the inverse hyperbolic sine of x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.asinh',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('796d2342d2ac483e9cd86f7f59f143f7')[0]),
					'flag': helper.set_entry_command_string('atanh(x)'),
					'description': [
						Markup('Return the inverse hyperbolic tangent of x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.atanh',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a42a0718a039455abded70352dce4b4b')[0]),
					'flag': helper.set_entry_command_string('cosh(x)'),
					'description': [
						Markup('Return the hyperbolic cosine of x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.cosh',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b6648fe9bcda4c2aaa20847a5f8da3db')[0]),
					'flag': helper.set_entry_command_string('sinh(x)'),
					'description': [
						Markup('Return the hyperbolic sine of x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.sinh',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7373a93d1c4746de8cebd8db735beefb')[0]),
					'flag': helper.set_entry_command_string('tanh(x)'),
					'description': [
						Markup('Return the hyperbolic tangent of x'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/math.html#math.tanh',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('File Methods'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '337264d0d09e492e8b57b7639214a953',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('da27acf9b9ad42d38379f8c32032e506')[0]),
					'flag': helper.set_entry_command_string('close()'),
					'description': [
						Markup('Close the file'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.close',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2740ee1949a94380ad940b189d0a14e1')[0]),
					'flag': helper.set_entry_command_string('flush()'),
					'description': [
						Markup('Flush the internal buffer, like stdio‘s fflush()'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.flush',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('22e22e95afa24dd49bd095f41cac408c')[0]),
					'flag': helper.set_entry_command_string('fileno()'),
					'description': [
						Markup('Return the integer “file descriptor” that is used by the underlying implementation to request I/O operations from the operating system'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.fileno',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('adf4aed36f5744c1a2521fc314ff5b52')[0]),
					'flag': helper.set_entry_command_string('isatty()'),
					'description': [
						Markup('Return True if the file is connected to a tty(-like) device, else False'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.isatty',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('68c677f86bf14a2493dfe6f069f92c19')[0]),
					'flag': helper.set_entry_command_string('next()'),
					'description': [
						Markup('A file object is its own iterator, for example iter(f) returns f (unless f is closed)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.next',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('08e47590ba7d4152879e1fd9c360fed3')[0]),
					'flag': helper.set_entry_command_string('read([size])'),
					'description': [
						Markup('Read at most size bytes from the file (less if the read hits EOF before obtaining size bytes)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.read',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('66e6a8a51f0d4b219f1459c161b00322')[0]),
					'flag': helper.set_entry_command_string('readline([size])'),
					'description': [
						Markup('Read one entire line from the file'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.readline',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b7aba2a1e6da4245b6e1e9d9ca28b6af')[0]),
					'flag': helper.set_entry_command_string('readlines([sizehint])'),
					'description': [
						Markup('Read until EOF using readline() and return a list containing the lines thus read'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.readlines',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('561339dba58c4819b35c387ce047fc96')[0]),
					'flag': helper.set_entry_command_string('xreadlines()'),
					'description': [
						Markup('This method returns the same thing as iter(f)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.xreadlines',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4072715fb3a14e4987716338015e937e')[0]),
					'flag': helper.set_entry_command_string('seek(offset[, whence])'),
					'description': [
						Markup('Set the file’s current position, like stdio‘s fseek()'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.seek',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('16d7f7784ddc462f91318c0c2b73591a')[0]),
					'flag': helper.set_entry_command_string('tell()'),
					'description': [
						Markup('Return the file’s current position, like stdio‘s ftell()'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.tell',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('44960c56b6864720bb20c4a441663804')[0]),
					'flag': helper.set_entry_command_string('truncate([size])'),
					'description': [
						Markup('Truncate the file’s size'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.truncate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fce5f4c79ab9482c96aa780ca548832c')[0]),
					'flag': helper.set_entry_command_string('write(str)'),
					'description': [
						Markup('Write a string to the file'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.write',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('67b44a9136ed43c3800721db6ba8a005')[0]),
					'flag': helper.set_entry_command_string('writelines(sequence)'),
					'description': [
						Markup('Write a sequence of strings to the file'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.writelines',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('File Attributes'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '5efc05d1ca4b4c1cb8ad9ae68704107a',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('584e6e6062b74d69a71fe6eb6d810b7a')[0]),
					'flag': helper.set_entry_command_string('closed'),
					'description': [
						Markup('Bool indicating the current state of the file object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.closed',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('500e6144a4a64c32a792816129408858')[0]),
					'flag': helper.set_entry_command_string('encoding'),
					'description': [
						Markup('The encoding that this file uses'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.encoding',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('272e50d823e04e98865248a1696a05ae')[0]),
					'flag': helper.set_entry_command_string('errors'),
					'description': [
						Markup('The Unicode error handler used along with the encoding'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.errors',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fcd2a7a4ec514bafb17c729cf3b34d6b')[0]),
					'flag': helper.set_entry_command_string('mode'),
					'description': [
						Markup('The I/O mode for the file'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.mode',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4c9a0ad6ee9a412c8a1dafe64a63364c')[0]),
					'flag': helper.set_entry_command_string('name'),
					'description': [
						Markup('If the file object was created using open(), the name of the file'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.name',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9cf3c679d0b541a9941d0bb807af497e')[0]),
					'flag': helper.set_entry_command_string('newlines'),
					'description': [
						Markup('If Python was built with the --with-universal-newlines option to configure (the default) this read-only attribute exists, and for files opened in universal newline read mode it keeps track of the types of newlines encountered while reading the file'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.newlines',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5526850602ab40aca2244c6f550c5af0')[0]),
					'flag': helper.set_entry_command_string('softspace'),
					'description': [
						Markup('Boolean that indicates whether a space character needs to be printed before another value when using the print statement'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#file.softspace',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('List Methods'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'b61f343357d94e19938e7a9ca43d2250',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ebcc790e1c3f4308ab9ac8fbdad24035')[0]),
					'flag': helper.set_entry_command_string('append(x)'),
					'description': [
						Markup('Append a new item with value x to the end of the array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.append',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('88e03f8fc51c4b0889ef024bb14d78db')[0]),
					'flag': helper.set_entry_command_string('buffer_info()'),
					'description': [
						Markup('Return a tuple (address, length) giving the current memory address and the length in elements of the buffer used to hold array’s contents'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.buffer_info',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3b4bb0960c77445b82484d783780def8')[0]),
					'flag': helper.set_entry_command_string('byteswap()'),
					'description': [
						Markup('“Byteswap” all items of the array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.byteswap',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a2e53b7eb7c34516987bdb0dbc077440')[0]),
					'flag': helper.set_entry_command_string('count(x)'),
					'description': [
						Markup('Return the number of occurrences of x in the array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.count',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5e1054344e2f4c159201bd1d824db6a0')[0]),
					'flag': helper.set_entry_command_string('extend(iterable)'),
					'description': [
						Markup('Append items from iterable to the end of the array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.extend',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f55b672d650e4e798510e080fdb31c1e')[0]),
					'flag': helper.set_entry_command_string('fromfile(f,n)'),
					'description': [
						Markup('Read n items (as machine values) from the file object f and append them to the end of the array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.fromfile',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a1e7e647ce3d42f483b56cfd884c598c')[0]),
					'flag': helper.set_entry_command_string('fromlist(list)'),
					'description': [
						Markup('Append items from the list'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.fromlist',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('41b09222aa8c48c8986fa1fc5b592396')[0]),
					'flag': helper.set_entry_command_string('fromstring(s)'),
					'description': [
						Markup('Appends items from the string, interpreting the string as an array of machine values (as if it had been read from a file using the fromfile() method)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.fromstring',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('088a7462e32e4c9fb7c49b638b24f19b')[0]),
					'flag': helper.set_entry_command_string('fromunicode(s)'),
					'description': [
						Markup('Extends this array with data from the given unicode string'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.fromunicode',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d8c656b0746f45bdb42795e82841794d')[0]),
					'flag': helper.set_entry_command_string('index(x)'),
					'description': [
						Markup('Return the smallest i such that i is the index of the first occurrence of x in the array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.index',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5cde14f8f0ba41239fb4c1a6915ea367')[0]),
					'flag': helper.set_entry_command_string('insert(i,x)'),
					'description': [
						Markup('Insert a new item with value x in the array before position i'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.insert',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('837dd3d1d01d44d2ac09f7c1e1bb271c')[0]),
					'flag': helper.set_entry_command_string('pop([i])'),
					'description': [
						Markup('Removes the item with the index i from the array and returns it'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.pop',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e43df263f51a4506bb005abb7864bc78')[0]),
					'flag': helper.set_entry_command_string('remove(x)'),
					'description': [
						Markup('Remove the first occurrence of x from the array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.remove',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d831d8ae199443c6ac170711d19a29bf')[0]),
					'flag': helper.set_entry_command_string('reverse()'),
					'description': [
						Markup('Reverse the order of the items in the array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.reverse',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('589a5559936d4b8581c85be4e958d877')[0]),
					'flag': helper.set_entry_command_string('tofile(f)'),
					'description': [
						Markup('Write all items (as machine values) to the file object f'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.tofile',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0db9765834e84f959d8f42b066d20aaa')[0]),
					'flag': helper.set_entry_command_string('tolist()'),
					'description': [
						Markup('Convert the array to an ordinary list with the same items'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.tolist',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('70fc33bff17742c9866c2f2e626c8af3')[0]),
					'flag': helper.set_entry_command_string('tostring()'),
					'description': [
						Markup('Convert the array to an array of machine values and return the string representation (the same sequence of bytes that would be written to a file by the tofile() method.)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.tostring',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bebaa817c21c49d4901cd2ff73197ab0')[0]),
					'flag': helper.set_entry_command_string('tounicode()'),
					'description': [
						Markup('Convert the array to a unicode string'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/array.html#array.array.tounicode',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Sets'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'baeaa2a8c09c45dc9dff24b59e85d8a7',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('30feb70420f64912a55e7d1864c085bf')[0]),
					'flag': helper.set_entry_command_string('isdisjoint(other)'),
					'description': [
						Markup('Return True if the set has no elements in common with other'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.isdisjoint',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9ec4cd2a25934214a44b0ce34ec08b2d')[0]),
					'flag': helper.set_entry_command_string('issubset(others)'),
					'description': [
						Markup('Test whether every element in the set is in others'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.issubset',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1da983b679784cf0b92f7d6d90fe631a')[0]),
					'flag': helper.set_entry_command_string('issuperset'),
					'description': [
						Markup('Test whether every element in other is in the set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.issuperset',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ee288be2aece4d9a8c7b5beae9d0fcf3')[0]),
					'flag': helper.set_entry_command_string('union(other...)'),
					'description': [
						Markup('Return a new set with elements from the set and all others'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.union',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('81594cbe9002439bb475fd504d6ee568')[0]),
					'flag': helper.set_entry_command_string('intersection(other, ...)'),
					'description': [
						Markup('Return a new set with elements common to the set and all others'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.intersection',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1d95723a601e43a083f0ed7013f20aaa')[0]),
					'flag': helper.set_entry_command_string('difference(other...)'),
					'description': [
						Markup('Return a new set with elements in the set that are not in the others'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.difference',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('40a7778bda9441959a319560edd39252')[0]),
					'flag': helper.set_entry_command_string('symmetric_difference(other)'),
					'description': [
						Markup('Return a new set with elements in either the set or other but not both'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.symmetric_difference',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fe00dc226a3f47d09fb8fca5f91de2fb')[0]),
					'flag': helper.set_entry_command_string('copy()'),
					'description': [
						Markup('Return a new set with a shallow copy of s'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.copy',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('df0da761965e44599008ca64598274a2')[0]),
					'flag': helper.set_entry_command_string('update()'),
					'description': [
						Markup('Update the set, adding elements from all others'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.update',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d4d6e89c9263401898e3df0a4fe671cb')[0]),
					'flag': helper.set_entry_command_string('intersection_update()'),
					'description': [
						Markup('Update the set, adding elements from all others'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.intersection_update',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('42e8bde320ab44b9a2e78b2aa88b447e')[0]),
					'flag': helper.set_entry_command_string('difference_update()'),
					'description': [
						Markup('Update the set, removing elements found in others'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.difference_update',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3a9536ee5701439d86d957aef70ef0e8')[0]),
					'flag': helper.set_entry_command_string('symmetric_difference_update()'),
					'description': [
						Markup('Update the set, keeping only elements found in either set, but not in both'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.symmetric_difference_update',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('12fd7b509b7f4c08a0fdd0915abec030')[0]),
					'flag': helper.set_entry_command_string('add(elem)'),
					'description': [
						Markup('Add element elem to the set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.add',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cd9436e7552b48f1aeb3471b7e614e5f')[0]),
					'flag': helper.set_entry_command_string('remove()'),
					'description': [
						Markup('Remove element elem from the set. Raises KeyError if elem is not contained in the set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.remove',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8013fb46d27944f6921c2cffebada4c2')[0]),
					'flag': helper.set_entry_command_string('discard(elem)'),
					'description': [
						Markup('Remove element elem from the set if it is present'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.discard',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1f2aa77bd33c422e9fdb2f497a37be2e')[0]),
					'flag': helper.set_entry_command_string('pop()'),
					'description': [
						Markup('Remove element elem from the set if it is present'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.pop',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('17c1ec86a8e043c49a52b1d6f26967f5')[0]),
					'flag': helper.set_entry_command_string('clear()'),
					'description': [
						Markup('Remove all elements from the set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#set.clear',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Dictionary Methods'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f13c8768c57c421d8d8781d412d43a34',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('64191e42708d42daa45e9791039d505b')[0]),
					'flag': helper.set_entry_command_string('clear()'),
					'description': [
						Markup('Remove all items from the dictionary'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.clear',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('be8e283615cc4fd790877d6353828d10')[0]),
					'flag': helper.set_entry_command_string('copy()'),
					'description': [
						Markup('Return a shallow copy of the dictionary'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.copy',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b67054ae1de645f784ab38be641a51cf')[0]),
					'flag': helper.set_entry_command_string('fromkeys(seq[, value])'),
					'description': [
						Markup('Create a new dictionary with keys from seq and values set to value'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.fromkeys',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('70702134ae1f4e259a68db1b1529a011')[0]),
					'flag': helper.set_entry_command_string('get(key[, default])'),
					'description': [
						Markup('Return the value for key if key is in the dictionary, else default'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.get',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('168bcbf6ab26419faebc95386cc8b4cd')[0]),
					'flag': helper.set_entry_command_string('has_key(key)'),
					'description': [
						Markup('Test for the presence of key in the dictionary. has_key() is deprecated in favor of key in d'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.has_key',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('edcbd027a3174a8caf21b618f2084759')[0]),
					'flag': helper.set_entry_command_string('items()'),
					'description': [
						Markup('Return a copy of the dictionary’s list of (key, value) pairs'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.items',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('875e476116664c0ebe0b25c1b2795a15')[0]),
					'flag': helper.set_entry_command_string('iteritems()'),
					'description': [
						Markup('Return an iterator over the dictionary’s (key, value) pairs. See the note for dict.items()'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.iteritems',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ca756a8b901d4a318a48f2aaafe9aea0')[0]),
					'flag': helper.set_entry_command_string('iterkeys()'),
					'description': [
						Markup('Return an iterator over the dictionary’s keys. See the note for dict.items()'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.iterkeys',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e8ed2ee1cc6a42218dae6ab26356ffbd')[0]),
					'flag': helper.set_entry_command_string('itervalues()'),
					'description': [
						Markup('Return an iterator over the dictionary’s values. See the note for dict.items()'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.itervalues',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5c50881e70dc4fc2be95f66757efd86a')[0]),
					'flag': helper.set_entry_command_string('keys()'),
					'description': [
						Markup('Return a copy of the dictionary’s list of keys. See the note for dict.items()'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.keys',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fbf6b5d8619a4a3eaacdb9ff36ed5301')[0]),
					'flag': helper.set_entry_command_string('pop(key[, default])'),
					'description': [
						Markup('If key is in the dictionary, remove it and return its value, else return default'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.pop',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1c16c0e47d89463b84657eb856d4b470')[0]),
					'flag': helper.set_entry_command_string('popitem()'),
					'description': [
						Markup('Remove and return an arbitrary (key, value) pair from the dictionary'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.popitem',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('90174121a1b84d0a85802213ede384c8')[0]),
					'flag': helper.set_entry_command_string('setdefault(key[, default])'),
					'description': [
						Markup('If key is in the dictionary, return its value. If not, insert key with a value of default and return default'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.setdefault',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ea84649f5f734b4eb425edf0b4d827c6')[0]),
					'flag': helper.set_entry_command_string('update([other])'),
					'description': [
						Markup('Update the dictionary with the key/value pairs from other, overwriting existing keys. Return None'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.update',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('943b90a8644a42298dbbc13bd821c3c4')[0]),
					'flag': helper.set_entry_command_string('values'),
					'description': [
						Markup('Return a copy of the dictionary’s list of values. See the note for dict.items()'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://docs.python.org/library/stdtypes.html#dict.values',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
]
# {
#     'heading':helper.set_folder(''),
#     'subtitle': '',
#     'description': '.',
#     'columns': 'col-lg-6 col-md-12',
#     'uuid': helper.get_uuid(),
# 'static_red': Markup(helper.set_entry_folder('9d51a035ee4344529eb61ddb4082405c')[0]),
#     'content': {
#         'descriptor': [
#             'Command',
#             'Description'
#         ],
#         'data': [
#
#         ]
#     }
# },
resources = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'link': 'https://www.python.org/',
			'title': 'Python Official Website',
			'description': Markup('The official website for Python - the best documentation out there'),
			'footer': Markup(''),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]
