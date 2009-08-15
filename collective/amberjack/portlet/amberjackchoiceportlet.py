from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.amberjack.core.tour_manager import IManageTourUtility
from collective.amberjack.portlet import AmberjackPortletMessageFactory as _
from collective.amberjack.portlet.vocabulary import vocabulary
from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
from zope import schema
from zope.component import getUtility
from zope.formlib import form
from zope.interface import implements
from zope.schema.vocabulary import getVocabularyRegistry


class IAmberjackChoicePortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    tours = schema.List(
                value_type=schema.Choice(title=_(u"Tour identifier"),
                              description=_(u"Select the tours that can be choosen by an user on this portlet"),
                              vocabulary="collective.amberjack.core.tours",
                              required=True)
                )


    skinId = schema.Choice(title=_(u"Choose the skin"),
                              description=_(u"Indicate the tour's window layout"),
                              vocabulary=vocabulary([("safari", "Safari"),
                                                     ("model_t", "Model_T")
                                                     ]),
                              default="safari")
    

class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IAmberjackChoicePortlet)

    def __init__(self, tours="", skinId="safari"):
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
    
    def tours(self):
        manager = getUtility(IManageTourUtility)
        portal_url = self.context.portal_url()
        
        if self.data.tours:
            tours = self.data.tours
        else:
            vr = getVocabularyRegistry()
            voc = vr.get(self.context, "collective.amberjack.core.tours")
            tours =  [v.value for v in voc]
            
        l = []    
        for tour in tours:
            tourDefinition = manager.getTour(tour, context=self.context)
            url ='%s?tourId=%s&skinId=%s' % (portal_url, tour, self.data.skinId)
            l.append({'title': tourDefinition.title(), 'url':url})

        return l

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
