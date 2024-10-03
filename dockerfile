FROM ubuntu:22.04

RUN apt-get update && \
    apt-get install -y git curl cron python3 python3-pip libpq-dev

COPY scripts/cronjob /scripts/cronjob
COPY scripts/run_update.sh /scripts/run_update.sh
COPY scripts/update_database.py /scripts/update_database.py
COPY requirements.txt /scripts/requirements.txt

RUN pip3 install -r /scripts/requirements.txt

RUN chmod +x /scripts/run_update.sh
RUN chmod +x /scripts/update_database.py

RUN touch /tmp/test_cron.txt

#RUN /scripts/run_update.sh

CMD ["cron", "-f"]