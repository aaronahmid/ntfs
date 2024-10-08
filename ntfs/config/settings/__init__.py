#!/usr/bin/env python
"""
settings initialization

Initializes a settings file
by checking the environmental variable [ENV]

if ENV=local:
    it loads the local settings file

if ENV=dev:
    loads dev settings file

if ENV=staging:
    it loads the beta settings file

if ENV=prod:
    it loads the production settings file called prod
    if it fails to load the prod settings file, it reverts to beta
"""

## settings to allow celery to be run in our tasks
# from ..celery import app as celery_app

# __all__ = ['celery_app']

# this helps us load environtmentals
# from a .env file
# if you're not using a .env file
# make sure to set environmental variable manually
# from config.settings.base import DEFAULT_FROM_EMAIL
try:
    from decouple import config as getenv
except ModuleNotFoundError:
    print(
        "python decouple not found, please install\
 using os.getenv for now but some things won't work"
    )
    from os import getenv

# get the environment type e.g production
# and load up the appropiate settings
env = getenv("ENV")
if env != "local":
    if env in ("prod", "production"):
        try:
            print("loading production settings, sit tight :)")
            from config.settings.prod import *
        except ModuleNotFoundError:
            print(":| No production settings found, reverting to beta")
            try:
                from config.settings.beta import *
            except ModuleNotFoundError:
                print(
                    "No beta settings found, if you're in \
local environment, set environmental variable ENV=local \
aborting... :("
                )
                exit()

    elif env == "staging":
        try:
            print(":) loading beta settings, sit tight")
            from config.settings.beta import *
        except ModuleNotFoundError:
            print(
                "No beta settings found, if you're in \
local environment, set environmental variable ENV=local \
aborting... :("
            )
            exit()

    elif env == "dev":
        try:
            print(
                ":) loading dev settings, sit tight \
\nWARNING: DO NOT USE THIS FOR PRODUCTION OR BETA"
            )
            from config.settings.dev import *
        except ModuleNotFoundError:
            print(
                "dev settings not found and ENV is set to dev \
trying to load local settings"
            )
            try:
                from config.settings.local import *

            except ModuleNotFoundError:
                print(
                    "local settings not found and ENV is set to local \
please check that the file isn't missing aborting... :("
                )
                exit()

else:
    try:
        print(
            ":) loading local settings, sit tight \
\nWARNING: DO NOT USE THIS FOR PRODUCTION OR BETA"
        )
        from config.settings.local import *
    except ModuleNotFoundError as error:
        print(error)
        print(
            "local settings not found and ENV is set to local \
please check that the file isn't missing aborting... :("
        )
