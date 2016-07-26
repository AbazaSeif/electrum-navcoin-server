![Electrum-NavCoin-Server](https://raw.githubusercontent.com/sherlockcoin/electrum-navcoin-server/master/navcoin.png)

electrum-navcoin-server for the electrum navcoin client
---------

  * Author: Thomas Voegtlin (Bitcoin Electrum Creator) & Soopy452000 (NavCoin Fork)
  * Language: Python

## NavCoin Electrum Homepage: http://www.navcoin.org/electrum

Features
--------

  * The server indexes UTXOs by address, in a Patricia tree structure
    described by Alan Reiner (see the 'ultimate blockchain
    compression' thread in the Bitcointalk forum)

  * The server requires navcoind v3.6.0 or above, leveldb and plyvel

  * The server code is open source. Anyone can run a server, removing
    single points of failure concerns.

Installation
------------

  1. To install and run a server, see INSTALL. For greater
     detail on the installation process, see HOWTO.md.

  2. To start and stop the server, use the 'electrum-navcoin-server' script



License
-------

Electrum-server is made available under the terms of the [GNU Affero General
Public License](http://www.gnu.org/licenses/agpl.html), version 3. See the 
included `LICENSE` for more details.
