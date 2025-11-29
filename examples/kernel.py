from ipykernel.kernelapp import IPKernelApp
from command_kernel import CommandKernel, command


class ExampleKernel(CommandKernel):
    @command("command1")
    def command1(self, code: str, *args, **kwargs) -> str:
        args = " ".join([a for a in args])
        kwargs = " ".join([f"{key}={value}" for key, value in kwargs.items()])
        return f"echo positionnal {args}\n echo keyword {kwargs}"


if __name__ == "__main__":
    IPKernelApp.launch_instance(kernel_class=ExampleKernel)
