from zope.interface import implements

from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base

from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from collective.amberjack.portlet.vocabulary import vocabulary

from collective.amberjack.portlet import AmberjackStartPortletMessageFactory as _


class IAmberjackStartPortlet(IPortletDataProvider):
    """A portlet

    It inherits from IPortletDataProvider because for this portlet, the
    data that is being rendered and the portlet assignment itself are the
    same.
    """

    # TODO: Add any zope.schema fields here to capture portlet configuration
    # information. Alternatively, if there are no settings, leave this as an
    # empty interface - see also notes around the add form and edit form
    # below.

    tourId = schema.Choice(title=_(u"Tour identifier"),
                              description=_(u"Indicate the tour's identifier you want to run on this portlet"),
                              vocabulary="collective.amberjack.core.tours",
                              required=True)
    

    skinId = schema.Choice(title=_(u"Choose the skin"),
                              description=_(u"Indicate the tour's window layout"),
                              vocabulary=vocabulary([("safari", "Safari"),
                                                     ("model_t", "Model_T")
                                                     ]),
                              default = 'safari')
    
    

class Assignment(base.Assignment):
    """Portlet assignment.

    This is what is actually managed through the portlets UI and associated
    with columns.
    """

    implements(IAmberjackStartPortlet)

    # TODO: Set default values for the configurable parameters here

    # some_field = u""

    # TODO: Add keyword parameters for configurable parameters here
    # def __init__(self, some_field=u""):
    #    self.some_field = some_field

    
    def __init__(self, tourId, skinId):
        self.tourId = tourId
        self.skinId = skinId


    @property
    def title(self):
        """This property is used to give the title of the portlet in the
        "manage portlets" screen.
        """
        return _(u"Amberjack start portlet %s/%s" % (self.tourId, self.skinId))


class Renderer(base.Renderer):
    """Portlet renderer.

    This is registered in configure.zcml. The referenced page template is
    rendered, and the implicit variable 'view' will refer to an instance
    of this class. Other methods can be added and referenced in the template.
    """

    render = ViewPageTemplateFile('amberjackstartportlet.pt')
    
    def __init__(self, context, request, view, manager, data): 
        self.context = context 
        self.request = request 
        self.view = view 
        self.manager = manager 
        self.data = data
    
    def tour(self):
        return '%s?tourId=%s&skinId=%s' % (self.context.portal_url(), self.data.tourId, self.data.skinId)

    def image(self):
        return '%s/amberjack.png' % self.context.portal_url()

class AddForm(base.AddForm):
    """Portlet add form.

    This is registered in configure.zcml. The form_fields variable tells
    zope.formlib which fields to display. The create() method actually
    constructs the assignment that is being added.
    """
    form_fields = form.Fields(IAmberjackStartPortlet)

    def create(self, data):
        return Assignment(**data)


# NOTE: If this portlet does not have any configurable parameters, you
# can use the next AddForm implementation instead of the previous.

# class AddForm(base.NullAddForm):
#     """Portlet add form.
#     """
#     def create(self):
#         return Assignment()


# NOTE: If this portlet does not have any configurable parameters, you
# can remove the EditForm class definition and delete the editview
# attribute from the <plone:portlet /> registration in configure.zcml


class EditForm(base.EditForm):
    """Portlet edit form.

    This is registered with configure.zcml. The form_fields variable tells
    zope.formlib which fields to display.
    """
    form_fields = form.Fields(IAmberjackStartPortlet)
