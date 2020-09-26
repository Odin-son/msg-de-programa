#!/bin/bash
echo 'install required python library...'
pip install -r requirements.txt

echo 'install this library...'
pip install pkg/mensaje-0.0.1.tar.gz

echo 'done!'