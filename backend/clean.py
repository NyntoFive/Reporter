"""
Clean input i'm sending over from my phone / Lens
"""
def main():
    from io import StringIO
    import json
    import pyperclip as PC
    import sys
    

def cleaner(blob):
    '''Clean input from Google Lens (from clipboard)
    def cleaner(blob):
     ...:     tmp = StringIO(blob)
     ...:     text = tmp.readlines()
     ...:     PC.copy(json.dumps(text))
     ...: 
     ...:     return json.dumps(text)
     ...: 
    '''
    tmp = StringIO(blob)
    text = tmp.readlines()
    PC.copy(json.dumps(text))
    
    return json.dumps(text)

