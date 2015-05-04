import os
from kaha.bootstrap import app, db
from flask import Response, jsonify, request
from flask.ext.sqlalchemy import SQLAlchemy
import flask.ext.restful

import markdown2

from kaha.models import KahaResource, KahaResourceType, KahaResourceStat

from kaha import schemas

def _get_data(district, resource_types=''):
    resource_for = request.args.get('for', None)
    query_filter = KahaResource.query
    if (district != 'all'):
        query_filter = query_filter.filter(KahaResource.district.ilike("%" + district + "%"))
    if (resource_for):
        query_filter = query_filter.filter_by(resource_for=resource_for)
    if resource_types:
        query_filter = query_filter.join(KahaResource.types).filter(KahaResourceType.resource_type.in_(resource_types.split(',')))
   
    datalist = query_filter.all()
    serializer = schemas.KahaResourceSchema(many=True)
    result = serializer.dump(datalist)
    return jsonify({'resources':result.data})

@app.route("/")
def hello():
    with open(os.path.join('./', 'APIDOC.md')) as doc:
        return markdown2.markdown(doc.read())

@app.route("/resources/<district>")
def get_resources(district):
    return _get_data(district)
 
@app.route("/resources/<district>/<resource_types>")
def get_resource_of_types(district, resource_types):
    return _get_data(district, resource_types)

@app.route("/resource/<uuid>")
def get_resource(uuid):
    data = KahaResource.query.filter_by(uuid=uuid).first()
    if data:
        serializer = schemas.KahaResourceSchema()
        result = serializer.dump(data)
        return jsonify((result.data))#; //{'data':result.data}


if __name__ == "__main__":
    print "Running app"
    _port = 2000
    if os.environ['APP_SETTINGS'] == 'kaha.config.ProductionConfig':
        _port = 80

    app.run(host='0.0.0.0', port=_port)
