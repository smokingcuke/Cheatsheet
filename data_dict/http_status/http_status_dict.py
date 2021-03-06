import os
import pathlib
from datetime import datetime

from markupsafe import Markup
from static.helper_functions import Helpers
from static.resource_collector import ResourceCollector

helper = Helpers('http_status', pathlib.Path(__file__))
iterrator = iter(helper)
cheatsheet_name = 'http_status'
meta = {
	'title': 'HTTP Status Codes',
	'description': '',
	'keywords': 'http, http2, http3, status codes, status code, cheatsheet, cheat sheet',
	'canonical': 'https://www.cheatsheet.wtf/HTTP/',

	'opengraph_title': 'HTTP Status Codes',
	'opengraph_description': '',
	'opengraph_image': '',
	'opengraph_url': 'https://www.cheatsheet.wtf/http/',

	'twitter_title': 'HTTP Status Codes',
	'twitter_description': '',
	'twitter_image': '',
}
information = {
	'tool': 'HTTP',
	'title': 'HTTP Cheatsheet',
	'subtitle': 'This site is a reference for the HyperText-Transfer Protocol (HTTP)',
	'description': 'HTTP is the foundation for communication on the World Wide Web. The development of the protocol was initiated by Sir Tim Berners Lee in 1989 at CERN. Three version (HTTP/1. HTTP/2 and HTTP/3) exists. HTTP/1 is no longer widespread and adoption is moving towards HTTP/3 whereas HTTP/2 is virtually supported by all browsers at this point. HTTP/3 uses UDP instead of TCP for the underlying transport protocol. HTTP/3 is enabled by default on the latest MacOS releases and can be enabled in stable versions of Chrome and Firefox.',
	'last_modified': (datetime.utcfromtimestamp(os.path.getmtime(__file__)).strftime('%d %B, %Y at %H:%M:%S')),
	'characteristics': [
		ResourceCollector.recieve_characteristics_from_dicts(
			'HTTP',
			[
				helper.characteristics.get('standard'),
			])
	],
	'topic_uris': [
		'standard',
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
cheatsheet = [
	{
		'heading': helper.set_folder('1xx'),
		'subtitle': 'Informational Responses',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '5e016279d25b4235a977c89873e87d25',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('33efd7f82cd84d388d9da1a8856bb30a')[0]),
					'flag': helper.set_entry_command_string("100"),
					'description': [
						Markup('Continue'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/100',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ea06d0110bca41cc965c630d9f2be4b5')[0]),
					'flag': helper.set_entry_command_string("101"),
					'description': [
						Markup('Switching Protocols'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/101',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('de85aa0005f74f6191570b19ce06a440')[0]),
					'flag': helper.set_entry_command_string("102"),
					'description': [
						Markup('Processing'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/102',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('2xx'),
		'subtitle': 'Success Responses',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': 'eafb3249355c4b6984f60e815756331b',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('6115e0d72ae0460b8649fede8be46331')[0]),
					'flag': helper.set_entry_command_string("200"),
					'description': [
						Markup('OK'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/200',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c7f8230dbf45463996d41e807b0efd00')[0]),
					'flag': helper.set_entry_command_string("201"),
					'description': [
						Markup('Created'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/201',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bf9e7e599423467e9c1dad5400e0abae')[0]),
					'flag': helper.set_entry_command_string("202"),
					'description': [
						Markup('Accepted'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/202',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b0d4e5f218cd492bbd9d3beee637d71c')[0]),
					'flag': helper.set_entry_command_string("203"),
					'description': [
						Markup('Non-Authoritative Information'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/203',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2789a8154ecb4cf38929be080a9e11ed')[0]),
					'flag': helper.set_entry_command_string("204"),
					'description': [
						Markup('No Content'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/204',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6b3bd99f5720481fa9932c18c27cbc5e')[0]),
					'flag': helper.set_entry_command_string("205"),
					'description': [
						Markup('Reset Content'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/205',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4a213a3ac77c49ee88d60d3790b3b79f')[0]),
					'flag': helper.set_entry_command_string("206"),
					'description': [
						Markup('Partial Content'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/206',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6dcad94d2bf54dda94675e15ca02b44f')[0]),
					'flag': helper.set_entry_command_string("207"),
					'description': [
						Markup('Multi-Status (WebDAV)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/207',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e12b1596df344d1487d5a93bdd3efaf6')[0]),
					'flag': helper.set_entry_command_string("208"),
					'description': [
						Markup('Already Reported (WebDAV)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/208',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3896879dd81f4456973ca1ad54d8be64')[0]),
					'flag': helper.set_entry_command_string("226"),
					'description': [
						Markup('IM Used'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/209',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('3xx'),
		'subtitle': 'Redirection Responses',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '397641e30bb84dfdb6ee82671f0d7d93',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('305261df80494d229303e07ba42c7f27')[0]),
					'flag': helper.set_entry_command_string("300"),
					'description': [
						Markup('Multiple Choices'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/300',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('241fedddf2d74a7fb08b84b176d18f89')[0]),
					'flag': helper.set_entry_command_string("301"),
					'description': [
						Markup('Moved Permanently'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/301',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('468c8a6df8074560943c20a8a5fba2d4')[0]),
					'flag': helper.set_entry_command_string("302"),
					'description': [
						Markup('Found'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/302',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c4558ae57b7d4e01be146550ebccf330')[0]),
					'flag': helper.set_entry_command_string("303"),
					'description': [
						Markup('See Other'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/303',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0882c2a3f09245369d7d6e03ae9ab2fb')[0]),
					'flag': helper.set_entry_command_string("304"),
					'description': [
						Markup('Not Modified'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/304',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2c377ef6af7747acb1d4ae5cc1b86c33')[0]),
					'flag': helper.set_entry_command_string("305"),
					'description': [
						Markup('Use Proxy'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/305',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('14f5b3a6581f4664865626cec6f9cb8b')[0]),
					'flag': helper.set_entry_command_string("306"),
					'description': [
						Markup('(Unused)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/306',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('2f71c0ca136545d8b74a7a2655443d34')[0]),
					'flag': helper.set_entry_command_string("307"),
					'description': [
						Markup('Temporary Redirect'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/307',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('abcb0f818eed4eb38dd5930ad15e0a23')[0]),
					'flag': helper.set_entry_command_string("308"),
					'description': [
						Markup('Permanent Redirect (experimental)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/308',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('4xx'),
		'subtitle': 'Client Error Responses',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '4cca759d080a446abe916975f5383e18',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('c3717f578a8d4b2cab4f551a46fcf791')[0]),
					'flag': helper.set_entry_command_string("400"),
					'description': [
						Markup('Bad Request'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/400',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0c84810a22d84025a36205d8b5b669f7')[0]),
					'flag': helper.set_entry_command_string("401"),
					'description': [
						Markup('Unauthorized'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/401',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e966269f796c49a59276e3fa44eb3e03')[0]),
					'flag': helper.set_entry_command_string("402"),
					'description': [
						Markup('Payment Required'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/402',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('05832545c8fb49708c045b7d307c86f2')[0]),
					'flag': helper.set_entry_command_string("403"),
					'description': [
						Markup('Forbidden'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/403',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fde549ef2b32420fb48e8f54baa08fbd')[0]),
					'flag': helper.set_entry_command_string("404"),
					'description': [
						Markup('Not Found'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/404',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('73997b75b8004282a26df43a62f85f3b')[0]),
					'flag': helper.set_entry_command_string("405"),
					'description': [
						Markup('Method Not Allowed'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/405',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('652c00431f5449dc8db6a2129f4514a3')[0]),
					'flag': helper.set_entry_command_string("406"),
					'description': [
						Markup('Not Acceptable'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/406',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('ce5e19e007db4974896ef0bd96825d15')[0]),
					'flag': helper.set_entry_command_string("407"),
					'description': [
						Markup('Proxy Authentication Required'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/407',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c35ba57f195e4f7e805230551027662b')[0]),
					'flag': helper.set_entry_command_string("408"),
					'description': [
						Markup('Request Timeout'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/408',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e1724efc48104599b599670c7a179bcc')[0]),
					'flag': helper.set_entry_command_string("409"),
					'description': [
						Markup('Conflict'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/409',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('29fad15d2b09463bad2f528b2991f180')[0]),
					'flag': helper.set_entry_command_string("410"),
					'description': [
						Markup('Gone'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/410',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('c9b827c0cb3245389b1512fcd5377ba1')[0]),
					'flag': helper.set_entry_command_string("411"),
					'description': [
						Markup('Length Required'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/411',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e6c5303adb114d5d84f87876a7885fbc')[0]),
					'flag': helper.set_entry_command_string("412"),
					'description': [
						Markup('Precondition Failed'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/412',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('36e9d83313b34f7ab6206463a88ac573')[0]),
					'flag': helper.set_entry_command_string("413"),
					'description': [
						Markup('Request Entity Too Large'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/413',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('3e95044a2ad04a268c154c5745666e93')[0]),
					'flag': helper.set_entry_command_string("414"),
					'description': [
						Markup('Request-URI Too Long'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/414',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('46400e3a891f4450bd8a71ba911778cc')[0]),
					'flag': helper.set_entry_command_string("415"),
					'description': [
						Markup('Unsupported Media Type'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/415',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('f7e50cf0416e42fcad023238e497e3da')[0]),
					'flag': helper.set_entry_command_string("416"),
					'description': [
						Markup('Requested Range Not Satisfiable'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/416',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('30618ccb04664001898f50bb14331d09')[0]),
					'flag': helper.set_entry_command_string("417"),
					'description': [
						Markup('Expectation Failed'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/417',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('0904a3e59ddb4dc781f69fe78c2a964e')[0]),
					'flag': helper.set_entry_command_string("418"),
					'description': [
						Markup('I\'m a teapot (RFC 2324)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/418',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('e5e08ae5a23247daa23100cb854fd40c')[0]),
					'flag': helper.set_entry_command_string("420"),
					'description': [
						Markup('Enhance Your Calm (Twitter)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/420',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6af89072b1bf41b6abb967b6d93be04d')[0]),
					'flag': helper.set_entry_command_string("422"),
					'description': [
						Markup('Unprocessable Entity (WebDAV)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/422',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('857fabf97df34330a8a44191019b4087')[0]),
					'flag': helper.set_entry_command_string("423"),
					'description': [
						Markup('Locked (WebDAV)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/423',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('dd1fff42836941608d70cb3afcf95f3d')[0]),
					'flag': helper.set_entry_command_string("424"),
					'description': [
						Markup('Failed Dependency (WebDAV)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/424',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('6d8d1c0be21e4917a319f03ff5d54c26')[0]),
					'flag': helper.set_entry_command_string("425"),
					'description': [
						Markup('Reserved for WebDAV'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/425',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4570353ef2994144b76d2f2c04f180ba')[0]),
					'flag': helper.set_entry_command_string("426"),
					'description': [
						Markup('Upgrade Required'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/426',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('859e493ab902443e8ebda8e44d8fae14')[0]),
					'flag': helper.set_entry_command_string("428"),
					'description': [
						Markup('Precondition Required'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/428',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('b45473019d424c6c9ec872dd2622b1a4')[0]),
					'flag': helper.set_entry_command_string("429"),
					'description': [
						Markup('Too Many Requests'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/429',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('a6866625f6794149bdbb1d080e5cbd81')[0]),
					'flag': helper.set_entry_command_string("431"),
					'description': [
						Markup('Request Header Fields Too Large'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/431',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('db9ea88edb5a49a6acd385fb40155cba')[0]),
					'flag': helper.set_entry_command_string("444"),
					'description': [
						Markup('No Response (Nginx)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/444',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9886d42b136546e5a711bfd0347dd3d8')[0]),
					'flag': helper.set_entry_command_string("449"),
					'description': [
						Markup('Retry With (Microsoft)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/449',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('10dc84a3d0ed43b6ae51b5a0dbb8c6ea')[0]),
					'flag': helper.set_entry_command_string("450"),
					'description': [
						Markup('Blocked by Windows Parental Controls (Microsoft)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/450',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d7b258492e8441d5bb7e589d1e984486')[0]),
					'flag': helper.set_entry_command_string("451"),
					'description': [
						Markup('Unavailable For Legal Reasons'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/451',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('9b1043670e58410f88470f4e09fdde0f')[0]),
					'flag': helper.set_entry_command_string("499"),
					'description': [
						Markup('Client Closed Request (Nginx)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/499',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
			]
		}
	},
	{
		'heading': helper.set_folder('5xx'),
		'subtitle': 'Server Error Responses',
		'description': '',
		'columns': 'col-lg-6 col-md-12',
		'uuid': helper.get_uuid(),
		'static_red': '18dc2bae18bb4b3c9b73a683e7898d3a',
		'content': {
			'descriptor': [
				'Command',
				'Description'
			],
			'data': [
				{
					'static_red': Markup(helper.set_entry_folder('49fad0c38d0749f5a2a20e08175542d3')[0]),
					'flag': helper.set_entry_command_string("500"),
					'description': [
						Markup('Internal Server Error'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/500',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('058fc6a02b384fbf911f80ee21a3655c')[0]),
					'flag': helper.set_entry_command_string("501"),
					'description': [
						Markup('Not Implemented'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/501',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('99b7ebe150c440bab13767430038d34f')[0]),
					'flag': helper.set_entry_command_string("502"),
					'description': [
						Markup('Bad Gateway'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/502',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('148dcc285a2a4e5895c4e8eb81518fc3')[0]),
					'flag': helper.set_entry_command_string("503"),
					'description': [
						Markup('Service Unavailable'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/503',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('774f588ee247427d8e823d2ea598f2c4')[0]),
					'flag': helper.set_entry_command_string("504"),
					'description': [
						Markup('Gateway Timeout'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/504',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('41bbc80535f9494b879cccee232f4731')[0]),
					'flag': helper.set_entry_command_string("505"),
					'description': [
						Markup('HTTP Version Not Supported'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/505',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('d4de34a7fe2e4ee2aeb7d37c876fb111')[0]),
					'flag': helper.set_entry_command_string("506"),
					'description': [
						Markup('Variant Also Negotiates (Experimental)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/506',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('85359626779f4ac0962de6089976a643')[0]),
					'flag': helper.set_entry_command_string("507"),
					'description': [
						Markup('Insufficient Storage (WebDAV)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/507',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('4f2d8d9245074c64a7eab00150668f01')[0]),
					'flag': helper.set_entry_command_string("508"),
					'description': [
						Markup('Loop Detected (WebDAV)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/508',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('148acac9777d483499084e05694a4916')[0]),
					'flag': helper.set_entry_command_string("509"),
					'description': [
						Markup('Bandwidth Limit Exceeded (Apache)'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/509',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('fedb28c03db84f31bc8c0b752a762f39')[0]),
					'flag': helper.set_entry_command_string("510"),
					'description': [
						Markup('Not Extended'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/510',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('bf2bdfc22e214daa8077bbc0b11dd2a4')[0]),
					'flag': helper.set_entry_command_string("511"),
					'description': [
						Markup('Network Authentication Required'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/511',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('53d8b38dc27c45e29464c09db044d2cb')[0]),
					'flag': helper.set_entry_command_string("598"),
					'description': [
						Markup('Network read timeout error'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/598',
					'video': Markup(''),
					'uuid': helper.get_uuid(),
				},
				{
					'static_red': Markup(helper.set_entry_folder('663365ae7b8c4c6b98de143b9851071f')[0]),
					'flag': helper.set_entry_command_string("599"),
					'description': [
						Markup('Network connect timeout error'),
					],
					'example': helper.example_path(),
					'ext_link': 'https://httpstatuses.com/599',
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
			'link': 'https://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html',
			'title': 'W3 RFC2616',
			'description': Markup('A description of the HTTP status codes'),
			'footer': Markup(''),
			'screencapture': ''
		},
		{
			'link': 'https://httpstatuses.com/',
			'title': 'HTTP Statuses',
			'description': Markup('An overview of the various HTTP statuses with descriptions of each'),
			'footer': Markup(''),
			'screencapture': ''
		},
	)
]
affiliate_products = [],
licensing = [
	Markup('')
]
