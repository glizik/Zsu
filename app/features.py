import xml.etree.ElementTree as ET

def find_and_replace(xml_filepath):
    """
    Given an XML string, finds and replaces features.
    """
    tree = ET.parse(xml_filepath)
    root = tree.getroot()

    # feature #1
    part_country_feature_from(root)

    # feature #2
    account_number_feature_from(root)

    # Save the modified XML file
    tree.write(xml_filepath)


# feature #1
def part_country_feature_from(root):
    print("finding PartCountry")
    # Find all PartCountry elements and update the value of the ones that are 'LU' to 'CN'
    for country in root.iter('PartCountry'):
        if country.text == 'LU':
            country.text = 'CN'

# feature #2
def account_number_feature_from(root):
    print("finding AccountNumber")
    # Find all Account numbers that are 26 character long, then remove the "-" and the first 8 characters
    for accountNumber in root.iter('AccountNumber'):
        if len(accountNumber.text) == 26:
            accountNumber.text = accountNumber.text[8:].replace("-", "")