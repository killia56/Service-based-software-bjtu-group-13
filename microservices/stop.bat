PowerShell.exe -Command "docker stop $(docker ps -a -q --filter ancestor=micro_users)"
PowerShell.exe -Command "docker stop $(docker ps -a -q --filter ancestor=micro_ticket)"
PowerShell.exe -Command "docker stop $(docker ps -a -q --filter ancestor=micro_payment)"