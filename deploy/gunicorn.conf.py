from __future__ import unicode_literals
import multiprocessing

bind = "unix:/home/simon/eatabattery/gunicorn.sock"
workers = 1
errorlog = "/home/simon/eatabattery/logs/eatabattery_error.log"
loglevel = "error"
proc_name = "eatabattery"
