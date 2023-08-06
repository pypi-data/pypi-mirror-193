#!/usr/bin/python3

import time
from datetime import datetime
import socket
#from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR
import signal
from pathlib import Path
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread
from multiprocessing import Pipe, Process
import yaml
import os
import logging
import getopt
import sys

class SignalHandler:
    shutdown_requested = False
    obj_toclose = None

    def __init__(self):
        #signal.signal(signal.SIGINT, self.request_shutdown)
        #signal.signal(signal.SIGTERM, self.request_shutdown)
        pass

    def request_shutdown(self, *args):
        print('Request to shutdown received, stopping')
        self.onshutdown()
        self.shutdown_requested = True

    def can_run(self):
        return not self.shutdown_requested

    def onshutdown(self):
        print('OnShutdown')
        if(self.obj_toclose != None):
            try:
                print("close conn")
                if self.obj_toclose is not None:
                    #socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect( (self.hostname, self.port))
                    self.obj_toclose.close()
                    #os._exit(0)
            except:
                pass

    def add_onshutdown(self, obj):
        self.obj_toclose = obj

class HTTPHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a GET response"
        self.wfile.write(bytes(message, "utf8"))
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()

        message = "Hello, World! Here is a POST response"
        self.wfile.write(bytes(message, "utf8"))

def detect_interrupt(conn):
    try:
        print("Listening for KeyboardInterrupt...", flush=True)
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Detected KeyboardInterrupt!", flush=True)
        print("Sending IPC...", flush=True)
        conn.send(True)
        conn.close()
        print("Detect End", flush=True)

def listen_for_interrupt(conn, sock):
    print("Listening for IPC...", flush=True)
    rec = conn.recv()
    print(f"Detected IPC! {rec}", flush=True)
    print("Closing sock...", flush=True)
    if rec: sock.close()

def simplyScocket(hostname="localhost", serverPort="8000", signal_handler=None, logfile=None):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.settimeout(1.0)
    s.bind((hostName, serverPort))
    s.listen(1)

    main_conn, detect_conn = Pipe()

    listen_for_interrupt_thread = Thread(target=listen_for_interrupt, args=(main_conn, s), daemon=True)
    #listen_for_interrupt_thread = Process(target=listen_for_interrupt, args=(main_conn, s))
    listen_for_interrupt_thread.start()
    
    detect_interrupt_process = Process(target=detect_interrupt, args=(detect_conn,))
    detect_interrupt_process.start()

    #detect_interrupt_process.join()
    #listen_for_interrupt_thread.join()

    print('Listening on port %s ...' % serverPort)


    if signal_handler is not None:
        #signal_handler.add_onshutdown(s)
        conn = None
        addr = None
        try:
            while signal_handler.can_run():
                try:
                    print('Hello from the Python Demo Service')
                    if logfile is not None:
                        with open(logfile, "a") as f:
                            f.write("\nThe current timestamp is: " + str(datetime.now()))
                            f.close()
                    conn, addr = s.accept()
                    req = conn.recv(1024).decode()
                    if not req:
                        print("Client disconnected")
                        break
                    else:
                        print("Message from client: {}".format(req))
                        res = 'HTTP/1.0 200 OK\n\nHello World'
                        conn.sendall(res.encode())
                        conn.close()
                except socket.timeout:
                    print('Timeout', flush=True)
                    continue 
                except Exception: 
                    print("Other exception %s" % Exception.__str__, flush=True)
                    s.close()
                    raise
                except IOError as msg:
                    print('ss', flush=True)
                    pass
                except (SystemExit, KeyboardInterrupt):
                    print("Socket was killed: %s" % str(addr), flush=True)
                    try:
                        if conn:
                            socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((hostName, serverPort))
                            conn.close()
                        s.close()
                    except: pass
                    break
                time.sleep(1)
        except (SystemExit, KeyboardInterrupt):
            print("Socket was killed (main): %s" % str(addr), flush=True)
            try:
                s.close()
                if conn:
                    socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((hostName, serverPort))
                    conn.close()
            except: pass

        s.shutdown
        s.close()
        if conn:
            conn.close()
        
def simplyHTTPServer(hostname="localhost", serverPort="8000"):
    with HTTPServer((hostName, serverPort), HTTPHandler) as server:
        print("Server started http://%s:%s" % (hostName, serverPort))
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
        server.server_close()
        print("Server stopped.")

if __name__ == '__main__':
    try:
        configfile="srv_test.yml"
        logfile="srv_test.log"
        configpath=os.path.dirname(os.path.realpath(__file__))
        configfile=f"{configpath}/{configfile}"
        daemon=False

        try:
            opts, args = getopt.getopt(sys.argv[1:],"hdc:",["help", "daemon" , "config="])
        except getopt.GetoptError:
            print ('srv_test.py -h -d [--help, --daemon]')
            sys.exit(2)

        for opt, arg in opts:
            if opt in ("-h", "--help"):
                print ('srv_test.py -h -d [--help, --daemon]')
                sys.exit()        
            elif opt in ("-d", "--daemon"):
                daemon=True
                configfile=f"/etc/srv_test/srv_test.yml"
                import systemd.daemon
                systemd.daemon.notify('READY=1')
            elif opt in ("-c", "--config"):
                configfile=arg

        if os.path.exists(configfile) == True:
            print('Load config')
            with open(configfile, "r") as f:
                config = yaml.safe_load(f) #, Loader=yaml.FullLoader)
            hostName = config['server']['ip']
            serverPort = config['server']['port']
            logpath = config['logger']['path']

            if daemon is True: 
                if os.path.exists(logpath) == False:
                    os.makedirs(logpath)
            else: logpath=configpath
            logfile = os.path.join(logpath, logfile)
            

        else:
            print(f'Config not exists {configfile}')
            exit(1)

        print('Starting up ...')
        time.sleep(0.1)
        print('Startup complete')

        signal_handler = SignalHandler()

        simplyScocket(hostName, serverPort, signal_handler, logfile=logfile)
        #simplyHTTPServer(hostName, serverPort)
    except Exception as ex:
        print(ex)

