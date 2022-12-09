import sqlite3
import datetime
import cherrypy
import threading
import time
import json

class RESTService(object):
    def __init__(self, service):
        self._service = service

    @cherrypy.expose
    def index(self):
        return "database plugin."
    
    @cherrypy.expose
    def fetch_all(self):
        return self._service._fetch_all()

    @cherrypy.expose
    def peek_all(self):
        return self._service._peek_all()

class DatabaseService:
    def __init__(self):
        self._data_queue = []

        server_thread = threading.Thread(target = self._server_job) # web service
        database_thread = threading.Thread(target = self._database_job) # database

        server_thread.start()
        database_thread.start()

    def _server_job(self):
        cherrypy.config.update({'server.socket_port': 8081})
        cherrypy.quickstart(RESTService(self))
    
    def _database_job(self):
        while True:
            self._process_data_queue()
            time.sleep(1)
    
    def _process_data_queue(self):
        while len(self._data_queue) > 0:
            with sqlite3.connect("DB0.db") as con:
                self._write(con, self._data_queue.pop(0))
    
    def _write(self, data, database_id):
        database = f"DB{database_id}.db"
        #print(database)
        with sqlite3.connect(database) as con:
            cur = con.cursor()

            # inserting
            count = cur.execute('INSERT OR IGNORE INTO data(id, GOT, GPT) VALUES (?, ?, ?) ON CONFLICT(id) DO UPDATE SET GOT = (?), GPT = (?)', (data["id"], data["GOT"], data["GPT"], data["GOT"], data["GPT"]))
            #count = cur.execute('ON CONFLICT(id) DO UPDATE SET GOT = data["GOT"], GPT = data["GPT"]')
            #sqlite_insert_query = f"INSERT OR IGNORE INTO data(id) VALUES (?)"
            #count = cur.execute(sqlite_insert_query, (3))
            #sqlite_insert_query = f"INSERT OR IGNORE INTO data(id, GOT, GPT) VALUES  (?, ?, ?)"
            #count = cur.execute(sqlite_insert_query, (data["id"], data["GOT"], data["GPT"]))
            con.commit()

       
    def _fetch_all(self, preserve_data = False):
        with sqlite3.connect("DB5.db") as con:
            cur = con.cursor()
            cur.execute('SELECT * FROM data')
            #cur.execute("""SELECT kind_name, field_name, value, timestamp, device_id, tag_name FROM records, kinds, fields, device_ids, tags, record_value, record_tag WHERE """
            #"""records.record_id = record_value.record_id AND records.kind_id = kinds.kind_id AND record_value.field_id = fields.field_id AND record_tag.tag_id = tags.tag_id""")
            rows = cur.fetchall()

            if not preserve_data:
                cur.execute("""DELETE FROM data""")
                con.commit()

            return json.dumps(rows)
        return ""

    def _peek_all(self):
        return self._fetch_all(preserve_data = True)
    
    def add_sample(self, data):
        self._data_queue.append((data, datetime.datetime.now()))

