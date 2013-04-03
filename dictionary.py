import urllib
import json

class urban_diction:
  def __init__(self):
    self.url = "http://api.urbandictionary.com/v0/define?term="

  def search(self, ser_string):
    search_json = urllib.urlopen(self.url+ser_string)
    search_map = json.loads(search_json.read())
    if search_map["list"] == []:
      print "Computer says no."
      return
    for res in search_map["list"]:
      print res["definition"]
      print "\n"

