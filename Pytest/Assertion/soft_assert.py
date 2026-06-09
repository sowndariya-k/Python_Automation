class SoftAssert:
    def __init__(self):
        self.errors = []

    def assert_true(self, condition, message="Assertion Failed"):
        if not condition:
            self.errors.append(message)

    def assert_equal(self, actual, expected, message=None):
        if actual != expected:
            self.errors.append(
                message or f"{actual} != {expected}"
            )

    def assert_all(self):
        if self.errors:
            raise AssertionError("\n".join(self.errors))