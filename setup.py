import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

requires = [
    'petrel',
    ]

test_requires = requires + [
    'nose',
    'coverage',
    ]

# FIXME
setup(name='petrel_example',
      version='0.0',
      description='An example site that uses Petrel',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: BFG",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='',
      author_email='',
      url='',
      keywords='web wsgi lightweight cms',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
      tests_require=requires,
      test_suite="petrel_example.tests",
      entry_points="""\
      [paste.app_factory]
      app = petrel_example.run:app
      """
      )

