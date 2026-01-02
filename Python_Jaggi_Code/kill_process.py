import psutil

def process_kill(targted_process_name):
    for x_process in psutil.process_iter(['name']):
        if x_process.info['name'] == targted_process_name:
            print("Killing the process:",targted_process_name)
            x_process.kill()

def main():
    process_kill("CalculatorApp.exe")

if __name__ == "__main__":
    main()