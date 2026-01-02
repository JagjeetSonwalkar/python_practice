import psutil

def process_scan():
    list_process = list()

    for x_process in psutil.process_iter():
        try:
            process_detials = x_process.as_dict(attrs=["pid", "name", "username"])
            process_detials["vms"] = x_process.memory_info().vms / (1024 * 1024)
            list_process.append(process_detials)
        except:
            print("Exception occured!")

    return list_process

def main():
    ret = process_scan()

    for i in ret:
        print(i)

if __name__ == "__main__":
    main()