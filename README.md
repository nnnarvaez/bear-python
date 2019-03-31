# Official Python BEARShares Library
WORK IN PROGRESS 95%
This port was complicated as the bearshares blockchian had many edits changing terms like `vests/vesting` to `coins/coining` and others.
Also the bearshare blockchain has the call to rewad_punds blocked for some reason. 

This repository only works for the bearshares blockchain, if you are looking for libraries to use on other of the STEEM clones see my other repo were i'm working on adding multi-chain capabilities to the commit methods. 

#### All operations have been tested and work
With the exception of calls to reward fund on the official bearshares API node, if you requiere those operations you will need to setup your own private API node.




`bear-python` is the official BEARShares library for Python. It comes with a
BIP38 encrypted wallet and a practical CLI utility called `bearpy`. (rename after update)

This library currently works on Python 2.7, 3.5 and 3.6. Python 3.3 and 3.4 support forthcoming.

# Installation

With pip:

From Source:

```
git clone https://github.com/nnnarvaez/bear-python.git
cd bear-python
python3 setup.py install        # python setup.py install for 2.7
```

## Homebrew Build Prereqs

If you're on a mac, you may need to do the following first:

```
brew install openssl
export CFLAGS="-I$(brew --prefix openssl)/include $CFLAGS"
export LDFLAGS="-L$(brew --prefix openssl)/lib $LDFLAGS"
```



# Documentation

The official STEEM python documentation applies, just replace the terms `vesting` for `coining` where needed

Documentation is available at **http://steem.readthedocs.io**

# Tests

Some tests are included.  They can be run via:

* `python setup.py test`

# Notice

This library is *under development*.  Beware.
