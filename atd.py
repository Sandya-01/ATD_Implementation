import requests
from xml.etree import ElementTree
import urllib
_key = None

def setDefaultKey(key):
     global _key
     _key = key
    
def checkDocument(text,key=None):
   
    print("check doc")
    global _key
    if key is None:
        if _key is None:
            raise Exception('Please provide key as argument or set it using setDefaultKey() first')
        key = _key
    
    params = urllib.urlencode({
        'key': key,
        'data': text,
    })
    print(params)
    response = requests.get("https://service.afterthedeadline.com/checkDocument",params)
    print(response.status_code)
     
    if response.status_code <> 200:
        response.close()
        raise Exception('Unexpected response code from AtD service %d' % response.status_code)
    print(response.text)

    tree = ElementTree.fromstring(response.text .encode('utf-8'))
    print(tree)
    e= tree.findall('error')
    print(e)
    
    list_err=[]
    for errors in e:
        pre= errors.findall('precontext')
   
        s= errors.findall('string')
   
        suggest = errors.findall('suggestions')
        type_err= errors.findall('type')
        
        
        for lis in suggest:
            for (a,b,c) in zip(type_err,pre,s):
            
                        print("%s errors for: %s %s " %(a.text,b.text,c.text))
                        if a.text != "spelling":
                            list_err.append(c.text)
                        
            if len(lis)!=0:
                for item in lis:
                    print("suggestions for: %s" %(item.text))
        if not suggest:
          
          for (a,b,c) in zip(type_err,pre,s):
                        print("%s errors for: %s %s " %(a.text,b.text,c.text))
                        if a.text != "spelling":
                            list_err.append(c.text)
    print(list_err)
                        
    print(len(list_err))
    
 
    length =  len(list_err)
    return length
#      
