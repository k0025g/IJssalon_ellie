def presenteer(dictionary, totaal):
    for k, v in dictionary.items():
        print(k,":", v, "euro")
    print("====================")
    print(f"totaal : {totaal} euro")
