from report import worker, INPUT_FOLDER, OUTPUT_FOLDER

def main():
    print("Running main")
    worker.run(INPUT_FOLDER, OUTPUT_FOLDER)

if __name__ == "__main__":
    main()