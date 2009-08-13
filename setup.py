from setuptools import setup, find_packages
import os

version = '1.0dev'

setup(name='collective.amberjack.portlet',
      version=version,
      description="The portlet for starting an amberjack demo",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Zope2",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='amberjack portlet demo tutorial',
      author='Massimo Azzolini',
      author_email='massimo@redturtle.net',
      url='http://pypi.python.org/pypi/collective.amberjack.portlet',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.amberjack'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.amberjack.core',
          'plone.app.portlets',
          'plone.portlets',
          # 'zope.formlib',
          # 'zope.i18n',
          # 'zope.i18nmessageid',
          # 'zope.interface',
          # 'zope.schema',
          # 'Zope2'
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
