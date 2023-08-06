"""
Preprocessing functions.
"""

def anonymize(report):
    """Anonymize a dream report using Named Entity Recognition.
    """
    raise NotImplementedError

def filter_rdreams(post):
    """Filter out non-dream r/Dreams posts based on flair.

    .. seealso:: froid.scrape_reddit
    """
    raise NotImplementedError

def is_dream_report(text):
    """Return confidence that ``text`` is a dream report.

    Based on a model we will have to train.

    Note, this can be used to see how "dream-y" text is, even if known to not be a dream.

    Parameters
    ----------
    text : str
        A text.

    Returns
    -------
    conf : bool
        Confidence level that ``text`` is a dream.
    """
    raise NotImplementedError

def isolate_dream_content(report):
    """Remove non-dream content from a dream report.

    Based on a model we will have to train.

    Parameters
    ----------
    report : str
        A dream report.

        .. important:: This model is trained specifically on dream reports, and thus should not be
            used on other texts. See also froid.is_dream_report.

    Returns
    -------
    dream : str
        The dream content from a dream report.
    
    Notes
    -----
    To get the non-dream content, isolate dream content and then get all of ``report`` that isn't there.
    """
    raise NotImplementedError
