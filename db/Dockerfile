FROM alpine:3.12
LABEL maintainer="vladislav st091242@student.spbu.ru"

RUN apk add --no-cache sqlite
WORKDIR /db
COPY init.sql /db/
RUN sqlite3 mydatabase.db < init.sql

VOLUME ["/db"]
CMD ["sqlite3", "/db/mydatabase.db"]
