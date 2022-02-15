#!encoding=utf8

import os
import time

if __name__ == '__main__':
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    print(current_time)
    root_path = os.path.dirname(os.path.realpath(__file__))
    print("root_path is {0}".format(root_path))

    report_dir = os.path.join('report', current_time)
    report_path = os.path.join(root_path, report_dir)
    if not os.path.exists(report_path):
            os.mkdir(report_path)

    for jmx_file in os.listdir('jmx_path'):
        print("jmx_file is {0}".format(jmx_file))
        jmx_path = os.path.join(root_path, 'jmx_path', jmx_file)
        csv_report_filepath = os.path.join(report_path, jmx_file.split('.')[0], 'result.csv')
        html_report_path = os.path.join(report_path, jmx_file.split('.')[0])
        if not os.path.exists(html_report_path):
            os.mkdir(html_report_path)

        jmeter_cmd = f'jmeter -n -t {jmx_path} -l {csv_report_filepath} -e -o {html_report_path}'
        print(jmeter_cmd)
        os.system(jmeter_cmd)