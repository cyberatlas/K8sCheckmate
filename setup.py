from setuptools import setup

setup(
    packages=[
      'Project',
      'Project.Modules',
      'Project.Modules.ConfigHandler',
      'Project.Modules.ErrorHandler',
      'Project.Modules.OutputHandler',
      'Project.Modules.Parser',
      'Project.Modules.ValueVerifier',
      ],
    include_package_data=True,
    install_requires=[],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],

)