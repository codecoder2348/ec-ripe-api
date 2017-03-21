import argparse
import requests

parser = argparse.ArgumentParser()

parser.add_argument('--actions', action='store', dest='actions',
                    help='Specify the value for data call')
parser.add_argument('--ipaddr', action='append', dest='ipaddr',
                    default=[],
                    help='Add ip addresses to a list',
                    )
parser.add_argument('--asn', action='append', dest='asn',
                    default=[],
                    help='Add asns to a list',
                    )
parser.add_argument('--format', action='store', dest='format',
                    help='Specify the data format')
clargs = parser.parse_args()


def get_result(action, ipaddr, asn, data_format):
    if action is None and (action != 'network-info' or action != 'geoloc' or action != 'as-overview'):
        print("Invalid Action, Kindly enter values from [network-info, geoloc, as-overview]")
        return
    if asn is None and ipaddr is None:
        print("Unsupported resource type. It should be an ASN, IP prefix/range/address or hostname")
        return
    if data_format is None and (data_format != 'json' or data_format != 'xml' or action != 'yaml'):
        print("Invalid Data Format, Supported formats: [json, yaml, xml]")
        return

    results = []

    if ipaddr:
        for val in ipaddr:
            response = requests.get(
                "https://stat.ripe.net/data/" + action + "/data." + data_format + "?resource=" + str(
                    val))
            results.append(response.content)

    if asn:
        for val in asn:
            response = requests.get(
                "https://stat.ripe.net/data/" + action + "/data." + data_format + "?resource=" + str(
                    val))
            results.append(response.content)

    return results


if __name__ == '__main__':
    get_result(clargs.actions, clargs.ipaddr, clargs.asn, clargs.format)
