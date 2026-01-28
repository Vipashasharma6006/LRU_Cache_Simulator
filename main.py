from lru_cache import LRUCache

def main():
    cap = int(input("Enter cache capacity: "))
    cache = LRUCache(cap)

    while True:
        print("\nOptions:\n1. Put\n2. Get\n3. Display\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            key = int(input("Enter key: "))
            val = int(input("Enter value: "))
            cache.put(key, val)
            print(f"Added ({key}, {val})")

        elif choice == "2":
            key = int(input("Enter key to get: "))
            val = cache.get(key)
            if val != -1:
                print(f"Value = {val}")
            else:
                print("Key not found!")

        elif choice == "3":
            cache.display()

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
