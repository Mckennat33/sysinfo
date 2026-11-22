# Runs Everything 
import collectors
import report

def mainfunc(): 
    # passing info to report as an argument
    information = collectors.collect_all()
    data = report.format_report(information)
    return data


mainfunc()