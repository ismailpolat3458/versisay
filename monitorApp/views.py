from django.shortcuts import render
from logging import debug
from flask import Flask, jsonify
import psutil
# Create your views here.

def root():
    ct = psutil.cpu_times()
    vm = psutil.virtual_memory()
    du = psutil.disk_usage('/')
    net = psutil.net_io_counters()
    return jsonify({
        'cpu': {
            'percent': psutil.cpu_percent(),
            'count': psutil.cpu_count(),
            'freq': psutil.cpu_freq().current,
            'times': {
                'user': round(ct.user/3600),
                'system': round(ct.system/3600),
                'idle': round(ct.idle/3600)
            }
        },
        'ram': {
            'total': vm.total,
            'available': vm.available,
            'used': vm.used,
            'percent': vm.percent
        },
        'disk': {
            'total': du.total,
            'free': du.free,
            'used': du.used,
            'percent': du.percent,
        },
        'network': {
            'bytes_sent': net.bytes_sent,
            'bytes_recv': net.bytes_recv
        }
    })


def cpu():
    ct = psutil.cpu_times()
    return jsonify({
        'percent': psutil.cpu_percent(),
        'count': psutil.cpu_count(),
        'freq': psutil.cpu_freq().current,
        'times': {
            'user': round(ct.user/3600),
            'system': round(ct.system/3600),
            'idle': round(ct.idle/3600)
        }
    })

def cpu_percent():
    return jsonify(psutil.cpu_percent())

def cpu_count():
    return jsonify(psutil.cpu_count())

def cpu_freq():
    return jsonify(psutil.cpu_freq().current)
def cpu_times():
    cpu_times = psutil.cpu_times()
    return jsonify({
        'user': round(cpu_times.user/3600),
        'system': round(cpu_times.system/3600),
        'idle': round(cpu_times.idle/3600)
    })


def cpu_times_user():
    return jsonify(round(psutil.cpu_times().user/3600))

def cpu_times_system():
    return jsonify(round(psutil.cpu_times().system/3600))


def cpu_times_idle():
    return jsonify(round(psutil.cpu_times().idle/3600))

def ram():
    vm = psutil.virtual_memory()
    return jsonify({
        'total': vm.total,
        'available': vm.available,
        'used': vm.used,
        'percent': vm.percent
    })
def ram_total():
    return jsonify(psutil.virtual_memory().total)

def ram_available():
    return jsonify(psutil.virtual_memory().available)

def ram_used():
    return jsonify(psutil.virtual_memory().used)


def ram_percent():
    return jsonify(psutil.virtual_memory().percent)

def disk():
    du = psutil.disk_usage('/')
    return jsonify({
        'total': du.total,
        'free': du.free,
        'used': du.used,
        'percent': du.percent,
    })
def disk_total():
    return jsonify(psutil.disk_usage('/').total)

def disk_free():
    return jsonify(psutil.disk_usage('/').free)

def disk_used():
    return jsonify(psutil.disk_usage('/').used)

def disk_percent():
    return jsonify(psutil.disk_usage('/').percent)

def network():
    net = psutil.net_io_counters()
    return jsonify({
        'bytes_sent': net.bytes_sent,
        'bytes_recv': net.bytes_recv
    })

def net_bytes_sent():
    return jsonify(psutil.net_io_counters().bytes_sent)

def net_bytes_recv():
    return jsonify(psutil.net_io_counters().bytes_recv)
