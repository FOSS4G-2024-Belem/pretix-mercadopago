import os
from distutils.command.build import build

from django.core import management
from setuptools import find_packages, setup

from pretix_mercadopago import __version__


try:
    with open(os.path.join(os.path.dirname(__file__), 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except:
    long_description = ''


class CustomBuild(build):
    def run(self):
        management.call_command('compilemessages', verbosity=1)
        build.run(self)


cmdclass = {
    'build': CustomBuild
}


setup(
    name='pretix-mercadopago',
    version=__version__,
    description='Payment Plugin using MercadoPago',
    long_description=long_description,
    url='https://github.com/Delawen/pretix-mercadopago',
    author='FOSS4G 2021 team',
    author_email='delawen@gmail.com',
    license='Apache',
    install_requires=['mercadopago>=1,<2'],
    packages=find_packages(exclude=['tests', 'tests.*']),
    include_package_data=True,
    cmdclass=cmdclass,
    entry_points="""
[pretix.plugin]
pretix.plugins.mercadopago=pretix_mercadopago:PretixPluginMeta
""",
)
