from five import grok
from plone.directives import dexterity, form

from zope import schema
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from plone.app.z3cform.wysiwyg import WysiwygFieldWidget

from zope.interface import invariant, Invalid

from z3c.form import group, field

from plone.namedfile.interfaces import IImageScaleTraversable
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile

from plone.app.textfield import RichText

from z3c.relationfield.schema import RelationList, RelationChoice
from plone.formwidget.contenttree import ObjPathSourceBinder
#from plone.multilingualbehavior.directives import languageindependent
from collective import dexteritytextindexer

from ilo.socialsticker import MessageFactory as _


# Interface class; used to define content-type schema.

class ISticker(form.Schema, IImageScaleTraversable):
    """
    Sticker
    """

    title = schema.TextLine(
           title=_(u"Title"),
           required=True,
        )

    sticker_image = NamedBlobFile(
        title=u'Image',
        required=True,
    )

    default_message = schema.TextLine(
           title=_(u"Default Message"),
           required=True,
        )

    pass

alsoProvides(ISticker, IFormFieldProvider)
