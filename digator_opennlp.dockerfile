FROM        docker.io/python:3.8-slim

ENV         APP_DIR="/digator-label-studio"
ENV         PIP_CONFIG_FILE="$APP_DIR/pip.conf"

COPY        "work/digator_opennlp.py" "$APP_DIR/digator_opennlp.py"
COPY        "work/requirements.txt" "$APP_DIR/requirements.txt"

RUN         pip install -r "$APP_DIR/requirements.txt" && \
            label-studio-ml init "$APP_DIR/digator_opennlp" --script "$APP_DIR/digator_opennlp.py"

RUN         groupadd -g 1000 "digator" && \
            useradd -l -u 1000 -g "digator" -s "/bin/bash" -d "$APP_DIR" "digator" && \
            chown -R "digator:digator" "$APP_DIR"

USER        "digator"

WORKDIR     "$APP_DIR"

CMD         ["label-studio-ml", "start", "./digator_opennlp"]