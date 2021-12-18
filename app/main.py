from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import csv

app = Flask(__name__)
api = Api(app)


class search_csv(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('name', type=str, default='')
        self.reqparse.add_argument('city', type=str, default='')
        self.reqparse.add_argument('quantity', type=str, default='')
        super(search_csv, self).__init__()

    def get(self):
        args = self.reqparse.parse_args()
        csv_file = csv.reader(open('vibra_challenge.csv', "r"), delimiter=",")
        rest = []
        max = False
        if args['quantity'] != '':
            max = int(args['quantity'])

        if args['name'] != '' and args['city'] != '':
            rest = []
            for row in csv_file:
                if row[1] == args['name'] and row[6] == args['city']:
                    if max:
                        if len(rest) < max:
                            rest.append({'name':row[1],'lastname':row[2],'email':row[3],
                                         'gender':row[4], 'other':row[5],'city':row[6]})
                        else:
                            break
                    else:
                        rest.append({'name': row[1], 'lastname': row[2], 'email': row[3],
                                     'gender': row[4], 'other': row[5], 'city': row[6]})
        else:
            if args['name'] != '':
                rest = []
                for row in csv_file:
                    if row[1] == args['name']:
                        if max:
                            if len(rest)<max:
                                rest.append({'name': row[1], 'lastname': row[2], 'email': row[3],
                                             'gender': row[4], 'other': row[5], 'city': row[6]})
                            else:
                                break
                        else:
                            rest.append({'name': row[1], 'lastname': row[2], 'email': row[3],
                                         'gender': row[4], 'other': row[5], 'city': row[6]})
            else:
                rest = []
                for row in csv_file:
                    if row[6] == args['city']:
                        if max:
                            if len(rest)<max:
                                rest.append({'name': row[1], 'lastname': row[2], 'email': row[3],
                                             'gender': row[4], 'other': row[5], 'city': row[6]})
                            else:
                                break
                        else:
                            rest.append({'name': row[1], 'lastname': row[2], 'email': row[3],
                                         'gender': row[4], 'other': row[5], 'city': row[6]})

        return rest

api.add_resource(search_csv,'/search')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
