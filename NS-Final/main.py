import tkinter as tk
from tkinter import messagebox, scrolledtext
import subprocess
import threading

# Dictionary mapping tool names to their shell commands.
# Update the paths below to reflect the actual directories on your system.
commands = {
    "Defensive-Network-IDPS": "chmod +x /home/subramanian/Downloads/NS\ Final/Defensive-Network-Intrusion-Detection-Prevention-System-IDPS/setup_ids.sh && sudo /home/subramanian/Downloads/NS\ Final/Defensive-Network-Intrusion-Detection-Prevention-System-IDPS/setup_ids.sh",
    "LDAP": "sudo python3 /home/subramanian/Downloads/NS\ Final/LDAP/ldpa.py",
    "Log Monitoring": "sudo python3 /home/subramanian/Downloads/NS\ Final/log_monitoring/log_monitor.py && cat /home/subramanian/Downloads/NS\ Final/log_monitoring/log_report.txt",
    "Packet Filter Firewall": "sudo python3 /home/subramanian/Downloads/NS\ Final/python-packet-filter-firewall/run.py",
    "TLS Traffic Analyzer": "sudo python3 /home/subramanian/Downloads/NS\ Final/TLS-Traffic-Analyzer/tls_analyzer.py",
    "SSLyze": "sslyze amrita.edu"
}
# List of tools that produce continuous output.
continuous_tools = [
    "LDAP",
    "Log Monitoring",
    "Packet Filter Firewall"
]

class ASPSFirewallGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ASPS Next-Gen Firewall")
        self.geometry("800x600")
        self.create_widgets()

    def create_widgets(self):
        # Left frame for tool selection and buttons.
        self.left_frame = tk.Frame(self, width=200)
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        # Listbox to display available tools.
        self.tool_listbox = tk.Listbox(self.left_frame)
        for tool in commands.keys():
            self.tool_listbox.insert(tk.END, tool)
        self.tool_listbox.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Button to run the selected tool.
        self.run_button = tk.Button(self.left_frame, text="Run Selected", command=self.run_selected)
        self.run_button.pack(fill=tk.X, padx=5, pady=5)

        # Button to run all tools.
        self.run_all_button = tk.Button(self.left_frame, text="Run All", command=self.run_all)
        self.run_all_button.pack(fill=tk.X, padx=5, pady=5)

        # Right frame for output display (divided into general and continuous output areas).
        self.right_frame = tk.Frame(self)
        self.right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Top frame for general output.
        self.general_frame = tk.Frame(self.right_frame)
        self.general_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.output_text = scrolledtext.ScrolledText(self.general_frame, height=15)
        self.output_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Bottom frame for continuous output.
        self.continuous_frame = tk.Frame(self.right_frame, bg="lightgray")
        self.continuous_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

        label = tk.Label(self.continuous_frame, text="Continuous Output", bg="lightgray")
        label.pack(anchor="w", padx=5)

        self.continuous_text = scrolledtext.ScrolledText(self.continuous_frame, height=10, bg="black", fg="lime")
        self.continuous_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def append_general(self, text):
        self.output_text.insert(tk.END, text + "\n")
        self.output_text.see(tk.END)

    def append_continuous(self, text):
        self.continuous_text.insert(tk.END, text + "\n")
        self.continuous_text.see(tk.END)

    def run_command(self, command, tool_name):
        try:
            process = subprocess.Popen(
                command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, text=True
            )
            # Read stdout line by line.
            while True:
                line = process.stdout.readline()
                if not line and process.poll() is not None:
                    break
                if line:
                    if tool_name in continuous_tools:
                        self.append_continuous(line.rstrip())
                    else:
                        self.append_general(line.rstrip())
            # Read any remaining stderr.
            stderr_output = process.stderr.read()
            if stderr_output:
                for line in stderr_output.splitlines():
                    if tool_name in continuous_tools:
                        self.append_continuous(line.rstrip())
                    else:
                        self.append_general(line.rstrip())
            process.wait()
            finish_message = f"Command '{tool_name}' finished with return code {process.returncode}\n"
            if tool_name in continuous_tools:
                self.append_continuous(finish_message)
            else:
                self.append_general(finish_message)
        except Exception as e:
            error_message = f"Error running {tool_name}: {str(e)}"
            if tool_name in continuous_tools:
                self.append_continuous(error_message)
            else:
                self.append_general(error_message)

    def run_selected(self):
        selection = self.tool_listbox.curselection()
        if selection:
            tool = self.tool_listbox.get(selection[0])
            command = commands[tool]
            start_message = f"Running {tool}...\n"
            if tool in continuous_tools:
                self.append_continuous(start_message)
            else:
                self.append_general(start_message)
            threading.Thread(target=self.run_command, args=(command, tool), daemon=True).start()
        else:
            messagebox.showwarning("No Selection", "Please select a tool to run.")

    def run_all(self):
        self.append_general("Running all tools (ASPS Next-Gen Firewall is running)...\n")
        def run_all_commands():
            for tool, command in commands.items():
                start_message = f"\n--- Running {tool} ---"
                if tool in continuous_tools:
                    self.append_continuous(start_message)
                else:
                    self.append_general(start_message)
                self.run_command(command, tool)
        threading.Thread(target=run_all_commands, daemon=True).start()

if __name__ == "__main__":
    app = ASPSFirewallGUI()
    app.mainloop()

