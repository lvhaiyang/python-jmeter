#!encoding=utf8

import os
import json
import csv

root_path = os.path.dirname(os.path.realpath(__file__))

def generate_report(report_dir, output_path):
    '''
    提取jmeter 报告中的信息
    report_dir: 测试报告路径
    output_path：csv 报告路径
    '''
    output_dir = os.path.split(output_path)[0]
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    
    with open(output_path, 'w') as fp:
        csv_write = csv.writer(fp)
        csv_write.writerow(["名称", "并发数量", "持续时间(秒)", "Average", "Transactions/s", "Error %"])
        for subdirectory in os.listdir(report_dir):
            # 判断是否是目录
            if os.path.isdir(os.path.join(report_dir, subdirectory)):
                json_file_path = os.path.join(report_dir, subdirectory, 'statistics.json')
                name = subdirectory.split('_')[0]
                threads = subdirectory.split('_')[1].replace('t', '') + "并发"
                duration = subdirectory.split('_')[2].replace('d', '') + "秒"
                with open(json_file_path, 'r') as fp:
                    value = json.load(fp)['Total']
                    avg = round(value["meanResTime"], 2)
                    tps = round(value["throughput"], 2)
                    error = '{0}%'.format(round(value["errorPct"], 2))
                    csv_write.writerow([name, threads, duration, avg, tps, error])

if __name__=='__main__':
    report_dir = os.path.join(root_path, 'report', '20220329194604')
    output_path = os.path.join(report_dir, 'csvoutput.csv')
    generate_report(report_dir, output_path)
                



