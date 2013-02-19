RealtimeWebStats
================

Real-time web application with CherryPy framework as server with WebSocket implementation ws4py.
Used for plotting cpu statistics retrieved with psutil.

Requirements
------------
- Python (tested with 2.7.2)
- CherryPy (tested with 3.2.2)
- Mako (tested with 0.7.3)
- ws4py (>= d60c3ac)

Usage
-----

Start server:

	python app.py

and start client:

	python sysmon.py

Open `http://127.0.0.1:9000` (port can be changed in global.conf)
