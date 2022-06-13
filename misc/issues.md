8000000-17307.08000000-17312.54000000-94.46270600
Checking timestamp 1606388820000 @ pos. 497 for ETHUSDT.
Getting candle ETHUSDT, time: 2020-11-26 12:08:00: OHLCV: 515.79000000-516.20000000-514.61000000-514.65000000-1225.20284000
Checking timestamp 1606388820000 @ pos. 497 for ADAUSDT.
Getting candle ADAUSDT, time: 2020-11-26 12:08:00: OHLCV: 0.13899000-0.13918000-0.13815000-0.13843000-1525975.40000000
Checking timestamp 1606388820000 @ pos. 497 for XRPUSDT.
Getting candle XRPUSDT, time: 2020-11-26 12:08:00: OHLCV: 0.54743000-0.54800000-0.54364000-0.54649000-2485905.40000000
The time is 2020-11-26 12:10:45.642308
Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 159, in _new_conn
    conn = connection.create_connection(
  File "/usr/lib/python3/dist-packages/urllib3/util/connection.py", line 61, in create_connection
    for res in socket.getaddrinfo(host, port, family, socket.SOCK_STREAM):
  File "/usr/lib/python3.8/socket.py", line 918, in getaddrinfo
    for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -3] Temporary failure in name resolution

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 665, in urlopen
    httplib_response = self._make_request(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 376, in _make_request
    self._validate_conn(conn)
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 996, in _validate_conn
    conn.connect()
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 314, in connect
    conn = self._new_conn()
  File "/usr/lib/python3/dist-packages/urllib3/connection.py", line 171, in _new_conn
    raise NewConnectionError(
urllib3.exceptions.NewConnectionError: <urllib3.connection.VerifiedHTTPSConnection object at 0x7f9f3b431c40>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 439, in send
    resp = conn.urlopen(
  File "/usr/lib/python3/dist-packages/urllib3/connectionpool.py", line 719, in urlopen
    retries = retries.increment(
  File "/usr/lib/python3/dist-packages/urllib3/util/retry.py", line 436, in increment
    raise MaxRetryError(_pool, url, error or ResponseError(cause))
urllib3.exceptions.MaxRetryError: HTTPSConnectionPool(host='api.binance.com', port=443): Max retries exceeded with url: /api/v3/klines?symbol=BTCUSDT&interval=1m (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f9f3b431c40>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "start.py", line 36, in <module>
    main()
  File "start.py", line 30, in main
    coin.checkHistory()
  File "./modules/candle.py", line 63, in checkHistory
    r = requests.get(url)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 75, in get
    return request('get', url, params=params, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/api.py", line 60, in request
    return session.request(method=method, url=url, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 533, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/lib/python3/dist-packages/requests/sessions.py", line 646, in send
    r = adapter.send(request, **kwargs)
  File "/usr/lib/python3/dist-packages/requests/adapters.py", line 516, in send
    raise ConnectionError(e, request=request)
requests.exceptions.ConnectionError: HTTPSConnectionPool(host='api.binance.com', port=443): Max retries exceeded with url: /api/v3/klines?symbol=BTCUSDT&interval=1m (Caused by NewConnectionError('<urllib3.connection.VerifiedHTTPSConnection object at 0x7f9f3b431c40>: Failed to establish a new connection: [Errno -3] Temporary failure in name resolution'))
