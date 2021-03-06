import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('bash', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'bash'
meta = {
	'title': 'Bash Cheatsheet',
	'description': 'File test operators · Exit Signals · Control Signals · Special Files · Parameters · History Expansion · Globbing · Builtins',
	'keywords': 'bash, shell, bourne shell, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/Bash/',

	'opengraph_title': 'Bash Cheatsheet',
	'opengraph_description': 'File test operators · Exit Signals · Control Signals · Special Files · Parameters · History Expansion · Globbing · Builtins',
	'opengraph_image': 'opengraph_bash.png',
	'opengraph_url': 'https://www.cheatsheet.wtf/bash/',

	'twitter_title': 'Bash Cheatsheet',
	'twitter_description': 'File test operators · Exit Signals · Control Signals · Special Files · Parameters · History Expansion · Globbing · Builtins',
	'twitter_image': 'twitter_card_bash.png',
}
information = {
	'tool': 'Bash',
	'title': 'Bash Cheatsheet',
	'subtitle': 'This site is a reference for the scripting language Bash',
	'description': 'Bash (Bourne Again Shell) is a shell language build on-top of the orignal Bourne Shell which was distributed with V7 Unix in 1979 and became the standard for writing shell scripts. Today it is primary to most Linux distributions, MacOS and it has even recently been enabled to run on Windows through something called WSL (Windows Subsystem for Linux).',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'Bash',
			[
				helper.characteristics.get('domain-specific-language'),
				helper.characteristics.get('scripting-language'),
				helper.characteristics.get('command-language'),
				helper.characteristics.get('imperative-programming'),
				helper.characteristics.get('dev-ops'),
				helper.characteristics.get('sys-admin'),
			]),
	],
	'topic_uris': [
		'domain-specific-language',
		'scripting-language',
		'command-language',
		'imperative-programming',
		'dev-ops',
		'sys-admin',
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
		'': '',
	},
]
cheatsheet = [
	{
		'heading': helper.set_folder('File Test Operators'),
		'subtitle': 'Used for testing of files files in shellscripts',
		'description': 'Testing files in scripts is easy and straight forward. This is where shell scripting starts to show its glory! In Bash you can do file testing for permissions, size, date, filetype or existence.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_red': '0b5580faacba4aa3a0e27e6c9798e03c',
		'content': {
			'descriptor': [
				'Flag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('c6b9ee6d66a34df996defbc522582bde')[0]),
					'flag': helper.set_entry_command_string('-e'),
					'description': [
						Markup('File exists'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5770c972fb9c4d04af53a80cf7770f63')[0]),
					'flag': helper.set_entry_command_string('-a'),
					'description': [
						Markup('File exists (identical to -e but is deprecated and outdated)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0455f6f2931c467b92e8aa853cfc01fb')[0]),
					'flag': helper.set_entry_command_string('-f'),
					'description': [
						Markup('File is a regular file (not a directory or device file)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup('https://www.youtube.com/embed/m8Cz5NhO-mE'),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('71709f4240994e42b9887fcc31d7e7ed')[0]),
					'flag': helper.set_entry_command_string('-s'),
					'description': [
						Markup('File is not zero size'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('979e6de7626248048b4b62688e8a8ef8')[0]),
					'flag': helper.set_entry_command_string('-d'),
					'description': [
						Markup('File is a directory'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cde01a0c245845548bf05304544933ba')[0]),
					'flag': helper.set_entry_command_string('-b'),
					'description': [
						Markup('File is a block device'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9688564620d34ba8964d3c2885fe1def')[0]),
					'flag': helper.set_entry_command_string('-c'),
					'description': [
						Markup('File is a character device'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8a963b6487c442a282879e5bfd6de3fd')[0]),
					'flag': helper.set_entry_command_string('-p'),
					'description': [
						Markup('File is a pipe'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a892d91b036344a4bdad74437a9e1781')[0]),
					'flag': helper.set_entry_command_string('-h'),
					'description': [
						Markup('File is a symbolic link'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3e7a23075b8a4897a101f9ca20d8a67c')[0]),
					'flag': helper.set_entry_command_string('-L'),
					'description': [
						Markup('File is a symbolic link'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e07ca2a4dce44d7e8b55ecc9403bfd12')[0]),
					'flag': helper.set_entry_command_string('-S'),
					'description': [
						Markup('File is a socket'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ae94f4ab07f849a9ae139987c58a8dea')[0]),
					'flag': helper.set_entry_command_string('-t'),
					'description': [
						Markup('File (descriptor) is associated with a terminal device'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cc9b3fb3f8aa4b44b4b391ce8322f6b2')[0]),
					'flag': helper.set_entry_command_string('-r'),
					'description': [
						Markup('File has read permission (for the user running the test)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('28cb2b9efb02461e977deca7a0b4bb79')[0]),
					'flag': helper.set_entry_command_string('-w'),
					'description': [
						Markup('File has write permission (for the user running the test)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('588b45c1951b438e81cfc03ffee88294')[0]),
					'flag': helper.set_entry_command_string('-x'),
					'description': [
						Markup('File has execute permission (for the user running the test)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9609df8c878846f58f3f0d3654870ab6')[0]),
					'flag': helper.set_entry_command_string('-g'),
					'description': [
						Markup('Set-group-id (sgid) flag set on file or directory'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dfc79889c2f44da399c5dcb3c9e1133a')[0]),
					'flag': helper.set_entry_command_string('-u'),
					'description': [
						Markup('Set-user-id (suid) flag set on file'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6af4973eee79439a9674fd129960948b')[0]),
					'flag': helper.set_entry_command_string('-k'),
					'description': [
						Markup('Sticky bit set'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('baed68fc76c8417aac5380680d2d0c0a')[0]),
					'flag': helper.set_entry_command_string('-O'),
					'description': [
						Markup('You are owner of file'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('783f545c480c421783850ea5f41775a0')[0]),
					'flag': helper.set_entry_command_string('-G'),
					'description': [
						Markup('Group-id of file same as yours'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8fcb5f820be843e1a357f521f814d904')[0]),
					'flag': helper.set_entry_command_string('-N'),
					'description': [
						Markup('File modified since it was last read'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6d655c20381c4f2b91e35660368ce417')[0]),
					'flag': Markup(helper.set_entry_command_string('f1&nbsp;-nt&nbsp;f2')),
					'description': [
						Markup('File f1 is newer than f2'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8dce8370da46435db2c1a0ae412a745a')[0]),
					'flag': Markup(helper.set_entry_command_string('f1&nbsp;-ot&nbsp;f2')),
					'description': [
						Markup('File f1 is older than f2'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('300a3fa668ec4f9e9bc02c722771850a')[0]),
					'flag': Markup(helper.set_entry_command_string('f1&nbsp;-ef&nbsp;f2')),
					'description': [
						Markup('Files f1 and f2 are hard links to the same file'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ded84626bf1c48018869a4f302a89baf')[0]),
					'flag': helper.set_entry_command_string('!'),
					'description': [
						Markup('Not operator, will reverse the any test and return true if a condition is absent'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://www.gnu.org/software/bash/manual/bash.html#Bash-Conditional-Expressions',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				}
			]
		}
	},
	{
		'heading': helper.set_folder('String Comparison'),
		'subtitle': 'Used for string comparison in Bash',
		'description': 'This section describes how to compare strings in Bash.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_red': '611e0c1252424ff7902606b5dd72c2a7',
		'content': {
			'descriptor': [
				'Flag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('707559cb2e8c415085aab63dcee60fad')[0]),
					'flag': helper.set_entry_command_string('='),
					'description': [
						Markup('Is equal to'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e857a1d7316242e4b6019545b12a8673')[0]),
					'flag': helper.set_entry_command_string('=='),
					'description': [
						Markup('Same as above, except the use of double equal symbols'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4af9c2b24d584d12a5fda2379952e878')[0]),
					'flag': helper.set_entry_command_string('!='),
					'description': [
						Markup('Is not equal to'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('caec0df1e0eb4a8a8226d2e615bc5079')[0]),
					'flag': helper.set_entry_command_string('<'),
					'description': [
						Markup('Is less than ASCII alphabetical order'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0b39b50e709f42f2a1e11fdb07709b41')[0]),
					'flag': helper.set_entry_command_string('>'),
					'description': [
						Markup('Is greater than ASCII alphabetical order'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3a6e6de8b3dc4fd2a3e300bb89d40838')[0]),
					'flag': helper.set_entry_command_string('-z'),
					'description': [
						Markup('String is null (i.e. zero length)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f958085c2d1c4ce4b1b6cf6f4dd87086')[0]),
					'flag': helper.set_entry_command_string('-n'),
					'description': [
						Markup('String is not null (i.e. !zero length)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				}
			]
		}
	},
	{
		'heading': helper.set_folder('Integer Comparison'),
		'subtitle': 'Used for comparing numbers',
		'description': 'How to compare integers or arithmetic expressions in shell scripts.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_red': helper.set_entry_folder('5b0de71518eb4a829aaef188baf78d73'),
		'content': {
			'descriptor': [
				'Flag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('5a9366b9f1d14b3fb3418306b6abf189')[0]),
					'flag': helper.set_entry_command_string('-eq'),
					'description': [
						Markup('Is equal to'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e52e4fbe8e6148ce9219890aece44d10')[0]),
					'flag': helper.set_entry_command_string('-ne'),
					'description': [
						Markup('Is not equal to'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b949778d55444f64b6069cbb5cab93c5')[0]),
					'flag': helper.set_entry_command_string('-gt'),
					'description': [
						Markup('Is greater than'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('53fc74805fe146f8b7f7e48374b226eb')[0]),
					'flag': helper.set_entry_command_string('-ge'),
					'description': [
						Markup('Is greater than or equal to'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0d974b4affe941a5afbae3fbeccd13cb')[0]),
					'flag': helper.set_entry_command_string('-lt'),
					'description': [
						Markup('Is less than'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5965b0e9c1714774851e47dd381d760c')[0]),
					'flag': helper.set_entry_command_string('-le'),
					'description': [
						Markup('Is less than or equal to'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('30b71aa71fea4e4d8bc365f5f06fde5c')[0]),
					'flag': helper.set_entry_command_string('<'),
					'description': [
						Markup('Is less than – place within double parentheses'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('78e9fcd950d44c16a44a7310d7445f8d')[0]),
					'flag': helper.set_entry_command_string('<='),
					'description': [
						Markup('Is less than or equal to (same rule as previous row)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c4687bc902fa4e679593f8f232f8a326')[0]),
					'flag': helper.set_entry_command_string('>'),
					'description': [
						Markup('Is greater than (same rule as previous row)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c0e96fc5c5b64272a2edfbd0c80e568d')[0]),
					'flag': helper.set_entry_command_string('>='),
					'description': [
						Markup('Is greater than or equal to (same rule as previous row)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				}
			]
		}
	},
	{
		'heading': helper.set_folder('Compound Operators'),
		'subtitle': '',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'info': {
			Markup('Useful for boolean expressions and is similar to <kbd>&&</kbd> and <kbd>||</kbd>'),
			Markup('The compound operators work with the <kbd>test</kbd> command or may occur within single brackets <kbd>[ &lt;expr&gt; ]</kbd>'),
		},
		'uuid': helper.get_uuid(),
		'static_red': '7f631be11f2c4ea3995bdaa32e778d99',
		'content': {
			'descriptor': [
				'Flag',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('37c6fe1923784172a28544b899962378')[0]),
					'flag': helper.set_entry_command_string('-a'),
					'description': [
						Markup('Logical and'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9351a9b5d6094739ada4072234f18a2c')[0]),
					'flag': helper.set_entry_command_string('-o'),
					'description': [
						Markup('Logical or'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('List Constructs'),
		'subtitle': '',
		'description': 'Provides a means of processing commands consecutively and in effect is able to replace complex if/then/case structures.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_red': 'fb352c3925c149ebb1edeacd5cec1c2f',
		'content': {
			'descriptor': [
				'Construct',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('d5da01e42afb415ebb013aa411591292')[0]),
					'flag': helper.set_entry_command_string('&&'),
					'description': [
						Markup('And construct'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0bbdd9b66c7e4d6ba42937fd4eb537e4')[0]),
					'flag': helper.set_entry_command_string('||'),
					'description': [
						Markup('Or construct'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Job Identifiers'),
		'subtitle': '',
		'description': 'Job control allows you to selectively stop (suspend) the execution of processes and continue their execution at a later point in time.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_red': 'f115aac7023747ad8b9910c4a4c21461',
		'content': {
			'descriptor': [
				'Notation',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('2ddde99619484a11bd150167c42b4e0a')[0]),
					'flag': Markup(helper.set_entry_command_string('%N')),
					'description': [
						Markup('Job number [N]'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b691e7725a59472fab529f88d63c32c9')[0]),
					'flag': Markup(helper.set_entry_command_string('%S')),
					'description': [
						Markup('Invocation (command-line) of job begins with string S'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('16816a2a9f6d45178a21cee7fdd8ee08')[0]),
					'flag': Markup(helper.set_entry_command_string('%?S')),
					'description': [
						Markup('Invocation (command-line) of job contains within it string S'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ff501697ee894c989b02ea82a66b351b')[0]),
					'flag': Markup(helper.set_entry_command_string('%%')),
					'description': [
						Markup('"current" job (last job stopped in foreground or started in background)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2359d152bde54cea835711f3701565b5')[0]),
					'flag': Markup(helper.set_entry_command_string('%+')),
					'description': [
						Markup('"current" job (last job stopped in foreground or started in background)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('927ec530c06d414eba135b6bf2b24920')[0]),
					'flag': Markup(helper.set_entry_command_string('%-')),
					'description': [
						Markup('Last job'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8e689e94e2af4cf4946a7f13daf9e544')[0]),
					'flag': Markup(helper.set_entry_command_string('%!')),
					'description': [
						Markup('Last background process'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Signals'),
		'subtitle': 'System V Signals',
		'description': 'UNIX System V Signals.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_red': '6da95027b15d401e851b8f9e3b674b44',
		'content': {
			'descriptor': [
				'Name',
				'Number',
				'Action',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e457cbc253dc44239cee3d0d053df361')[0]),
					'flag': helper.set_entry_command_string('SIGHUP'),
					'description': [
						Markup('1'),
						Markup('Exit'),
						Markup('Hangs up'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('45bbec820e9447ecb82ba0ee3d81bceb')[0]),
					'flag': helper.set_entry_command_string('SIGINT'),
					'description': [
						Markup('2'),
						Markup('Exit'),
						Markup('Interrupts'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8251c7068d8448c694707556ccb041c5')[0]),
					'flag': helper.set_entry_command_string('SIGQUIT'),
					'description': [
						Markup('3'),
						Markup('core dump'),
						Markup('Quits'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9f06200eccc54ea080efb4805e4d4aae')[0]),
					'flag': helper.set_entry_command_string('SIGILL'),
					'description': [
						Markup('4'),
						Markup('core dump'),
						Markup('Illegal instruction'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('802adc8f1f6e48eea867b307e27c13b6')[0]),
					'flag': helper.set_entry_command_string('SIGTRAP'),
					'description': [
						Markup('5'),
						Markup('core dump'),
						Markup('Trace trap'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ed0dc5514386470dac6dafa4497950b4')[0]),
					'flag': helper.set_entry_command_string('SIGIOT'),
					'description': [
						Markup('6'),
						Markup('core dump'),
						Markup('IOT instruction'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('892610a4d53f45ba962e1272c574fbe4')[0]),
					'flag': helper.set_entry_command_string('SIGEMT'),
					'description': [
						Markup('7'),
						Markup('core dump'),
						Markup('MT instruction'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ef053e513cd64f7cbe13da57b8385ffa')[0]),
					'flag': helper.set_entry_command_string('SIGFPE'),
					'description': [
						Markup('8'),
						Markup('core dump'),
						Markup('Floating point exception'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('16ffa8297aea44cabafb8fac20cafb90')[0]),
					'flag': helper.set_entry_command_string('SIGKILL'),
					'description': [
						Markup('9'),
						Markup('exit'),
						Markup('Kills (cannot be caught or ignored)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c613ee7ab8e744fda1f461176f247bc2')[0]),
					'flag': helper.set_entry_command_string('SIGBUS'),
					'description': [
						Markup('10'),
						Markup('core dump'),
						Markup('Bus error'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d08fe51fd232417abfeb8b1b748fc7b8')[0]),
					'flag': helper.set_entry_command_string('SIGSEGV'),
					'description': [
						Markup('11'),
						Markup('core dump'),
						Markup('Segmentation violation'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a93ae3d24ebd41d4a4fc4466f88bc6a1')[0]),
					'flag': helper.set_entry_command_string('SIGSYS'),
					'description': [
						Markup('12'),
						Markup('core dump'),
						Markup('Bad argument to system call'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('50c24e9f2401435e84d83aceafcbfa0d')[0]),
					'flag': helper.set_entry_command_string('SIGPIPE'),
					'description': [
						Markup('13'),
						Markup('exit'),
						Markup('Writes on a pipe with no one to read it'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dff6bc69b3e1464ba88bb12e34a9775e')[0]),
					'flag': helper.set_entry_command_string('SIGALRM'),
					'description': [
						Markup('14'),
						Markup('exit'),
						Markup('Alarm clock'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6f53d4c59b4849388e7d686dea2edc7f')[0]),
					'flag': helper.set_entry_command_string('SIGTERM'),
					'description': [
						Markup('15'),
						Markup('exit'),
						Markup('Software termination signal'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				}
			]
		}
	},
	{
		'heading': helper.set_folder('Reserved Exit Codes'),
		'subtitle': '',
		'description': 'Useful for debugging a script. Exit takes integer args in the range 0-255. ',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_red': helper.set_entry_folder('64716dfd4f5b45de9a4a60fb1c4b4a9d'),
		'content': {
			'descriptor': [
				'Exit Code No.',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('2407da690dfe483f9faa5aac16dd4295')[0]),
					'flag': helper.set_entry_command_string('1'),
					'description': [
						Markup('Catchall for general errors'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('56bd0143e338439abe09e5ba8375b4ee')[0]),
					'flag': helper.set_entry_command_string('2'),
					'description': [
						Markup('Misuse of shell builtins'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a0d2b764d903486ea0a3de43a555f05c')[0]),
					'flag': helper.set_entry_command_string('126'),
					'description': [
						Markup('Command invoked cannot execute'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4a402b55e1d445a4802b9c7fc01d5a7a')[0]),
					'flag': helper.set_entry_command_string('127'),
					'description': [
						Markup('Command not found'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cec559fee2504e429f1e3aab5b8905fa')[0]),
					'flag': helper.set_entry_command_string('128'),
					'description': [
						Markup('Invalid argument to exit'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('41243996fbca4103ac8b578a848fae56')[0]),
					'flag': helper.set_entry_command_string('128+n'),
					'description': [
						Markup('Fatal error signal "n"'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('383c7f8718e547eb990830f64a5901ba')[0]),
					'flag': helper.set_entry_command_string('130'),
					'description': [
						Markup('Script terminated by Control-C'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Sending Control Signals'),
		'subtitle': '',
		'description': 'You can use these key-combinations to send signals or control the output. Check your stty settings. Suspend and resume of output is usually disabled if you are using "modern" terminal emulations. The standard xterm supports Ctrl+S and Ctrl+Q by default.',
		'warning': {
			'Check your stty settings. Suspend and resume of output is usually disabled if you are using "modern" terminal emulations. The standard xterm supports Ctrl+S and Ctrl+Q by default.'
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '6c8c72ae4634465097097ce196faef21',
		'content': {
			'descriptor': [
				'Key Combo',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('e01b106c1c4c4cf1a62b6ec069fbb679')[0]),
					'flag': helper.set_entry_command_string('Ctrl+C'),
					'description': [
						Markup('The interrupt signal, sends SIGINT to the job running in the foreground'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e5650b0947e84cc9b6e7939980f9a7ac')[0]),
					'flag': helper.set_entry_command_string('Ctrl+Y'),
					'description': [
						Markup(
							'The delayed suspend character. Causes a running process to be stopped when it attempts to read input from the terminal. Control is returned to the shell, the user can foreground, background or kill the process. Delayed suspend is only available on operating systems supporting this feature.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f57b400a14de4766991b2b94c0381a57')[0]),
					'flag': helper.set_entry_command_string('Ctrl+Z'),
					'description': [
						Markup('The suspend signal, sends a SIGTSTP to a running program, thus stopping it and returning control to the shell.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fc491d4fcb5643cb99d26ff4e43ce33d')[0]),
					'flag': helper.set_entry_command_string('Ctrl + s'),
					'description': [
						Markup('Stops the output to the screen (for long running verbose command)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7a5336c86fc74f52968daee198dee5bb')[0]),
					'flag': helper.set_entry_command_string('Ctrl + q'),
					'description': [
						Markup('Allow output to the screen (if previously stopped using command above)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('23f34c800a1d41baa54ba77bee206c36')[0]),
					'flag': helper.set_entry_command_string('Ctrl + l'),
					'description': [
						Markup('Clear the screen'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Command Editing'),
		'subtitle': 'Keyboard Shortcuts',
		'description': 'Shortcuts to use in the CLI for swiftly editing a command. These shortcuts are provided by the GNU Readline library.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '1cd904923c9c4f9b89426b5fdee5ddd0',
		'content': {
			'descriptor': [
				'Key Combo',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('b0643a1e9db241bcb27e86f36902d155')[0]),
					'flag': helper.set_entry_command_string('Ctrl + a'),
					'description': [
						Markup('Go to the start of the command line'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('759d087ed2ac4ca9af407e3120da5b47')[0]),
					'flag': helper.set_entry_command_string('Ctrl + e'),
					'description': [
						Markup('Go to the end of the command line'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f8ed165f530f41cabfa2caa8adf36344')[0]),
					'flag': helper.set_entry_command_string('Ctrl + k'),
					'description': [
						Markup('Delete from cursor to the end of the command line'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('731f8e7499c6452fbc405b686901d2c5')[0]),
					'flag': helper.set_entry_command_string('Ctrl + u'),
					'description': [
						Markup('Delete from cursor to the start of the command line'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8b890b8122da45b7b75436d134b92bfc')[0]),
					'flag': helper.set_entry_command_string('Ctrl + w '),
					'description': [
						Markup('Delete from cursor to start of word (i.e. delete backwards one word)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2b37a4c3c4e64404a2a6cf876b90817e')[0]),
					'flag': helper.set_entry_command_string('Ctrl + y'),
					'description': [
						Markup('Paste word or text that was cut using one of the deletion shortcuts (such as the one above) after the cursor'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('46c508c896c4454eb6e641b7ac7e7241')[0]),
					'flag': helper.set_entry_command_string('Ctrl + xx'),
					'description': [
						Markup('Move between start of command line and current cursor position (and back again)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('225544086a7348f188584657f3fdc581')[0]),
					'flag': helper.set_entry_command_string('Alt + b'),
					'description': [
						Markup('Move backward one word (or go to start of word the cursor is currently on)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ea1e4ba4f6384344abab168f61edb450')[0]),
					'flag': helper.set_entry_command_string('Alt + f'),
					'description': [
						Markup('Move forward one word (or go to end of word the cursor is currently on)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a8945beedeb4485d83886fbf937b9c00')[0]),
					'flag': helper.set_entry_command_string('Alt + d'),
					'description': [
						Markup('Delete to end of word starting at cursor (whole word if cursor is at the beginning of word)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('76658fded2174c7c98c0c7086b09963b')[0]),
					'flag': helper.set_entry_command_string('Alt + c'),
					'description': [
						Markup('Capitalize to end of word starting at cursor (whole word if cursor is at the beginning of word)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1a5a23feb2f94c5db0728c0c86a0a36c')[0]),
					'flag': helper.set_entry_command_string('Alt + u'),
					'description': [
						Markup('Make uppercase from cursor to end of word'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0d8082a5c421409e8b1f41be0e56364d')[0]),
					'flag': helper.set_entry_command_string('Alt + l'),
					'description': [
						Markup('Make lowercase from cursor to end of word'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cc8b4298e3d3492bae352b61e03508cb')[0]),
					'flag': helper.set_entry_command_string('Alt + t'),
					'description': [
						Markup('Swap current word with previous'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('af2199d1e95f4647816d5b95f413330e')[0]),
					'flag': helper.set_entry_command_string('Ctrl + f'),
					'description': [
						Markup('Move forward one character'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1d9ba73090fc4de09f72ab5ca1fead6d')[0]),
					'flag': helper.set_entry_command_string('Ctrl + b'),
					'description': [
						Markup('Move backward one character'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9d2115bdf96245e0b9742409ecf3b90d')[0]),
					'flag': helper.set_entry_command_string('Ctrl + d'),
					'description': [
						Markup('Delete character under the cursor'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9610a16a3e5f4e87bc26a49e6593730b')[0]),
					'flag': helper.set_entry_command_string('Ctrl + h'),
					'description': [
						Markup('Delete character before the cursor'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9b298b890cd8472e9be29c698de4dad4')[0]),
					'flag': helper.set_entry_command_string('Ctrl + t '),
					'description': [
						Markup('Swap character under cursor with the previous one'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('File Types'),
		'subtitle': '',
		'description': 'This is very different from Windows but straight forward once you get it.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_red': '6e74df9d57d04d24a97f3a5d67b69a0e',
		'content': {
			'descriptor': [
				'Symbol',
				'Meaning'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('07c3b45160dd47a98103c2d140e8aa3e')[0]),
					'flag': helper.set_entry_command_string('-'),
					'description': [
						Markup('Regular file'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1c1fe6aefcc94be9a0e1bdad0b156686')[0]),
					'flag': helper.set_entry_command_string('d'),
					'description': [
						Markup('Directory'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5294478e08204048a0c4bb15dbf930cc')[0]),
					'flag': helper.set_entry_command_string('l'),
					'description': [
						Markup('(Symbolic) Link'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('61563108851e4da1a8839640f4840e62')[0]),
					'flag': helper.set_entry_command_string('c'),
					'description': [
						Markup('Character device'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('212f491f5459454daf75d286e2a9fe95')[0]),
					'flag': helper.set_entry_command_string('s'),
					'description': [
						Markup('Socket'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('42fd472218bc43fd8d8b85c74a345323')[0]),
					'flag': helper.set_entry_command_string('p'),
					'description': [
						Markup('Named pipe'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('507229794785426dacdd1ada942e46e8')[0]),
					'flag': helper.set_entry_command_string('b'),
					'description': [
						Markup('Block device'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Special Files'),
		'subtitle': '',
		'description': 'Files that are read by the shell. Listed in order of their execution.',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_red': '66229c8239bd45e6ae958f54a14c2e7b',
		'content': {
			'descriptor': [
				'File',
				'Info'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('d03f36d4febd4991a49e4d1f3b1a7b68')[0]),
					'flag': helper.set_entry_command_string('/etc/profile'),
					'description': [
						Markup('Executed automatically at login'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7062aaa5fc1840eb9ae4951a28478731')[0]),
					'flag': Markup(helper.set_entry_command_string('~.bash_profile</kbd><br><kbd>~/.bash_login</kbd><br><kbd>~.profile')),
					'description': [
						Markup('Whichever is found first is executed at login'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a45e75da4e5145d0ada27d2d2623ed34')[0]),
					'flag': helper.set_entry_command_string('~/.bashrc'),
					'description': [
						Markup('Is read by every nonlogin shell'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Permissions'),
		'subtitle': '',
		'description': 'Now you may know what that arcane looking string rwxrwxrwx is when you invoke ls -l',
		'columns': 'col-lg-6 col-md-12',
		'warning': {
		},
		'danger': {
		},
		'uuid': helper.get_uuid(),
		'static_red': '4cd8779fe99549fbbc24284ada5ad11f',
		'content': {
			'descriptor': [
				'Code',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('5a9dae8d737b4a5c8755c185ac0d3e54')[0]),
					'flag': helper.set_entry_command_string('s'),
					'description': [
						Markup('Setuid when in user column'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('478d69f3bc3548d1a52b661b388bb29d')[0]),
					'flag': helper.set_entry_command_string('s'),
					'description': [
						Markup('Setgid when in group column'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a1e043267ae0471abef535b5d883eaed')[0]),
					'flag': helper.set_entry_command_string('t'),
					'description': [
						Markup('Sticky bit'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('65d971383eea49b1a60f5bc02780dcc4')[0]),
					'flag': Markup(helper.set_entry_command_string('0</kbd><br><kbd>-')),
					'description': [
						Markup('The access right that is supposed to be on this place is not granted.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('509cd813b84f4570aa9d0a0f38cb2060')[0]),
					'flag': Markup(helper.set_entry_command_string('4</kbd><br><kbd>r')),
					'description': [
						Markup('Read access is granted to the user category defined in this place'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6b8a5f680bd0499a85175338e4aa18db')[0]),
					'flag': Markup(helper.set_entry_command_string('2</kbd><br><kbd>w')),
					'description': [
						Markup('Write permission is granted to the user category defined in this place'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('abf6bb25717940b9b70b79618526fc6d')[0]),
					'flag': Markup(helper.set_entry_command_string('1</kbd><br><kbd>x')),
					'description': [
						Markup('Execute permission is granted to the user category defined in this place'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5203f1e657a24b8894a4f67ac501ea9d')[0]),
					'flag': helper.set_entry_command_string('u'),
					'description': [
						Markup('User permissions'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('87aaaca7d5d5442c8465e03bbcfcf141')[0]),
					'flag': helper.set_entry_command_string('g'),
					'description': [
						Markup('Group permissions'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7da61260c59a477788f88f10c1dd3f35')[0]),
					'flag': helper.set_entry_command_string('o'),
					'description': [
						Markup('Others permissions'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('String Manipulation'),
		'subtitle': '',
		'description': 'Bash supports a surprisingly big number of string operations! Unfortunately, these tools lack a unified focus. Some are a subset of parameter substitution, and others fall under the functionality of the UNIX expr command. This results in inconsistent command syntax and overlap of functionality.',
		'warning': {
			'MacOS built-in bash is from 2007 and won\'t support many of these.',
		},
		'danger': {
		},
		'columns': 'col-lg-12 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '0662effaa7474feeb11a12fa04197bfd',
		'content': {
			'descriptor': [
				'Pattern',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('2fe577599c4848d795cdf2b5b8485a29')[0]),
					'flag': helper.set_entry_command_string('${#var}'),
					'description': [
						Markup('Find the length of the string'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d3eed40b6442451eb7ff27c38892b813')[0]),
					'flag': helper.set_entry_command_string('${var%pattern}'),
					'description': [
						Markup('Remove from shortest rear (end) pattern'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1355ea5684c24dcb99dd5d510dde2d0c')[0]),
					'flag': helper.set_entry_command_string('${var%%pattern}'),
					'description': [
						Markup('Remove from longest rear (end) pattern'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4212cc2302ca4045a65c483970f42941')[0]),
					'flag': helper.set_entry_command_string('${var:position}'),
					'description': [
						Markup('Extract substring from $var at $position'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('80d05a77df104469b4603177e662b4f0')[0]),
					'flag': helper.set_entry_command_string('${var:num1:num2}'),
					'description': [
						Markup('Substring'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b49e89ce5cf248178c8852b1c2afa616')[0]),
					'flag': helper.set_entry_command_string('${var#pattern}'),
					'description': [
						Markup('Remove from shortest front pattern'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('971815b76a32446db2ff7751276acae5')[0]),
					'flag': helper.set_entry_command_string('${var##pattern}'),
					'description': [
						Markup('Remove from longest front pattern'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('76fd1e09187141b28683a442129124c1')[0]),
					'flag': helper.set_entry_command_string('${var/pattern/string}'),
					'description': [
						Markup('Find and replace (only replace first occurrence)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5f24f76d6d1d48fa9ca81989ad7b7cc6')[0]),
					'flag': helper.set_entry_command_string('${var//pattern/string}'),
					'description': [
						Markup('Find and replace all occurrences'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e0146410235e44c08738d20947b64330')[0]),
					'flag': helper.set_entry_command_string('${!prefix*}'),
					'description': [
						Markup('Expands to the names of variables whose names begin with prefix.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a0723ecf624f4ba29099c8fc918ea95c')[0]),
					'flag': Markup(helper.set_entry_command_string('${var,}</kbd><br><kbd>${var,pattern}')),
					'description': [
						Markup('Convert first character to lowercase'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5d82425a383e4a94957c686d290d6ccc')[0]),
					'flag': Markup(helper.set_entry_command_string('${var,}</kbd><br><kbd>${var,pattern}')),
					'description': [
						Markup('Convert all characters to lowercase'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('14efdfefefd043159947a0770930b83e')[0]),
					'flag': Markup(helper.set_entry_command_string('${var^}</kbd><br><kbd>${var^pattern}')),
					'description': [
						Markup('Convert first character to uppercase'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('21cdb7a33c55436a9f3c1aeecae4b6d4')[0]),
					'flag': Markup(helper.set_entry_command_string('${var^^}</kbd><br><kbd>${var^^pattern}')),
					'description': [
						Markup('Convert all character to uppercase'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5d3cfacef63744a09523f5d6d0f2b580')[0]),
					'flag': helper.set_entry_command_string('${string/substring/replacement}'),
					'description': [
						Markup('Replace first match of $substring with $replacement'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3f3a2e6eb70f4eafb81ebecac91ccea3')[0]),
					'flag': helper.set_entry_command_string('${string//substring/replacement}'),
					'description': [
						Markup('Replace all matches of $substring with $replacement'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ce0409094402400e8edb910d79fd6239')[0]),
					'flag': helper.set_entry_command_string('${string/#substring/replacement}'),
					'description': [
						Markup('If $substring matches front end of $string, substitute $replacement for $substring'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4702785c1d3f4a9eb6e3c2330c4850a4')[0]),
					'flag': helper.set_entry_command_string('${string/%substring/replacement}'),
					'description': [
						Markup('If $substring matches back end of $string, substitute $replacement for $substring'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('25b9ea83371c484aac8914ea013bbcd9')[0]),
					'flag': helper.set_entry_command_string("expr match \"$string\" '$substring'"),
					'description': [
						Markup('Length of matching $substring* at beginning of $string'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('779257393f5f4ad1b259fb83dfb2acd6')[0]),
					'flag': helper.set_entry_command_string("expr \"$string\" : '$substring'"),
					'description': [
						Markup('Length of matching $substring* at beginning of $string'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3c565bada4a742839f5611bc01d7a9f6')[0]),
					'flag': helper.set_entry_command_string('expr index \"$string\" $substring'),
					'description': [
						Markup('Numerical position in $string of first character in $substring* that matches [0 if no match, first character counts as position 1]'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a8b8cdfaba6149bc998b2208dd8aaba9')[0]),
					'flag': helper.set_entry_command_string('expr substr $string $position $length'),
					'description': [
						Markup('Extract $length characters from $string starting at $position [0 if no match, first character counts as position 1]'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bc3f06ce233a4d08a358c9a812743b7b')[0]),
					'flag': helper.set_entry_command_string('expr match "$string" \'\($substring\)\''),
					'description': [
						Markup('Extract $substring*, searching from beginning of $string'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f3b797d118594c459a6194cc60f994ba')[0]),
					'flag': helper.set_entry_command_string('expr "$string" : \'\($substring\)\''),
					'description': [
						Markup('Extract $substring* , searching from beginning of $string'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7267bc2a665440c39e645786a0cbbd09')[0]),
					'flag': helper.set_entry_command_string('expr match "$string" \'.*\($substring\)\''),
					'description': [
						Markup('Extract $substring*, searching from end of $string'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dc470fbc4a354be6bbf07adf8e60c105')[0]),
					'flag': helper.set_entry_command_string('expr "$string" : \'.*\($substring\)\''),
					'description': [
						Markup('Extract $substring*, searching from end of $string'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Quoting'),
		'subtitle': '',
		'description': 'The following text shows characters that need to be quoted if you want to use their literal symbols and not their special meaning.',
		'warning': {
			Markup('Everything between double-quotes is taken literally, except <kbd>$&lt;alnum&gt;</kbd> (<kbd>$a</kbd>, <kbd>$1</kbd>) <kbd>`</kbd> and <kbd>"</kbd>, <kbd>\</kbd> and line-breaks.'),
			Markup('Everything between single-quotes is taken literally, except <kbd>\'</kbd>.'),
		},
		'danger': {
			'Using a dollar sign before double-quotation or single-quotation causes some special behavior. $"..." is the same as "..." except that locale translation is done and:wq $\'...\' is similar to $\'...\' except that the quoted string is processed for escape sequences.',
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '6a9a9eb818ac456bbd887bfb6377e529',
		'content': {
			'descriptor': {
				'Symbol',
				'Literal Meaning'
			},
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('a7ac942b65914dd49f9e719ddce52dbf')[0]),
					'flag': helper.set_entry_command_string(';'),
					'description': [
						Markup('Command seperator'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3c976cb02e7e4984924b1f51bd16191b')[0]),
					'flag': helper.set_entry_command_string('&'),
					'description': [
						Markup('Background execution'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('24c5096c32624affb8f821e0f619092f')[0]),
					'flag': helper.set_entry_command_string('()'),
					'description': [
						Markup('Command grouping'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4e3a5664b8a3426cba190a8fd31412fa')[0]),
					'flag': helper.set_entry_command_string('|'),
					'description': [
						Markup('Pipe'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('83ca2523336242228b814a2f5cfdfb66')[0]),
					'flag': helper.set_entry_command_string('< > &'),
					'description': [
						Markup('Redirection symbols'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a500a0662af3440b9582bb78ff79a9df')[0]),
					'flag': helper.set_entry_command_string('* ? [ ] ~ + - @ !'),
					'description': [
						Markup('Filename metacharacters'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('92e87aee078d4da3825f1c2ebace424e')[0]),
					'flag': helper.set_entry_command_string('" \' \\'),
					'description': [
						Markup('Used in quoting characters'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8ab3ba0de99d461eadc0dda268248811')[0]),
					'flag': helper.set_entry_command_string('$'),
					'description': [
						Markup('Variable, command or arithmetic substituion'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('983bb4d122294a36b5dbf3b7c07a7b69')[0]),
					'flag': helper.set_entry_command_string('#'),
					'description': [
						Markup('Start a command that ends on a linebreak'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6430807db0b649cd935564f9b61897e9')[0]),
					'flag': helper.set_entry_command_string('space tab newline'),
					'description': [
						Markup('Word seperators'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Command Parameters'),
		'subtitle': '',
		'description': 'Command parameters, also known as arguments, are used when invoking a Bash script.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'dc65e4c43d99490886e2d5577759afec',
		'content': {
			'descriptor': {
				'Command',
				'Description'
			},
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('4ede025faa544a489812999a2a5b9484')[0]),
					'flag': helper.set_entry_command_string('$0'),
					'description': [
						Markup('Name of the script itself'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e883e5374eec4ca5abe8b04c377fc2de')[0]),
					'flag': helper.set_entry_command_string('$1 … $9'),
					'description': [
						Markup('Parameter 1 ... 9'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('903bbe364317400eb198ecc02b9c01c7')[0]),
					'flag': helper.set_entry_command_string('${10} ... ${nn}'),
					'description': [
						Markup('Positional parameter 10 or greater'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6bb1d531a5bb4200b1c9daee1d6243c3')[0]),
					'flag': helper.set_entry_command_string('$*'),
					'description': [
						Markup('Expands to the positional parameters, starting from one'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c29b5267291d45e68bbe42679d439e97')[0]),
					'flag': helper.set_entry_command_string('$-'),
					'description': [
						Markup('Current options'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a0e431b3d58141de937c8ec4a1bc339d')[0]),
					'flag': helper.set_entry_command_string('$_'),
					'description': [
						Markup('Contains the absolute file name of the shell or script being executed'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7cc8324d67be466ebf04db8b5c71db1e')[0]),
					'flag': helper.set_entry_command_string('$$'),
					'description': [
						Markup('Process id of the shell'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f764dd8c7ab2482da0444931fbe42c44')[0]),
					'flag': helper.set_entry_command_string('$?'),
					'description': [
						Markup('Exit status of the most recently executed command'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8a575f4daf1e48aabe65447b647f0ecc')[0]),
					'flag': helper.set_entry_command_string('$@'),
					'description': [
						Markup('All arguments as separate words'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3bb939ae4c12480dadab6c2d1b18419c')[0]),
					'flag': helper.set_entry_command_string('$#'),
					'description': [
						Markup('Number of arguments'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e86c18d2bc0d44518b4cff445baf581d')[0]),
					'flag': helper.set_entry_command_string('$!'),
					'description': [
						Markup('PID of most recently backgrounded process'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('History Expansion'),
		'subtitle': '',
		'description': 'Enables use and manipulation of previous commands.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f6e277806ad045b0b110d171cdbe13fb',
		'content': {
			'descriptor': {
				'Command',
				'Description'
			},
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('2491f8e5ca6d4f968bf2506242a13111')[0]),
					'flag': helper.set_entry_command_string('!'),
					'description': [
						Markup('Starts a history substitution'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b7eaac2541dd409cb1a81fb40a75b266')[0]),
					'flag': helper.set_entry_command_string('!!'),
					'description': [
						Markup('Refers to the last command'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f7f72313829e4be78ae021289a803d32')[0]),
					'flag': helper.set_entry_command_string('!n'),
					'description': [
						Markup('Refers to the <n>-th command line'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('87d9154e03b94620bc4f21a78d4961f1')[0]),
					'flag': helper.set_entry_command_string('!-n'),
					'description': [
						Markup('Refers to the current command line minus <n>'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fe4daacb82104b8980a331942bbbd3a3')[0]),
					'flag': helper.set_entry_command_string('!string'),
					'description': [
						Markup('Refers to the most recent command starting with <string>'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('60479b4c32434839940d67c8545b5795')[0]),
					'flag': helper.set_entry_command_string('!string:p'),
					'description': [
						Markup('Print out the command that !string would run (also adds it as the latest command in the command history)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6cc2f59f90bb492d8a9b3879f5b0a2e8')[0]),
					'flag': helper.set_entry_command_string('!$'),
					'description': [
						Markup('The last word of the previous command (same as Alt + .)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('898da8ed52a94e798143f05b3f8c6afa')[0]),
					'flag': helper.set_entry_command_string('!$:p'),
					'description': [
						Markup('Print out the word that !$ would substitute'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e7499cf5cdc342b6b57d9a166b80b1eb')[0]),
					'flag': helper.set_entry_command_string('!*'),
					'description': [
						Markup('The previous command except for the last word (e.g. if you type ‘_find somefile.txt /’, then !* would give you ‘_find somefile.txt’)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('10cb16f7add24978bd87bca652cf5ad9')[0]),
					'flag': helper.set_entry_command_string('!*:p'),
					'description': [
						Markup('Print out what !* would substitute'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3227a5fc038143218e92dfd661952532')[0]),
					'flag': helper.set_entry_command_string('!?string?'),
					'description': [
						Markup('Refers to the most recent command containing <string> (the ending ? is optional)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('22b96257a273432f8bead2bdebf5a814')[0]),
					'flag': helper.set_entry_command_string('^string1^string2^'),
					'description': [
						Markup('Quick substitution. Repeats the last command, replacing <string1> with <string2>'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('08ad155d36d649b6a4561bcfbc8f40a1')[0]),
					'flag': helper.set_entry_command_string('!#'),
					'description': [
						Markup('Refers to the entire command line typed so far'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Variable Operations'),
		'subtitle': 'Parameter Expansions',
		'description': Markup(''),
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '55dc47818c604f58916b2d829e9d0fec',
		'content': {
			'descriptor': {
				'Expression',
				'Set and not null',
				'Set but null',
				'Unset',
			},
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('5df22ef9bde94ac2b352c1b1d223f85f')[0]),
					'flag': helper.set_entry_command_string('${parameter:-word}'),
					'description': [
						Markup('Substitute parameter'),
						Markup('Substitute word'),
						Markup('Substitute word'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('da72a4333f9c48a6af78a4e794fc20c9')[0]),
					'flag': helper.set_entry_command_string('${parameter-word}'),
					'description': [
						Markup('Substitute parameter'),
						Markup('Substitute null'),
						Markup('Substitute word'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('23cd74bb8fda4c7386068f63bd7adc9c')[0]),
					'flag': helper.set_entry_command_string('${parameter:=word}'),
					'description': [
						Markup('Substitute parameter'),
						Markup('Assign word'),
						Markup('Assign word'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6e6698347ce64f1abfada6194b1d19c8')[0]),
					'flag': helper.set_entry_command_string('${parameter=word}'),
					'description': [
						Markup('Substitute parameter'),
						Markup('Substitute null'),
						Markup('Assign word'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c47cae8658b8467ea551e8ef69498e31')[0]),
					'flag': helper.set_entry_command_string('${parameter:?word}'),
					'description': [
						Markup('Substitute parameter'),
						Markup('Error, exit'),
						Markup('Error, exit'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('468972db0dab46ac9558a4c3fa34d90e')[0]),
					'flag': helper.set_entry_command_string('${parameter?word}'),
					'description': [
						Markup('Substitute parameter'),
						Markup('Substitute null'),
						Markup('Error, exit'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('080c30011f014ab98ab5970dc7a7ecd3')[0]),
					'flag': helper.set_entry_command_string('${parameter:+word}'),
					'description': [
						Markup('Substitute word'),
						Markup('Substitute null'),
						Markup('Substitute null'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a7af7a86d2744a2aa1d1428a6aa34445')[0]),
					'flag': helper.set_entry_command_string('${parameter+word}'),
					'description': [
						Markup('Substitute word'),
						Markup('Substitute word'),
						Markup('Substitute null'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Bash Globbing'),
		'subtitle': '',
		'description': 'Bash cannot recognize RegEx but understand globbing. Globbing is done to filenames by the shell while RegEx is used for searching text.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'e13b66c105ef4c41a93aad34b5248277',
		'content': {
			'descriptor': {
				'Glob',
				'Description'
			},
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('c5b8e1aafb7e4c2c9b917bc2d3144292')[0]),
					'flag': helper.set_entry_command_string('*'),
					'description': [
						Markup('Matches zero or more occurences of a given pattern'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('02cd8a442643440fa68c8cfb40b74086')[0]),
					'flag': helper.set_entry_command_string('?'),
					'description': [
						Markup('Matches zero or one occurences of a given pattern'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5c283855d50a4e02a3245738ffe24d4c')[0]),
					'flag': helper.set_entry_command_string('+'),
					'description': [
						Markup('Matches one or more occurences of a given pattern'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f2aa22fb053547f59b385b4a11b82a9d')[0]),
					'flag': helper.set_entry_command_string('!'),
					'description': [
						Markup('Negates any pattern matches — reverses the pattern so to speak'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Character Classes in BRE'),
		'subtitle': '',
		'description': 'A character class is a pattern you can use instead of a regular expression. They are easier to remember and work with.',
		'warning': {
		},
		'danger': {
		},
		'info': {
			Markup('Character classes has the format <kbd>[:CharClass:]</kbd>'),
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'be049dd423274908a32e57800bfa3e1e',
		'content': {
			'descriptor': {
				'Character Class',
				'Equivalent',
				'Explanation'
			},
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('6cc03df8d0d643f0bb77c23ae5b744ca')[0]),
					'flag': helper.set_entry_command_string('[:lower:]'),
					'description': [
						Markup('[a-z]'),
						'Lowercase letters.',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('11b248bcc8e94697b830c1a042cd8840')[0]),
					'flag': helper.set_entry_command_string('[:upper:]'),
					'description': [
						Markup('[A-Z]'),
						'Uppercase letters.',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fcfdc499c87f41d6a6ed22aadfdcf35e')[0]),
					'flag': helper.set_entry_command_string('[:alpha:]'),
					'description': [
						Markup('[A-Za-z]'),
						'Alphabetic letters, both upper- and lowercase.',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ff6b16dadb1c4d19a41fc326459c36e3')[0]),
					'flag': helper.set_entry_command_string('[:digit:]'),
					'description': [
						Markup('[0-9]'),
						'Numbers 0-9.',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a0d4e72410f144b89fcd66e1864da611')[0]),
					'flag': helper.set_entry_command_string('[:alnum:]'),
					'description': [
						Markup('[a-zA-Z0-9]'),
						'Alphanumeric: both letters (upper- + lowercase) and digits.',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('02225d771fae4c89b85d8910cc858e25')[0]),
					'flag': helper.set_entry_command_string('[:xdigit:]'),
					'description': [
						Markup('[0-9A-Fa-f]'),
						'Hexadecimal digits.',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2f4fda204f374a2e9d5979a0b31ef231')[0]),
					'flag': helper.set_entry_command_string('[:space:]'),
					'description': [
						Markup('[ \\t\\n\\r\\f\\v]'),
						'Whitespace. Spaces, tabs, newline and similar.',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e42a7fb7526d482181f6c3db2263384e')[0]),
					'flag': helper.set_entry_command_string('[:punct:]'),
					'description': [
						Markup(''),
						'Symbols (minus digits and letters).',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('615bf32552144aecbac7bbcbd53b3e31')[0]),
					'flag': helper.set_entry_command_string('[:print:]'),
					'description': [
						Markup('[[:graph] ]'),
						'Printable characters (spaces included).',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('341f563cd85f4dc8b75ccf4be06aee7d')[0]),
					'flag': helper.set_entry_command_string('[:blank:]'),
					'description': [
						Markup('[ \\t]'),
						'Space and tab characters only.',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cf21a81796264b22b4b5793c7673ef17')[0]),
					'flag': helper.set_entry_command_string('[:graph:]'),
					'description': [
						Markup('[^ [:cntrl:]]'),
						'Graphically printable characters excluding space.',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('51b0e026c08f4610a6d09bf7b07aa896')[0]),
					'flag': helper.set_entry_command_string('[:cntrl:]'),
					'description': [
						Markup(''),
						'Control characters. Non-printable characters.',
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Flow Control'),
		'subtitle': '',
		'description': 'Flow control structures in Bash are straight forward, albeit Bash is unforgiving if you get the syntax wrong.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '4b38656715454e05998bb90a6811bfe2',
		'content': {
			'descriptor': {
				'Keyword',
				'Description'
			},
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('0994c38ae2d3465f95d0f70834dc7772')[0]),
					'flag': helper.set_entry_command_string('if'),
					'description': [
						Markup('Test a condition.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b542502e8fc444de8a6e56366ac80e17')[0]),
					'flag': helper.set_entry_command_string('else'),
					'description': [
						Markup('Test a condition and use a fallback if the test fails.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cbb44143e95c40eb880ff9dc98382be3')[0]),
					'flag': helper.set_entry_command_string('elif'),
					'description': [
						Markup('Provides additional testing plus a fallback if all tests fail. You may skip the elif conditions or add as many in-between as you like. Similarly, you may skip the else fallback'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cd4b565d8aff421cb09c47c1407abbbe')[0]),
					'flag': helper.set_entry_command_string('for'),
					'description': [
						Markup('Iterate over a sequence, a list or anything as far as the imagination goes'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b4e85bb418584b0b82306ad1860f55c7')[0]),
					'flag': helper.set_entry_command_string('while'),
					'description': [
						Markup('While a condition is true - repeat until that condition is no longer true'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7c7f50534b044514a95f618307f4a8b8')[0]),
					'flag': helper.set_entry_command_string('until'),
					'description': [
						Markup('The inverse of the while loop - as long as the test-command fails, the until-loop continues'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('24ab31603d8a48438542ad69666266c1')[0]),
					'flag': helper.set_entry_command_string('select'),
					'description': [
						Markup('Used for easy menu generation. Any statement within can be another select construct, thus enabling sub-menu creation'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0fa14021973a4fa192cb60338f10394d')[0]),
					'flag': helper.set_entry_command_string('case'),
					'description': [
						Markup('Alternative if-branching. Each case is an expression which matches a given pattern (i.e., a case)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Overview of Bash Symbols'),
		'subtitle': '',
		'description': 'Here we have gathered a collection of all arcane syntax along with a brief description. A bunch of these symbols are repeated from earlier but many are new - this is a good starting point if you are new to the language.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-12 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'b9cdf2466ed049488f347eecd5c84347',
		'content': {
			'descriptor': {
				'Builtin',
				'Description'
			},
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('1ee61de0731845f4bbbaa9f9339cae6f')[0]),
					'flag': helper.set_entry_command_string('#'),
					'description': [
						Markup('Used for comments'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('79c854c45ffc4f99806a59b74a341eaf')[0]),
					'flag': helper.set_entry_command_string('$'),
					'description': [
						Markup('Used for parameters and variables. Has a bunch of edge cases'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('79c8e976dc0d4c9aa777a589975ab38a')[0]),
					'flag': helper.set_entry_command_string('( )'),
					'description': [
						Markup('Is used for running commands in a subshell'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c663e41f59234a9c8baf5dd35a788bde')[0]),
					'flag': helper.set_entry_command_string('$( )'),
					'description': [
						Markup('Is used for saving output of commands that are send to run in a subshell'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('70c2eaeb186447079966b193456c13d7')[0]),
					'flag': helper.set_entry_command_string('(( ))'),
					'description': [
						Markup('Is used for arithmetic'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('add6ed1fe50e4c628085828dd59db649')[0]),
					'flag': helper.set_entry_command_string('$(( ))'),
					'description': [
						Markup('Is used for retrieving the output of arithmetic expressions, either for usage with a command or to save the output in a variable.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('285321ca0c4c47ab9597fb47f26f053a')[0]),
					'flag': helper.set_entry_command_string('$[]'),
					'description': [
						Markup('Deprecated integer expansion construct which is replaced by $(( )). Evaluates integers between the square brackets'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4fd6e730c42b42de9785b87772019887')[0]),
					'flag': helper.set_entry_command_string('[ ]'),
					'description': [
						Markup('Is used for testing and is a built-in. Is useful in some cases for filename expansion and string manipulation.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('41bf5307321148769e7206dd8dac8ea3')[0]),
					'flag': helper.set_entry_command_string('[[ ]]'),
					'description': [
						Markup('Is used for testing. This is the one you should use unless you can think of a reason not to.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c694b065a07c4c2d85903696fac55eac')[0]),
					'flag': helper.set_entry_command_string('<( )'),
					'description': [
						Markup('Used for process substitution and is similar to a pipe. Can be used whenever a command expects a file and you can use multiple at once.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c74ac32ae7cc473a9777a5eca3d10f63')[0]),
					'flag': helper.set_entry_command_string('{ }'),
					'description': [
						Markup('Is used for expansion of sequences'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fe9e2b30412d4d84847622221ed1cada')[0]),
					'flag': helper.set_entry_command_string('${ }'),
					'description': [
						Markup('Is used for variable interpolation and string manipulation'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e432340cc5444ce295de5edf713e089c')[0]),
					'flag': helper.set_entry_command_string('|'),
					'description': [
						Markup('Is a pipe which is used for chaining commands together'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3e5a6daf42a741e8bb1f85e0b611f5f9')[0]),
					'flag': helper.set_entry_command_string('<'),
					'description': [
						Markup('Used for feeding input to commands from a file'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('27aa5c65955047e6b1c97d0a3f3e8c83')[0]),
					'flag': helper.set_entry_command_string('>'),
					'description': [
						Markup('Used for sending output to a file and erasing any previous content in that file.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7a4063bf8d0e4dffaa8bd6838fdee4cd')[0]),
					'flag': helper.set_entry_command_string('||'),
					'description': [
						Markup('Logical or'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3bc1b1e66da64fb3a2bb14809dd265e5')[0]),
					'flag': helper.set_entry_command_string('&&'),
					'description': [
						Markup('Logical and'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ec758285130948d1b8fd38c096bdce52')[0]),
					'flag': helper.set_entry_command_string('-'),
					'description': [
						Markup('Used for option prefixes'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('09b0b15fcd2b4c238608aca1f77060d1')[0]),
					'flag': helper.set_entry_command_string('--'),
					'description': [
						Markup('Used for the long-option prefixes'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3a112fc481bb41fcbcfe7c03d6693ed3')[0]),
					'flag': helper.set_entry_command_string('&'),
					'description': [
						Markup('Used to send a job to the background'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d43f594603fd44e5b162bacfc612bf27')[0]),
					'flag': Markup(helper.set_entry_command_string('&lt;&lt;WORD</kbd><br><kbd>&lt;&lt;-WORD</kbd><br><kbd>&lt;&lt;\'WORD\'</kbd><br><kbd>&lt;&lt;-\'WORD\'')),
					'description': [
						Markup('Is used for heredocs'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ccaf4ea74971445e89ad956645fde857')[0]),
					'flag': helper.set_entry_command_string('<<<'),
					'description': [
						Markup('Is used for herestrings'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e78fbf2145df417296a129812b027451')[0]),
					'flag': helper.set_entry_command_string('>>'),
					'description': [
						Markup('Is used to append output to a file'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('318cbc76598a4f6295b0a6d10ca38dcf')[0]),
					'flag': helper.set_entry_command_string('\' \''),
					'description': [
						Markup('Single quotes are used to preserve the literal value'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1b5a8d5c939043f6ab4a63c460bbe6d1')[0]),
					'flag': helper.set_entry_command_string('" "'),
					'description': [
						Markup('Double quotes are used to preserve the literal value of all characters except $, ` ` and \\'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2a734964f1274141945f36448c69b98f')[0]),
					'flag': helper.set_entry_command_string('\\'),
					'description': [
						Markup('Backslash is used to escape otherwise interpreted symbols/characters which has a special meaning'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1149d92de01a4d898e8a28a5bb9521ea')[0]),
					'flag': helper.set_entry_command_string('/'),
					'description': [
						Markup('Used for seperating the components of a filename'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('608b3454f25742279f0b5e557cc70298')[0]),
					'flag': helper.set_entry_command_string(':'),
					'description': [
						Markup('Similar to a NOP – a do nothing operation. It is a shell builtin with an exit status of true'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2c98c90718fe48c6a8f3460c97f65a74')[0]),
					'flag': helper.set_entry_command_string(';'),
					'description': [
						Markup('Used to seperate commands intended to run sequentally'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('99666a78a6f5493baf411c13218410d4')[0]),
					'flag': helper.set_entry_command_string(','),
					'description': [
						Markup('Used for linking together arithmetic operations. All are evalutated but only the last is returned'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1a9fa0a275fd48919eb5bff4e2104a05')[0]),
					'flag': helper.set_entry_command_string('.'),
					'description': [
						Markup('Represents the current directory'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e6dc9494fc08410e83da8974eca04184')[0]),
					'flag': helper.set_entry_command_string('..'),
					'description': [
						Markup('Represents parent directory'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2fa99ae5c79647dcb60df5114c4ab30c')[0]),
					'flag': helper.set_entry_command_string('~'),
					'description': [
						Markup('Expands to home directory'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('623ed7fae8544e8aa329f69d0b047121')[0]),
					'flag': helper.set_entry_command_string('` `'),
					'description': [
						Markup('Is deprecated and should not be used. Read further in its respective section'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Bash Builtins'),
		'subtitle': '',
		'description': 'Shell builins are built into Bash are often very (if not extremely) fast compared to external programs. Some of the builtins are inherited from the Bourne Shell (sh) — these inherited commands will also work in the original Bourne Shell.',
		'warning': {
		},
		'danger': {
		},
		'columns': 'col-lg-12 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'aa2b161266a04226a786758de5d9e2b2',
		'content': {
			'descriptor': {
				'Symbol',
				'Usage'
			},
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('27c687992ff241a799b4f45bb8c480e3')[0]),
					'flag': helper.set_entry_command_string(':'),
					'description': [
						Markup('Equivalent to true'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5895e7284dfa4f6987f7b133a5e7aa00')[0]),
					'flag': helper.set_entry_command_string('.'),
					'description': [
						Markup('Reads and executes commands from a designated file in the current shell'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5d2aa78d1ac24b15b1256714214b7c0e')[0]),
					'flag': helper.set_entry_command_string('['),
					'description': [
						Markup('Is a synonym for test but requires a final argument of ]'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2f44417bf8fe4228a2956a7aaa636c40')[0]),
					'flag': helper.set_entry_command_string('alias'),
					'description': [
						Markup('Defines an alias for the specified command'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('088fcbaed7ae4e949fb76ea39b843311')[0]),
					'flag': helper.set_entry_command_string('bg'),
					'description': [
						Markup('Resumes a job in background mode'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b0579eebcb404fca9478c8211590dda8')[0]),
					'flag': helper.set_entry_command_string('bind'),
					'description': [
						Markup('Binds a keyboard sequence to a read line function or macro'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b2629f90cea0458589667847da79850d')[0]),
					'flag': helper.set_entry_command_string('break'),
					'description': [
						Markup('Exits from a for, while, select, or until loop'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2d95141e230e4340b29180ac6e600a61')[0]),
					'flag': helper.set_entry_command_string('builtin'),
					'description': [
						Markup('Executes the specified shell built-in command'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1885f257e16b4afb9c5649ba979fcc16')[0]),
					'flag': helper.set_entry_command_string('caller'),
					'description': [
						Markup('Returns the context of any active subroutine call'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2dfe8e1a074b40b7822db86ec6b28219')[0]),
					'flag': helper.set_entry_command_string('case'),
					'description': [
						Markup('Used to simplify complex conditionals'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('18c6210407ec415cb67b3048a83eccf7')[0]),
					'flag': helper.set_entry_command_string('cd'),
					'description': [
						Markup('Changes the current directory to the specified directory'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('15591c508ab440cbad7188689de48159')[0]),
					'flag': helper.set_entry_command_string('command'),
					'description': [
						Markup('Executes the specified command without the normal shell lookup'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7f5cc3d3d1c84f26a3089effceba24d5')[0]),
					'flag': helper.set_entry_command_string('compgen'),
					'description': [
						Markup('Generates possible completion matches for the specified word'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f88889b9212b4f9ab3759916ef35a892')[0]),
					'flag': helper.set_entry_command_string('complete'),
					'description': [
						Markup('Displays how the specified words would be completed'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6eef0888b5ad414285f5f837afd55b51')[0]),
					'flag': helper.set_entry_command_string('comopt'),
					'description': [
						Markup('Print or change the completion options for a command'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a5f3a92afd8c41d993b2c38a53f6779b')[0]),
					'flag': helper.set_entry_command_string('continue'),
					'description': [
						Markup('Resumes the next iteration of a for, while, select, or until loop'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('124e30fcf1aa4f24bc6d445176f067b2')[0]),
					'flag': helper.set_entry_command_string('declare'),
					'description': [
						Markup('Declares a variable or variable type'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fc68b73b9be9483b8ddb9c5ac43759d3')[0]),
					'flag': helper.set_entry_command_string('dirs'),
					'description': [
						Markup('Displays a list of currently remembered directories'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4d15a54d2e05476d899e806c4715f957')[0]),
					'flag': helper.set_entry_command_string('disown'),
					'description': [
						Markup('Removes the specified jobs from the jobs table for the process'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('55484a0df39248caa5b53e1f9d00aa86')[0]),
					'flag': helper.set_entry_command_string('echo'),
					'description': [
						Markup('Displays the specified string to STDOUT'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('705ebe693f41431a894b4e6b93752183')[0]),
					'flag': helper.set_entry_command_string('enable'),
					'description': [
						Markup('Enables or disables the specified built-in shell command'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e15033550f524f82a91f3cc33091ee8d')[0]),
					'flag': helper.set_entry_command_string('eval'),
					'description': [
						Markup('Concatenates the specified arguments into a single command, and executes the command.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a476061065dc4f0fb2239b1e851c546e')[0]),
					'flag': helper.set_entry_command_string('exec'),
					'description': [
						Markup('Replaces the shell process with the specified command'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cf83ef8c6015491ea326a45148c9fece')[0]),
					'flag': helper.set_entry_command_string('exit'),
					'description': [
						Markup('Forces the shell to exit with the specified exit status'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('145292a9b9174b55979080259da7062a')[0]),
					'flag': helper.set_entry_command_string('export'),
					'description': [
						Markup('Sets the specified variables to be available for child shell processes'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4a0ff445435e4328b17f2f03b9b132d7')[0]),
					'flag': helper.set_entry_command_string('fc'),
					'description': [
						Markup('Selects a list of commands from the history list'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8e4d76d4da55406f9af27f956a04434b')[0]),
					'flag': helper.set_entry_command_string('fg'),
					'description': [
						Markup('Resumes a job in foreground mode'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9f81202dcfca490db1959cabaa08e624')[0]),
					'flag': helper.set_entry_command_string('getopts'),
					'description': [
						Markup('Parses the specified positional parameters'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0d6c1a72728847c3be54f65f6ad7ec5b')[0]),
					'flag': helper.set_entry_command_string('hash'),
					'description': [
						Markup('Finds and remembers the full pathname of the specified command'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('92d6860e810b46fc94616807b8f5cb03')[0]),
					'flag': helper.set_entry_command_string('help'),
					'description': [
						Markup('Displays a help file'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('738ebdd78a494efc93a34c1a2bec7472')[0]),
					'flag': helper.set_entry_command_string('history'),
					'description': [
						Markup('Displays the command history'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1bc2a746ca4844ffacd392372a550cc2')[0]),
					'flag': helper.set_entry_command_string('if'),
					'description': [
						Markup('Used for branching'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('072e871c64cb4a77876897006e0ec075')[0]),
					'flag': helper.set_entry_command_string('jobs'),
					'description': [
						Markup('Lists active jobs'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('90a49f71dcf04bc5835ad29338711414')[0]),
					'flag': helper.set_entry_command_string('kill'),
					'description': [
						Markup('Sends a system signal to the specified process ID (PID)'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a595c344243a4151a402325d673ac0cd')[0]),
					'flag': helper.set_entry_command_string('let'),
					'description': [
						Markup('Evaluates each argument in a mathematical expression'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a4faf8a8709a473694ebd92036f0e017')[0]),
					'flag': helper.set_entry_command_string('local'),
					'description': [
						Markup('Creates a limited-scope variable in a function'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('25ebf5b578f04468a165fc7839cef058')[0]),
					'flag': helper.set_entry_command_string('logout'),
					'description': [
						Markup('Exits a login shell'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d348b6be6bc940349d3188e1cb4b3d46')[0]),
					'flag': helper.set_entry_command_string('mapfile'),
					'description': [
						Markup('Reads lines from standard input into an indexed array'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d6f97c31808340dd8da37d700b62f8d5')[0]),
					'flag': helper.set_entry_command_string('popd'),
					'description': [
						Markup('Removes entries from the directory stack'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5bbc9c80ac254cb887c937e55fcd4e0b')[0]),
					'flag': helper.set_entry_command_string('printf'),
					'description': [
						Markup('Displays text using formatted strings'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7a0481bf5fc44f898e263c0df4c21b17')[0]),
					'flag': helper.set_entry_command_string('pushd'),
					'description': [
						Markup('Adds a directory to the directory stack'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('be942bbf942d4fdba3e80da4cd539ebf')[0]),
					'flag': helper.set_entry_command_string('pwd'),
					'description': [
						Markup('Displays the pathname of the current working directory'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c2f4c8a0e605431da8c6443d7981b625')[0]),
					'flag': helper.set_entry_command_string('read'),
					'description': [
						Markup('Reads one line of data from STDIN, and assigns it to a variable'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8b86add6297b4ba0b13381ac39dc0970')[0]),
					'flag': helper.set_entry_command_string('readonly'),
					'description': [
						Markup('Reads one line of data from STDIN, and assigns it to a variable that can’t be changed.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e5c4aaca26d4455cbd46feac2f74005a')[0]),
					'flag': helper.set_entry_command_string('return'),
					'description': [
						Markup('Forces a function to exit with a value that can be retrieved by the calling script'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('234cf21d90a14e8994c9c686915160eb')[0]),
					'flag': helper.set_entry_command_string('set'),
					'description': [
						Markup('Sets and displays environment variable values and shell attributes'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f690f92e191643249fc06188983edd08')[0]),
					'flag': helper.set_entry_command_string('shift'),
					'description': [
						Markup('Rotates positional parameters down one position'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1a8e1d4598064109b95a0c826e3a422a')[0]),
					'flag': helper.set_entry_command_string('shopt'),
					'description': [
						Markup('Toggles the values of variables controlling optional shell behavior'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('adf3011bb8874483a1e59b6d98681bab')[0]),
					'flag': helper.set_entry_command_string('source'),
					'description': [
						Markup('Reads and executes commands from a designated file in the current shell'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9e3c8c95df9d415592f5185413cddc45')[0]),
					'flag': helper.set_entry_command_string('suspend'),
					'description': [
						Markup('Suspends the execution of the shell until a SIGCONT signal is received'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2d8de362a8db4a9eb524d80b8065c63c')[0]),
					'flag': helper.set_entry_command_string('test'),
					'description': [
						Markup('Returns an exit status of 0 or 1 based on the specified condition'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6d192f8db96242098bc4877a8005cda0')[0]),
					'flag': helper.set_entry_command_string('times'),
					'description': [
						Markup('Displays the accumulated user and system shell time'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('52e85652ac804e77a15ff0f1a2d1b39b')[0]),
					'flag': helper.set_entry_command_string('trap'),
					'description': [
						Markup('Executes the specified command if the specified system signal is received'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('04773fc5992540eb9dfb1aacb0ca1381')[0]),
					'flag': helper.set_entry_command_string('type'),
					'description': [
						Markup('Displays how the specified words would be interpreted if used as a command'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c516cf35cb394f1d88ff0431b4ef735f')[0]),
					'flag': helper.set_entry_command_string('typeset'),
					'description': [
						Markup('Declares a variable or variable type'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a43a00003b29482a9c87e7907a797965')[0]),
					'flag': helper.set_entry_command_string('ulimit'),
					'description': [
						Markup('Sets a limit on the specific resource for system users'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f2eee0f2fe5646b8b93964a925dce679')[0]),
					'flag': helper.set_entry_command_string('umask'),
					'description': [
						Markup('Sets default permissions for newly created files and directories'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('70f5941642f342c4a362285bc28da6ad')[0]),
					'flag': helper.set_entry_command_string('unalias'),
					'description': [
						Markup('Removes specified alias'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ad0798c816ed44458ac98b6994f74f7e')[0]),
					'flag': helper.set_entry_command_string('unset'),
					'description': [
						Markup('Removes the specified environment variable or shell attribute'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1506e195b766446fbbfc35af43bfc633')[0]),
					'flag': helper.set_entry_command_string('until'),
					'description': [
						Markup('Loop that is very similar to the while-loop except that it executes until the test-command executes succesfully. As long as the test-command fails, the until-loop continues.'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('94027ec5a6b14eaa8cfce99b4a485cc9')[0]),
					'flag': helper.set_entry_command_string('wait'),
					'description': [
						Markup('Make the shell wait for a job to finish'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6ff932fe3bad47368486c8f761ba3186')[0]),
					'flag': helper.set_entry_command_string('while'),
					'description': [
						Markup('Waits for the specified process to complete, and returns the exit status'),
					],
					'example': helper.example_path(),
					'ext_link': '',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
]
resources = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'link': 'https://en.wikipedia.org/wiki/Shellshock_(software_bug)',
			'title': 'Shellshock',
			'description': Markup('A group of severe privilege escalation vulnerabilities existing in the wild for about 25 years'),
		},
		{
			'link': 'http://mywiki.wooledge.org/BashGuide',
			'title': 'Greg\'s Wiki 🧠',
			'description': Markup('A lot of great articles teaching good practices and how to avoid pitfalls'),
			'screencapture': 'resources/graphic/link_screen_captures/mywiki_wooledge_org_bash_pitfalls.png'
		},
		{
			'link': 'https://www.shellcheck.net/',
			'title': 'Shellcheck',
			'description': Markup('A linter to check your shellscripts. Extremely useful'),
			'screencapture': 'resources/graphic/link_screen_captures/www_shellcheck_net.png'
		},
		{
			'link': 'https://explainshell.com/',
			'title': 'Explain Shell 🐚',
			'description': Markup('If you have wondered how a fork-bomb or any similar obscure command is parsed and executed'),
			'screencapture': 'resources/graphic/link_screen_captures/www_explainshell_com.png'
		},
		{
			'link': 'https://www.gnu.org/savannah-checkouts/gnu/bash/manual/bash.html',
			'title': 'GNU Bash Manual',
			'description': Markup('Perhaps the most comphehensive manual out there'),
			'screencapture': 'resources/graphic/link_screen_captures/gnu_org_savannah_checkouts_gnu_bash_manual_bash.png',
			'footer': 'Everything you need really.'
		},
		{
			'link': 'https://google.github.io/styleguide/shellguide.html',
			'title': 'Shell Style Guide',
			'description': Markup('Google\'s style guide for shellscripts'),
			'screencapture': 'resources/graphic/link_screen_captures/google_github_io_styleguide_shellguide.png',
		},
		{
			'link': 'https://apenwarr.ca/log/20110228',
			'title': 'Insufficiently known POSIX shell features',
			'screencapture': 'resources/graphic/link_screen_captures/apenwarr_ca.png',
		},
		{
			'link': 'http://www.pixelbeat.org/programming/shell_script_mistakes.html',
			'title': 'Shellscript Mistakes',
			'screencapture': 'resources/graphic/link_screen_captures/pixelbeat_org.png',
		},
	)
]
affiliate_products = [
	ResourceCollector.recieve_resources_from_dicts(
		{
			'title': Markup('Bash Pocket Guide'),
			'affiliate_link': Markup(
				'<a target="_blank" rel="nofollow noopener" href="https://www.amazon.com/gp/offer-listing/1491941596/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1491941596&linkCode=am2&tag=cheatsheet01-20&linkId=df0ea5b4a57a7727ee805cab61cd7a7a"><img width="91" height="150" alt="Amazon affiliate product" '
				'border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=1491941596&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet01-20" ></a>'),
			'footer': Markup('Concise little pocket reference'),
			'description': '',
		},
		{
			'title': Markup('UNIX and Linux System Administration Handbook'),
			'affiliate_link': Markup(
				'<a target="_blank" rel="nofollow noopener" href="https://www.amazon.com/gp/offer-listing/0134277554/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=0134277554&linkCode=am2&tag=cheatsheet01-20&linkId=66fd5de4389733e6aa708b93bb3455b4"><img width="115" height="150" alt="Amazon affiliate product" '
				'border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=0134277554&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet01-20" ></a>'),
			'footer': Markup(''),
			'description': '',
		},
		{
			'title': Markup('Linux Command Line & Shell Scripting Bible'),
			'affiliate_link': Markup(
				'<a target="_blank" rel="nofollow noopener" href="https://www.amazon.com/gp/offer-listing/1119578884/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=1119578884&linkCode=am2&tag=cheatsheet01-20&linkId=eefa15d9d1d5c345c8336cf464e87138"><img width="122" height="150" alt="Amazon affiliate product" '
				'border="0" src="//ws-na.amazon-adsystem.com/widgets/q?_encoding=UTF8&MarketPlace=US&ASIN=1119578884&ServiceVersion=20070822&ID=AsinImage&WS=1&Format=_SL160_&tag=cheatsheet01-20" ></a>'),
			'footer': Markup('Great for beginners. New edition is on the horizon'),
			'description': '',
		}
	)
]
licensing = [
	Markup('<a href="https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02">Parameter Expansions Table</a>')
]
