"""Class is used for Insert Api"""
import os
import sys
import inspect
from flask import Flask
from flask import request
from flask_restful import Resource, Api
from flask_cors import CORS
import pymysql
import pymysql.err
import lib.commonutility as commonutility
import json


api = ''
app = Flask(__name__)
api = Api(app)
cors = CORS(app, resources={r"/api/*" : {"origins" : "*"}})
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

base_dir = os.getcwd()
if not os.access(base_dir, os.W_OK) :
    sys.exit("No Write  Permission")
filename = inspect.getframeinfo(inspect.currentframe()).filename
programname = os.path.splitext(os.path.basename(filename))[0]
cfg_dir = os.path.join(base_dir, 'Cfg')
lib_dir = os.path.join(base_dir, 'lib')
LOG_DIR = os.path.join(base_dir, 'log')
if not os.path.exists(LOG_DIR) :
    os.mkdir(LOG_DIR)
if not os.path.exists(cfg_dir) or not os.path.exists(lib_dir):
    return_code, logger = commonutility.set_logs(programname, LOG_DIR)
    commonutility.api_logs('Config / Lib Directory missing', '', logger)
    commonutility.api_logs('Process Termination', '', logger)
    sys.exit()
cfg_file = cfg_dir + '//mysqlgpp.ini'
if not os.path.exists(cfg_file) :
    return_code, logger = commonutility.set_logs(programname, LOG_DIR)
    commonutility.api_logs('configuration file missing', '', logger)
return_code, logger = commonutility.set_logs(programname, LOG_DIR)


class SelectQuery(Resource ) :
    """Class is used for select Api"""
    api_name = 'MYSQL : Update Query'

    def post(self):
        """Function to check method """
        result = commonutility.method_check_get(request.method, logger)
        return result

    def put(self):
        """Function to check method """
        result = commonutility.method_check_get(request.method, logger)
        return result

    def get(self) :
        """function is used for select Api"""
        request_json = request.get_json()
        if request_json and 'action' in request_json :
            commonutility.api_logs('Initiate Process : ' + programname, 'info', logger)
            if request_json['action'] == 'predefined' :
                request_list = ['database', 'table', 'tag']
                result_code = commonutility.validate_param(request_list, request_json ,logger)

                if result_code != '200'  :
                    result = commonutility.create_json('Invalid Request','Incorrect Parameters')
                    commonutility.api_logs(result, '', logger)
                    return result
                details = commonutility.read_config('Cfg/mysqlgpp.ini')
                try:
                    mysql = commonutility.db_conn_mysql (app,details['mysql']['mysql_user']
                                                         , details['mysql']['mysql_password']
                                                         , details['mysql']['mysql_host']
                                                         , details['mysql']['mysql_port']
                                                         , details['database']['database_name'])
                    conn = mysql.connect()
                    cursor = conn.cursor()

                    tempquery = request_json['table']
                    tempquery = tempquery.lower()
                    var1 = request_json['tag']
                    query = details[tempquery + '_select'+'_'+var1][tempquery + '_query']
                    commonutility.api_logs("Query : " + query, 'info', logger)
                    cursor.execute(query)
                except Exception as error:
                    msg = 'Invalid Request'
                    res = commonutility.create_json(msg, 'Incorrect Parameters ' + str(error))
                    commonutility.api_logs(res, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return res
                except pymysql.DatabaseError as error:
                    msg = 'connection error'
                    result = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(result, 'error', logger)
                    commonutility.api_logs('Process Termination', 'error', logger)
                    return result
                if details[tempquery + '_select'+'_'+var1][tempquery + '_action'] !=\
                        request_json["action"] or \
                        details[tempquery + '_select'+'_'+var1][tempquery + '_tag'] !=\
                        request_json["tag"] or \
                        details['database']['database_name'] != \
                        request_json["database"]:
                    result = commonutility.create_json\
                        ('Incorrect Parameters', 'configuration file inputs mismatch')
                    commonutility.api_logs(result, '', logger)
                    return result
                if conn:
                    commonutility.api_logs\
                        ('Database Connection Status : Success', 'info', logger)
                    record_list = []
                    record = cursor.fetchall()
                    if not record :
                        res = commonutility.create_json('success', 'No Records Found')
                        commonutility.api_logs(res, 'info', logger)
                        commonutility.api_logs('Process Completed', 'info', logger)
                        return res
                    main_list = []
                    for rec in record:
                        sub_list = []
                        for value in range(0, len(rec)):
                            sub_list.append(rec[value])
                        main_list.append(sub_list)
                    record = json.dumps(main_list)
                    result = commonutility.create_json('success',
                                                   record)
                    commonutility.api_logs(result, 'info', logger)
                    commonutility.api_logs('Process Completed', 'info', logger)
                    return result
            elif request_json['action'] == 'runtime':
                request_list = ['database', 'table', 'fields',
                                'host', 'username', 'password', 'port']
                result_code = commonutility.validate_param(request_list, request_json ,logger)
                if result_code != '200':
                    result = commonutility.create_json('Invalid Request',
                                                       'invalid mandatory parameter')
                    commonutility.api_logs(result, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return result
                try :
                    mysql = commonutility.db_conn_mysql(app, request_json['username']
                                                                , request_json['password']
                                                                , request_json['host']
                                                                , request_json['port']
                                                                , request_json['database'])
                    conn = mysql.connect()
                except pymysql.DatabaseError as error:
                    msg = 'database error'
                    result = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(result, 'error', logger)
                    commonutility.api_logs('Process Termination', 'error', logger)
                    return result
                except ValueError as error:
                    msg = 'Invalid Request'
                    res = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(res, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return res
                if not conn:
                    msg = 'database error'
                    result = commonutility.create_json(msg, 'database issue')
                    commonutility.api_logs(result, 'error', logger)
                    commonutility.api_logs('Process Termination', 'error', logger)
                    return result
                if conn:
                    commonutility.api_logs('Successfull Database Connection', 'info', logger)
                cursor = conn.cursor()

                try:
                    query1 = 'select ' + request_json['fields'] + ' from ' + request_json['table']
                    if (request_json['condition'] and request_json['groupby']) == "":
                        query = query1
                    if request_json['condition'] != "":
                        query = query1 + ' where ' + request_json['condition']
                    if request_json['groupby'] != "":
                        query = query1 + ' group by ' + request_json['groupby']
                    if (request_json['condition'] and request_json['groupby']) != "":
                        query = query1 + ' where ' + request_json['condition'] + ' group by ' + request_json['groupby']
                    commonutility.api_logs("Query : " + query , 'info', logger)
                    cursor.execute(query)
                except Exception as error :
                    msg = 'Invalid Request'
                    result = commonutility.create_json(msg, str(error) )
                    commonutility.api_logs(result, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return result
                record = cursor.fetchall()
                if not record:
                    res = commonutility.create_json('success', 'No Records Found')
                    commonutility.api_logs(res, 'info', logger)
                    commonutility.api_logs('Process Completed', 'info', logger)
                    return res

                main_list = []
                for rec in record:
                    sub_list= []
                    for value in range(0,len(rec)):
                        sub_list.append(rec[value])
                    main_list.append(sub_list)
                #record = json.dumps(main_list)
                result = commonutility.create_json('success',
                                                   main_list)
                commonutility.api_logs(result, 'info', logger)
                commonutility.api_logs('Process Completed', 'info', logger)
                return result
            else:
                msg = 'Invalid Request'
                result = commonutility.create_json(msg, 'Incorrect Action')
                commonutility.api_logs(result, '', logger)
                commonutility.api_logs('Process Termination', '', logger)
                return result
        else:
            msg = 'Invalid Request'
            result = commonutility.create_json(msg, 'Incorrect Parameters')
            commonutility.api_logs(result, '', logger)
            commonutility.api_logs('Process Termination', '', logger)
            return result

class InsertQuery(Resource) :
    """Class is used for Insert Api"""
    api_name = 'MYSQL : Update Query'
    def get(self):
        """Function to check method """
        result = commonutility.method_check_post(request.method, logger)
        return result

    def put(self):
        """Function to check method """
        result = commonutility.method_check_post(request.method, logger)
        return result
    def post(self) :
        """function is used for Insert Api"""
        request_json = request.get_json()
        if request_json and 'action' in request_json :
            commonutility.api_logs('Initiate Process : ' + programname, 'info', logger)
            if request_json['action'] == 'predefined' :
                request_list = ['database', 'table', 'tag']
                result_code = commonutility.validate_param(request_list, request_json ,logger)
                if result_code != '200':
                    result = commonutility.create_json('Invalid Request',
                                                       'invalid mandatory parameter')
                    commonutility.api_logs(result, '', logger)
                    return result
                details = commonutility.read_config('Cfg/mysqlgpp.ini')
                try:
                    mysql = commonutility.db_conn_mysql (app,details['mysql']['mysql_user']
                                                         , details['mysql']['mysql_password']
                                                         , details['mysql']['mysql_host']
                                                         , details['mysql']['mysql_port']
                                                         , details['database']['database_name'])
                    conn = mysql.connect()
                    commonutility.api_logs('Successfull Database Connection', 'info', logger)
                    cursor = conn.cursor()
                    tempquery = request_json['table']
                    tempquery = tempquery.lower()
                    var1 = request_json['tag'].lower()
                    query = "insert into " + \
                            details[tempquery + '_insert'+'_'+var1][tempquery + '_table_name'] \
                            + "(" + details[tempquery + '_insert'+'_'+var1][tempquery + '_fields'] \
                            + ") values ( " \
                            + details[tempquery + '_insert' +'_'+var1][tempquery + '_values'] \
                            + ")"

                    query = query.lower()
                    if details[tempquery + '_insert'+'_'+var1][tempquery + '_action'] != \
                                request_json["action"] or \
                                details[tempquery + '_insert'+'_'+var1][tempquery + '_tag'] != \
                                request_json["tag"] or \
                                details['database']['database_name'] != \
                                request_json["database"]:
                        result = commonutility.create_json \
                            ('Incorrect Parameters', 'configuration file inputs mismatch')
                        commonutility.api_logs(result, '', logger)
                        return result
                    cursor.execute(query)
                    conn.commit()
                except pymysql.DatabaseError as error:
                    msg = 'database error'
                    result = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(result, 'error', logger)
                    commonutility.api_logs('Process Termination', 'error', logger)
                    return result
                except Exception as error:
                    msg = 'Invalid Request'
                    res = commonutility.create_json(msg, 'Incorrect Parameters '+str(error))
                    commonutility.api_logs(res, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return res
                if conn:
                    commonutility.api_logs('Database Connection Status : Success', 'info', logger)
                    res = {'Status': 'Records Inserted in fields -> ' +
                                     details[tempquery + '_insert'+'_'+var1][tempquery + '_fields']
                                     + '  with values -> ' + details[tempquery + '_insert'+'_'+var1]
                                     [tempquery + '_values'] }
                    result = commonutility.create_json('success',
                                                       res)
                    commonutility.api_logs(result, 'info', logger)
                    commonutility.api_logs('Process Completed', 'info', logger)
                    return result
            elif request_json['action'] == 'runtime':
                request_list = ['database', 'table', 'fields', 'values',
                                'host', 'username', 'password', 'port']
                result_code = commonutility.validate_param(request_list,
                                                           request_json ,logger)
                if result_code != '200':
                    result = commonutility.create_json('Invalid Request',
                                                       'invalid mandatory parameter')
                    commonutility.api_logs(result, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return result
                try :
                    mysql = commonutility.db_conn_mysql(app, request_json['username']
                                                                , request_json['password']
                                                                , request_json['host']
                                                                , request_json['port']
                                                                , request_json['database'])
                    conn = mysql.connect()
                except pymysql.DatabaseError as error:
                    msg = 'database error'
                    result = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(result, 'error', logger)
                    commonutility.api_logs('Process Termination', 'error', logger)
                    return result
                except ValueError as error:
                    msg = 'Invalid Request'
                    res = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(res, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return res
                if not conn:
                    msg = 'database error'
                    result = commonutility.create_json(msg, 'database issue')
                    commonutility.api_logs(result, 'error', logger)
                    commonutility.api_logs('Process Termination', 'error', logger)
                    return result
                if conn:
                    commonutility.api_logs('Successfull Database Connection', 'info', logger)
                cursor = conn.cursor()
                try:
                    query = 'INSERT INTO ' + request_json['table'] + \
                            '(' + request_json['fields'] + \
                            ' ) ' + 'VALUES ( ' + request_json['values'] + ')'
                    cursor.execute(query)
                    conn.commit()
                except pymysql.DatabaseError as error:
                    msg = 'database error'
                    result = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(result, 'error', logger)
                    commonutility.api_logs('Process Termination', 'error', logger)
                    return result
                except Exception as error:
                    msg = 'Invalid Request'
                    res = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(res, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return res
                res = {'Status': 'Records Inserted in fields -> '
                                 + request_json['fields']
                                 +'  with values -> '
                                 + request_json['values'] }
                result = commonutility.create_json('success',
                                                   res)
                commonutility.api_logs(result, 'info', logger)
                commonutility.api_logs('Process Completed', 'info', logger)
                return result
            else:
                msg = 'Invalid Request'
                result = commonutility.create_json(msg, 'Incorrect Action')
                commonutility.api_logs(result, '', logger)
                return result
        else:
            msg = 'Invalid Request'
            result = commonutility.create_json(msg, 'Incorrect Parameters')
            commonutility.api_logs(result, '', logger)
            commonutility.api_logs('Process Termination', '', logger)
            return result

class UpdateQuery(Resource) :
    """Class is used for Insert Api"""
    api_name = 'MYSQL : Update Query'
    def get(self):
        """Function to check method """
        result = commonutility.method_check_put( request.method , logger)
        return result
    def post(self):
        """Function to check method """
        result = commonutility.method_check_put(request.method, logger)
        return result
    def put(self) :
        """function is used for Insert Api"""
        request_json = request.get_json()
        if request_json and 'action' in request_json :
            commonutility.api_logs('Initiate Process : ' + programname, 'info', logger)
            if request_json['action'] == 'predefined' :
                request_list = ['database', 'table', 'tag']
                result_code = commonutility.validate_param(request_list, request_json ,logger)
                if result_code != '200':
                    result = commonutility.create_json('Invalid Request',
                                                       'invalid mandatory parameter')
                    commonutility.api_logs(result, '', logger)
                    return result
                details = commonutility.read_config('Cfg/mysqlgpp.ini')
                try:
                    mysql = commonutility.db_conn_mysql (app,details['mysql']['mysql_user']
                                                         , details['mysql']['mysql_password']
                                                         , details['mysql']['mysql_host']
                                                         , details['mysql']['mysql_port']
                                                         , details['database']['database_name'])
                    conn = mysql.connect()
                    commonutility.api_logs('Successfull Database Connection', 'info', logger)
                    cursor = conn.cursor()
                    tempquery = request_json['table']
                    tempquery = tempquery.lower()
                    var1 = request_json['tag'].lower()
                    if details[tempquery + '_update'+'_'+var1][tempquery + '_action'] != \
                            request_json["action"] or \
                            details[tempquery + '_update'+'_'+var1][tempquery + '_tag'] != \
                            request_json["tag"] or \
                            details['database']['database_name'] != \
                            request_json["database"]:
                        result = commonutility.create_json \
                            ('Incorrect Parameters', 'configuration file inputs mismatch')
                        commonutility.api_logs(result, '', logger)
                        return result
                    query = "update  " + details[tempquery + '_update'+'_'+var1][tempquery + '_table_name'] \
                            + "  set " + details[tempquery + '_update'+'_'+var1][tempquery + '_colvalues']\
                            + "  where  "+details[tempquery + '_update'+'_'+var1][tempquery + '_condition']
                    query = query.lower()
                    cursor.execute(query)
                    conn.commit()
                except pymysql.DatabaseError as error:
                    msg = 'database error'
                    result = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(result, 'error', logger)
                    commonutility.api_logs('Process Termination', 'error', logger)
                    return result
                except Exception as error:
                    msg = 'Invalid Request'
                    res = commonutility.create_json(msg, 'Incorrect Parameters '+str(error))
                    commonutility.api_logs(res, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return res
                if conn:
                    commonutility.api_logs('Database Connection Status : Success', 'info', logger)
                    res = {'Status': 'Records Updated , setting  ' +
                                     details[tempquery + '_update'+'_'+var1][tempquery + '_colvalues']
                                     + '  where  '
                                     + details[tempquery + '_update'+'_'+var1][tempquery + '_condition']}
                    result = commonutility.create_json('success',
                                                       res)
                    commonutility.api_logs(result, 'info', logger)
                    commonutility.api_logs('Process Completed', 'info', logger)
                    return result
            elif request_json['action'] == 'runtime':
                request_list = ['database', 'table', 'condition', 'colvalues',
                                'host', 'username', 'password', 'port']
                result_code = commonutility.validate_param(request_list,
                                                           request_json ,logger)
                if result_code != '200':
                    result = commonutility.create_json('Invalid Request',
                                                       'invalid mandatory parameter')
                    commonutility.api_logs(result, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return result
                try :
                    mysql = commonutility.db_conn_mysql(app, request_json['username']
                                                                , request_json['password']
                                                                , request_json['host']
                                                                , request_json['port']
                                                                , request_json['database'])
                    conn = mysql.connect()
                except pymysql.DatabaseError as error:
                    msg = 'database error'
                    result = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(result, 'error', logger)
                    commonutility.api_logs('Process Termination', 'error', logger)
                    return result
                except ValueError as error:
                    msg = 'Invalid Request'
                    res = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(res, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return res
                if not conn:
                    msg = 'database error'
                    result = commonutility.create_json(msg, 'database issue')
                    commonutility.api_logs(result, 'error', logger)
                    commonutility.api_logs('Process Termination', 'error', logger)
                    return result
                if conn:
                    commonutility.api_logs('Successfull Database Connection', 'info', logger)
                cursor = conn.cursor()
                try:
                    query = 'UPDATE ' + request_json['table'] + '  SET  ' + \
                            request_json['colvalues'] + '  where ' + \
                            request_json['condition']
                    cursor.execute(query)
                    conn.commit()
                except pymysql.DatabaseError as error:
                    msg = 'database error'
                    result = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(result, 'error', logger)
                    commonutility.api_logs('Process Termination', 'error', logger)
                    return result
                except Exception as error:
                    msg = 'Invalid Request'
                    res = commonutility.create_json(msg, str(error))
                    commonutility.api_logs(res, '', logger)
                    commonutility.api_logs('Process Termination', '', logger)
                    return res
                else :
                    res = {'Status': 'Records Updated , setting  '
                                     + request_json['colvalues']
                                     + '  where  '
                                     + request_json['condition'] }
                    result = commonutility.create_json('success',
                                                       res)
                    commonutility.api_logs(result, 'info', logger)
                    commonutility.api_logs('Process Completed', 'info', logger)
                    return result
            else:
                msg = 'Invalid Request'
                result = commonutility.create_json(msg, 'Incorrect Action')
                commonutility.api_logs(result, '', logger)
                commonutility.api_logs('Process Termination', '', logger)
                return result
        else:
            msg = 'Invalid Request'
            result = commonutility.create_json(msg, 'Incorrect Parameters')
            commonutility.api_logs(result, '', logger)
            commonutility.api_logs('Process Termination', '', logger)
            return result

api.add_resource(SelectQuery, '/SelectQuery/')
api.add_resource(InsertQuery, '/InsertQuery/')
api.add_resource(UpdateQuery, '/UpdateQuery/')
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5010)
    app.run(debug=True)