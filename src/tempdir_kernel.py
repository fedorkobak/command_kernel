import logging
from pathlib import Path
from tempfile import TemporaryDirectory
from ipykernel.kernelapp import IPKernelApp
from command_kernel import CommandKernel, command

logger = logging.getLogger(__file__)


class TempDirKernel(CommandKernel):
    """
    Wrapper for the `tempfile.TemporaryDirectory` to operate with bash in
    temporary directory.

    Use commands:
    - `#init` to create a new directory.
    - `#file` to save the content of the cell to file in temporary directory.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_dir()

    def _init_dir(self):
        self.dir = TemporaryDirectory()
        self.bashwrapper.run_command(f"cd {self.dir.name}")

    @command("#init")
    def init_env(self, command: str) -> str:
        self._init_dir()
        return command

    @command("#file")
    def file(self, code: str, *args, **kwargs) -> str:
        logger.info("File command is invoked")
        filename = args[0]
        with open(Path(self.dir.name) / filename, "w") as file:
            file.write(code)
        return ""


if __name__ == "__main__":
    IPKernelApp.launch_instance(kernel_class=TempDirKernel)
