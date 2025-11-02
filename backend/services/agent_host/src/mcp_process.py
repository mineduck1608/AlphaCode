# helper to spawn & communicate with a STDIO MCP process (JSON-lines)
import subprocess
import threading
import json
import queue
import sys
from typing import Optional, Dict, Any

class MCPProcess:
    def __init__(self, cmd: list):
        self.proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        self._out_q = queue.Queue()
        self._reader = threading.Thread(target=self._read_loop, daemon=True)
        self._reader.start()

    def _read_loop(self):
        for line in self.proc.stdout:
            line = line.strip()
            if line:
                try:
                    obj = json.loads(line)
                except Exception:
                    obj = {"raw": line}
                self._out_q.put(obj)

    def send(self, message: Dict[str, Any]):
        self.proc.stdin.write(json.dumps(message) + "\n")
        self.proc.stdin.flush()

    def recv(self, timeout: Optional[float] = None):
        try:
            return self._out_q.get(timeout=timeout)
        except queue.Empty:
            return None

    def terminate(self):
        self.proc.terminate()
        self.proc.wait()
