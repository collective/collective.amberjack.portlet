i18ndude rebuild-pot --pot collective.amberjack.portlet.pot --create collective.amberjack.portlet ../
i18ndude sync --pot collective.amberjack.portlet.pot ./*/LC_MESSAGES/collective.amberjack.portlet.po

#i18ndude rebuild-pot --pot ../i18n/collective.amberjack.portlet-plone.pot --create plone ../
i18ndude sync --pot ../i18n/collective.amberjack.portlet-plone.pot ../i18n/collective.amberjack.portlet-plone-*.po
