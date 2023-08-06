from . import synth

from .morse import DIT, DAH, MORSE_TABLE
from .morse import generate
from .morse import stream_wave
from .morse import output_wave
from .morse import normalize_text

__version__ = '0.0.1'

__all__ = [
    "synth",
    "DIT",
    "DAH",
    "MORSE_TABLE",
    "generate",
    "stream_wave",
    "output_wave",
    "normalize_text"
]