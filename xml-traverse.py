# Depth first or breadth first traversal of an xml file of any depth and breadth 
# --cem bozsahin, Mar 2019

# argument index 0: this script, index 1: input file, 2: d or b

import sys # for interface
import xml.etree.ElementTree as ET   # for xml processing

def xml_recurse (rt):
    agenda=[]
    for elm in rt:
        if sys.argv[2] == "d":
            agenda.append(elm)
        elif sys.argv[2] == "b":
            agenda.insert(0,elm)
        else:
            agenda.append(elm)  # default is depth first
    for a in agenda:
        print("tag: %s  text: %s" % (a.attrib,a.text))
        xml_recurse(a)


# get the xml file's structured representation
tree = ET.parse(sys.argv[1])
root = tree.getroot()
# fire away
xml_recurse(root)
