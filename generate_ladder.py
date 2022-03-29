#!encoding=utf8

import os

root_path = os.path.dirname(os.path.realpath(__file__))

def generate_ladder(source_jmx, output, threads=[10,20,30,40,50], duration=60):
    '''
    jmx文件生成阶梯压测脚本
    source_jmx: jmx 源文件
    output： 输出路径 不存在则创建
    threads：阶梯压测并发数量  list 
    duration: 持续时间 默认 60 秒
    '''
    if not os.path.exists(output):
        os.makedirs(output)

    values = ''
    with open(source_jmx, 'r') as fp_src:
        values = fp_src.readlines()

    file_name = os.path.split(source_jmx)[-1].split('.jmx')[0]
    for thread in threads:
        dst = os.path.join(output, f'{file_name}_t{thread}_d{duration}.jmx')
        with open(dst, 'w') as fp_dst:
            for value in values:
                if "ThreadGroup.on_sample_error" in value:
                    fp_dst.write(f'        <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>\n')
                elif "LoopController.continue_forever" in value:
                    fp_dst.write(f'          <boolProp name="LoopController.continue_forever">false</boolProp>\n')
                elif "LoopController.loops" in value:
                    fp_dst.write(f'          <intProp name="LoopController.loops">-1</intProp>\n')
                elif "ThreadGroup.num_threads" in value:
                    fp_dst.write(f'        <stringProp name="ThreadGroup.num_threads">{thread}</stringProp>\n')
                elif "ThreadGroup.ramp_time" in value:
                    fp_dst.write(f'        <stringProp name="ThreadGroup.ramp_time">0</stringProp>\n')
                elif "ThreadGroup.scheduler" in value:
                    fp_dst.write(f'        <boolProp name="ThreadGroup.scheduler">true</boolProp>\n')
                elif "ThreadGroup.duration" in value:
                    fp_dst.write(f'        <stringProp name="ThreadGroup.duration">{duration}</stringProp>\n')
                elif "ThreadGroup.delay" in value:
                    fp_dst.write(f'        <stringProp name="ThreadGroup.delay">0</stringProp>\n')
                else:
                    fp_dst.write(value)   

if __name__=='__main__':
    source_jmx = os.path.join(root_path, 'jmx_path', 'demo', 'demo.jmx')
    output = os.path.join(root_path, 'jmx_path', 'demo_阶梯压测')
    threads = [10, 20, 30, 40, 50]
    duration=10

    generate_ladder(source_jmx, output, threads, duration)
                
            

