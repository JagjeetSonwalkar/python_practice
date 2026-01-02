import psutil

def process_display():
    Border = "-"*100

    print(Border)
    print("Information of currently running process")

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs=["pid", "name"])
        print(info)
        # print(proc)

    print(Border)

def main():
    process_display()

if __name__ == "__main__":
    main()