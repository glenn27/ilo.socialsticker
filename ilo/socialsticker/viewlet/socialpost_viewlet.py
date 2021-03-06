#from five import grok
from Acquisition import aq_inner
from plone.app.layout.viewlets.interfaces import IAboveContent
from Products.CMFCore.utils import getToolByName
#from ilo.pledge.content.pledge import IPledge
from plone.app.layout.viewlets import common as base
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

#grok.templatedir('templates')


class socialpost_viewlet(base.ViewletBase):
    #grok.context(IPledge)
    #grok.require('zope2.View')
    #grok.template('socialpost_viewlet')
    #grok.viewletmanager(IAboveContent)
    
    index = ViewPageTemplateFile('templates/socialpost_viewlet.pt')
    

    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    def contents(self):
        context = self.context
        catalog = self.catalog
        path = '/'.join(context.aq_parent.getPhysicalPath())
        brains = catalog.unrestrictedSearchResults(path={'query': path, 'depth' : 1}, portal_type='ilo.socialsticker.sticker',review_state='published')
        
        return brains




