from ReportGenerator import ReportGenerator


def generuj_raport(path):
    generator = ReportGenerator()
    lines = generator.read_log(path)
    return generator.generuj_raport(lines)


if __name__ == '__main__':
    print(generuj_raport("C:\\Users\\Piotr\\PycharmProjects\\Zaliczenie\\test.txt"))
