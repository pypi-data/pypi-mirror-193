from __future__ import print_function

import os
import sys
import logging as log
import psutil
import datetime
import json


class Utils_BDB:

    def get_json_value(self, json_data, key):
        value = None
        try:
            if json_data != None and key in json_data:
                value = json_data[key]
        except Exception as e:
            raise Exception(Utils_BDB.__name__ + "value error", e)
        finally:
            pass
        return value

    def iskey_validate(self, json_data, key):
        try:
            if json_data != None and key in json_data:
                return True
        except Exception as e:
            raise Exception(Utils_BDB.__name__ + "dict not have key", e)
        finally:
            pass
        return False

    def get_system_usage(self):
        '''
        :param str data:
        :return:
        '''
        try:
            sys = {}
            process = psutil.Process(os.getpid())
            sys['currentHeapSize'] = self.format_bytes(process.memory_full_info().rss)
            sys['maxHeapSize'] = self.format_bytes(psutil.virtual_memory().total)
            sys['commitedHeapSize'] = self.format_bytes(psutil.virtual_memory().total)
            sys['percentage'] = psutil.virtual_memory().percent
            sys['totalPhysicalMemory'] = self.format_bytes(psutil.virtual_memory().total)
            sys['freePhysicalMemory'] = self.format_bytes(psutil.virtual_memory().free)
            sys['percentage'] = process.memory_percent()
            sys['cpu'] = psutil.cpu_percent()
            return sys
        except Exception as e:
            log.exception(e)
        finally:
            pass

    def format_bytes(self, b):
        # 2**10 = 1024
        if b < 1000:
            return '%i' % b + ' B'
        elif 1000 <= b < 1000000:
            return '%.1f' % float(b / 1000) + ' KB'
        elif 1000000 <= b < 1000000000:
            return '%.1f' % float(b / 1000000) + ' MB'
        elif 1000000000 <= b < 1000000000000:
            return '%.1f' % float(b / 1000000000) + ' GB'
        elif 1000000000000 <= b:
            return '%.1f' % float(b / 1000000000000) + ' TB'

    def get_updated_logger(self, logger):
        usage = self.get_system_usage()
        logger.pop('usedMemory')
        logger['cpu'] = usage['cpu']
        logger['usedMemory'] = usage['currentHeapSize']
        return logger

    def get_monitor_logs(self, logger, data_list, is_success, start_time, end_time, total=0):
        monitor = {}
        usage = self.get_system_usage()
        logger = self.get_updated_logger(logger)
        logger.pop('monitor')
        monitor['processingSuccessful'] = is_success
        if len(data_list) > 0:
            data = sys.getsizeof(data_list)
            size = self.format_bytes(data)
            monitor['sizeofRecords'] = size
            monitor['numberOfRecords'] = len(data_list)
        else:
            monitor['numberOfRecords'] = 0
            monitor['sizeofRecords'] = '0.00 KB'
        monitor['processingStartTime'] = start_time
        monitor['processingEndTime'] = end_time
        monitor['totalNumberOfRecords'] = total
        monitor['consumedCPU'] = usage['cpu']
        logger['monitor'] = json.dumps(monitor)
        return logger

    def get_current_time(self):
        now = datetime.datetime.now()
        return now.strftime("%d-%m-%Y %H:%M:%S")


if __name__ == '__main__':
    utils = Utils_BDB()
    print(utils.get_system_usage())
    print(psutil.cpu_times().idle)
    pass
