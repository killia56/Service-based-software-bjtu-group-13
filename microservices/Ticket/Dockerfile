FROM python:3
ADD Ticket.py /
ADD Ticket.db /
RUN pip install flask requests db-sqlite3
EXPOSE 5002
CMD [ "python", "./Ticket.py"]