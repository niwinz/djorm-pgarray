# -*- coding: utf-8 -*-

import os, sys
sys.path.insert(0, "testing")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

from django.core.management import call_command

if __name__ == "__main__":
    import django
    if django.VERSION[:2] >= (1, 7):
        django.setup()
    args = sys.argv[1:]
    if len(args) == 0:
        args.append("pg_array_fields")
    call_command("test", *args, verbosity=2)
