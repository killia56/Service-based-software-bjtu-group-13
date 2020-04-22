FROM python:3
ADD Payment.py /
ADD Payment.db /
RUN pip install flask requests db-sqlite3
EXPOSE 5003
CMD [ "python", "./Payment.py"]