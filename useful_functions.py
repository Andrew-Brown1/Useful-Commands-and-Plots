"""some useful functions that I have copy & pasted too many times"""

def expandrect(ROI, extensionx=0.4, extensiony=0.4, shape=(1000000,1000000)):
    """
    a function for expanding a rectangle in all directions to be drawn on an image
    ROI: a list of floats/ints for rectangle coordinates in image: [x1, y1, x2, y2]
    extensionx: how much (as a proportion of original size) the rectangle should be symmetrically expanded in x axis direction (1 = 100% extension)
    extensiony: how much (as a proportion of original size) the rectangle should be symmetrically expanded in y axis direction (1 = 100% extension)
    shape: tuple for size of image (so that rectangle does not extend outside of image) (height, width)
    
    returns: new expanded coordinates
    """
    width = ROI[2] - ROI[0]
    height = ROI[3] - ROI[1]
    #Length = (width + height) / 2
    centrepoint = [int(ROI[0]) + (width / 2), int(ROI[1]) + (height / 2)]
    x1 = int(centrepoint[0] - int((1 + extensionx) * width / 2))
    y1 = int(centrepoint[1] - int((1 + extensiony) * height / 2))
    x2 = int(centrepoint[0] + int((1 + extensionx) * width / 2))
    y2 = int(centrepoint[1] + int((1 + extensiony) * height / 2))

    x1 = max(1, x1)
    y1 = max(1, y1)
    x2 = min(x2, shape[1])
    y2 = min(y2, shape[0])

    return [x1, y1, x2, y2]
