"""Mapping tools configuration parameters module.

Author:
    Paulo Sanchez (@erlete)
"""

from typing import Dict

CONES: Dict = {
    "yellow": {
        "size": {
            "base": 8,
            "strip_low": 6,
            "mid": 4,
            "strip_high": 2,
            "top": 1
        },
        "colors": {
            "base": "#bfae15",
            "strip_low": "#fae420",
            "mid": "#000000",
            "strip_high": "#fae73c",
            "top": "#bfae15"
        }
    },
    "orange": {
        "size": {
            "base": 8,
            "strip_low": 6,
            "mid": 4,
            "strip_high": 2,
            "top": 1
        },
        "colors": {
            "base": "#c76016",
            "strip_low": "#eb9915",
            "mid": "#ffffff",
            "strip_high": "#e07528",
            "top": "#c76016"
        }
    },
    "orange-big": {
        "size": {
            "base": 15,
            "strip_low": 12,
            "mid": 10,
            "strip_high": 8,
            "top": 6
        },
        "colors": {
            "base": "#c76016",
            "strip_low": "#ffffff",
            "mid": "#eb9915",
            "strip_high": "#ffffff",
            "top": "#c76016"
        }
    },
    "blue": {
        "size": {
            "base": 10,
            "strip_low": 8,
            "mid": 6,
            "strip_high": 4,
            "top": 2
        },
        "colors": {
            "base": "#050780",
            "strip_low": "#05079e",
            "mid": "#ffffff",
            "strip_high": "#1417c9",
            "top": "#050780"
        }
    }
}
