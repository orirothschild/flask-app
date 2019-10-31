#!/bin/bash

/usr/sbin/sshd

/usr/sbin/php-fpm -c /etc/php/fpm

nginx -g 'daemon off;'
