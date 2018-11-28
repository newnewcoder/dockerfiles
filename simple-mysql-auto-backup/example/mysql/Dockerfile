FROM mysql:5.7
ADD db.sql /docker-entrypoint-initdb.d/db.sql
RUN chmod -R 775 /docker-entrypoint-initdb.d