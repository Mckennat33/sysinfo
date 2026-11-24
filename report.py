# Formats Information (Report). Saves report -> output/reports

def format_report(sys_info):
    # want = OS Architecture | Computer Name
    # print(sys_info.keys())
    for key, values in sys_info.items():
        if key == "OS":
            print(values)
       
    




def save_report():
    print("Save Report")


# format_report()
# save_report()
if __name__ == "__main__":
    import collectors
    format_report(collectors.collect_all())