"""
Functions to quantify dream reports (i.e., convert text to meaningful number).
"""

def hvdc(report, category=None):
    """Automated Hall and Van de Castle scores.
    """
    raise NotImplementedError

def lucidity(report):
    """Return a continuous confidence value for lucidity.

    Based on model we will have to develop.
    """
    raise NotImplementedError

def common_themes(report):
    """Return a continuous confidence value for presence of common dream themes.
    Based on model we will have to develop.
    """
    raise NotImplementedError

def meaning_extraction(report):
    """Return dream-based meaning.

    Based on a model (semantic space) we will have to develop, based on dream reports (SDDb).
    """
    raise NotImplementedError
    