import importlib

try:
    importlib.import_module('psycopg2')
    print('psycopg2 imported')
except ModuleNotFoundError:
    print('psycopg2 not imported')
    