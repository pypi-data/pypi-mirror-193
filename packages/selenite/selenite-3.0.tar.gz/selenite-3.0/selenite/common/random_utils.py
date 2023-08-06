import random
import string


class RandomGenerator:
    @staticmethod
    def random_int(min_value=0, max_value=100):
        return random.randint(min_value, max_value)

    @staticmethod
    def random_float(min_value=0.0, max_value=1.0):
        return random.uniform(min_value, max_value)

    @staticmethod
    def random_string(length=10):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for _ in range(length))

    @staticmethod
    def random_bool():
        return bool(random.getrandbits(1))

    @staticmethod
    def random_choice(lst):
        return random.choice(lst)

    @staticmethod
    def random_dict(length=10):
        return {
            RandomGenerator.random_string(): RandomGenerator.random_int() for _ in range(length)
        }

    @staticmethod
    def random_list(length=10, element_type='int', **kwargs):
        element_generator = getattr(RandomGenerator, f'random_{element_type}')
        return [
            element_generator(**kwargs) for _ in range(length)
        ]

    @staticmethod
    def random_chinese(length):
        return ''.join(chr(random.randint(0x4e00, 0x9fa5)) for _ in range(length))
