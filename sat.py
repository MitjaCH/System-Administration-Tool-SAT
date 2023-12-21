import platform
import os
import colorama
import psutil

# Initialize colorama
colorama.init()

# Define colors
GREEN = colorama.Fore.GREEN
WHITE = colorama.Fore.WHITE
YELLOW = colorama.Fore.YELLOW
RED = colorama.Fore.RED
CYAN = colorama.Fore.CYAN

class SystemAdminTool:
    def __init__(self):
        self.is_running = True

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        self.clear_screen()
        big_title = (
            f"\n\n{CYAN}███████╗ █████╗ ████████╗    ██████╗ ██╗   ██╗    ███╗   ███╗██╗████████╗  ██╗ █████╗  ██████╗██╗  ██╗\n"
            f"{CYAN}██╔════╝██╔══██╗╚══██╔══╝    ██╔══██╗╚██╗ ██╔╝    ████╗ ████║██║╚══██╔══╝  ██║██╔══██╗██╔════╝██║  ██║\n"
            f"{CYAN}███████╗███████║   ██║       ██████╔╝ ╚████╔╝     ██╔████╔██║██║   ██║     ██║███████║██║     ███████║\n"
            f"{CYAN}╚════██║██╔══██║   ██║       ██╔══██╗  ╚██╔╝      ██║╚██╔╝██║██║   ██║██   ██║██╔══██║██║     ██╔══██║\n"
            f"{CYAN}███████║██║  ██║   ██║       ██████╔╝   ██║       ██║ ╚═╝ ██║██║   ██║╚█████╔╝██║  ██║╚██████╗██║  ██║\n"
            f"{CYAN}╚══════╝╚═╝  ╚═╝   ╚═╝       ╚═════╝    ╚═╝       ╚═╝     ╚═╝╚═╝   ╚═╝ ╚════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝\n\n"
        )
        print(big_title)
        print(f"{YELLOW}[1] {GREEN}View System Information")
        print(f"{YELLOW}[2] {GREEN}View Storage Capacity")
        print(f"{YELLOW}[3] {GREEN}View CPU Usage")
        print(f"{YELLOW}[4] {GREEN}View Memory Usage")
        print(f"{YELLOW}[5] {GREEN}View Network Information")
        print(f"{YELLOW}[6] {GREEN}List Running Processes")
        print(f"{YELLOW}[7] {RED}Kill a Process")
        print(f"{YELLOW}[8] {RED}Exit")

    def view_system_info(self):
        self.clear_screen()
        print(f"{CYAN}=== System Information ==={WHITE}\n")
        print(f"{YELLOW}System: {WHITE}{platform.system()}")
        print(f"{YELLOW}Node Name: {WHITE}{platform.node()}")
        print(f"{YELLOW}Release: {WHITE}{platform.release()}")
        print(f"{YELLOW}Version: {WHITE}{platform.version()}")
        print(f"{YELLOW}Machine: {WHITE}{platform.machine()}")
        print(f"{YELLOW}Processor: {WHITE}{platform.processor()}")
        input("\nPress Enter to return to the main menu.")

    def view_storage_capacity(self):
        self.clear_screen()
        print(f"{CYAN}=== Storage Capacity ==={WHITE}\n")
        partitions = psutil.disk_partitions()
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            print(f"{YELLOW}Partition: {WHITE}{partition.device}")
            print(f"{YELLOW}Mountpoint: {WHITE}{partition.mountpoint}")
            print(f"{YELLOW}Total Space: {WHITE}{usage.total / (2**30):.2f} GB")
            print(f"{YELLOW}Used Space: {WHITE}{usage.used / (2**30):.2f} GB")
            print(f"{YELLOW}Free Space: {WHITE}{usage.free / (2**30):.2f} GB\n")
        input("Press Enter to return to the main menu.")

    def view_cpu_usage(self):
        self.clear_screen()
        print(f"{CYAN}=== CPU Usage ==={WHITE}\n")
        cpu_percent = psutil.cpu_percent(interval=1, percpu=True)
        for i, percent in enumerate(cpu_percent):
            print(f"{YELLOW}CPU {i}: {WHITE}{percent}%")
        input("\nPress Enter to return to the main menu.")

    def view_memory_usage(self):
        self.clear_screen()
        print(f"{CYAN}=== Memory Usage ==={WHITE}\n")
        memory = psutil.virtual_memory()
        print(f"{YELLOW}Total Memory: {WHITE}{memory.total / (2**30):.2f} GB")
        print(f"{YELLOW}Used Memory: {WHITE}{memory.used / (2**30):.2f} GB")
        print(f"{YELLOW}Free Memory: {WHITE}{memory.available / (2**30):.2f} GB")
        input("\nPress Enter to return to the main menu.")

    def view_network_info(self):
        self.clear_screen()
        print(f"{CYAN}=== Network Information ==={WHITE}\n")
        interfaces = psutil.net_if_addrs()
        for name, addrs in interfaces.items():
            print(f"{YELLOW}Interface: {WHITE}{name}")
            for addr in addrs:
                print(f"{YELLOW}   {addr.family.name}: {WHITE}{addr.address}")
        input("\nPress Enter to return to the main menu.")

    def list_running_processes(self):
        self.clear_screen()
        print(f"{CYAN}=== Running Processes ==={WHITE}\n")
        for process in psutil.process_iter(['pid', 'name']):
            print(f"{YELLOW}PID: {WHITE}{process.info['pid']}, {YELLOW}Name: {WHITE}{process.info['name']}")
        input("\nPress Enter to return to the main menu.")

    def kill_process(self, pid):
        if platform.system().lower() == "windows":
            os.system(f"taskkill /F /PID {pid}")
            print(f"\n{RED}Process with PID {pid} terminated successfully.")
        else:
            print(f"\n{RED}Sorry, the taskkill feature is only supported on Windows.")

    def view_uptime(self):
        self.clear_screen()
        print(f"{CYAN}=== Uptime ==={WHITE}\n")
        uptime = psutil.boot_time()
        print(f"{YELLOW}Uptime: {WHITE}{psutil.datetime.datetime.fromtimestamp(uptime)}")
        input("\nPress Enter to return to the main menu.")

    def exit_tool(self):
        self.is_running = False
        print(f"{RED}Exiting the System Administration Tool. Goodbye!")

    def main(self):
        while self.is_running:
            self.display_menu()
            choice = input(f"{CYAN}Enter your choice (1-8): ")
            if choice == '1':
                self.view_system_info()
            elif choice == '2':
                self.view_storage_capacity()
            elif choice == '3':
                self.view_cpu_usage()
            elif choice == '4':
                self.view_memory_usage()
            elif choice == '5':
                self.view_network_info()
            elif choice == '6':
                self.list_running_processes()
            elif choice == '7':
                process_pid = input(f"{CYAN}Enter the PID of the process to kill: ")
                self.kill_process(int(process_pid))
            elif choice == '8':
                self.exit_tool()
            else:
                input(f"{WHITE}Invalid choice. Press Enter to try again.")


if __name__ == "__main__":
    sys_admin_tool = SystemAdminTool()
    sys_admin_tool.main()
