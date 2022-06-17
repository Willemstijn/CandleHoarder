#!/usr/bin/python
# coding=utf-8
import subprocess
import datetime
from config import *
from distutils.dir_util import copy_tree

# ct stores current time
ct = datetime.datetime.now()

# ts store timestamp of current time
ts = ct.timestamp()

comment = f"last updated {ct}"

def sync_plots():
    """
    This funtion copies the plots from the symbols to a 
    Wiki environment for internet publishing
    """
    print("Copying plots to wiki")
    src = "{}mdwiki/plots".format(dir)
    dst = plots
    copy_tree(src, dst)

def sync_pages():
    """
    This funtion copies the pages of the strategies plots to a 
    Wiki environment for internet publishing
    """
    print("Copying markdown pages to wiki")
    src = "{}mdwiki/content".format(dir)
    dst = pages
    copy_tree(src, dst)


def sync_git():
    # GIT commands
    # from: https://geekflare.com/python-run-bash/
    CURRENT_REPO_CMD = ["git", "config", "--get", "remote.origin.url"]
    SYNC_REPO_WITH_ORIGIN = ["git", "pull"]
    ADD_FILES_TO_REPO = ["git", "add", "."]
    COMMIT_FILES_WITH_TIMESTAMP = ["git", "commit", "-m", comment]
    PUSH_REPO = ["git", "push"]

    print("Print current git repository")
    result = subprocess.run(
        CURRENT_REPO_CMD, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    print(result.stdout)

    print("Pull remote changes from Github")
    result = subprocess.run(
        SYNC_REPO_WITH_ORIGIN, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    print(result.stdout)


    print("Add changes")
    result = subprocess.run(
        ADD_FILES_TO_REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    print(result.stdout)

    print("Commit changes to repository")
    result = subprocess.run(
        COMMIT_FILES_WITH_TIMESTAMP,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    print(result.stdout)

    print("Push commit to Github")
    result = subprocess.run(
        PUSH_REPO, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
