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

# def load_images(item):
    # start_position = 1
    # images = re.findall(r"'(\S+)'", item.all_images)
    # for i,img in enumerate(images, start=1):
        # source = item.link
        # name = img
        # CKKImage.objects.get_or_create(item=CKKItem.objects.get(id=item.id), source=source, position=i, fname=name)