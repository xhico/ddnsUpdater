# -*- coding: utf-8 -*-
# !/usr/bin/python3

import json
import os
import datetime
import traceback
import logging
import urllib.request
from Misc import get911, sendEmail


def getLog():
    """
    Retrieve log information from the saved file or create a new one if not available.

    Returns:
        dict: Log information with 'datetime' and 'externalIP'.
    """
    try:
        with open(SAVED_INFO_FILE) as inFile:
            log = json.load(inFile)
    except Exception:
        log = {"datetime": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "externalIP": "0.0.0.0"}

    return log


def main():
    """
    Main function to check for external IP changes and update the log.
    """
    # Get LOG
    logger.info("getLog()")
    log = getLog()

    # Get external ip
    logger.info("Get externalIP")
    externalIP = urllib.request.urlopen("https://v4.ident.me/").read().decode("utf8")

    # Check if externalIP has changed
    if log["externalIP"] != externalIP:
        logger.info("EXTERNAL IP CHANGE")
        logger.info("From: " + log["externalIP"])
        logger.info("To: " + externalIP)
        sendEmail("EXTERNAL IP CHANGE", "From: " + log["externalIP"] + "\n" + "To: " + externalIP)
    else:
        logger.info("NO CHANGE")

    # Update LOG
    log = {"datetime": datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"), "externalIP": externalIP}
    with open(SAVED_INFO_FILE, "w") as outFile:
        json.dump(log, outFile, indent=2)


if __name__ == '__main__':
    # Set Logging
    LOG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.abspath(__file__).replace(".py", ".log"))
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s", handlers=[logging.FileHandler(LOG_FILE), logging.StreamHandler()])
    logger = logging.getLogger()

    logger.info("----------------------------------------------------")

    # Set SAVED_INFO_FILE File
    SAVED_INFO_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saved_info.json")

    # Run Main
    try:
        main()
    except Exception as ex:
        logger.error(traceback.format_exc())
        sendEmail(os.path.basename(__file__), str(traceback.format_exc()))
    finally:
        logger.info("End")
