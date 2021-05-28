from libs import Employee, Human

def main():
    """Main"""
    bf = Human("Buttfucker", 3000)
    bf.name = "Donald"
    print(bf.name)
    print(bf.age)

    admin = Employee("admin", bf.name, bf.age)
    print(admin.position)
    print(admin.name)
    print(admin.age)

if __name__ == "__main__":
    main()
