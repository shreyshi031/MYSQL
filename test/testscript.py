import unittest
from unittest import mock
import pytest
import MYSQLGPP  # importing main code
# from mysql import app  # importing app from main code
import flask as Flask
import MYSQLGPP
from MYSQLGPP import app
from flask import json
import json

class test_msql(unittest.TestCase) :
    def setUp(self) :
        self.myapp = app.test_client()
    def test_sample(self) :
        print("test_sample")
        response = self.myapp.get('/SelectQuery/')
        response = response.get_json()
        data = (json.loads(response))
        valid = data['statusCode']
        assert valid == '400'

    def test_validate_param2(self):
        print("Param 2")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type" : "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '200'
    def test_validate_param3(self):
        print("Param 3")
        payload = "{\r\n    \"action\": \"runtime1\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type" : "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'
    def test_validate_param4(self):
        print("Param 4")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root1\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type" : "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param5(self):
        print("Param 5")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"33061\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'
    def test_validate_param6(self):
        print("Param 6")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon1\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'
    def test_validate_param7(self):
        print("Param 7")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost1\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param8(self):
        print("Param 8")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts1\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'
    def test_validate_param9(self):
        print("Param 9")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName1\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param10(self):
        print("Param 10")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man11'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '200'
    def test_validate_param11(self):
        print("Param 11")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName1\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param12(self):
        print("Param 12")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null1\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param13(self):
        print("Param 13")
        payload = "{\r\n    \"action1\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param14(self):
        print("Param 14")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database1\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param15(self):
        print("Param 15")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username1\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'
    def test_validate_param16(self):
        print("Param 16")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password1\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param17(self):
        print("Param 17")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host1\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'
    def test_validate_param18(self):
        print("Param 18")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port1\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'
    def test_validate_param19(self):
        print("Param 19")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table1\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param20(self):
        print("Param 20")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields1\":\"vehicleName\",\r\n    \"condition\":\"customerName = 'man1'\",\r\n   \"groupby\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param21(self):
        print("Param 21")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName\",\r\n    \"condition1\":\"customerName = 'man1'\",\r\n   \"groupby1\":\"vehicleName\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param22(self):
        print("Param 22- predef")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"discarded_vehicle_alerts\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '200'

    def test_validate_param23(self):
        print("Param 23")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"discarded_vehicle_alerts\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '200'

    def test_validate_param24(self):
        print("Param 24")
        payload = "{\r\n    \"action1\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"discarded_vehicle_alerts\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param25(self):
        print("Param 25")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database1\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"discarded_vehicle_alerts\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param26(self):
        print("Param 26")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table1\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"discarded_vehicle_alerts\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param27(self):
        print("Param 27")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag1\":\"discarded_vehicle_alerts\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param28(self):
        print("Param 28")
        payload = "{\r\n    \"action\": \"predefined1\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"discarded_vehicle_alerts\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'
    def test_validate_param29(self):
        print("Param 29")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon1\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"discarded_vehicle_alerts\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '401'
    def test_validate_param30(self):
        print("Param 30")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts1\",\r\n    \"tag\":\"discarded_vehicle_alerts\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param31(self):
        print("Param 31")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"discarded_vehicle_alerts1\"}"
        response = self.myapp.get('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '401'

    def test_validate_param32(self):
        print("Param 32")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.post('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'

    def test_validate_param33(self):
        print("Param 33")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.put('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'

    def test_validate_param34(self):
        print("Param 34")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"}"
        response = self.myapp.post('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'

    def test_validate_param35(self):
        print("Param 35")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"}"
        response = self.myapp.put('/SelectQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'

#########################################################################################################################################################################################
    #####################################################################################################################################################################################



    def test_sampleinsert(self):
        print("test_sample")
        response = self.myapp.post('/InsertQuery/')
        response = response.get_json()
        data = (json.loads(response))
        valid = data['statusCode']
        assert valid == '400'

    # def test_validate_param_insert1(self):
    #     print("Param 1")
    #     # payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"LibraryDB\" ,\r\n    \"username\" : \"admin\" ,\r\n    \"password\": \"1234\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"1433\",\r\n    \"table\":\"books\",\r\n    \"fields\":\"Name\",\r\n    \"values\":\"Name='Book - A' OR Name='Book - B'\"\r\n}"
    #     payload = {   "action": "runtime1" , "database" :"icon" , "username" : "root" , "password": "null" , "host":"localhost" , "port":"3306", "table" :"discarded_vehicle_alerts" , "fields" :"vehicleName, customerName, StatusCheck" , "values" : "'TANISHQkhanna11ddd221' , 'man1' , 'fine'" , "groupby" : "vehicleName, customerName, StatusCheck"}
    #     response = self.myapp.get('/InsertQuery/', headers={"Content-Type" : "application/json"}, data=payload)
    #     print("Valid Test res first")
    #     print(response)
    #     response = response.get_json()
    #     print("Valid Test Res")
    #     print(response)
    #     data = (json.loads(response))
    #     print("Valid Test JSON")
    #     print(data)
    #     valid = data['statusCode']
    #     print("Valid Test")
    #     print(valid)
    #     assert valid == '200'
    def test_validate_param_insert2(self):
        print("Param 2")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'OMkaar' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '200'

    def test_validate_param_insert3(self):
        print("Param 3")
        payload = "{\r\n    \"action\": \"runtime1\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert4(self):
        print("Param 4")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root1\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_insert5(self):
        print("Param 5")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"33061\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_insert6(self):
        print("Param 6")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon1\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_insert7(self):
        print("Param 7")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost1\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_insert8(self):
        print("Param 8")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts1\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_insert9(self):
        print("Param 9")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck1\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_insert10(self):
        print("Param 10")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' \"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_insert11(self):
        print("Param 11")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkha' , 'man1' , 'fine'\"}"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_insert12(self):
        print("Param 12")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null1\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_insert13(self):
        print("Param 13")
        payload = "{\r\n    \"action1\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert14(self):
        print("Param 14")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database1\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert15(self):
        print("Param 15")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username1\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert16(self):
        print("Param 16")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password1\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert17(self):
        print("Param 17")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host1\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert18(self):
        print("Param 18")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port1\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert19(self):
        print("Param 19")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table1\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert20(self):
        print("Param 20")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields1\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"  }"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert21(self):
        print("Param 21")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"fields\":\"vehicleName, customerName, StatusCheck\",\r\n    \"values1\":\"'TANISHQkhanna11ddd221' , 'man1' , 'fine'\"}"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert22(self):
        print("Param 22- predef")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUSHSTATUS\"}"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '200'

    def test_validate_param_insert23(self):
        print("Param 23")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUSHSTATUS\"}"
        response = self.myapp.put('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'

    def test_validate_param_insert24(self):
        print("Param 24")
        payload = "{\r\n    \"action1\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUSHSTATUS\"}"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert25(self):
        print("Param 25")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database1\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUSHSTATUS\"}"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert26(self):
        print("Param 26")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table1\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUSHSTATUS\"}"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert27(self):
        print("Param 27")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag1\":\"PUSHSTATUS\"}"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert28(self):
        print("Param 28")
        payload = "{\r\n    \"action\": \"predefined1\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUSHSTATUS\"}"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert29(self):
        print("Param 29")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon1\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUSHSTATUS\"}"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '401'

    def test_validate_param_insert30(self):
        print("Param 30")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts1\",\r\n    \"tag\":\"PUSHSTATUS\"}"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_insert31(self):
        print("Param 31")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUSHSTATUS1\"}"
        response = self.myapp.post('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '401'

    def test_validate_param_insert32(self):
        print("Param 32")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.get('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'

    def test_validate_param_insert33(self):
        print("Param 33")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.put('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'

    def test_validate_param_insert34(self):
        print("Param 34")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"}"
        response = self.myapp.get('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'

    def test_validate_param_insert35(self):
        print("Param 35")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"}"
        response = self.myapp.put('/InsertQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'

    ##################################################################################################------------------------------------------------------------------------------------------------------
    def test_sampleupdate(self) :
        print("test_sample")
        response = self.myapp.put('/UpdateQuery/')
        response = response.get_json()
        data = (json.loads(response))
        valid = data['statusCode']
        assert valid == '400'
    # def test_validate_param_update1(self):
    #     print("Param 1")
    #     payload = {   "action": "runtime1" , "database" :"icon" , "username" : "root" , "password": "null" , "host":"localhost" , "port":"3306", "table" :"discarded_vehicle_alerts" , "colvalues" :"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'" , "condition" : "vehicleName = 'test 1'" , "groupby" : "vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'"}
    #     response = self.myapp.get('/UpdateQuery/', headers={"Content-Type" : "application/json"}, data=payload)
    #     print("Valid Test res first")
    #     print(response)
    #     response = response.get_json()
    #     print("Valid Test Res")
    #     print(response)
    #     data = (json.loads(response))
    #     print("Valid Test JSON")
    #     print(data)
    #     valid = data['statusCode']
    #     print("Valid Test")
    #     print(valid)
    #     assert valid == '200'
    def test_validate_param_update2(self):
        print("Param 2")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is succes' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'TANISHQpass1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type" : "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '200'
    def test_validate_param_update3(self):
        print("Param 3")
        payload = "{\r\n    \"action\": \"runtime1\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type" : "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'
    def test_validate_param_update4(self):
        print("Param 4")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root1\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type" : "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_update5(self):
        print("Param 5")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"33061\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'
    def test_validate_param_update6(self):
        print("Param 6")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon1\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'
    def test_validate_param_update7(self):
        print("Param 7")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost1\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_update8(self):
        print("Param 8")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts1\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'
    def test_validate_param_update9(self):
        print("Param 9")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'1\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_update10(self):
        print("Param 10")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successfu' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'TANISHQpass'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '200'
    def test_validate_param_update11(self):
        print("Param 11")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"'TANISHQkha' , 'man1' \"}"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_update12(self):
        print("Param 12 sahi ker")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null111\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '502'

    def test_validate_param_update13(self):
        print("Param 13")
        payload = "{\r\n    \"action1\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_update14(self):
        print("Param 14")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database1\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_update15(self):
        print("Param 15")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username1\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'
    def test_validate_param_update16(self):
        print("Param 16")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password1\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_update17(self):
        print("Param 17")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host1\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'
    def test_validate_param_update18(self):
        print("Param 18")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port1\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'
    def test_validate_param_update19(self):
        print("Param 19")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table1\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_update20(self):
        print("Param 20")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues1\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"  }"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_update21(self):
        print("Param 21")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition1\":\"vehicleName = 'test 1'\"}"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_update22(self):
        print("Param 22- predef")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '200'

    def test_validate_param_update23(self):
        print("Param 23")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.post('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'

    def test_validate_param_update24(self):
        print("Param 24")
        payload = "{\r\n    \"action1\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_update25(self):
        print("Param 25")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database1\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_update26(self):
        print("Param 26")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table1\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_update27(self):
        print("Param 27")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag1\":\"PUTSTATUS\"}"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_update28(self):
        print("Param 28")
        payload = "{\r\n    \"action\": \"predefined1\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'
    def test_validate_param_update29(self):
        print("Param 29")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon1\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '401'
    def test_validate_param_update30(self):
        print("Param 30")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts1\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '400'

    def test_validate_param_update31(self):
        print("Param 31")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS1\"}"
        response = self.myapp.put('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '401'

    def test_validate_param_update32(self):
        print("Param 32")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.get('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'


    def test_validate_param_update33(self):
        print("Param 33")
        payload = "{\r\n    \"action\": \"predefined\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"tag\":\"PUTSTATUS\"}"
        response = self.myapp.post('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'


    def test_validate_param_update34(self):
        print("Param 34")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"}"
        response = self.myapp.get('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'


    def test_validate_param_update35(self):
        print("Param 35")
        payload = "{\r\n    \"action\": \"runtime\" ,\r\n    \"database\" :\"icon\" ,\r\n    \"username\" : \"root\" ,\r\n    \"password\": \"null\" ,\r\n    \"host\":\"localhost\" ,\r\n    \"port\":\"3306\",\r\n    \"table\":\"discarded_vehicle_alerts\",\r\n    \"colvalues\":\"vehicleName = 'TEST is successful' , customerName = 'man1' , StatusCheck = 'fine'\",\r\n    \"condition\":\"vehicleName = 'test 1'\"}"
        response = self.myapp.post('/UpdateQuery/', headers={"Content-Type": "application/json"}, data=payload)
        print("Valid Test res first")
        print(response)
        response = response.get_json()
        print("Valid Test Res")
        print(response)
        data = (json.loads(response))
        print("Valid Test JSON")
        print(data)
        valid = data['statusCode']
        print("Valid Test")
        print(valid)
        assert valid == '405'
if __name__ == '__main__' :
    unittest.main()