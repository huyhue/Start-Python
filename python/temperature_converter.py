def cConvert():
    while True:
        cTemp = input("Please enter C degree: ")
        if cTemp:
            cTemp = float(cTemp)
            fTemp = round(9*cTemp/5 +32, 1)

            print(f"{cTemp}C is converted to {fTemp}F")
            break
        else:
            print("cTemp input empty")
            continue

def main():
    cConvert()

if __name__ == "__main__":
    main()