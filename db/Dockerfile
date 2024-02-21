FROM alpine:3.12
LABEL maintainer="vladislav st091242@student.spbu.ru"

RUN apk add --no-cache sqlite
WORKDIR /db
RUN sqlite3 mydatabase.db "CREATE TABLE IF NOT EXISTS test (id INTEGER PRIMARY KEY, value TEXT NOT NULL);"
VOLUME ["/db"]
CMD ["sqlite3", "/db/mydatabase.db"]
