import sys
from store import Store

def main(fname):
    store = Store("Austin's Emporium")
    print(f"{store.store_name} open!")


    with open(fname, 'r') as f:
        for line in f:
            line = line.strip()
            tokens = line.split(" ")

            # STOCK carrot 100 1
            if tokens[0] == 'STOCK':
                print(f"STOCKING ITEM! {line}")
                store.stock(tokens[1],  float(tokens[2]), int(tokens[3]),)

            # PURCHASE carrot 1 Samantha 123-321-123
            elif tokens[0] == 'PURCHASE':
                print(f"PURHCASING ITEM! {line}")
                store.purchase(tokens[3], tokens[1], int(tokens[2]), tokens[4])
            else:
                print(f"ERROR! The first token, {tokens[0]} is not a valid command. Exiting")
                exit()

    print(store.summarize())
    print("Goodbye!")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    if len(sys.argv) != 2: #
        print("Please provide one argument, the input file")
        exit()

    arg1 = sys.argv[1] # asking first argument (another you can ask for the last argument sys.argv[-1])
    # negitive indexing for lists is reverse:
        # a = []
        # a[1] #second thing in the lst
        # a[-x] <--> a[len(a) - x)
    main(arg1)

