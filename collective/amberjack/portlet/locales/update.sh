i18ndude rebuild-pot --pot collective.amberjack.portlet.pot --create collective.amberjack.portlet --merge collective.amberjack.portlet-manual.pot ../
i18ndude sync --pot collective.amberjack.portlet.pot ./*/LC_MESSAGES/collective.amberjack.portlet.po
