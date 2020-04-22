FROM python:3
ADD Gateway.py /
RUN pip install flask requests
EXPOSE 5004
CMD [ "python", "./Gateway.py"]