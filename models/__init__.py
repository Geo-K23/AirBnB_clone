#!/usr/bin/python3
""" This modle contains the initialization of file storage"""
from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
