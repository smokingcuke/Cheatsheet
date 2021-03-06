import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('jquery', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'jquery'
meta = {
	'title': 'JQuery Cheatsheet',
	'description': 'Selectors · Ajax · Traversing · Effects · CSS Attributes · Utilities · Manipulation',
	'keywords': 'jquery, javascript, typescript, js, vanilla js, frontend, framework, toolset, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/JQuery/',

	'opengraph_title': 'JQuery Cheatsheet',
	'opengraph_description': 'Selectors · Ajax · Traversing · Effects · CSS Attributes · Utilities · Manipulation',
	'opengraph_image': 'opengraph_jquery.png',
	'opengraph_url': 'https://www.cheatsheet.wtf/jquery/',

	'twitter_title': 'JQuery Cheatsheet',
	'twitter_description': 'Selectors · Ajax · Traversing · Effects · CSS Attributes · Utilities · Manipulation',
	'twitter_image': 'twitter_card_jquery.png',
}
information = {
	'tool': 'JQuery',
	'title': 'JQuery Cheatsheet',
	'subtitle': 'This site is a reference for JQuery',
	'description': 'JQuery is a popular free and open-source JavaScript library used for the front-end in web applications. It is designed to simplify HTML DOM and tree traversel and manipulation, as well as event handling, CSS animation and Ajax.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'JQuery',
			[
				helper.characteristics.get('library'),
				helper.characteristics.get('front-end'),
				helper.characteristics.get('web-development'),
			])
	],
	'topic_uris': [
		'library',
		'front-end',
		'web-development',
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
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Attribute Selectors',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '61ab06340f2844b5943cd20cbd408ca0',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('9b038c7502d04c138abd71351c4f266e')[0]),
					'flag': helper.set_entry_command_string('[name|="value"]'),
					'description': [
						Markup('Selects elements that have the specified attribute with a value either equal to a given string or starting with that string followed by a hyphen (-)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-contains-prefix-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5cb62f7caeb24cf1bf0c548631afd21d')[0]),
					'flag': helper.set_entry_command_string('[name*="value"]'),
					'description': [
						Markup('Selects elements that have the specified attribute with a value containing a given substring'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-contains-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1c375e27ef084738a9601d586abdd21a')[0]),
					'flag': helper.set_entry_command_string('[name~="value"]'),
					'description': [
						Markup('Selects elements that have the specified attribute with a value containing a given word, delimited by spaces'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-contains-word-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('80a4671f78434456a5d30e2981fb2e6a')[0]),
					'flag': helper.set_entry_command_string('[name$="value"]'),
					'description': [
						Markup('Selects elements that have the specified attribute with a value ending exactly with a given string. The comparison is case sensitive'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-ends-with-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2dbc6dde6ff448caa60b462a8c23941b')[0]),
					'flag': helper.set_entry_command_string('[name="value"]'),
					'description': [
						Markup('Selects elements that have the specified attribute with a value exactly equal to a certain value'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-equals-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('80808813dd5c46019fa8d00da8450f7c')[0]),
					'flag': helper.set_entry_command_string('[name!="value"]'),
					'description': [
						Markup('Select elements that either don\'t have the specified attribute, or do have the specified attribute but not with a certain value'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-not-equal-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fe112e0c75684b7083f024424b6ded65')[0]),
					'flag': helper.set_entry_command_string('[name^="value"]'),
					'description': [
						Markup('Selects elements that have the specified attribute with a value beginning exactly with a given string'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attribute-starts-with-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e3a758cb567642ae8d39f35697e11095')[0]),
					'flag': helper.set_entry_command_string('[name]'),
					'description': [
						Markup('Selects elements that have the specified attribute, with any value'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/has-attribute-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a58f2f2bbbcf4eb8966d8d742ac07f57')[0]),
					'flag': helper.set_entry_command_string('[name="value"][name2="value2"]'),
					'description': [
						Markup('Matches elements that match all of the specified attribute filters'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/multiple-attribute-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Form Selectors',
		'description': 'Form selectors. Used to select form elements.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'c7cc431e79e64837869d4a110a6f9234',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('da7090cb9e3848d7b4859da7eaece69f')[0]),
					'flag': helper.set_entry_command_string(':button'),
					'description': [
						Markup('Selects all button elements and elements of type button'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/button-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7f9746fa697740709903e12868273b2b')[0]),
					'flag': helper.set_entry_command_string(':checkbox'),
					'description': [
						Markup('Selects all elements of type checkbox'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/checkbox-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a3e160d2f0ae4097a57395436be0d082')[0]),
					'flag': helper.set_entry_command_string(':checked'),
					'description': [
						Markup('Matches all elements that are checked or selected'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/checked-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('16fd9d5cd2ca46edac9ddd70ce557e2e')[0]),
					'flag': helper.set_entry_command_string(':disabled'),
					'description': [
						Markup('Selects all elements that are disabled'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/disabled-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0d5e1e1728b947f1b85974d388477b8e')[0]),
					'flag': helper.set_entry_command_string(':enabled'),
					'description': [
						Markup('Selects all elements that are enabled'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/enabled-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e7cd544c051f42e09b88666471f8055f')[0]),
					'flag': helper.set_entry_command_string(':focus'),
					'description': [
						Markup('Selects element if it is currently focused'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/focus-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b291e2a0d4cc4a97963683ba64a59be5')[0]),
					'flag': helper.set_entry_command_string(':file'),
					'description': [
						Markup('Selects all elements of type file'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/file-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('665110e414f747da835f5a21884bf422')[0]),
					'flag': helper.set_entry_command_string(':image'),
					'description': [
						Markup('Selects all elements of type image'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/image-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ced5c7819bb6451a97c3228c01dae323')[0]),
					'flag': helper.set_entry_command_string(':input'),
					'description': [
						Markup('Selects all input, textarea, select and button elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/input-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6531c50f6343490d806e1bdd0fc14e7b')[0]),
					'flag': helper.set_entry_command_string(':password'),
					'description': [
						Markup('Selects all elements of type password'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/password-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f4aa31f3221b4e94a1db2a97b6d6805f')[0]),
					'flag': helper.set_entry_command_string(':radio'),
					'description': [
						Markup('Selects all elements of type radio'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/radio-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5a4e97a08d004b03a91acae64c0d634b')[0]),
					'flag': helper.set_entry_command_string(':reset'),
					'description': [
						Markup('Selects all elements of type reset'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/reset-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3c1f3d2ba7db485e99cc35015ac89c1a')[0]),
					'flag': helper.set_entry_command_string(':selected'),
					'description': [
						Markup('Selects all elements that are selected'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/selected-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('27b0ada407874ddcb0e0affd3d440345')[0]),
					'flag': helper.set_entry_command_string(':submit'),
					'description': [
						Markup('Selects all elements of type submit'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/submit-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d4386934688d41979416645397d5f2d3')[0]),
					'flag': helper.set_entry_command_string(':text'),
					'description': [
						Markup('Selects all input elements of type text'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/text-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Basic Selectors',
		'description': 'Elementary JQuery selectors',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'fb4cd10ca19446ef8fa20fdc95229471',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('9ff300251c374975a78e4ec8a2d4281b')[0]),
					'flag': helper.set_entry_command_string('*'),
					'description': [
						Markup('Selects all elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/all-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9155f3f600344f8497982b77006f1fcd')[0]),
					'flag': helper.set_entry_command_string('.class'),
					'description': [
						Markup('Selects all elements with the given class'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/class-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bc6e5092bcbe4139b007cb71ecdd5302')[0]),
					'flag': helper.set_entry_command_string('element'),
					'description': [
						Markup('Selects all elements with the given tag name'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/element-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('20805548533647e3bf1493c02cd3cc12')[0]),
					'flag': helper.set_entry_command_string('#id'),
					'description': [
						Markup('Selects a single element with the given id attribute'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/id-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fe7883ef814d4019b7e210de6d052293')[0]),
					'flag': helper.set_entry_command_string('selector1, selectorN, ...'),
					'description': [
						Markup('Selects the combined results of all the specified selectors'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/multiple-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Hidden Selectors',
		'description': 'Used to select all elements that are either hidden or visible',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f98c979263604405b9a4403bd5697971',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('0242f010df784f1b8cbdc10db96e7dfe')[0]),
					'flag': helper.set_entry_command_string(':hidden'),
					'description': [
						Markup('Selects all elements that are hidden'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/hidden-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('56abc8e79d254d28ba04547da3ebf397')[0]),
					'flag': helper.set_entry_command_string(':visible'),
					'description': [
						Markup('Selects all elements that are visible'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/visible-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Basic Filter Selectors',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '400218ea6e764dddbc3a7cce688b3dbf',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('373c37b9b6f94f71999c4962d5b15a96')[0]),
					'flag': helper.set_entry_command_string(':animated'),
					'description': [
						Markup('Select all elements that are in the progress of an animation at the time the selector is run'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/animated-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('18eb9a9090874f2fa618ef2814445c02')[0]),
					'flag': helper.set_entry_command_string(':eq()'),
					'description': [
						Markup('Select the element at index n within the matched set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/eq-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e616cb86391b4b748eb0bf4b78d0fa6b')[0]),
					'flag': helper.set_entry_command_string(':even'),
					'description': [
						Markup('Selects even elements, zero-indexed'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/even-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cc1c13cc0797424fa4b7bbd6f23c7574')[0]),
					'flag': helper.set_entry_command_string(':first'),
					'description': [
						Markup('Selects the first matched DOM element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/first-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7c0e7fe601ff4905aedf4809373b6762')[0]),
					'flag': helper.set_entry_command_string(':gt()'),
					'description': [
						Markup('Select all elements at an index greater than index within the matched set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/gt-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('afb165db8c21469299489101f9dd493b')[0]),
					'flag': helper.set_entry_command_string(':header'),
					'description': [
						Markup('Selects all elements that are headers, like h1, h2, h3 and so on'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/header-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('43378954b420414385668b1c2baec372')[0]),
					'flag': helper.set_entry_command_string(':last'),
					'description': [
						Markup('Selects the last matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/last-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fdaee5475ea549dbbc1c1eb70c809d1e')[0]),
					'flag': helper.set_entry_command_string(':lt()'),
					'description': [
						Markup('Select all elements at an index less than index within the matched set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/lt-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d1c78aadc329489bb467e62f23f1e879')[0]),
					'flag': helper.set_entry_command_string(':not()'),
					'description': [
						Markup('Selects all elements that do not match the given selector'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/not-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d81ab5157a3c4b8ba0849e4d7dd6374e')[0]),
					'flag': helper.set_entry_command_string(':odd'),
					'description': [
						Markup('Selects odd elements, zero-indexed'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/odd-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Child Filter Selectors',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '331d08429cd047078a49ad767fc139ec',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('a653363f15a74548bb94d7f8f2988b18')[0]),
					'flag': helper.set_entry_command_string(':first-child'),
					'description': [
						Markup('Selects all elements that are the first child of their parent'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/first-child-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ae894adf8dc14f83ab9577982591f99f')[0]),
					'flag': helper.set_entry_command_string(':last-child'),
					'description': [
						Markup('Selects all elements that are the last child of their parent'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/last-child-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4ef073b4cfd749fe891345d89893e6ee')[0]),
					'flag': helper.set_entry_command_string(':nth-child()'),
					'description': [
						Markup('Selects all elements that are the nth-child of their parent'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/nth-child-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('24f0e52a6b1f4dd083a3a25626044b0c')[0]),
					'flag': helper.set_entry_command_string(':only-child'),
					'description': [
						Markup('Selects all elements that are the only child of their parent'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/only-child-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Content Filter Selectors',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'ad9f7c067e8a49c098beec12a7683e5b',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('72e7095abceb4107ab302f704ebbe49e')[0]),
					'flag': helper.set_entry_command_string(':contains()'),
					'description': [
						Markup('Select all elements that contain the specified text'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/contains-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d955b3d2f411485db864298bbcbe4982')[0]),
					'flag': helper.set_entry_command_string(':empty'),
					'description': [
						Markup('Select all elements that have no children (including text nodes)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/empty-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0b8a8e9ddfe34a66adf303da3d08777c')[0]),
					'flag': helper.set_entry_command_string(':has()'),
					'description': [
						Markup('Selects elements which contain at least one element that matches the specified selector'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/has-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('14964267f2754b8697181d2f1c9ff234')[0]),
					'flag': helper.set_entry_command_string(':parent'),
					'description': [
						Markup('Select all elements that have at least one child node (either an element or text)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/parent-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Selectors'),
		'subtitle': 'Hierarchy Selectors',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'd288d5dc51fd4f3d817c490e2c387e8b',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('cf7ada5124c24a4c92643a133a7d829c')[0]),
					'flag': helper.set_entry_command_string('parent > child'),
					'description': [
						Markup('Selects all direct child elements specified by "child" of elements specified by "parent"'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/child-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5e43a57108a2407b884726efdf16ca2a')[0]),
					'flag': helper.set_entry_command_string('ancestor descendant'),
					'description': [
						Markup('Selects all elements that are descendants of a given ancestor'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/descendant-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f01e5dcb94164e9a931e24ecd57920c6')[0]),
					'flag': helper.set_entry_command_string('prev + next'),
					'description': [
						Markup('Selects all next elements matching "next" that are immediately preceded by a sibling "prev"'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/next-adjacent-Selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('39a65f80ceb64018ba930be2ca7b79b2')[0]),
					'flag': helper.set_entry_command_string('prev ~ siblings'),
					'description': [
						Markup('Selects all sibling elements that follow after the "prev" element, have the same parent, and match the filtering "siblings" selector'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/next-siblings-selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Effects'),
		'subtitle': 'Basic Effects',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '22cd49efc53644bfb2522538e6ca1b0a',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('6cc840709fd04db1981087885dac91b5')[0]),
					'flag': helper.set_entry_command_string('.hide()'),
					'description': [
						Markup('Hide the matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/hide/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('94389aa637684472869b26e24bf36faf')[0]),
					'flag': helper.set_entry_command_string('.show()'),
					'description': [
						Markup('Display the matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/show/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('436a1e3a0a4e45c98bc9e23ad3b46633')[0]),
					'flag': helper.set_entry_command_string('.toggle()'),
					'description': [
						Markup('Display or hide the matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/toggle/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Effects'),
		'subtitle': 'Custom Effects',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f37acf01dd9f4094845ca02ee39403b0',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('86f317aea9e94b90ac945830ef5c4bca')[0]),
					'flag': helper.set_entry_command_string('.animate()'),
					'description': [
						Markup('Perform a custom animation of a set of CSS properties'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/animate',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b4ad21a872db41729d866d036640c70e')[0]),
					'flag': helper.set_entry_command_string('.clearQueue()'),
					'description': [
						Markup('Remove from the queue all items that have not yet been run'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/clearQueue',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('03d0a264d29d4f4c806ef557e456f685')[0]),
					'flag': helper.set_entry_command_string('.delay()'),
					'description': [
						Markup('Set a timer to delay execution of subsequent items in the queue'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/delay',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3577b82ee3a740db9064ae3c18b88d1a')[0]),
					'flag': helper.set_entry_command_string('.dequeue()'),
					'description': [
						Markup('Execute the next function on the queue for the matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/dequeue',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('55fc572d23284d2283a370c3af07ad97')[0]),
					'flag': helper.set_entry_command_string('jQuery.dequeue()'),
					'description': [
						Markup('Execute the next function on the queue for the matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.dequeue/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('87c99e7d0a7a4912aab0c0fe269a982e')[0]),
					'flag': helper.set_entry_command_string('jQuery.fx.interval'),
					'description': [
						Markup('The rate (in milliseconds) at which animations fire'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.fx.interval',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dd7c26e81b7b4b7d9ac9a63bea8aa17e')[0]),
					'flag': helper.set_entry_command_string('jQuery.fx.off'),
					'description': [
						Markup('Globally disable all animations'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.fx.off',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('be9f21efb7494a9da3c51d6b1167a8ec')[0]),
					'flag': helper.set_entry_command_string('.queue()'),
					'description': [
						Markup('Show or manipulate the queue of functions to be executed on the matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/queue',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('73b6ca3a49ed48bc9df5037cf0576212')[0]),
					'flag': helper.set_entry_command_string('jQuery.queue()'),
					'description': [
						Markup('Show or manipulate the queue of functions to be executed on the matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.queue/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e256a7a6ba05494d8ab7b18a4702b531')[0]),
					'flag': helper.set_entry_command_string('.stop()'),
					'description': [
						Markup('Stop the currently-running animation on the matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/stop',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Effects'),
		'subtitle': 'Fading Effects',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '522d40a9c09944628f42da6b1744238d',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('beea6d143f7546efbf7c29d66b0d1ade')[0]),
					'flag': helper.set_entry_command_string('.fadeIn()'),
					'description': [
						Markup('Display the matched elements by fading them to opaque'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/fadeIn/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('75ce6e0a81f34ff89af0d765df3d5488')[0]),
					'flag': helper.set_entry_command_string('.fadeOut()'),
					'description': [
						Markup('Hide the matched elements by fading them to transparent'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/fadeOut/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('331d5c8d8f0e431d9d6b5a6e89c9bba2')[0]),
					'flag': helper.set_entry_command_string('.fadeTo()'),
					'description': [
						Markup('Adjust the opacity of the matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/fadeTo/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fd872dc8883741dea774bffd368f191e')[0]),
					'flag': helper.set_entry_command_string('.fadeToggle()'),
					'description': [
						Markup('Display or hide the matched elements by animating their opacity'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/fadeToggle/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Effects'),
		'subtitle': 'Sliding Effects',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '0d958d48009943b5b4a0d605e4e3231c',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('47d6976b98994a298ac8c0b322aefc83')[0]),
					'flag': helper.set_entry_command_string('.slideDown()'),
					'description': [
						Markup('Display the matched elements with a sliding motion'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/slideDown',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b00409a608db4535a61f99ca744ebe9f')[0]),
					'flag': helper.set_entry_command_string('.slideToggle()'),
					'description': [
						Markup('Display or hide the matched elements with a sliding motion'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/slideToggle',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('68b010d673a341149e03e9f983b7106d')[0]),
					'flag': helper.set_entry_command_string('.slideUp()'),
					'description': [
						Markup('Hide the matched elements with a sliding motion'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/slideUp',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Attributes (CSS)'),
		'subtitle': 'Attributes',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'f30c769746654d258fd20f68264d188a',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('0e0938d8941541be8af2695a8bbf37dc')[0]),
					'flag': helper.set_entry_command_string('.attr()'),
					'description': [
						Markup('Get the value of an attribute for the first element in the set of matched elements or set one or more attributes for every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/attr/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f220909c83b442c6ad0ace98f780bbd5')[0]),
					'flag': helper.set_entry_command_string('.prop()'),
					'description': [
						Markup('Get the value of a property for the first element in the set of matched elements or set one or more properties for every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prop/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1f750acd99b64acabeae58cc8cbfe13a')[0]),
					'flag': helper.set_entry_command_string('.removeAttr()'),
					'description': [
						Markup('Remove an attribute from each element in the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/removeAttr/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a880e4b7ac494e79b63d3285b46a3ead')[0]),
					'flag': helper.set_entry_command_string('.removeProp()'),
					'description': [
						Markup('Remove a property for the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/removeProp/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e285c896a520407c9f511c8d69bb266b')[0]),
					'flag': helper.set_entry_command_string('.val()'),
					'description': [
						Markup('Get the current value of the first element in the set of matched elements or set the value of every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/val/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Attributes (CSS)'),
		'subtitle': 'CSS Attributes',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '16a367f309654240b0245df0b21d9f6b',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('23e0e4e4f65b443cbcd2e7a423f3dfba')[0]),
					'flag': helper.set_entry_command_string('.addClass()'),
					'description': [
						Markup('Adds the specified class(es) to each element in the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/addClass/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5b4ae0609d62434d92cdb4ed34125ec3')[0]),
					'flag': helper.set_entry_command_string('.css()'),
					'description': [
						Markup('Get the value of a computed style property for the first element in the set of matched elements or set one or more CSS properties for every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/css/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8b9500763c5944008dd0f3fc674e9db9')[0]),
					'flag': helper.set_entry_command_string('jQuery.cssHooks'),
					'description': [
						Markup('Hook directly into jQuery to override how particular CSS properties are retrieved or set, normalize CSS property naming, or create custom properties'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.cssHooks/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7b46d4c2b3434b1498e3bed5aa0533ac')[0]),
					'flag': helper.set_entry_command_string('.hasClass()'),
					'description': [
						Markup('Determine whether any of the matched elements are assigned the given class'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/hasClass/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9d70c06fda864882893e2580d64e7324')[0]),
					'flag': helper.set_entry_command_string('.removeClass()'),
					'description': [
						Markup('Remove a single class, multiple classes, or all classes from each element in the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/removeClass/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('490d0acecca2426f898f541cbef56c44')[0]),
					'flag': helper.set_entry_command_string('.toggleClass()'),
					'description': [
						Markup('Add or remove one or more classes from each element in the set of matched elements, depending on either the class\'s presence or the value of the state argument'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/toggleClass/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Attributes (CSS)'),
		'subtitle': 'Dimension Attributes',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '4995fc9f781847d9b532ab8288c2cec2',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('aa4b809906774dd28ac8137767881738')[0]),
					'flag': helper.set_entry_command_string('.height()'),
					'description': [
						Markup('Get the current computed height for the first element in the set of matched elements or set the height of every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/height/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d77fee4826bd4604837e8c1babdc3ca4')[0]),
					'flag': helper.set_entry_command_string('.innerHeight()'),
					'description': [
						Markup('Get the current computed inner height (including padding but not border) for the first element in the set of matched elements or set the inner height of every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/innerHeight/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2fdcb82505204e25abb764622de1ccb6')[0]),
					'flag': helper.set_entry_command_string('.outerHeight()'),
					'description': [
						Markup('Get the current computed outer height (including padding, border, and optionally margin) for the first element in the set of matched elements or set the outer height of every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/outerHeight/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0a71a7e74960497c9c00de0d91fea38b')[0]),
					'flag': helper.set_entry_command_string('.width()'),
					'description': [
						Markup('Get the current computed width for the first element in the set of matched elements or set the width of every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/width/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dc753c9ea0f14586923d403c3fe3a094')[0]),
					'flag': helper.set_entry_command_string('.innerWidth()'),
					'description': [
						Markup('Get the current computed inner width (including padding but not border) for the first element in the set of matched elements or set the inner width of every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/innerWidth/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b960ef2857b74a57a20ca598eec7e4be')[0]),
					'flag': helper.set_entry_command_string('.outerWidth()'),
					'description': [
						Markup('Get the current computed outer width (including padding, border, and optionally margin) for the first element in the set of matched elements or set the outer width of every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/outerWidth/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Attributes (CSS)'),
		'subtitle': 'Offset Attributes',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '6b70340aafa4480594a312fff0bcbbf9',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('8de26256f65d498c971c5094e4097a96')[0]),
					'flag': helper.set_entry_command_string('.offset()'),
					'description': [
						Markup('Get the current coordinates of the first element, or set the coordinates of every element, in the set of matched elements, relative to the document'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/offset/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b81d47d8f5934c05bf29442e335538b1')[0]),
					'flag': helper.set_entry_command_string('.offsetParent()'),
					'description': [
						Markup('Get the closest ancestor element that is positioned'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/offsetParent/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('19d66fbabd3e4f3f9b4e56c6a9bc4c65')[0]),
					'flag': helper.set_entry_command_string('.position()'),
					'description': [
						Markup('Get the current coordinates of the first element in the set of matched elements, relative to the offset parent'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/position/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('797672521b5f4b9ba7763986823de064')[0]),
					'flag': helper.set_entry_command_string('.scrollLeft()'),
					'description': [
						Markup('Get the current horizontal position of the scroll bar for the first element in the set of matched elements or set the horizontal position of the scroll bar for every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/scrollLeft/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d687c9f16ecb4a63bbaa181ae6b20498')[0]),
					'flag': helper.set_entry_command_string('.scrollTop()'),
					'description': [
						Markup('Get the current vertical position of the scroll bar for the first element in the set of matched elements or set the vertical position of the scroll bar for every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/scrollTop/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Attributes (CSS)'),
		'subtitle': 'Data Attributes',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'a4ada49895a54cb18e08f5f119e00c98',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('2f31906510f74ac8b821d07a385a91ea')[0]),
					'flag': helper.set_entry_command_string('jQuery.data()'),
					'description': [
						Markup('Store arbitrary data associated with the specified element and/or return the value that was set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.data/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cedc85971283426286eaccbc5bd512c1')[0]),
					'flag': helper.set_entry_command_string('.data()'),
					'description': [
						Markup('Store arbitrary data associated with the matched elements or return the value at the named data store for the first element in the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/data/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('34062bed37624a41aef174d971d5dc24')[0]),
					'flag': helper.set_entry_command_string('jQuery.hasData()'),
					'description': [
						Markup('Determine whether an element has any jQuery data associated with it'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.hasData/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('49789bb366d34b5fb92a5e316baabfe8')[0]),
					'flag': helper.set_entry_command_string('jQuery.removeData()'),
					'description': [
						Markup('Remove a previously-stored piece of data'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.removeData/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2668e228a37542a29e975c963ea3a368')[0]),
					'flag': helper.set_entry_command_string('.removeData()'),
					'description': [
						Markup('Remove a previously-stored piece of data'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/removeData/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Utilities'),
		'subtitle': 'Utilities',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '94272d54ee94444089787617f74489a0',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('2809c52083144e39959b703f4be0c8b9')[0]),
					'flag': helper.set_entry_command_string('jQuery.browser'),
					'description': [
						Markup('Contains flags for the useragent, read from navigator.userAgent. This property was removed in jQuery 1.9 and is available only through the jQuery.migrate plugin'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.browser/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('796f2851f44546958d5da18e6769109f')[0]),
					'flag': helper.set_entry_command_string('jQuery.contains()'),
					'description': [
						Markup('Check to see if a DOM element is a descendant of another DOM element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.contains/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('eb9adac9372149d5841d6cb55bfc5927')[0]),
					'flag': helper.set_entry_command_string('each'),
					'description': [
						Markup('Iterate over a jQuery object, executing a function for each matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/each/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('297ade3b88da4897b8e034e192b4b87c')[0]),
					'flag': helper.set_entry_command_string('jQuery.each()'),
					'description': [
						Markup('A generic iterator function, which can be used to seamlessly iterate over both objects and arrays'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.each/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ae2fd7b8dede4357913ff4d449bfa3dd')[0]),
					'flag': helper.set_entry_command_string('jQuery.extend()'),
					'description': [
						Markup('Merge the contents of two or more objects together into the first object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.extend/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c5984c2546e74fbcb40a52530398a137')[0]),
					'flag': helper.set_entry_command_string('jQuery.globalEval()'),
					'description': [
						Markup('Execute some JavaScript code globally'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.globalEval/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('772036871a344d539273e24a7ae450a7')[0]),
					'flag': helper.set_entry_command_string('jQuery.grep()'),
					'description': [
						Markup('Finds the elements of an array which satisfy a filter function. The original array is not affected'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.grep/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8a0f2d68c28245679d8cb8a9306b6fb6')[0]),
					'flag': helper.set_entry_command_string('jQuery.inArray()'),
					'description': [
						Markup('Search for a specified value within an array and return its index (or -1 if not found)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.inArray/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('83c9d9eaace34f58915db86356f430d9')[0]),
					'flag': helper.set_entry_command_string('jQuery.isArray()'),
					'description': [
						Markup('Determine whether the argument is an array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isArray/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dd8f76a838274ca1acc73c0195f31275')[0]),
					'flag': helper.set_entry_command_string('jQuery.isEmptyObject()'),
					'description': [
						Markup('Check to see if an object is empty (contains no enumerable properties)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isEmptyObject/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e2ec7f3cd08b41a2baa91d4b7a607752')[0]),
					'flag': helper.set_entry_command_string('jQuery.isFunction()'),
					'description': [
						Markup('Determines if its argument is callable as a function'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isFunction/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a8c1fc57f2364c25a8426768820c6adc')[0]),
					'flag': helper.set_entry_command_string('jQuery.isNumeric()'),
					'description': [
						Markup('Determines whether its argument represents a JavaScript number'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isNumeric/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4b861066c1e045218a0c43ce4911064b')[0]),
					'flag': helper.set_entry_command_string('jQuery.isPlainObject()'),
					'description': [
						Markup('Check to see if an object is a plain object (created using "{}" or "new Object")'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isPlainObject/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dcc167d8f6fb4bfb92fbb393ecf289d9')[0]),
					'flag': helper.set_entry_command_string('jQuery.isWindow()'),
					'description': [
						Markup('Determine whether the argument is a window'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isWindow/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('269c688d5a3b4b7d8a962d4301e72e87')[0]),
					'flag': helper.set_entry_command_string('jQuery.isXMLDoc()'),
					'description': [
						Markup('Check to see if a DOM node is within an XML document (or is an XML document)'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.isXMLDoc/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ff86cfd9bb874d2a99f6c98fc8f92c6b')[0]),
					'flag': helper.set_entry_command_string('jQuery.makeArray()'),
					'description': [
						Markup('Convert an array-like object into a true JavaScript array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.makeArray/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('50996a8a7bfe427d95dcfb3ee0d29434')[0]),
					'flag': helper.set_entry_command_string('jQuery.map()'),
					'description': [
						Markup('Translate all items in an array or object to new array of items'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.map/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8a355d15689e482ebd643cd229b9cf38')[0]),
					'flag': helper.set_entry_command_string('jQuery.merge()'),
					'description': [
						Markup('Merge the contents of two arrays together into the first array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.merge/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bb36a2946cd847eb87ffad989f2e0538')[0]),
					'flag': helper.set_entry_command_string('jQuery.noop()'),
					'description': [
						Markup('An empty function'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.noop/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('30d10b63aef148d6b7309706f6783b28')[0]),
					'flag': helper.set_entry_command_string('jQuery.now()'),
					'description': [
						Markup('Return a number representing the current time'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.now/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('78eb1abe8a1b4126badde6ebd64e191a')[0]),
					'flag': helper.set_entry_command_string('jQuery.parseJSON()'),
					'description': [
						Markup('Takes a well-formed JSON string and returns the resulting JavaScript value'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.parseJSON/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e824a9bc3a1041c8a29e784e9f3c71ca')[0]),
					'flag': helper.set_entry_command_string('jQuery.parseXML()'),
					'description': [
						Markup('Parses a string into an XML document'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.parseXML/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('86a9dc298443471fb769dcbbc3ae5e4d')[0]),
					'flag': helper.set_entry_command_string('jQuery.proxy()'),
					'description': [
						Markup('Takes a function and returns a new one that will always have a particular context'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.proxy/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7da500c718b94318a688b7e212de8ed3')[0]),
					'flag': helper.set_entry_command_string('jQuery.support'),
					'description': [
						Markup('A collection of properties that represent the presence of different browser features or bugs. Intended for jQuery\'s internal use'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.support/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a6532501b1344ca8b2a4c6f79b1581f1')[0]),
					'flag': helper.set_entry_command_string('jQuery.trim()'),
					'description': [
						Markup('Remove the whitespace from the beginning and end of a string'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.trim/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c344a0c1e62b4474b9134697b9a116dc')[0]),
					'flag': helper.set_entry_command_string('jQuery.type()'),
					'description': [
						Markup('Determine the internal JavaScript [[Class]] of an object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.type/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('49f527bf34404b82bb67e999c1bb2f9e')[0]),
					'flag': helper.set_entry_command_string('jQuery.unique()'),
					'description': [
						Markup('Sorts an array of DOM elements, in place, with the duplicates removed. Note that this only works on arrays of DOM elements, not strings or numbers'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.unique/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'Copying',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '459c00495c2849319be5c08f7260a51b',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('f9c1413a0da64b808286e46fdc786424')[0]),
					'flag': helper.set_entry_command_string('.clone()'),
					'description': [
						Markup('Create a deep copy of the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/clone/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'DOM Insertion (Around)',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'e0c89793a7274202ad2b54a66e311c35',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('8bdefc20189145b7a0e99166c5687fd2')[0]),
					'flag': helper.set_entry_command_string('.wrap()'),
					'description': [
						Markup('Wrap an HTML structure around each element in the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/wrap/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cd5ef00e6d634b3eb1c8166ae993fd33')[0]),
					'flag': helper.set_entry_command_string('.wrapAll()'),
					'description': [
						Markup('Wrap an HTML structure around all elements in the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/wrapAll/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('74b0632b8753443489e602d92cf0a57a')[0]),
					'flag': helper.set_entry_command_string('.wrapInner()'),
					'description': [
						Markup('Wrap an HTML structure around the content of each element in the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/wrapInner/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'DOM Insertion (Inside)',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'c7446643389d4ac099afb54d43ac3823',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('147c65e404ef49e4b76aab107c8074be')[0]),
					'flag': helper.set_entry_command_string('.append()'),
					'description': [
						Markup('Insert content, specified by the parameter, to the end of each element in the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/append/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('907bffedd0ae4ffe8b67cf2ee4565596')[0]),
					'flag': helper.set_entry_command_string('.appendTo()'),
					'description': [
						Markup('Insert every element in the set of matched elements to the end of the target'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/appendTo/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9adf46c4d0f94c8290c11b1c386f7ab7')[0]),
					'flag': helper.set_entry_command_string('.html()'),
					'description': [
						Markup('Get the HTML contents of the first element in the set of matched elements or set the HTML contents of every matched element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/html/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('53c6d92e9e7f42c8af94d1ac1116269a')[0]),
					'flag': helper.set_entry_command_string('.prepend()'),
					'description': [
						Markup('Insert content, specified by the parameter, to the beginning of each element in the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prepend/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('aec621f9e4694bcc8064af2dbd5c0348')[0]),
					'flag': helper.set_entry_command_string('.prependTo()'),
					'description': [
						Markup('Insert every element in the set of matched elements to the beginning of the target'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prependTo/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a22ffd304f8340a59e18bef888a22deb')[0]),
					'flag': helper.set_entry_command_string('.text()'),
					'description': [
						Markup('Get the combined text contents of each element in the set of matched elements, including their descendants, or set the text contents of the matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/text/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'DOM Insertion (Outside)',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '13a6ae57e2e044e79d2535f8f7bfd3b5',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ebf1143551bd43699044b86869da9dd8')[0]),
					'flag': helper.set_entry_command_string('.after()'),
					'description': [
						Markup('Insert content, specified by the parameter, after each element in the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/after/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b9c2ed61fcda4b73b067e83d5975ae40')[0]),
					'flag': helper.set_entry_command_string('.before()'),
					'description': [
						Markup('Insert content, specified by the parameter, before each element in the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/before/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ccd9d43ba8764731822129c8de8c394d')[0]),
					'flag': helper.set_entry_command_string('.insertAfter()'),
					'description': [
						Markup('Insert every element in the set of matched elements after the target'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/insertAfter/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5045a673ad98427ead004ebb09405703')[0]),
					'flag': helper.set_entry_command_string('.insertBefore()'),
					'description': [
						Markup('Insert every element in the set of matched elements before the target'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/insertBefore/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'DOM Removal',
		'description': 'Used to manipulate DOM elements from a selection of matched elements',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'ba012c2dccec4cccb72a409481cb1c1f',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('beeb7a19faca471b93f5245a68d461e9')[0]),
					'flag': helper.set_entry_command_string('.detach()'),
					'description': [
						Markup('Remove the set of matched elements from the DOM'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/detach/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2eb15831d9af48d3b8622602d69afa5a')[0]),
					'flag': helper.set_entry_command_string('.empty()'),
					'description': [
						Markup('Remove all child nodes of the set of matched elements from the DOM'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/empty/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('92111bdeee5a464fbb6d3ec5f278b583')[0]),
					'flag': helper.set_entry_command_string('.remove()'),
					'description': [
						Markup('Remove the set of matched elements from the DOM'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/remove/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('328bcf040bbb4b4c8a26c9cb130c8a19')[0]),
					'flag': helper.set_entry_command_string('.unwrap()'),
					'description': [
						Markup('Remove the parents of the set of matched elements from the DOM, leaving the matched elements in their place'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/unwrap/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Manipulation'),
		'subtitle': 'DOM Replacement',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '30370c61eb484c7094a69126047d11ad',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('a58888fccb4849ccaaa3582f98adee21')[0]),
					'flag': helper.set_entry_command_string('.replaceAll()'),
					'description': [
						Markup('Replace each target element with the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/replaceAll/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('18874f741d0d4e0e9a4cbdc784ccaf52')[0]),
					'flag': helper.set_entry_command_string('.replaceWith()'),
					'description': [
						Markup('Replace each element in the set of matched elements with the provided new content and return the set of elements that was removed'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/replaceWith/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Ajax'),
		'subtitle': 'Global Ajax Event Handlers',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '337589736ab34bc98a847942bd38c768',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('47b6c44eaadd48868836f5f1d1a33277')[0]),
					'flag': helper.set_entry_command_string('.ajaxComplete()'),
					'description': [
						Markup('Register a handler to be called when Ajax requests complete'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxComplete/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('23e365244d2246e6bce1a3b8523d3e81')[0]),
					'flag': helper.set_entry_command_string('.ajaxError()'),
					'description': [
						Markup('Register a handler to be called when Ajax requests complete with an error'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxError/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('66b146b0729c4c039a1fc52e3244a2f9')[0]),
					'flag': helper.set_entry_command_string('.ajaxSend()'),
					'description': [
						Markup('Attach a function to be executed before an Ajax request is sent'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxSend/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('00750033d2eb4229bb65968d8ee6d39b')[0]),
					'flag': helper.set_entry_command_string('.ajaxStart()'),
					'description': [
						Markup('Register a handler to be called when the first Ajax request begins'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxStart/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8b897dfb1ad94f46ba7d8ff81eeed529')[0]),
					'flag': helper.set_entry_command_string('.ajaxStop()'),
					'description': [
						Markup('Register a handler to be called when all Ajax requests have completed'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxStop/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1fc3f0c1d99d465da326672c66e60714')[0]),
					'flag': helper.set_entry_command_string('.ajaxSuccess()'),
					'description': [
						Markup('Attach a function to be executed whenever an Ajax request completes successfully'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ajaxSuccess/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Ajax'),
		'subtitle': 'Ajax Helper Functions',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'd20f1a45baa94f61ac6d0cfa557683ec',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('bb2a53e3b40644f191a76e1d39243f9e')[0]),
					'flag': helper.set_entry_command_string('jQuery.param()'),
					'description': [
						Markup('Create a serialized representation of an array, a plain object, or a jQuery object suitable for use in a URL query string or Ajax request'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.param/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c8ed5e2709624660bc2efe3bd9afdfaa')[0]),
					'flag': helper.set_entry_command_string('.serialize()'),
					'description': [
						Markup('Encode a set of form elements as a string for submission'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/serialize/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('13cccb3c847a48949d7a2ad32566cc3a')[0]),
					'flag': helper.set_entry_command_string('.serializeArray()'),
					'description': [
						Markup('Encode a set of form elements as an array of names and values'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/serializeArray/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Ajax'),
		'subtitle': 'Ajax Low-Level Interface',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'aa1e1b9238664278959e9bc286917878',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('fecad96007294ff8ada98d72ebd0ca34')[0]),
					'flag': helper.set_entry_command_string('jQuery.ajax()'),
					'description': [
						Markup('Perform an asynchronous HTTP (Ajax) request'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.ajax/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('76c0241af5af44928940c02f434c7407')[0]),
					'flag': helper.set_entry_command_string('jQuery.ajaxSetup()'),
					'description': [
						Markup('Set default values for future Ajax requests. Its use is not recommended'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.ajaxSetup',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Ajax'),
		'subtitle': 'Ajax Shorthand Methods',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '14a1fe1c5df24d98aafc05ad37cbe193',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('cb508bc4c7394a58806e6ead1f2173fc')[0]),
					'flag': helper.set_entry_command_string('jQuery.get()'),
					'description': [
						Markup('Load data from the server using a HTTP GET request'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.get/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a93d6d9486d04e7ebc6cb0129be03355')[0]),
					'flag': helper.set_entry_command_string('jQuery.getJSON()'),
					'description': [
						Markup('Load JSON-encoded data from the server using a GET HTTP request'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.getJSON/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('704cc2b5590e44dd8467fb1c053af37b')[0]),
					'flag': helper.set_entry_command_string('jQuery.getScript()'),
					'description': [
						Markup('Load a JavaScript file from the server using a GET HTTP request, then execute it'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.getScript/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8a36f3996eba401b8f9df13569495c0d')[0]),
					'flag': helper.set_entry_command_string('.load()'),
					'description': [
						Markup('Load data from the server and place the returned HTML into the matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/load/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4c9ed1156d9e4e50b3ae168007f35e3b')[0]),
					'flag': helper.set_entry_command_string('jQuery.post()'),
					'description': [
						Markup('Send data to the server using a HTTP POST request'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.post/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Traversing'),
		'subtitle': 'Filter Traversing',
		'description': 'Used to filter traversed DOM elements that has been matched',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'bf651165dac64700b9c86afb0e310f3f',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('662824eb59834de29a2660d0df55e62b')[0]),
					'flag': helper.set_entry_command_string('.eq()'),
					'description': [
						Markup('Reduce the set of matched elements to the one at the specified index'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/eq/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('033d46dd39394e9d9e63c4bbf06f6da3')[0]),
					'flag': helper.set_entry_command_string('.filter()'),
					'description': [
						Markup('Reduce the set of matched elements to those that match the selector or pass the function\'s test'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/filter/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('be843e46babb47f8afa1f18464b6fba2')[0]),
					'flag': helper.set_entry_command_string('.first()'),
					'description': [
						Markup('Reduce the set of matched elements to the first in the set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/first/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7108c1a3afc14271a7683e0c1acac8e1')[0]),
					'flag': helper.set_entry_command_string('.has()'),
					'description': [
						Markup('Reduce the set of matched elements to those that have a descendant that matches the selector or DOM element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/has/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4bf15651a7b9417686cd3a3f85f2f052')[0]),
					'flag': helper.set_entry_command_string('.is()'),
					'description': [
						Markup('Check the current matched set of elements against a selector, element, or jQuery object and return true if at least one of these elements matches the given arguments'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/is/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9db28d175a8e4126a2ae25d8b5a4363e')[0]),
					'flag': helper.set_entry_command_string('.last()'),
					'description': [
						Markup('Reduce the set of matched elements to the final one in the set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/last/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8cd72a0219504f06855a3cbb9547e9f5')[0]),
					'flag': helper.set_entry_command_string('.map()'),
					'description': [
						Markup('Pass each element in the current matched set through a function, producing a new jQuery object containing the return values'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/map/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0b4f0270229a4a2a8a0b0e31c49d5b01')[0]),
					'flag': helper.set_entry_command_string('.not()'),
					'description': [
						Markup('Remove elements from the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/not/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6ee06e27bffa403c8a658bf4b6646064')[0]),
					'flag': helper.set_entry_command_string('.slice()'),
					'description': [
						Markup('Reduce the set of matched elements to a subset specified by a range of indices'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/slice/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Traversing'),
		'subtitle': 'Miscellaneous Traversing',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '279c3103bd8949c1bee8462646cb1103',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('9954b0bc539e4c5ea662ec4d982633cf')[0]),
					'flag': helper.set_entry_command_string('.add()'),
					'description': [
						Markup('Create a new jQuery object with elements added to the set of matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/add/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('88be6800dc7a41beb27160dc77741477')[0]),
					'flag': helper.set_entry_command_string('.andSelf()'),
					'description': [
						Markup('Add the previous set of elements on the stack to the current set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/andSelf/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9ef2669dc26348b19c621587ba2ca477')[0]),
					'flag': helper.set_entry_command_string('.contents()'),
					'description': [
						Markup('Get the children of each element in the set of matched elements, including text and comment nodes'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/contents/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('80dbc89b826e47b6a91ac503e88fa9a4')[0]),
					'flag': helper.set_entry_command_string('.end()'),
					'description': [
						Markup('End the most recent filtering operation in the current chain and return the set of matched elements to its previous state'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/end/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Traversing'),
		'subtitle': 'Tree Traversal',
		'description': 'Used to traverse the DOM tree',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '59d3bf60e3f74b98bb6591b771b6b903',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('c440201bf5c24f00bbfd99713010d182')[0]),
					'flag': helper.set_entry_command_string('.children()'),
					'description': [
						Markup('Get the children of each element in the set of matched elements, optionally filtered by a selector'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/children/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b16c60dde4fa4f4a9d8affdc3b935de1')[0]),
					'flag': helper.set_entry_command_string('.closest()'),
					'description': [
						Markup('For each element in the set, get the first element that matches the selector by testing the element itself and traversing up through its ancestors in the DOM tree'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/closest/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6f3e676da9864e068ea94bddb3aa6fdd')[0]),
					'flag': helper.set_entry_command_string('.find()'),
					'description': [
						Markup('Get the descendants of each element in the current set of matched elements, filtered by a selector, jQuery object, or element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/find/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1c80f2fe784a431cbe68e24a4012cdb1')[0]),
					'flag': helper.set_entry_command_string('.next()'),
					'description': [
						Markup('Get the immediately following sibling of each element in the set of matched elements. If a selector is provided, it retrieves the next sibling only if it matches that selector'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/next/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('44b1658daf684f2b8e848e4c2c5aeb7e')[0]),
					'flag': helper.set_entry_command_string('.nextAll()'),
					'description': [
						Markup('Get all following siblings of each element in the set of matched elements, optionally filtered by a selector'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/nextAll/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a7e3f162ae734409bb0e0870e71e7ef5')[0]),
					'flag': helper.set_entry_command_string('.nextUntil()'),
					'description': [
						Markup('Get all following siblings of each element up to but not including the element matched by the selector, DOM node, or jQuery object passed'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/nextUntil/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('283d78b383fa44c2b62141a7715b9d55')[0]),
					'flag': helper.set_entry_command_string('.parent()'),
					'description': [
						Markup('Get the parent of each element in the current set of matched elements, optionally filtered by a selector'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/parent/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0f4f95586ab24f9ebd9fbb259588637c')[0]),
					'flag': helper.set_entry_command_string('.parents()'),
					'description': [
						Markup('Get the ancestors of each element in the current set of matched elements, optionally filtered by a selector'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/parents/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b68641cfe5284deab128bdd599979fa8')[0]),
					'flag': helper.set_entry_command_string('.parentsUntil()'),
					'description': [
						Markup('Get the ancestors of each element in the current set of matched elements, up to but not including the element matched by the selector, DOM node, or jQuery object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/parentsUntil/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('471d58c856cd4248ae5285684db3665d')[0]),
					'flag': helper.set_entry_command_string('.prev()'),
					'description': [
						Markup('Get the immediately preceding sibling of each element in the set of matched elements. If a selector is provided, it retrieves the previous sibling only if it matches that selector'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prev/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('947009e080bd40149a22a0a28df6b60d')[0]),
					'flag': helper.set_entry_command_string('.prevAll()'),
					'description': [
						Markup('Get all preceding siblings of each element in the set of matched elements, optionally filtered by a selector'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prevAll/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dcf09c90e3a04af1b01c04d9b56feeb7')[0]),
					'flag': helper.set_entry_command_string('.prevUntil()'),
					'description': [
						Markup('Get all preceding siblings of each element up to but not including the element matched by the selector, DOM node, or jQuery object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/prevUntil/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cd44998167324ee69e5a0d37a115a94c')[0]),
					'flag': helper.set_entry_command_string('.siblings()'),
					'description': [
						Markup('Get the siblings of each element in the set of matched elements, optionally filtered by a selector'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/siblings/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Core'),
		'subtitle': 'jQuery Core Object',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'd96e67b1d27c4fed9a60240046c23fd3',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('9329f6a578b64c6c85dbf4f28825a9d4')[0]),
					'flag': helper.set_entry_command_string('jQuery()'),
					'description': [
						Markup('Return a collection of matched elements either found in the DOM based on passed argument(s) or created by passing an HTML string'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('063ad275442144cd97b2ff158835c3fa')[0]),
					'flag': helper.set_entry_command_string('jQuery.noConflict()'),
					'description': [
						Markup('Relinquish jQuery\'s control of the $ variable'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.noConflict/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2f28d84e629e4198b59c5deb35014e04')[0]),
					'flag': helper.set_entry_command_string('jQuery.sub()'),
					'description': [
						Markup('Creates a new copy of jQuery whose properties and methods can be modified without affecting the original jQuery object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.sub/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ece8f48bc35346faa492ec114bcf873a')[0]),
					'flag': helper.set_entry_command_string('jQuery.when()'),
					'description': [
						Markup('Provides a way to execute callback functions based on zero or more Thenable objects, usually Deferred objects that represent asynchronous events'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.when/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Core'),
		'subtitle': 'DOM Element Methods',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'c07dccae8f7243e4841ffd35cddc931b',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('aa7dcda704994ae28c6acc3fe5be54b0')[0]),
					'flag': helper.set_entry_command_string('.get()'),
					'description': [
						Markup('Retrieve the DOM elements matched by the jQuery object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/get/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('07ece37c2a024f7b9d185a4a2f3db5e0')[0]),
					'flag': helper.set_entry_command_string('.index()'),
					'description': [
						Markup('Search for a given element from among the matched elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/index/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0bdd7030b696492f89e6e8df39fd503e')[0]),
					'flag': helper.set_entry_command_string('.size()'),
					'description': [
						Markup('Return the number of elements in the jQuery object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/size/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b1866774a58549a099a7695003756087')[0]),
					'flag': helper.set_entry_command_string('toArray()'),
					'description': [
						Markup('Retrieve all the elements contained in the jQuery set, as an array'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/toArray/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Core'),
		'subtitle': 'Core Internals',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'd5162d0a9756471da76a32fdcb9173f6',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('8e55be643c6f4892bd1435924d7a9897')[0]),
					'flag': helper.set_entry_command_string('.jquery'),
					'description': [
						Markup(''),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/.jquery/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d6212439b12e4274b7a62f951bc21375')[0]),
					'flag': helper.set_entry_command_string('.context'),
					'description': [
						Markup('The DOM node context originally passed to jQuery(); if none was passed then context will likely be the document'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/context/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d9963d72e503408a8f9127e545459e4c')[0]),
					'flag': helper.set_entry_command_string('jQuery.error'),
					'description': [
						Markup('Takes a string and throws an exception containing it'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.error/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('cc177502e93e4512ab45a771350d7739')[0]),
					'flag': helper.set_entry_command_string('.length'),
					'description': [
						Markup('The number of elements in the jQuery object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/length/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9e44e4ce347c4d5783102c2f614d6b56')[0]),
					'flag': helper.set_entry_command_string('.pushStack()'),
					'description': [
						Markup('Add a collection of DOM elements onto the jQuery stack'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/pushStack/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('421612251f394d83abdfdbaa07b2b1da')[0]),
					'flag': helper.set_entry_command_string('.selector'),
					'description': [
						Markup('A selector representing selector passed to jQuery(), if any, when creating the original set'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/selector/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Core'),
		'subtitle': 'Deferred Object',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '400c8e03142a47578e296b696df8cb0d',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('22c18575c6ef4908b0c8e7888e5956b3')[0]),
					'flag': helper.set_entry_command_string('deferred.always()'),
					'description': [
						Markup('Add handlers to be called when the Deferred object is either resolved or rejected'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.always/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d19e503f13f64731b28b138b513bb90c')[0]),
					'flag': helper.set_entry_command_string('deferred.done()'),
					'description': [
						Markup('Add handlers to be called when the Deferred object is resolved'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.done/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4357038c95824744868f960052a93076')[0]),
					'flag': helper.set_entry_command_string('deferred.fail()'),
					'description': [
						Markup('Add handlers to be called when the Deferred object is rejected'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.fail/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('748638d3a09248389fb43a96c300277f')[0]),
					'flag': helper.set_entry_command_string('deferred.isRejected()'),
					'description': [
						Markup('Determine whether a Deferred object has been rejected'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.isRejected/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6dd4a026c63a48d3b90291865ed27230')[0]),
					'flag': helper.set_entry_command_string('deferred.isResolved()'),
					'description': [
						Markup('Determine whether a Deferred object has been resolved'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.isResolved/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d1dc67233a8d4412812a0491776f5be0')[0]),
					'flag': helper.set_entry_command_string('deferred.notify()'),
					'description': [
						Markup('Call the progressCallbacks on a Deferred object with the given args'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.notify/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b9260a773b464ccd92478be55d12fdc9')[0]),
					'flag': helper.set_entry_command_string('deferred.notifyWith()'),
					'description': [
						Markup('Call the progressCallbacks on a Deferred object with the given context and args'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.notifyWith/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('66fa963ea3734806bbfebe150441b9ab')[0]),
					'flag': helper.set_entry_command_string('deferred.pipe()'),
					'description': [
						Markup('Utility method to filter and/or chain Deferreds'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.pipe/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ec0c65fca11c47ac9d60772a49cd2808')[0]),
					'flag': helper.set_entry_command_string('deferred.progress()'),
					'description': [
						Markup('Add handlers to be called when the Deferred object generates progress notifications'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.progress/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4b016516e35e4f2e91e80c4741eb2a36')[0]),
					'flag': helper.set_entry_command_string('deferred.promise()'),
					'description': [
						Markup('Return a Deferred\'s Promise object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.promise/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2fa27f7838304d84b180ff3ce7d8f880')[0]),
					'flag': helper.set_entry_command_string('deferred.reject()'),
					'description': [
						Markup('Reject a Deferred object and call any failCallbacks with the given args'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.reject/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('46aa0e5c775045b78f76b8315ba7f352')[0]),
					'flag': helper.set_entry_command_string('deferred.rejectWith()'),
					'description': [
						Markup('Reject a Deferred object and call any failCallbacks with the given context and args'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.rejectWith/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e697f84473e64abe8902ddcb8b52e276')[0]),
					'flag': helper.set_entry_command_string('deferred.resolve()'),
					'description': [
						Markup('Resolve a Deferred object and call any doneCallbacks with the given args'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.resolve/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ce8fce43c7ec4195bdb3687b1aa80d19')[0]),
					'flag': helper.set_entry_command_string('deferred.resolveWith()'),
					'description': [
						Markup('Resolve a Deferred object and call any doneCallbacks with the given context and args'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.resolveWith/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c68411aa556d45a6bb3437b746000408')[0]),
					'flag': helper.set_entry_command_string('deferred.state()'),
					'description': [
						Markup('Determine the current state of a Deferred object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.state/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4d58bd4296c349d5b2bddfdebc2a2a3f')[0]),
					'flag': helper.set_entry_command_string('deferred.then()'),
					'description': [
						Markup('Add handlers to be called when the Deferred object is resolved, rejected, or still in progress'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/deferred.then/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('31734d5b74444b919464f46504b666b8')[0]),
					'flag': helper.set_entry_command_string('.promise()'),
					'description': [
						Markup('Return a Promise object to observe when all actions of a certain type bound to the collection, queued or not, have finished'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/promise/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Core'),
		'subtitle': 'Callbacks Object',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'c3a2a74ef987448baf7a9ed0d3e76cf1',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('cf95441d144b419d9b380e69d839652d')[0]),
					'flag': helper.set_entry_command_string('jQuery.Callbacks()'),
					'description': [
						Markup('A multi-purpose callbacks list object that provides a powerful way to manage callback lists'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.Callbacks/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e2acb35f88304380b9b72be1356f32e5')[0]),
					'flag': helper.set_entry_command_string('callbacks.add()'),
					'description': [
						Markup('Add a callback or a collection of callbacks to a callback list'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.add/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bc573df9e3dd48c98e4ca9d7e6c9c268')[0]),
					'flag': helper.set_entry_command_string('callbacks.disable()'),
					'description': [
						Markup('Disable a callback list from doing anything more'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.disable/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a05c23bc833c4f009a8de3f949434e99')[0]),
					'flag': helper.set_entry_command_string('callbacks.empty()'),
					'description': [
						Markup('Remove all of the callbacks from a list'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.empty/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('46d9917bd39b47baae745beadef07eab')[0]),
					'flag': helper.set_entry_command_string('callbacks.fire()'),
					'description': [
						Markup('Call all of the callbacks with the given arguments'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.fire/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ea611e26566445c4b1e354badf03dd2d')[0]),
					'flag': helper.set_entry_command_string('callbacks.fired()'),
					'description': [
						Markup('Determine if the callbacks have already been called at least once'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.fired/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ce0735f6ee1642ef9b0cdd55e6d6b24b')[0]),
					'flag': helper.set_entry_command_string('callbacks.fireWith()'),
					'description': [
						Markup('Call all callbacks in a list with the given context and arguments'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.fireWith/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6bf23410f89f490aa842bfd15c091523')[0]),
					'flag': helper.set_entry_command_string('callbacks.has()'),
					'description': [
						Markup('Determine whether or not the list has any callbacks attached. If a callback is provided as an argument, determine whether it is in a list'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.has/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b34e2cbcbdcb4a5e95c822209c3a0dd1')[0]),
					'flag': helper.set_entry_command_string('callbacks.lock()'),
					'description': [
						Markup('Lock a callback list in its current state'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.lock/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6cebee35a8dd482ba1d845341949bb26')[0]),
					'flag': helper.set_entry_command_string('callbacks.locked()'),
					'description': [
						Markup('Determine if the callbacks list has been locked'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.locked/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8883487e63d64d21b3f0597fdd513483')[0]),
					'flag': helper.set_entry_command_string('callbacks.remove()'),
					'description': [
						Markup('Remove a callback or a collection of callbacks from a callback list'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/callbacks.remove/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Event Object',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'fb994114da59487f8468550d5ef83c21',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('22b79614aed64f89b86995a86c8c0e97')[0]),
					'flag': helper.set_entry_command_string('event.currentTarget'),
					'description': [
						Markup('The current DOM element within the event bubbling phase'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.currentTarget/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c871dc75bf554793acaff5237d092b5f')[0]),
					'flag': helper.set_entry_command_string('event.data'),
					'description': [
						Markup('An optional object of data passed to an event method when the current executing handler is bound'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.data/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1e4434d86cce483ba3cdce5d5e5ce1c1')[0]),
					'flag': helper.set_entry_command_string('event.isDefaultPrevented()'),
					'description': [
						Markup('Returns whether event.preventDefault() was ever called on this event object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.isDefaultPrevented/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4b127880e706488897eea4e2e9ec19c0')[0]),
					'flag': helper.set_entry_command_string('event.isImmediatePropagationStopped()'),
					'description': [
						Markup('Returns whether event.stopImmediatePropagation() was ever called on this event object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.isImmediatePropagationStopped/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0b6bf1fd628f457d925bf88ada1f181f')[0]),
					'flag': helper.set_entry_command_string('event.isPropagationStopped()'),
					'description': [
						Markup('Returns whether event.stopPropagation() was ever called on this event object'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.isPropagationStopped/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ae2772fc2224442ab5f79079d9245a39')[0]),
					'flag': helper.set_entry_command_string('event.namespace'),
					'description': [
						Markup('The namespace specified when the event was triggered'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.namespace/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c6f1a37cced6432581d45ef314928490')[0]),
					'flag': helper.set_entry_command_string('event.pageX'),
					'description': [
						Markup('The mouse position relative to the left edge of the document'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.pageX/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('68b83666e9c643d1b01d625a108e1b1a')[0]),
					'flag': helper.set_entry_command_string('event.pageY'),
					'description': [
						Markup('The mouse position relative to the top edge of the document'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.pageY/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('abbd91c5b0094eadbfd3c39ba8b36d6d')[0]),
					'flag': helper.set_entry_command_string('event.preventDefault()'),
					'description': [
						Markup('If this method is called, the default action of the event will not be triggered'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.preventDefault/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('72075c497229490c96c747b26547d446')[0]),
					'flag': helper.set_entry_command_string('event.relatedTarget'),
					'description': [
						Markup('The other DOM element involved in the event, if any'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.relatedTarget/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('46cbad8d7c2347f3955f227a02013a20')[0]),
					'flag': helper.set_entry_command_string('event.result'),
					'description': [
						Markup('The last value returned by an event handler that was triggered by this event, unless the value was undefined'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.result/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0059628ddebb4fd2b4e372ba8a37a2ad')[0]),
					'flag': helper.set_entry_command_string('event.stopImmediatePropagation()'),
					'description': [
						Markup('Keeps the rest of the handlers from being executed and prevents the event from bubbling up the DOM tree'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.stopImmediatePropagation/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bcaf863584ab4d948ed2452975ce068c')[0]),
					'flag': helper.set_entry_command_string('event.stopPropagation()'),
					'description': [
						Markup('Prevents the event from bubbling up the DOM tree, preventing any parent handlers from being notified of the event'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.stopPropagation/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('deb5260051e948698ab9a7afa94bba1c')[0]),
					'flag': helper.set_entry_command_string('event.target'),
					'description': [
						Markup('The DOM element that initiated the event'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.target/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2903e9e27df94833afc71c4a8771da25')[0]),
					'flag': helper.set_entry_command_string('event.timeStamp'),
					'description': [
						Markup('The difference in milliseconds between the time the browser created the event and January 1, 1970'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.timeStamp/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bd59fcf6b53c4780a1aea832d26dcfb1')[0]),
					'flag': helper.set_entry_command_string('event.type'),
					'description': [
						Markup('Describes the nature of the event'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.type/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ce57bbab9d6640438b0b1a46a65b5f7e')[0]),
					'flag': helper.set_entry_command_string('event.which'),
					'description': [
						Markup('For key or mouse events, this property indicates the specific key or button that was pressed'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/event.which/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Mouse Events',
		'description': 'Used to bind an event handler to mouse clicks, hovering and focusing on elements',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'b9008100133e471dbaa900053e6d5ca2',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('571cb390b8604e3fa159368eac3b58ec')[0]),
					'flag': helper.set_entry_command_string('.click()'),
					'description': [
						Markup('Bind an event handler to the "click" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/click/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7ae99add84ca45f088ea4ace2ed0ab11')[0]),
					'flag': helper.set_entry_command_string('.dblclick()'),
					'description': [
						Markup('Bind an event handler to the "dblclick" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/dblclick/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e3774a16ffed486085e254a3f59fc6a8')[0]),
					'flag': helper.set_entry_command_string('.focusin()'),
					'description': [
						Markup('Bind an event handler to the "focusin" event'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/focusin/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f4adc58a070e4c7ebadf466cc4e9ffb1')[0]),
					'flag': helper.set_entry_command_string('.focusout()'),
					'description': [
						Markup('Bind an event handler to the "focusout" JavaScript event'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/focusout/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4cb871df7d37431abe1aa5712a52f9eb')[0]),
					'flag': helper.set_entry_command_string('.hover()'),
					'description': [
						Markup('Bind one or two handlers to the matched elements, to be executed when the mouse pointer enters and leaves the elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/hover/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3c2984f2347e4e04b4c56c733b5f2099')[0]),
					'flag': helper.set_entry_command_string('.mousedown()'),
					'description': [
						Markup('Bind an event handler to the "mousedown" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mousedown/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b887ad3281d140ea8b3c8b7ceb749574')[0]),
					'flag': helper.set_entry_command_string('.mouseenter()'),
					'description': [
						Markup('Bind an event handler to be fired when the mouse enters an element, or trigger that handler on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mouseenter/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('5acff74a507e4322b016e77ba064fbe7')[0]),
					'flag': helper.set_entry_command_string('.mouseleave()'),
					'description': [
						Markup('Bind an event handler to be fired when the mouse leaves an element, or trigger that handler on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mouseleave/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('de071be5a68d4feba4e7e9c5e79024ac')[0]),
					'flag': helper.set_entry_command_string('.mousemove()'),
					'description': [
						Markup('Bind an event handler to the "mousemove" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mousemove/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4d9094936b474556b6c558fcc7c3c1b6')[0]),
					'flag': helper.set_entry_command_string('.mouseout()'),
					'description': [
						Markup('Bind an event handler to the "mouseout" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mouseout/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a77527b2cbce4f91a4aceedc6cb919d2')[0]),
					'flag': helper.set_entry_command_string('.mouseover()'),
					'description': [
						Markup('Bind an event handler to the "mouseover" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mouseover/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b9d9669e5b2a4b3a933f31c4ff617e3f')[0]),
					'flag': helper.set_entry_command_string('.mouseup()'),
					'description': [
						Markup('Bind an event handler to the "mouseup" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/mouseup/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f356d904537b41d4a211af71efb9d523')[0]),
					'flag': helper.set_entry_command_string('.toggle()'),
					'description': [
						Markup('Bind two or more handlers to the matched elements, to be executed on alternate clicks'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/toggle-event/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Browser Events',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '8079e8934b6b4d16a62a7f8b69fe23cc',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('a58711b0487f481694f3170e7e1b2df1')[0]),
					'flag': helper.set_entry_command_string('.error()'),
					'description': [
						Markup('Bind an event handler to the "error" JavaScript event'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/error/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('761e89b4a1cc4adcaf94b5f8e5040efa')[0]),
					'flag': helper.set_entry_command_string('.resize()'),
					'description': [
						Markup('Bind an event handler to the "resize" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/resize/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('1ee1f32fe05046c9b6754edbbdd4e5f4')[0]),
					'flag': helper.set_entry_command_string('.scroll()'),
					'description': [
						Markup('Bind an event handler to the "scroll" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/scroll/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Document Loading',
		'description': 'Used to bind event handlers to be fired upon loading the document f.e.',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '332c36e3086c4893b024f08105fb5917',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('434b9df00481472d83befffcd235562e')[0]),
					'flag': helper.set_entry_command_string('.holdReady()'),
					'description': [
						Markup('Holds or releases the execution of jQuery\'s ready event'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/jQuery.holdReady/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('617907ff29894be695a3895802d059a3')[0]),
					'flag': helper.set_entry_command_string('.load()'),
					'description': [
						Markup('Bind an event handler to the "load" JavaScript event'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/load-event/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d3d037be6cfd4323beef9b62d6e34efe')[0]),
					'flag': helper.set_entry_command_string('.ready()'),
					'description': [
						Markup('Specify a function to execute when the DOM is fully loaded'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/ready/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('898ebf0ed71345ebae02839e6ee13ab9')[0]),
					'flag': helper.set_entry_command_string('.unload()'),
					'description': [
						Markup('Bind an event handler to the "unload" JavaScript event'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/unload/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Event Handler Attachment',
		'description': 'Used to attach event handlers',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '2fe4208cc51a431d884ddf36f3d4603d',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('5e9c14e91e4748d09abc8f0865d2f4ab')[0]),
					'flag': helper.set_entry_command_string('.bind()'),
					'description': [
						Markup('Attach a handler to an event for the elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/bind/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('af54108b8b9e4b0080f396f46397f53d')[0]),
					'flag': helper.set_entry_command_string('.delegate()'),
					'description': [
						Markup('Attach a handler to one or more events for all elements that match the selector, now or in the future, based on a specific set of root elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/delegate/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('7648a919e8fa4d20bf28de48cbf478c8')[0]),
					'flag': helper.set_entry_command_string('.die()'),
					'description': [
						Markup('Remove event handlers previously attached using .live() from the elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/die/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('687f1ff73b4e4c2c950d99a9f9010ac5')[0]),
					'flag': helper.set_entry_command_string('.live()'),
					'description': [
						Markup('Attach an event handler for all elements which match the current selector, now and in the future'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/live/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('52fd43d293244422ad519fee2b660b14')[0]),
					'flag': helper.set_entry_command_string('.off()'),
					'description': [
						Markup('Remove an event handler'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/off/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('08d604480b2e49a0b7fe91ca7b571490')[0]),
					'flag': helper.set_entry_command_string('.on()'),
					'description': [
						Markup('Attach an event handler function for one or more events to the selected elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/on/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bd656457fc6548e78cf00e670b8660e3')[0]),
					'flag': helper.set_entry_command_string('.one()'),
					'description': [
						Markup('Attach a handler to an event for the elements. The handler is executed at most once per element per event type'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/one/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('35831498e598440e933e81bc4f10b273')[0]),
					'flag': helper.set_entry_command_string('.trigger()'),
					'description': [
						Markup('Execute all handlers and behaviors attached to the matched elements for the given event type'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/trigger/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('193cb092578c47b28e0be640455b6bc1')[0]),
					'flag': helper.set_entry_command_string('.triggerHandler()'),
					'description': [
						Markup('Execute all handlers attached to an element for an event'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/triggerHandler/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4bcbefc1b739485fad7ceae78daf8150')[0]),
					'flag': helper.set_entry_command_string('.unbind()'),
					'description': [
						Markup('Remove a previously-attached event handler from the elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/unbind/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('35ffdb85e8f14dbe891def62fb4d61f6')[0]),
					'flag': helper.set_entry_command_string('.undelegate()'),
					'description': [
						Markup('Remove a handler from the event for all elements which match the current selector, based upon a specific set of root elements'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/undelegate/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Form Events',
		'description': 'Used to bind event handlers to form elements',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'd9040c42990e45f3addcf5b7eca2569d',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ce01b54f50fd4f219e31eb6acdf69298')[0]),
					'flag': helper.set_entry_command_string('.blur()'),
					'description': [
						Markup('Bind an event handler to the "blur" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/blur/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('33f8cfb41b96422982d6b6589d7453aa')[0]),
					'flag': helper.set_entry_command_string('.change()'),
					'description': [
						Markup('Bind an event handler to the "change" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/change/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('871f1abd871d4b5da3b09ec8edb031b8')[0]),
					'flag': helper.set_entry_command_string('.focus()'),
					'description': [
						Markup('Bind an event handler to the "focus" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/focus/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c52f7f10c47540b1890ca12f47356742')[0]),
					'flag': helper.set_entry_command_string('.select()'),
					'description': [
						Markup('Bind an event handler to the "select" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/select/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d26b9d139d734bf2952098e75c175830')[0]),
					'flag': helper.set_entry_command_string('.submit()'),
					'description': [
						Markup('Bind an event handler to the "submit" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/submit/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('Events'),
		'subtitle': 'Keyboard Events',
		'description': 'Used to bind event handlers to keyboard events such as pressing or releasing a key',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'df8712b69581418eb4f2daa8b3ccd8d2',
		'content': {
			'descriptor': [
				'Example',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('ac55590d1b814bb1aae1e3ea65376749')[0]),
					'flag': helper.set_entry_command_string('.keydown()'),
					'description': [
						Markup('Bind an event handler to the "keydown" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/keydown/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('8a51696487de4b3899f6357e3c58824d')[0]),
					'flag': helper.set_entry_command_string('.keypress()'),
					'description': [
						Markup('Bind an event handler to the "keypress" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/keypress/',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('209c1e96045840f18a54ab93397b2924')[0]),
					'flag': helper.set_entry_command_string('.keyup()'),
					'description': [
						Markup('Bind an event handler to the "keyup" JavaScript event, or trigger that event on an element'),
					],
					'example': helper.example_path(),
					'ext_link': 'http://api.jquery.com/keyup/',
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
			'link': 'https://jquery.com/',
			'title': 'JQuery Website',
			'description': Markup('The official website for JQuery - the best documentation out there'),
			'footer': Markup(''),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]
