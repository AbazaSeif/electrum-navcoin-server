from setuptools import setup

setup(
    name="electrum-navcoin-server",
    version="0.9",
    scripts=['run_electrum_navcoin_server','electrum-navcoin-server'],
    install_requires=['plyvel','jsonrpclib', 'irc>=11'],
    package_dir={
        'electrumnavcoinserver':'src'
        },
    py_modules=[
        'electrumnavcoinserver.__init__',
        'electrumnavcoinserver.utils',
        'electrumnavcoinserver.storage',
        'electrumnavcoinserver.deserialize',
        'electrumnavcoinserver.networks',
        'electrumnavcoinserver.blockchain_processor',
        'electrumnavcoinserver.server_processor',
        'electrumnavcoinserver.processor',
        'electrumnavcoinserver.version',
        'electrumnavcoinserver.ircthread',
        'electrumnavcoinserver.stratum_tcp',
        'electrumnavcoinserver.stratum_http'
    ],
    description="NavCoin Electrum Server",
    author="Thomas Voegtlin & Soopy452000",
    author_email="thomasv1@gmx.de",
    license="GNU Affero GPLv3",
    url="https://github.com/sherlockcoin/electrum-navcoin-server/",
    long_description="""Server for the Electrum Lightweight NavCoin Wallet"""
)


