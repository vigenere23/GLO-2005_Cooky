gunicorn app:app -b 0.0.0.0:5000 -w 1 --log-level debug \
--env MYSQL_USER=api \
--env MYSQL_PASSWORD=e7364202-2f94-4355-b354-c95907adfef6
