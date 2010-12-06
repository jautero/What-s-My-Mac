#!/usr/bin/env python
#
# WhatsMyMac.py -- scan mac and report it to What's My Mac site.
#

import os
import simplejson, sha, uuid
import urllib, urllib2

site_url="http://whatsmymac.appspot.com/"

def read_system_profile():
  return parse_dictionary(os.popen("system_profiler").readlines(),0)
  
def parse_dictionary(lines,indent):
  current_dict={}
  while lines:
    if count_indent(lines[0])<indent:
      return current_dict
    line=lines.pop(0).strip()
    if line:
      name,value=line.split(":",1)
      if value=="":
        current_dict[name]=parse_dictionary(lines,indent+2)
      else:
        current_dict[name]=value
  return current_dict

def count_indent(str):
  count=0
  while str[count]==" ":
    count=count+1

def post_value(dictionary):
  post_url=os.path.join(site_url,"add_data")
  jsondata=simplejson.dumps(dictionary)
  id=sha.new(jsondata+str(uuid.uuid1())).hexdigest()
  urllib2.urlopen(post_url,urllib.urlencode([("id",id),("jsondata",jsondata)]))
  return id
  
def register_id(id):
  register_url=os.path.join(site_url,"register_id")
  query=urllib.urlencode("id",id)
  os.system("open %s?%s" % (register_id,query))

if __name__ == '__main__':
  register_id(post_value(read_system_profile()))
