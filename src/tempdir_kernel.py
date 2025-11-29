from tempfile import TemporaryDirectory
from ipykernel.kernelapp import IPKernelApp
from command_kernel import CommandKernel, command


class TempDirKernel(CommandKernel):
    """
    Wrapper for the `tempfile.TemporaryDirectory` to operate with bash in
    temporary directory.

    Use commands:
    - `#init` to create a new directory.
    - `#file` to save the content of the cell to file in temporary directory.
    """
    def __init__(self):
        self._init_env()

    def _init_env(self):
        self.dir = TemporaryDirectory()
        self.bashwrapper.run_command(f"cd {self.dir.name}")

    @command("#init")
    def init_env(self, command: str) -> str:
        self._init_env()
        return command

    @command("#file")
    def file(self, code: str, *args, **kwargs) -> str:
        return ""


if __name__ == "__main__":
    IPKernelApp.launch_instance(kernel_class=TempDirKernel)
