from libs import Employee, Human, check

def main():
    """Main"""
    bf = Human("Donald", 40)
    admin = Employee("admin", bf.name, bf.age)
    check(admin)

if __name__ == "__main__":
    main()
