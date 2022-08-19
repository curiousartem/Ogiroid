from __future__ import annotations

import os
from dataclasses import dataclass

__VERSION__ = "1.7.0"

from typing import Final


@dataclass
class Channels:
    suggestion_reddit_bot: int = 982353129913851924
    bug_report_reddit_bot: int = 982669110926250004
    suggestion_ogiroid: int = 985554479405490216
    bug_report_ogiroid: int = 985554459948122142
    errors: int = 986531210283069450
    reddit_faq: int = 985908874362093620
    tickets: int = 1005904969737711760
    logs: int = 977581277010100315
    staff_vote: int = 1005741491861344286
    welcome: int = 905183354930995320
    goodbye: int = 905183354930995320  # same as welcome

    @classmethod
    def dev(cls):
        cls.suggestion_reddit_bot: int = 1007334702442619010
        cls.bug_report_reddit_bot: int = 1007334758214279198
        cls.suggestion_ogiroid: int = 985554479405490216
        cls.bug_report_ogiroid: int = 985554459948122142
        cls.reddit_faq: int = 985908874362093620
        cls.tickets: int = 1003006753564262452
        cls.logs: int = 988162723890217040
        cls.staff_vote: int = 1002132747441152071
        cls.welcome = cls.goodbye = 985961186107461673
        return cls


@dataclass
class Roles:
    staff: int = 980700205328502794

    @classmethod
    def dev(cls):
        cls.staff: int = 1005904440039047208  # 985943266115584010 one of those is the staff role
        return cls


@dataclass
class Emojis:
    rules: str = "<:rules:1006016761809866752>"
    roles: str = "<:roles:1006016760731926641>"

    @classmethod
    def dev(cls):
        cls.rules: str = "<:emoji_18:1006073757976244244>"
        cls.roles: str = "<:role:990310706874290216>"
        return cls


@dataclass
class Colors:
    invis: int = 0x2F3136
    white: int = 0xFFFFFF


@dataclass
class Tokens:
    SRA: str = os.getenv("SRA_API_KEY")
    bot: str = os.getenv("TOKEN")
    weathermap: str = os.getenv("OPEN_WEATHER_MAP_API_KEY")


@dataclass
class timings:
    SECOND = 1
    MINUTE = 60
    HOUR = MINUTE * 60
    DAY = HOUR * 24
    WEEK = DAY * 7
    MONTH = 2592000


def status(stat):
    statuses = {
        "dnd": "<:dnd:879146778182692934>",
        "online": "<:online:879146898219483176>",
        "offline": "<:offline:879146897951035435>",
        "idle": "<:idle:879146778388205618>",
        "streaming": "<:streaming:879146899809128478>",
    }
    return statuses[stat]


xp_probability = sorted(list(range(10, 25)) + list(range(10, 25)) + list(range(25, 35, 1)))
LEVELS_AND_XP: Final = {  # credit's for this goes to the mee6 developers as we use the same exp values as them
    "0": 0,
    "1": 100,
    "2": 255,
    "3": 475,
    "4": 770,
    "5": 1150,
    "6": 1625,
    "7": 2205,
    "8": 2900,
    "9": 3720,
    "10": 4675,
    "11": 5775,
    "12": 7030,
    "13": 8450,
    "14": 10045,
    "15": 11825,
    "16": 13800,
    "17": 15980,
    "18": 18375,
    "19": 20995,
    "20": 23850,
    "21": 26950,
    "22": 30305,
    "23": 33925,
    "24": 37820,
    "25": 42000,
    "26": 46475,
    "27": 51255,
    "28": 56350,
    "29": 61770,
    "30": 67525,
    "31": 73625,
    "32": 80080,
    "33": 86900,
    "34": 94095,
    "35": 101675,
    "36": 109650,
    "37": 118030,
    "38": 126825,
    "39": 136045,
    "40": 145700,
    "41": 155800,
    "42": 166355,
    "43": 177375,
    "44": 188870,
    "45": 200850,
    "46": 213325,
    "47": 226305,
    "48": 239800,
    "49": 253820,
    "50": 268375,
    "51": 283475,
    "52": 299130,
    "53": 315350,
    "54": 332145,
    "55": 349525,
    "56": 367500,
    "57": 386080,
    "58": 405275,
    "59": 425095,
    "60": 445550,
    "61": 466650,
    "62": 488405,
    "63": 510825,
    "64": 533920,
    "65": 557700,
    "66": 582175,
    "67": 607355,
    "68": 633250,
    "69": 659870,
    "70": 687225,
    "71": 715325,
    "72": 744180,
    "73": 773800,
    "74": 804195,
    "75": 835375,
    "76": 867350,
    "77": 900130,
    "78": 933725,
    "79": 968145,
    "80": 1003400,
    "81": 1039500,
    "82": 1076455,
    "83": 1114275,
    "84": 1152970,
    "85": 1192550,
    "86": 1233025,
    "87": 1274405,
    "88": 1316700,
    "89": 1359920,
    "90": 1404075,
    "91": 1449175,
    "92": 1495230,
    "93": 1542250,
    "94": 1590245,
    "95": 1639225,
    "96": 1689200,
    "97": 1740180,
    "98": 1792175,
    "99": 1845195,
    "100": 1899250,
}
MAX_LEVEL: Final = len(LEVELS_AND_XP) - 1
MAX_XP: Final = LEVELS_AND_XP[str(MAX_LEVEL)]

IGNORE_EXCEPTIONS = ["UserBlacklisted"]
morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-",
}
TICKET_PERMS = {
    "send_messages": True,
    "read_messages": True,
    "add_reactions": True,
    "embed_links": True,
    "attach_files": True,
    "read_message_history": True,
    "external_emojis": True,
}
tag_help = {
    "public": {
        "tag get (or /t)": "Gives you the tags value",
        "tag create": "Creates a tag",
        "tag help": "Gives you this help",
        "tag info": "Gives you the tags info (views, owner, etc)",
        "tag list": "Gives you a lists of tags (use the arrows to navigate)",
        "tag claim": "Claims a tag (can only be used if the previous owner is no longer in the server)",
    },
    "owner_only": {
        "tag rename": "Renames a tag",
        "tag edit": "Edits a tag",
        "tag transfer": "Transfers a tag to another user",
        "tag delete": "Deletes a tag",
        "tag alias add": "Adds an alias to a tag",
        "tag alias remove": "Removes an alias from a tag",
    },
}
# noinspection SpellCheckingInspection
COUNTRIES = {
    "🇦🇫": "Afghanistan",
    "🇦🇱": "Albania",
    "🇩🇿": "Algeria",
    "🇦🇩": "Andorra",
    "🇦🇴": "Angola",
    "🇦🇮": "Anguilla",
    "🇦🇬": "Antigua and Barbuda",
    "🇦🇷": "Argentina",
    "🇦🇲": "Armenia",
    "🇦🇺": "Australia",
    "🇦🇹": "Austria",
    "🇦🇿": "Azerbaijan",
    "🇧🇸": "Bahamas",
    "🇧🇭": "Bahrain",
    "🇧🇩": "Bangladesh",
    "🇧🇧": "Barbados",
    "🇧🇾": "Belarus",
    "🇧🇪": "Belgium",
    "🇧🇿": "Belize",
    "🇧🇯": "Benin",
    "🇧🇲": "Bermuda",
    "🇧🇹": "Bhutan",
    "🇧🇴": "Bolivia",
    "🇧🇦": "Bosnia and Herzegovina",
    "🇧🇼": "Botswana",
    "🇧🇷": "Brazil",
    "🇧🇳": "Brunei",
    "🇧🇬": "Bulgaria",
    "🇧🇫": "Burkina Faso",
    "🇧🇮": "Burundi",
    "🇰🇭": "Cambodia",
    "🇨🇲": "Cameroon",
    "🇨🇦": "Canada",
    "🇨🇻": "Cape Verde",
    "🇰🇾": "Cayman Islands",
    "🇨🇫": "Central African Republic",
    "🇹🇩": "Chad",
    "🇨🇱": "Chile",
    "🇨🇳": "China",
    "🇨🇴": "Colombia",
    "🇨🇬": "Republic of the Congo",
    "🇨🇩": "DR Congo",
    "🇨🇷": "Costa Rica",
    "🇨🇮": "Ivory Coast",
    "🇭🇷": "Croatia",
    "🇨🇺": "Cuba",
    "🇨🇾": "Cyprus",
    "🇨🇿": "Czechia",
    "🇩🇰": "Denmark",
    "🇩🇯": "Djibouti",
    "🇩🇲": "Dominica",
    "🇩🇴": "Dominican Republic",
    "🇪🇨": "Ecuador",
    "🇪🇬": "Egypt",
    "🇸🇻": "El Salvador",
    "🇬🇶": "Equatorial Guinea",
    "🇪🇷": "Eritrea",
    "🇪🇪": "Estonia",
    "🇸🇿": "Eswatini",
    "🇪🇹": "Ethiopia",
    "🇫🇯": "Fiji",
    "🇫🇮": "Finland",
    "🇫🇷": "France",
    "🇬🇦": "Gabon",
    "🇬🇲": "Gambia",
    "🇬🇪": "Georgia",
    "🇩🇪": "Germany",
    "🇬🇭": "Ghana",
    "🇬🇷": "Greece",
    "🇬🇩": "Grenada",
    "🇬🇺": "Guam",
    "🇬🇹": "Guatemala",
    "🇬🇳": "Guinea",
    "🇬🇼": "Guinea-Bissau",
    "🇬🇾": "Guyana",
    "🇭🇹": "Haiti",
    "🇭🇳": "Honduras",
    "🇭🇺": "Hungary",
    "🇮🇸": "Iceland",
    "🇮🇳": "India",
    "🇮🇩": "Indonesia",
    "🇮🇷": "Iran",
    "🇮🇶": "Iraq",
    "🇮🇪": "Ireland",
    "🇮🇱": "Israel",
    "🇮🇹": "Italy",
    "🇯🇲": "Jamaica",
    "🇯🇵": "Japan",
    "🇯🇴": "Jordan",
    "🇰🇿": "Kazakhstan",
    "🇰🇪": "Kenya",
    "🇰🇮": "Kiribati",
    "🇰🇵": "North Korea",
    "🇰🇷": "South Korea",
    "🇽🇰": "Kosovo",
    "🇰🇼": "Kuwait",
    "kg": "Kyrgyzstan",
    "🇱🇦": "Laos",
    "🇱🇻": "Latvia",
    "🇱🇧": "Lebanon",
    "🇱🇸": "Lesotho",
    "🇱🇷": "Liberia",
    "🇱🇾": "Libya",
    "🇱🇮": "Liechtenstein",
    "🇱🇹": "Lithuania",
    "🇱🇺": "Luxembourg",
    "🇲🇬": "Madagascar",
    "🇲🇼": "Malawi",
    "🇲🇾": "Malaysia",
    "🇲🇻": "Maldives",
    "🇲🇱": "Mali",
    "🇲🇹": "Malta",
    "🇲🇷": "Mauritania",
    "🇲🇺": "Mauritius",
    "🇲🇽": "Mexico",
    "🇫🇲": "Micronesia",
    "🇲🇩": "Moldova",
    "🇲🇨": "Monaco",
    "🇲🇳": "Mongolia",
    "🇲🇪": "Montenegro",
    "🇲🇦": "Morocco",
    "🇲🇿": "Mozambique",
    "🇲🇲": "Myanmar",
    "🇳🇦": "Namibia",
    "🇳🇷": "Nauru",
    "🇳🇵": "Nepal",
    "🇳🇱": "Netherlands",
    "🇳🇿": "New Zealand",
    "🇳🇮": "Nicaragua",
    "🇳🇪": "Niger",
    "🇳🇬": "Nigeria",
    "🇳🇺": "Niue",
    "🇲🇰": "North Macedonia",
    "🇳🇴": "Norway",
    "🇴🇲": "Oman",
    "🇵🇰": "Pakistan",
    "🇵🇼": "Palau",
    "🇵🇦": "Panama",
    "🇵🇬": "Papua New Guinea",
    "🇵🇾": "Paraguay",
    "🇵🇪": "Peru",
    "🇵🇭": "Philippines",
    "🇵🇱": "Poland",
    "🇵🇹": "Portugal",
    "🇶🇦": "Qatar",
    "🇷🇴": "Romania",
    "🇷🇺": "Russia",
    "🇷🇼": "Rwanda",
    "🇰🇳": "Saint Kitts and Nevis",
    "🇱🇨": "Saint Lucia",
    "🇲🇫": "Saint Martin",
    "🇻🇨": "Saint Vincent and the Grenadines",
    "🇼🇸": "Samoa",
    "🇸🇲": "San Marino",
    "🇸🇹": "São Tomé and Príncipe",
    "🇸🇦": "Saudi Arabia",
    "🇸🇳": "Senegal",
    "🇷🇸": "Serbia",
    "🇸🇨": "Seychelles",
    "🇸🇱": "Sierra Leone",
    "🇸🇬": "Singapore",
    "🇸🇰": "Slovakia",
    "🇸🇮": "Slovenia",
    "🇸🇧": "Solomon Islands",
    "🇸🇴": "Somalia",
    "🇿🇦": "South Africa",
    "🇪🇸": "Spain",
    "🇱🇰": "Sri Lanka",
    "🇸🇩": "Sudan",
    "🇸🇷": "Suriname",
    "🇸🇪": "Sweden",
    "🇨🇭": "Switzerland",
    "🇸🇾": "Syria",
    "🇹🇼": "Taiwan",
    "🇹🇯": "Tajikistan",
    "🇹🇿": "Tanzania",
    "🇹🇭": "Thailand",
    "🇹🇱": "Timor-Leste",
    "🇹🇬": "Togo",
    "🇹🇴": "Tonga",
    "🇹🇹": "Trinidad and Tobago",
    "🇹🇳": "Tunisia",
    "🇹🇷": "Turkey",
    "🇹🇲": "Turkmenistan",
    "🇹🇻": "Tuvalu",
    "🇺🇬": "Uganda",
    "🇺🇦": "Ukraine",
    "🇦🇪": "United Arab Emirates",
    "🇬🇧": "United Kingdom",
    "🇺🇸": "United States",
    "🇺🇾": "Uruguay",
    "🇺🇿": "Uzbekistan",
    "🇻🇺": "Vanuatu",
    "🇻🇦": "Vatican City",
    "🇻🇪": "Venezuela",
    "🇻🇳": "Vietnam",
    "🇾🇪": "Yemen",
    "🇿🇲": "Zambia",
    "🇿🇼": "Zimbabwe",
}

# noinspection SpellCheckingInspection
VALID_CODE_LANGUAGES = [
    "abap",
    "aes",
    "apex",
    "awk",
    "azcli",
    "bat",
    "bicep",
    "c",
    "cameligo",
    "cjam",
    "clojure",
    "cobol",
    "coffeescript",
    "cow",
    "cpp",
    "crystal",
    "csharp",
    "csp",
    "css",
    "d",
    "dart",
    "dash",
    "dockerfile",
    "dragon",
    "ecl",
    "elixir",
    "emacs",
    "erlang",
    "fortran",
    "fsharp",
    "go",
    "golfscript",
    "graphql",
    "groovy",
    "handlebars",
    "haskell",
    "hcl",
    "html",
    "ini",
    "java",
    "javascript",
    "jelly",
    "json",
    "julia",
    "kotlin",
    "less",
    "lexon",
    "liquid",
    "lisp",
    "lua",
    "lolcode",
    "m3",
    "markdown",
    "mips",
    "msdax",
    "mysql",
    "sql",
    "objective-c",
    "nasm",
    "nasm64",
    "nim",
    "ocaml",
    "octave",
    "osabie",
    "paradoc",
    "pascal",
    "pascaligo",
    "perl",
    "pgsql",
    "php",
    "plaintext",
    "ponylang",
    "postiats",
    "powerquery",
    "powershell",
    "prolog",
    "pure",
    "pug",
    "py",
    "pyth",
    "python",
    "python2",
    "qsharp",
    "r",
    "raku",
    "razor",
    "redis",
    "redshift",
    "restructuredtext",
    "rockstar",
    "ruby",
    "rust",
    "sb",
    "scala",
    "scheme",
    "scss",
    "shell",
    "sol",
    "sparql",
    "st",
    "swift",
    "systemverilog",
    "tcl",
    "twig",
    "typescript",
    "vb",
    "verilog",
    "vlang",
    "xml",
    "yaml",
    "yeethon",
    "zig",
]

TRIVIA_CATEGORIES = [
    {"id": 9, "name": "General Knowledge"},
    {"id": 10, "name": "Entertainment: Books"},
    {"id": 11, "name": "Entertainment: Film"},
    {"id": 12, "name": "Entertainment: Music"},
    {"id": 13, "name": "Entertainment: Musicals & Theatres"},
    {"id": 14, "name": "Entertainment: Television"},
    {"id": 15, "name": "Entertainment: Video Games"},
    {"id": 16, "name": "Entertainment: Board Games"},
    {"id": 17, "name": "Science & Nature"},
    {"id": 18, "name": "Science: Computers"},
    {"id": 19, "name": "Science: Mathematics"},
    {"id": 20, "name": "Mythology"},
    {"id": 21, "name": "Sports"},
    {"id": 22, "name": "Geography"},
    {"id": 23, "name": "History"},
    {"id": 24, "name": "Politics"},
    {"id": 25, "name": "Art"},
    {"id": 26, "name": "Celebrities"},
    {"id": 27, "name": "Animals"},
    {"id": 28, "name": "Vehicles"},
    {"id": 29, "name": "Entertainment: Comics"},
    {"id": 30, "name": "Science: Gadgets"},
    {"id": 31, "name": "Entertainment: Japanese Anime & Manga"},
    {"id": 32, "name": "Entertainment: Cartoon & Animations"},
]
