# Formats Information (Report). Saves report -> output/reports

def format_report(sys_info):
    user_os = sys_info["OS"]
    user_cpu = sys_info["CPU"]
    user_disk = sys_info["Disk"]
    user_ram = sys_info["Ram"]
    user_network = sys_info["Network"]
    user_uptime = sys_info["Uptime"]

    for key, values in user_os.items():
        
        print(f"Key {key}, Value {values}")

def save_report():
    print("Save Report")


# format_report()
# save_report()
if __name__ == "__main__":
    import collectors
    format_report(collectors.collect_all())