#!/usr/bin/env bash
su -c "celery -A app worker -l info"