#!encoding=utf8

import os
import time

root_path = os.path.dirname(os.path.realpath(__file__))

def run_jmeter_test(jmx_path='jmx_path'):
    '''
    运行jmeter 测试并生成 html 报告
    jmx_path: 
            1、如果为路径，则执行路径下所有jmx文件的性能测试
            2、如果为 jmx 文件，则执行单个文件的性能测试
    '''
    # 创建报告目录
    current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    print(current_time)
    print("root_path is {0}".format(root_path))
    report_dir = os.path.join('report', current_time)
    report_path = os.path.join(root_path, report_dir)
    if not os.path.exists(report_path):
            os.mkdir(report_path)

    # 执行测试
    jmx_file = ''
    jmx_file_name = ''
    test_jmx_path = ''
    csv_report_filepath = ''
    html_report_path = ''
    if os.path.isdir(jmx_path):
        print(f'参数是路径 {jmx_path}')
        for file in os.listdir(jmx_path):
            jmx_file = file  
            jmx_file_name = jmx_file.split('.')[0]
            print("jmx_file is {0}".format(jmx_file))
            test_jmx_path = os.path.join(jmx_path, jmx_file)
            csv_report_filepath = os.path.join(report_path, jmx_file_name, 'result.csv')
            html_report_path = os.path.join(report_path, jmx_file_name)
            if not os.path.exists(html_report_path):
                os.mkdir(html_report_path)

            jmeter_cmd = f'jmeter -n -t {test_jmx_path} -l {csv_report_filepath} -e -o {html_report_path}'
            print(jmeter_cmd)
            os.system(jmeter_cmd)
           
    else:
        print(f'参数是文件 {jmx_path}')
        jmx_file = os.path.split(jmx_path)[-1]
        if jmx_file.split('.')[1] == 'jmx':
            jmx_file_name = jmx_file.split('.')[0]
            print("jmx_file is {0}".format(jmx_file))
            test_jmx_path = jmx_path
            csv_report_filepath = os.path.join(report_path, jmx_file_name, 'result.csv')
            html_report_path = os.path.join(report_path, jmx_file_name)
            if not os.path.exists(html_report_path):
                os.mkdir(html_report_path)

            jmeter_cmd = f'jmeter -n -t {test_jmx_path} -l {csv_report_filepath} -e -o {html_report_path}'
            print(jmeter_cmd)
            os.system(jmeter_cmd)
      

if __name__ == '__main__':
    
    # 传文件
    # jmx_path = os.path.join(root_path, 'jmx_path', 'demo_阶梯压测', 'demo_t10_d60.jmx')
    # 传目录
    jmx_path = os.path.join(root_path, 'jmx_path', 'demo_阶梯压测')
    
    run_jmeter_test(jmx_path=jmx_path)
