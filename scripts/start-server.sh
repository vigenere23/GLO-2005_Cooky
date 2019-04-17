gunicorn app:app -b 0.0.0.0:5000 -w 1 --log-level debug \
--env DB_HOST=localhost