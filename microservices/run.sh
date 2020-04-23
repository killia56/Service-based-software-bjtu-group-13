cd Users
docker build -t micro_users .
docker run -i -p 5001:5001 -d micro_users
cd ../Ticket
docker build -t micro_ticket .
docker run -i -p 5002:5002 -d micro_ticket
cd ../Payment
docker build -t micro_payment .
docker run -i -p 5003:5003 -d micro_payment
cd ../Gateway
docker build -t micro_gateway .
docker run -i -p 5004:5004 -d micro_gateway