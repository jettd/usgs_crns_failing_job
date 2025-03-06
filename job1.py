def main():
    print("Executing failing job")
    print("Returning 1.")
    return 1

if __name__ == "__main__":
    result = main()
    print(result)