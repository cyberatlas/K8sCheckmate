from setuptools import setup

setup(
    name='K8sCheckmate',
    version='1.2.0',
    packages=[
      'Project',
      'Project.Models',
      'Project.Modules',
      'Project.Modules.ConfigHandler',
      'Project.Modules.ErrorHandler',
      'Project.Modules.OutputHandler',
      'Project.Modules.Parser',
      'Project.Modules.ValueVerifier',
      ],
    python_requires='>=3.7',
    include_package_data=True,
    install_requires=[
        'pyyaml',
        'pytest',
    ],
    setup_requires=[
        'pytest-runner',
    ],

)