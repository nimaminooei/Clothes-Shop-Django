#!/bin/bash

set -e

echo "🔧 در حال ساخت پوشه monitoring..."
mkdir -p ~/monitoring/{prometheus,alertmanager,grafana}

cd ~/monitoring

echo "📝 در حال ساخت فایل پیکربندی Prometheus..."
cat > prometheus/prometheus.yml <<EOF
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'prometheus'
    static_configs:
      - targets: ['localhost:9090']

  - job_name: 'node_exporter'
    static_configs:
      - targets: ['node_exporter:9100']

  - job_name: 'cadvisor'
    static_configs:
      - targets: ['cadvisor:8080']
EOF

echo "📧 در حال ساخت فایل Alertmanager (موقت بدون ایمیل)..."
cat > alertmanager/alertmanager.yml <<EOF
route:
  receiver: 'default'

receivers:
  - name: 'default'
EOF

echo "📦 در حال ساخت فایل Docker Compose..."
cat > docker-compose.yml <<EOF
version: '3.8'

services:
  prometheus:
    image: prom/prometheus
    volumes:
      - ./prometheus/prometheus.yml:/etc/prometheus/prometheus.yml
    ports:
      - "9090:9090"
    restart: always

  grafana:
    image: grafana/grafana
    ports:
      - "3000:3000"
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=admin
    volumes:
      - grafana-storage:/var/lib/grafana
    restart: always

  node_exporter:
    image: prom/node-exporter
    ports:
      - "9100:9100"
    restart: always

  cadvisor:
    image: gcr.io/cadvisor/cadvisor
    ports:
      - "8080:8080"
    volumes:
      - /:/rootfs:ro
      - /var/run:/var/run:ro
      - /sys:/sys:ro
      - /var/lib/docker:/var/lib/docker:ro
    restart: always

  alertmanager:
    image: prom/alertmanager
    ports:
      - "9093:9093"
    volumes:
      - ./alertmanager/alertmanager.yml:/etc/alertmanager/alertmanager.yml
    restart: always

volumes:
  grafana-storage:
EOF

echo "🚀 اجرای کانتینرها با Docker Compose..."
docker compose up -d

echo "✅ سیستم مانیتورینگ راه‌اندازی شد!"
echo ""
echo "🟢 Prometheus: http://localhost:9090"
echo "🟢 Grafana: http://localhost:3000 (user: admin, pass: admin)"
echo "🟢 Node Exporter: http://localhost:9100"
echo "🟢 cAdvisor: http://localhost:8080"
echo "🟢 Alertmanager: http://localhost:9093"