# -*- coding: utf-8 -*-
#
# GNU General Public Licence Version 2 or later - see LICENCE.GPL

__author__ = """Massimo Azzolini <massimo@redturtle.net"""
__docformat__ = 'plaintext'

from zope.interface import implements
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleVocabulary

class AvailableSkinsVocabulary(object):
    implements(IVocabularyFactory)
    
    def __call__(self, context):
        return SimpleVocabulary([SimpleVocabulary.createTerm(value="safari", token="safari", title="Safari"),
                                 SimpleVocabulary.createTerm("model_t", "model_t", "Model_T")])

