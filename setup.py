from setuptools import setup

entry_points = """
    [paste.app_factory]
    main = powerHourApp:main
"""

requires = [
    'pyramid',
    'waitress',
    'sqlalchemy'
]

setup(name='powerHourApp',
      version='0.0.1',
      description='Power Hour Drinking Game App',
      install_requires=requires,
      packages=['powerHourApp'],
      entry_points=entry_points
)
