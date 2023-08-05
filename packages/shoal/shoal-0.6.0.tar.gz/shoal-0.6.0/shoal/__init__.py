"""shoal."""

from warnings import filterwarnings

from beartype.roar import BeartypeDecorHintPep585DeprecationWarning

__version__ = '0.2.0'
__pkg_name__ = 'shoal'

# ====== Above is the recommended code from calcipy_template and may be updated on new releases ======

# FYI: https://github.com/beartype/beartype#are-we-on-the-worst-timeline
filterwarnings('ignore', category=BeartypeDecorHintPep585DeprecationWarning)
