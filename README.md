一、实现功能  
1、执行 jmeter 测试，生成html报告  
2、根据jmx文件生成阶梯压测jmeter脚本   
3、批量修改目录下所有jmx文件的并发数量和持续时间
4、提取html报告中的信息到csv文件 

二、运行环境   
python3 jmeter    

三、脚本介绍    
generate_ladder.py  
根据jmx文件生成阶梯压测脚本  

generate_report.py  
根据jmeter 生成的html 测试报告 提取出报告需要的数据写入csv文件  

generate_threads_duration.py    
批量修改目录下所有jmx文件的并发数量和持续时间

run_jmeter_test.py  
1、传参为路径：根据给定的路径执行路径下所有 jmx 文件的性能测试并生成html报告  
2、传参为文件：根据指定的 jmx 文件进行性能测试并生成html报告  

