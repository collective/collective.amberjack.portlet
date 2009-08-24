from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope import schema
from zope.component import getMultiAdapter
from zope.formlib import form
from zope.interface import implements
from zope.schema.vocabulary import getVocabularyRegistry

from collective.amberjack.portlet import AmberjackPortletMessageFactory as _


class IAmberjackChoicePortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    tours = schema.List(
                title=_(u"Choose the tours"),
                description=_(u"Select the tours that can be choosen by an user on this portlet"),
                value_type=schema.Choice(
                              vocabulary="collective.amberjack.core.tours",
                              required=True)
                )


    skinId = schema.Choice(title=_(u"Choose the skin"),
                              description=_(u"Indicate the tour's window layout"),
                              vocabulary="collective.amberjack.skins",
                              default="model_t")
    

class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IAmberjackChoicePortlet)

    def __init__(self, tours=None, skinId="model_t"):
        if tours is None:
            self.tours = []
        else:
            self.tours = tours
        self.skinId = skinId

    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return _(u"Amberjack Choice portlet ${skinId}", mapping={'skinId': self.skinId})


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('amberjackchoiceportlet.pt')
    
    def __init__(self, context, request, view, manager, data): 
        self.context = context 
        self.request = request 
        self.view = view 
        self.manager = manager 
        self.data = data

    @property
    def available(self):
        portal_state = getMultiAdapter((self.context, self.request),
                                       name=u'plone_portal_state')
        navigation_root_url = portal_state.navigation_root_url()
        
        vr = getVocabularyRegistry()
        voc = vr.get(self.context, "collective.amberjack.core.tours")
        if self.data.tours:
            tours = self.data.tours
        else:
            tours = [term.token for term in voc]
            
        selected_tours = []
        for tour_id in tours:
            try:
                term = voc.getTermByToken(tour_id)
                url ='%s?tourId=%s&skinId=%s' % (navigation_root_url, tour_id, self.data.skinId)
                selected_tours.append({'object': term.value,
                                       'title': term.title,
                                       'url': url})
            except LookupError:
                pass
                # continue silently if a tour is not in the vocabulary anymore

        self.selected_tours = selected_tours
        return bool(self.selected_tours)
    
    def tours(self):
        return self.selected_tours


class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IAmberjackChoicePortlet)

    def create(self, data):
        return Assignment(**data)
    

class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IAmberjackChoicePortlet)
