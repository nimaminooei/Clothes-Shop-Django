#!/bin/bash
TEMP=$(sensors | grep -Po 'Package id 0:\s+\+?\K[0-9.]+')
echo "cpu_temperature_celsius $TEMP" > /var/lib/node_exporter/textfile_collector/cpu_temp.prom
