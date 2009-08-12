from setuptools import setup, find_packages
import os

version = '1.0'

setup(name='collective.amberjack.portlet',
      version=version,
      description="The portlet for starting an amberjack demo",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='amberjack portlet demo tutorial',
      author='Massimo Azzolini',
      author_email='massimo@redturtle.net',
      url='https://svn.plone.org/svn/collective/collective.amberjack.portlet',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective', 'collective.amberjack'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.amberjack.core',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
