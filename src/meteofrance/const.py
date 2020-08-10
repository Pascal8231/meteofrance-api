# -*- coding: utf-8 -*-
"""Consts for Météo-France weather forecast python API."""
# TODO: add package version
METEOFRANCE_API_URL = "http://webservice.meteofrance.com"
# Additionan API URL used with getDetail, getAllVigilances, getVigilance
METEOFRANCE_WS_API_URL = "http://ws.meteofrance.com/ws"
# Additionan API URL used with ImageJour, radarEU
METEONET_API_URL = "http://www.meteo.fr/meteonet/temps"
METEOFRANCE_API_TOKEN = "__Wj7dVSTjV9YGu1guveLyDq0g7S7TfTjaHBTPTpO0kj8__"

# enums used in all Warning classes. First indice is 0
# Weather alert criticity
ALERT_COLOR_LIST_FR = [None, "Vert", "Jaune", "Orange", "Rouge"]
ALERT_COLOR_LIST_EN = [None, "Green", "Yellow", "Orange", "Red"]

# Weather alert type
ALERT_TYPE_LIST_FR = [
    None,
    "Vent violent",
    "Pluie-inondation",
    "Orages",
    "Inondation",
    "Neige-verglas",
    "Canicule",
    "Grand-froid",
    "Avalanches",
    "Vagues-submersion",
]

ALERT_TYPE_LIST_EN = [
    None,
    "Wind",
    "Rain-Flood",
    "Thunderstorms",
    "Flood",
    "Snow/Ice",
    "Extreme high temperature",
    "Extreme low temperature",
    "Avalanches",
    "Coastal Event",
]


# Valide departments list for weather alert bulletin
VALID_DEPARTMENT_LIST = [
    "01",
    "02",
    "03",
    "04",
    "05",
    "06",
    "07",
    "08",
    "09",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",
    "18",
    "19",
    "20",
    "21",
    "22",
    "23",
    "24",
    "25",
    "26",
    "27",
    "28",
    "29",
    "2A",
    "2B",
    "30",
    "31",
    "32",
    "33",
    "34",
    "35",
    "36",
    "37",
    "38",
    "39",
    "40",
    "41",
    "42",
    "43",
    "44",
    "45",
    "46",
    "47",
    "48",
    "49",
    "50",
    "51",
    "52",
    "53",
    "54",
    "55",
    "56",
    "57",
    "58",
    "59",
    "60",
    "61",
    "62",
    "63",
    "64",
    "65",
    "66",
    "67",
    "68",
    "69",
    "70",
    "71",
    "72",
    "73",
    "74",
    "75",
    "76",
    "77",
    "78",
    "79",
    "80",
    "81",
    "82",
    "83",
    "84",
    "85",
    "86",
    "87",
    "88",
    "89",
    "90",
    "91",
    "92",
    "93",
    "94",
    "95",
    "99",
]

# Area code list for Coastal Departments
COASTAL_DEPARTMENT_LIST = [
    "06",
    "11",
    "13",
    "14",
    "17",
    "22",
    "29",
    "2A",
    "2B",
    "30",
    "33",
    "34",
    "35",
    "40",
    "44",
    "50",
    "56",
    "59",
    "62",
    "64",
    "66",
    "76",
    "80",
    "83",
    "85",
]
