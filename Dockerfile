FROM python:3.8-slim
WORKDIR /root/MYSQLAPI/MYSQL
ADD . /root/MYSQLAPI/MYSQL
RUN pip install --upgrade pip
RUN pip install --no-cache-dir pymysql
RUN pip install -r requirements.txt
CMD ["python","-u","mysqlgpp.py","--host", "0.0.0.0"]
