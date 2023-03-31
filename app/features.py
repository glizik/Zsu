import xml.etree.ElementTree as ET

def find_and_replace_part_country_elements(xml_filepath):
    """
    Given an XML string, finds and replaces all PartCountry elements in the XML.
    """
    tree = ET.parse(xml_filepath)

    # Get the root element
    root = tree.getroot()

    # Find all PartCountry elements and update the value of the ones that are 'LU' to 'CN'
    for country in root.iter('PartCountry'):
        if country.text == 'LU':
            country.text = 'CN'

    # Save the modified XML file
    tree.write(xml_filepath)