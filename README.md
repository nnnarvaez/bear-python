# A complete and updated Python library for BearShares
(If it goes somewhere)
Since Bearshares was poorly implemented as steem clon by just using `sed` to replace the word `STEEM` with the word `BEAR` making this lobrary work was a PITA, but i like challenges, have fun, i will post a few examples of BOTs that can be made with the library. 


`bear-python` is the most complete and updated BEARShares library for Python. It comes with a
BIP38 encrypted wallet and a practical CLI utility called `bearpy`. (rename after update)

This library currently works on Python 2.7, 3.5 and 3.6. Python 3.3 and 3.4 support forthcoming.

# Do what what removed from the interface (website)

#### Create accounts!

Without delegation (current cost 300 BEARS)
```
from bear import Bear
bear = Bear(keys = "active-key-here") # your WIF/active keys
bear.commit.create_account('newaccount', creator='youraccount',password='somepassword', delegation_fee_bear='0.000 BEARS')
```

With delegation (current cost 1 BEAR and about 30 delegated to the account)
```
from bear import Bear
bear = Bear(keys = "active-key-here") # your WIF/active keys
bear.commit.create_account('newaccount', creator='youraccount',password='somepassword', delegation_fee_bear='30.000 BEARS')
```

#### Convert 1 BSD to 1 BEAR 
Dont sell your BSD cheap in the market, don't scam youself... Convert them instead and help the platform get rid of the debt the BSD generate and increase your Vote Value

```
acco = 'theAccountYouWantToCommentTO'
from bear import Bear
bear = Bear(keys = "active-key-here") # your WIF/active keys
bsd = float(str.split(bear.beard.get_account(acco)['bsd_balance'])[0])
bear.commit.convert(bsd,acco) #SBD to BEARS

```

#### Make an auto reply bot
Follow the posts and comments of any account and post a nice message to it.
Warning, you need to add some sort of memory or it will just post again everytime you run it...
This is a simple example, examples are meant to give you starting points so you add the fancy stuff.

```
from bear import Bear
from bear.account import Account
from bear.post import Post
import random, string
import time

acc_to_comment = 'UserYouWantToComment' # the user to which you want to reply automatically 
author = 'youraccount' 
title = 'Some nice title, does not matter because it is a reply but will aid to generate url put something otherwise is fails' 
body = 'The body of the message, replace <enter> key and returns with \n '

acc = Account(acc_to_comment)
test=acc.get_account_history(index=-1,start=1, limit=2500, filter_by='comment', raw_output=False, order=1)

for i in test:
    if i['author'] == acc:
        reply_identifier= '@{}/{}'.format(i[ 'author'],i['permlink'])  
        reply_identifier
        post = Post(reply_identifier)
        bear = Bear(keys = "YourPostingKeyGoesHere") #Posting key of the account posting   
        post.reply(body, title, author, meta=None)     
        print('I have posted successfully, waiting 23 secs to do the next comment (Because the nodes time limit)')
        time.sleep(23)         
```




WORK IN PROGRESS 95%
This port was complicated as the bearshares blockchian had many edits changing terms like `vests/vesting` to `coins/coining` and others.
Also the bearshare blockchain has the call to rewad_punds blocked for some reason. 

This repository only works for the bearshares blockchain, if you are looking for libraries to use on other of the STEEM clones see my other repo were i'm working on adding multi-chain capabilities to the commit methods. 

#### All operations have been tested and work
With the exception of calls to reward fund on the official bearshares API node, those work but if you requiere those operations you will need to setup your own private API node.


### API NODE
Use example: Get a dict with all conversion requests from an user and print it in the console
```
user_c = 'someUserName'
from bear import Bear
bear = Bear(keys = "putYourPostingorActiveKeyHere", nodes = ["http://api.bearshares.com"]) 
conv = bear.beard.get_conversion_requests(user_c)
for c in conv:
  c,conv[c]
  
```
Note: it is reccomended that you use the provided cli basic wallet instead of putting keys in the code, this example is meant to show basic usage.

# Installation

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
