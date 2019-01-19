import os
def delete_png():
    list = os.listdir()
    images = [x for x in list if ".png" in x]
    for x in images:
        os.remove(x)
