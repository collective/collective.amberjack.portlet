# -*- coding: utf-8 -*-
#
# GNU General Public Licence Version 2 or later - see LICENCE.GPL

__author__ = """Massimo Azzolini <massimo@redturtle.net"""
__docformat__ = 'plaintext'

from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.vocabulary import SimpleTerm

def vocabulary(choices):
    """Create a SimpleVocabulary from a list of values and titles.

    >>> v = vocabulary([('value1', u"Title for value1"),
    ...                 ('value2', u"Title for value2")])
    >>> for term in v:
    ...   print term.value, '|', term.token, '|', term.title
    value1 | value1 | Title for value1
    value2 | value2 | Title for value2

    """
    return SimpleVocabulary(
        [SimpleTerm(v, title=t) for v, t in choices])
