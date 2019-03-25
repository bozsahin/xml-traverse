# Depth first or breadth first traversal of an xml file of any depth and breadth 
# --cem bozsahin, Mar 2019

# argument index 0: this script, index 1: input file, 2: d or b

import sys # for interface
import xml.etree.ElementTree as ET   # for xml processing

tmode="d"
if sys.argv[2] == "b":
    tmode="b"
def xml_recurse (rt,tmode):
    agenda=[]
    for elm in rt:
        if tmode == "d":
            agenda.append(elm)
        else:
            agenda.insert(0,elm)
    for a in agenda if tmode == "d" else reversed(agenda):  
        xml_recurse(a,tmode)
        print("tag: %s\n  attrib:  %s\n  text: %s" % (a.tag,a.attrib,a.text))


# get the xml file's structured representation
tree = ET.parse(sys.argv[1])
root = tree.getroot()
print("Traversing file %s in %s mode:\n--------------" % (sys.argv[1],tmode))
# fire away
xml_recurse(root,tmode)
