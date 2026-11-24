# Runs Everything 
import collectors
import report

def mainfunc(): 
    # passing info to report as an argument
    information = collectors.collect_all()
    system_info = report.format_report(information)
    return system_info


mainfunc()

