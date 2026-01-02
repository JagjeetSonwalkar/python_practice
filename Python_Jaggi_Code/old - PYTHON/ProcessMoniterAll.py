import psutil

def process_display():
    border = "-"*100

    print(border)
    print("---- Displaying all process ----")

    for x_process in psutil.process_iter():
        process_detials = x_process.as_dict(attrs=["pid", "name", "username"])
        process_detials["vms"] = x_process.memory_info().vms / (1024 * 1024)
        print(process_detials)
        


    print(border)

def main():
    process_display()

if __name__ == "__main__":
    main()