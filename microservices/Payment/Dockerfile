FROM python:3
ADD Users.py /
ADD Users.db /
RUN pip install flask requests db-sqlite3
EXPOSE 5003
CMD [ "python", "./Users.py"]