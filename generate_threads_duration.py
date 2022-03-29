#!encoding=utf8

import os

root_path = os.path.dirname(os.path.realpath(__file__))

def generate_threads_duration(src, dst, threads, duration):
    '''
    jmx文件修改并发数量和循环时间
    src： 源 jmx 文件路径
    dst: 目标 jmx 文件路径
    threads： 并发数量
    duration：持续时间
    '''
    if not os.path.exists(dst):
        os.makedirs(dst)

    with open(src, 'r') as fp_src:
        file_name = os.path.split(src)[-1].split('.jmx')[0]
        dst = os.path.join(dst, f'{file_name}_t{threads}_d{duration}.jmx')
        with open(dst, 'w') as fp_dst:
            for value in fp_src.readlines():
                if "ThreadGroup.on_sample_error" in value:
                    fp_dst.write(f'        <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>\n')
                elif "LoopController.continue_forever" in value:
                    fp_dst.write(f'          <boolProp name="LoopController.continue_forever">false</boolProp>\n')
                elif "LoopController.loops" in value:
                    fp_dst.write(f'          <intProp name="LoopController.loops">-1</intProp>\n')
                elif "ThreadGroup.num_threads" in value:
                    fp_dst.write(f'        <stringProp name="ThreadGroup.num_threads">{threads}</stringProp>\n')
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

def main(src, dst, threads, duration):
    '''批量修改目录下所有jmx 的并发数量和持续时间
    '''
    if os.path.isdir(src):
        for f in os.listdir(src):
            src_file = os.path.join(src, f)
            generate_threads_duration(src_file, dst, threads, duration)    
    else:
        generate_threads_duration(src, dst, threads, duration)     

if __name__=='__main__':
    src = os.path.join(root_path, 'jmx_path', 'demo')
    dst = os.path.join(root_path, 'jmx_path', 'demo_10并发_持续60秒')
    threads = 10
    duration = 60

    main(src, dst, threads, duration)
                
            

