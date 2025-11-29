from pathlib import Path
from unittest import TestCase
from tempdir_kernel import TempDirKernel

environment_kernel = TempDirKernel()


class TestEnvironment(TestCase):
    def test_file(self):
        """
        Checks that the content specified by the `#file` command has been
        saved to the directory correctly.
        """
        file_name = "my_file"
        exp_content = "content"
        code = (
            f"#file {file_name}\n" +
            exp_content
        )

        environment_kernel.do_execute(code=code)

        with open(Path(environment_kernel.dir.name) / file_name, "r") as f:
            content = f.read()
        self.assertEqual(exp_content, content)
