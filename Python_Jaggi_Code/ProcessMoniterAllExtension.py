import psutil

def process_display():
    border = "-"*100

    print(border)
    print("---- Displaying all process ----")

    for x_process in psutil.process_iter():
        try:
            process_detials = x_process.as_dict(attrs=["pid", "name", "username"])
            process_detials["vms"] = x_process.memory_info().vms / (1024 * 1024)
            print(process_detials)
        except:
            print("Exception occured!")

    print(border)

def main():
    process_display()

if __name__ == "__main__":
    main()