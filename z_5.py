import csv
import argparse

from flask import Flask, jsonify

parser = argparse.ArgumentParser()
parser.add_argument('--port', type=int)
parser.add_argument('--server', type=str)
parser.add_argument('--filename', type=str)
args = parser.parse_args()

with open(args.filename, encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile, delimiter='+', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    out_list = []
    for dct in reader:
        index = None
        for i in range(len(out_list)):
            if f"{dct['last_name']} {dct['first_name']}" in out_list[i]['name']:
                index = i
                break
        if index is None:
            if dct['validity'] == 'lie':
                out_list.append({'name': f"{dct['last_name']} {dct['first_name']}",
                                 'lie': [dct['message']],
                                 'truth': []})
            elif dct['validity'] == 'truth':
                out_list.append({'name': f"{dct['last_name']} {dct['first_name']}",
                                 'lie': [],
                                 'truth': [dct['message']]})
        else:
            if dct['validity'] == 'lie':
                out_list[i]['lie'].append(dct['message'])
            elif dct['validity'] == 'truth':
                out_list[i]['truth'].append(dct['message'])

    out_list = sorted(out_list, key=lambda x: x['name'])


app = Flask(__name__)


@app.route('/false')
def false():
    return jsonify(out_list)


if __name__ == '__main__':
    app.run(port=args.port, host=args.server)