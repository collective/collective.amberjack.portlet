#i18ndude rebuild-pot --pot ./Content.pot \ 
#                     --merge ../i18n/generated.pot \ 
#                     --exclude=`find ../profiles -name "*.*py"` \
#                     --create content ../ || exit 1

rm ./rebuild_i18n.log

i18ndude rebuild-pot --pot collective.amberjack.portlet.pot --create collective.amberjack.portlet --merge collective.amberjack.portlet-manual.pot ../
i18ndude sync --pot collective.amberjack.portlet.pot ./*/LC_MESSAGES/collective.amberjack.portlet.po

i18ndude rebuild-pot --pot ../i18n/collective.amberjack.portlet-plone.pot --create plone ../profiles
i18ndude sync --pot ../i18n/collective.amberjack.portlet-plone.pot ../i18n/collective.amberjack.portlet-plone-*.po

WARNINGS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-WARN' | wc -l`
ERRORS=`find . -name "*pt" | xargs i18ndude find-untranslated | grep -e '^-ERROR' | wc -l`
FATAL=`find . -name "*pt"  | xargs i18ndude find-untranslated | grep -e '^-FATAL' | wc -l`

echo
echo "There are $WARNINGS warnings \(possibly missing i18n markup\)"
echo "There are $ERRORS errors \(almost definitely missing i18n markup\)"
echo "There are $FATAL fatal errors \(template could not be parsed, eg. if it\'s not html\)"
echo "For more details, run \'find . -name \"\*pt\" \| xargs i18ndude find-untranslated\' or" 
echo "Look the rebuild i18n log generate for this script called \'rebuild_i18n.log\' on locales dir" 

touch ./rebuild_i18n.log

find ../ -name "*pt" | xargs i18ndude find-untranslated > rebuild_i18n.log
