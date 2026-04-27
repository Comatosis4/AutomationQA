import logging
import xml.etree.ElementTree as ET

logging.basicConfig(filename='xml_Cherniai.log',
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    encoding='utf-8')

def xml_search(filename, num):
    tree = ET.parse(filename)
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.find('number')

        if number is not None and number.text == str(num):
            timing = group.find('timingExbytes')

            if timing is not None:
                for child in timing:
                    logging.info(f"{child.tag} = {child.text}")
            else:
                logging.info("Відсутній тег: timingExbytes")

xml_search('groups.xml', 1)
xml_search('groups.xml', 4)