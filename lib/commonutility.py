"""API FOR COMMON FUNCTIONS IN MYSQLGPP"""
import json
import logging
import configparser
import inspect
import os
import sys
import time
from datetime import datetime
from flaskext.mysql import MySQL
tms = time.time()

tms_format = datetime.fromtimestamp(tms).strftime('%Y-%m-%d')

base_dir = os.getcwd()
if not os.access(base_dir, os.W_OK):
    sys.exit("No Write Permission")
filename = inspect.getframeinfo(inspect.currentframe()).filename
executablepath = os.path.dirname(os.path.abspath(filename))
programname = os.path.splitext(os.path.basename(filename))[0]
path = executablepath.split("\\")
path.pop()
S = "\\"
LOG_DIR = S.join(path)

codes = {'info': 'info'
    , 'success': '200'
    , 'Invalid Request': '400'
    , 'missing environment variables': '400'
    , 'configuration file missing': '400'
    , 'internal error': '500'
    , 'connection error': '501'
    , 'database error': '502'
    , 'Incorrect Parameters': '401'
    , 'directory missing' : '400'
    , 'invalid method':'405'
    , 'No Write Permission': '400'}

def read_config(file_name) :
    """Function To Read The Configuration File"""
    config = configparser.ConfigParser()
    config._interpolation = configparser.ExtendedInterpolation()
    config.read(file_name)
    filesection = config.sections()
    details = {}
    for section in filesection :
        details_dict = dict(config.items(section))
        details[section.lower()] = details_dict
    return details

def db_conn_mysql(app, username ,password ,host , port ,db_name):
    """Function To Create The connection"""
    if password.lower() == 'null':
        password =''
    app.config['MYSQL_DATABASE_USER'] = username
    app.config['MYSQL_DATABASE_PASSWORD'] = password
    app.config['MYSQL_DATABASE_DB'] = db_name
    app.config['MYSQL_DATABASE_HOST'] = host
    app.config['MYSQL_DATABASE_PORT'] = int(port)
    mysql = MySQL(app)
    return mysql

def db_conn_mssql(username, password, host, port, database) :
    """Function To Connect To The Database"""
    if password.lower() == 'null' :
        password = ''
    mssql = pymssql.connect(host=host,
                            user=username,
                            password=password,
                            port=port,
                            database=database)
    return mssql

def create_json(msg, custom_msg) :
    """Function To Create The JSON"""

    try :
        #custom_msg = str(custom_msg)
        if codes[msg] :
            result = {'headers' : {'Content-Type' : 'application/json'}, 'statusCode' : codes[msg]}
            if codes[msg] == '200' :
                result['body'] = custom_msg
            else :
                result['body'] = msg + ' : ' + custom_msg
            result = json.dumps(result)
            print(result)
            return result
        if not codes[msg] :
            result = {'headers' : {'Content-Type' : 'application/json'}, 'statusCode' : 'invalid code'}
            return result
    except Exception as e:
        msg = 'Invalid Request'
        res = create_json(msg, str(e))
        return res


def set_logs(program_name,logdir):
    """Function To Create The set logs"""
    program_name = logdir + '/' + program_name + "_" + str(tms_format)
    logger = logging.getLogger(program_name)
    loghandle = logging.FileHandler(program_name)
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    loghandle.setFormatter(formatter)
    logger.addHandler(loghandle)
    logger.setLevel(logging.DEBUG)
    return codes['success'], logger

def api_logs(inputdata,status,logger):
    """Function for logs"""
    if status == 'info':
        logger.info (inputdata)
    else:
        logger.error(inputdata)

def validate_param(request_list, request_json,logger ) :
    """Function To validate parameters"""
    print(request_json)
    print(request_list)
    if request_json['action'] == 'runtime':
        api_logs("Action : Runtime", 'info', logger)
        api_logs("Validating Parameters", 'info', logger)
        result_codes = loop_param_verfication(request_json,request_list,logger )
    elif request_json['action'] == 'predefined':
        api_logs("Action : Predefined", 'info', logger)
        api_logs("Validating Parameters", 'info', logger)
        result_codes = loop_param_verfication(request_json,request_list,logger )
    else:
        return codes['Invalid Request']
    return codes[result_codes]

def loop_param_verfication(request_json,request_list,logger ):
    """Function To Check the passing parameters"""
    # result = {}
    count = 0
    for param in request_list :
        count+=1
        if param in request_json and request_json[param] :
            api_logs(("Param " + str(count) + " : " + param), 'info', logger)
            pass
        else :
            msg = 'Invalid Request'
            api_logs(msg,'', logger)
            return msg
    return 'success'

def resultpredefine(record) :
    """Function To fetch results"""
    rowarray_list = []
    for result in record :
        content = {
            result[0]
        }
        rowarray_list.append(content)
        content = {}
    return rowarray_list

def lost_con(logger, error) :
    """Function TO Run When Connection is Lost or Not able to connect"""
    msg = 'connection error'
    result = create_json(msg, str(error))
    api_logs(result, '', logger)
    api_logs('Process Termination', '', logger)
    return result

def method_check_get(method , logger) :
    """Function to check method """
    if method != 'GET':
        res = create_json('invalid method', 'Valid Method is GET')
        api_logs(res, '', logger)
        return res
def method_check_post(method , logger) :
    """Function to check method """
    if method != 'POST':
        res = create_json('invalid method', 'Valid Method is POST')
        api_logs(res, '', logger)
        return res
def method_check_put(method , logger) :
    """Function to check method """
    if method != 'PUT':
        res = create_json('invalid method', 'Valid Method is PUT')
        api_logs(res, '', logger)
        return res

class MismatchError(Exception) :
    """class for mismatch error"""
    pass
