https://github.com/torfsen/python-systemd-tutorial
https://github.com/systemd/python-systemd
https://www.freedesktop.org/software/systemd/man/systemd.service.html
https://www.freedesktop.org/wiki/Software/systemd/
https://www.freedesktop.org/software/systemd/python-systemd/journal.html
https://peps.python.org/pep-3143/#correct-daemon-behaviour
https://oxylabs.io/blog/python-script-service-guide
https://gist.github.com/kylemanna/d193aaa6b33a89f649524ad27ce47c4b
dbus
---
systemctl --user list-unit-files | grep python_demo_service

systemctl --user start python_demo_service
systemctl --user enable python_demo_service
systemctl --user daemon-reload
systemctl --user status python_demo_service
systemctl --user stop python_demo_service
--- stdout stderr
--- Environment=PYTHONUNBUFFERED=1
systemctl --user daemon-reload
systemctl --user restart python_demo_service
less /var/log/syslog
journalctl -f --user-unit python_demo_service
---
-- WantedBy=default.target
systemctl --user enable python_demo_service
sudo loginctl enable-linger $USER
systemctl --user disable python_demo_service
---
--- Restart=on-failure
systemctl --user --signal=SIGKILL kill python_demo_service
journalctl --user-unit python_demo_service

--- ~/.config/systemd/user/foo.service
sudo mv ~/.config/systemd/user/python_demo_service.service /etc/systemd/system/
sudo chown root:root /etc/systemd/system/python_demo_service.service
sudo chmod 644 /etc/systemd/system/python_demo_service.service
systemctl list-unit-files | grep python_demo_service
journalctl --unit python_demo_service
---
--- ExecStart=...
$ sudo mkdir /usr/local/lib/python_demo_service
$ sudo mv ~/path/to/your/python_demo_service.py /usr/local/lib/python_demo_service/
$ sudo chown root:root /usr/local/lib/python_demo_service/python_demo_service.py
$ sudo chmod 644 /usr/local/lib/python_demo_service/python_demo-service.py
---
--- User=python_demo_service
sudo useradd -r -s /bin/false python_demo_service
sudo systemctl --property=MainPID show python_demo_service
---

--- install python module
pip install pyp2rpm
yum install rpm-build
pip install --upgrade setuptools wheel
pip install --upgrade build
pip install pyyaml
pip install virtualenv --upgrade
---
alien -i dist/srv_test-0.1-1.noarch.rpm
---
python setup.py bdist_rpm
python setup.py sdist bdist_wheel
python setup.py install --record install.log
xargs rm -rf < install.log
python setup.py clean
pip uninstall srv_test
---
pip install pipreqs
pip3 install pip-tools
pipreqs /path/to/project
pipreqs --savepath=requirements.in && pip-compile
python -m  pipreqs.pipreqs --encoding utf-8  /path/to/project

pip3 freeze > requirements.txt
pip install -r requirements.txt
---
rpmbuild -ba ./build/bdist.linux-x86_64/rpm/SPECS/color_print.spec
-- test
get -XGET loclahost:8080
date  | netcat 127.0.0.1 8080
echo "test" | socat - TCP:127.0.0.1:8080

-- virtualenv
pip3 install virtualenv
python3 -m venv srv_venv
virtualenv -p python3 srv_venv

srv_venv\Scripts\activate

pip install -r requirements.txt
python -m pip freeze > requirements.txt

deactivate

--- PYPI.ORG
pip install twine
twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
twine upload dist/*


rm -r dist ;
python setup.py sdist bdist_wheel ;
if twine check dist/* ; then
  if [ "$1" = "--test" ] ; then
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
  else
    twine upload dist/* ;
  fi
fi


