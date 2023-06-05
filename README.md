#### Run from docker hub
`docker run -d --name zato-cron plydot/zato-cron`

##### Start the container
###### Test Env
- `docker run -d --name zato-cron  -e DEBUG=1 plydot/zato-cron:latest`
- `docker run -d --name zato-cron  -e DEBUG=1 -e START_COUNT=1 -e END_COUNT=2 plydot/zato-cron:latest`

##### Prod SetUp
###### Quick Start

```sh 
git clone https://github.com/whippetwilson/nira-data-transfer.git && cd nira-data-transfer && chmod +x run-zato-cron.sh && ./run-zato-cron.sh
```
##### Customized SetUp

```sh
docker run  -d --name zato-cron -e NIRA_URL=http://example.com \
           -e NIRA_USERNAME=myusername \
           -e NIRA_PASSWORD=mypassword \
           -e NIRA_REALM=myrealm \
           -e DHIS_BASE_URL=https://example.org \
           -e DHIS_DATA_URL=/my/data/url \
           -e DHIS_USERNAME=mydhisusername \
           -e DHIS_PASSWORD=mydhispwd \
           -e DEBUG=0 \
           plydot/zato-cron:latest
```

#### Build Container your self
```sh
docker build -t zato-cron:latest .
```

#### Run Inside the container
`docker exec -it zato-cron bash` \
`python3 /main.py` \
`export START_COUNT=10` \
`export END_COUNT=20`

