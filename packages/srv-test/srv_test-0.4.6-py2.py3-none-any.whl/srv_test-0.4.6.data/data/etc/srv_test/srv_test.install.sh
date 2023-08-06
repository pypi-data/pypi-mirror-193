#!/bin/bash

help()
{
    echo -e "\nUsage: $(basename $-11) [-i] [-r] [-b] [-h] [-t arg]"
    exit 2
}

function install2() {
    
    SYSTEMD_SCRIPT_DIR=$( cd  $(dirname "${BASH_SOURCE:=$0}") && pwd)
    cp -f "$SYSTEMD_SCRIPT_DIR/srv_test.service" /etc/systemd/system
    chown root:root /etc/systemd/system/srv_test.service

    systemctl daemon-reload
    systemctl enable srv_test.service
}

function install_user() {
    # ~/.config/systemd/user/foo.service
    systemctl --user daemon-reload
    systemctl --user start srv_test.socket
}

function install() {
    mkdir /usr/local/lib/srv_test
    cp -f ./srv_test.py /usr/local/lib/srv_test
    chown root:root /usr/local/lib/srv_test/srv_test.py
    chmod 644 /usr/local/lib/srv_test/srv_test.py

    cp -f srv_test.s* /etc/systemd/system/
    chown root:root /etc/systemd/system/srv_test.*
    chmod 644 /etc/systemd/system/srv_test.*
    systemctl list-unit-files | grep service.service
    #journalctl --unit srv_test.service
    #journalctl -f --user-unit srv_test.service

    [ ! -d /etc/srv_test ] && mkdir /etc/srv_test
    cp srv_test.yml /etc/srv_test/
    chown root: /etc/srv_test/srv_test.yml
    chmod -R 664 /etc/srv_test

    [ ! -d /var/log/srv_test ] && mkdir /var/log/srv_test
    touch /var/log/srv_test/srv_test.log
    chmod -R 644 /var/log/srv_test/srv_test.log

    systemctl daemon-reload
}

function remove() {
    systemctl stop srv_test.service
    systemctl stop srv_test.socket

    rm /usr/local/lib/srv_test -f -r
    rm /etc/systemd/system/srv_test.* -f
    rm /etc/srv_test -f -r
    rm /var/log/srv_test -f -r

    systemctl daemon-reload
}

function build_rpm() {
    #make prm package
    python setup.py bdist_rpm
}


LONG=install,remove,build,help,test:
SHORT=i,u,b,h,t:
VALID_ARGS=$(getopt --alternative --name srv_test -o $SHORT --long $LONG -- "$@")

VALID_ARGUMENTS=$# #$?
if [ "$VALID_ARGUMENTS" -eq 0 ]; then
    help
fi

eval set -- "$VALID_ARGS"

while [ : ]; do
  case "$1" in
    -i | --install)
        echo "Install service"
        install2
        break
        ;;
    -r | --remove)
        echo "Remove service"
        remove
        break;        
        ;;
    -b | --build)
        echo "Build rpm"
        #build_rpm
        break
        ;;
    -t | --test)
        echo "Tesshiftt. Input argument is '$2'"
        res=$(curl -XGET http://localhost:8080 -s)
        echo -e "\n$res\n"
        shift 2;
        ;;
    -h | --help)
        echo "Usage: $(basename $0) [-i] [-r] [-b] [-h] [-t arg]"
        exit 2
        ;;
    -* | --*) shift; # :)
        echo -e "option requires an argument."
        help
        break 
        ;;
    *)  # shift; # ?)
        echo "Unexpected option: $1"
        echo -e "Invalid command option."
        help
        exit 1
        ;;
  esac
done

shift "$(($OPTIND -1))"