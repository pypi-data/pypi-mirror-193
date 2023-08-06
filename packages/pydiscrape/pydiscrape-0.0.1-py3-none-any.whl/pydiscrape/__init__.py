import hclient
import random
import json
import time
import os


class client:
    def __init__(
      this, 
      proxies: dict, 
      timeout: int, 
      ssl_verify: bool, 
      ciphers=None
    ):
        this.session = hclient.Session(
          proxies=proxies, 
          timeout=timeout, 
          verify=ssl_verify, 
          ciphers=ciphers
        )
        this.page = 0
        this._data = []
        this.dir_items = "https://{}/directory_items.json?period=all&page={}"
        this.user_json = "https://{}/u/{}.json"

    def get_all(this, host: str):
      while True:
        time.sleep(5)
        this.page += 1
        try:
            _dir = this.session.get(this.dir_items.format(host, this.page)).json()[
                "directory_items"
            ]
            # user is a sub object of directory items
            for x in _dir:
                username = x["user"]["username"]
                _userdata = this.session.get(
                    this.user_json.format(host, username)
                ).json()
                # this._data.append(_userdata)
                if os.path.exists("./data/{}.json".format(username)) == True:
                    pass
                else:
                    with open("./data/{}.json".format(username), "w") as _save:
                        json.dump(_userdata, _save)
                        _save.close()
            return "scraped {} users!".format(len(os.listdir("./data")))
        except Exception as e:
            pass

