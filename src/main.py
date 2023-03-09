"""Demo module."""
class Main:
    '''Define simple message'''

    def __init__(self) -> None:
        self.message = ""

    def run(self):
        """Run function."""
        self.hello_world()

    def hello_world(self):
        """Define message function."""
        self.message = "Hello World"

if __name__ == "__main__":
    Main().run()
