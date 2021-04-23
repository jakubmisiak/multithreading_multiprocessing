import  platform, sys, os
from report_builder import ReportBuiler
from thread import one_thread, multi_threading
from process import four_processes, all_processes
from statistics import median
import timeit


def main():
    test1=timeit.repeat(one_thread,repeat=5, number=1)
    test2=timeit.repeat(multi_threading,repeat=5,number=1)
    test3=timeit.repeat(four_processes,repeat=5, number=1)
    test4=timeit.repeat(all_processes,repeat=5, number=1)
    results=[test1,test2,test3,test4]
    result_median=[median(results[0]),median(results[1]),median(results[2]),median(results[3]),]
    f = open('report.html', 'w')
    report_builder = ReportBuiler()
    report = report_builder \
            .header() \
            .env(
                python_version = platform.python_version(),
                interpreter = platform.python_implementation(),
                interpreter_version = sys.version,
                os = platform.system(),
                os_version = platform.release(),
                cpu = platform.processor(),
                cores = str(os.cpu_count())
            ) \
            .test(results) \
            .summary(result_median) \
            .author(name='Jakub Misiak') \
            .footer() \
            .build()
    print(report)
    f.write(report)
    f.close()






if __name__ == "__main__":
    main()
   
