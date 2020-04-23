docker stop $(docker ps -a -q --filter ancestor=micro_users)
docker stop $(docker ps -a -q --filter ancestor=micro_ticket)
docker stop $(docker ps -a -q --filter ancestor=micro_payment)
docker stop $(docker ps -a -q --filter ancestor=micro_gateway)
