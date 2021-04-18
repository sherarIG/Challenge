import json
import dicttoxml
from xml.dom.minidom import parseString


def generate_json(urls_dict):
    """ create a json file based on a dictionary
    :param urls_dict: dictionary with all the urls
    :return: True if the file is successfully created. False if not
    """
    try:
        with open('url_haus_json.json', 'w') as outfile:
            json.dump(urls_dict, outfile)
        return True
    except Exception as e:
        print('Unable to write file: ' + str(e))
        return False


def generate_csv(urls_dict):
    """ create a csv file based on a dictionary
        :param urls_dict: dictionary with all the urls
        :return: True if the file is successfully created. False if not
    """
    try:
        with open('url_haus_csv.csv', 'w') as f:
            for key in urls_dict.keys():
                f.write("%s,%s\n" % (key, urls_dict[key]))
        return True
    except Exception as e:
        print('Unable to write file:' + str(e))
        return False


def generate_xml(urls_dict):
    """ create a prettified xml file based on a dictionary
            :param urls_dict: dictionary with all the urls
            :return: True if the file is successfully created. False if not
    """
    try:
        xml = dicttoxml.dicttoxml(urls_dict)
        dom = parseString(xml)
        with open("url_haus.xml", "w") as f:
            f.write(str(dom.toprettyxml()))
    except Exception as e:
        print('Unable to write file:' + str(e))
