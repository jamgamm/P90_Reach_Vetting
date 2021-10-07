from DatabaseConnect import get_database
from pandas import DataFrame
dbname = get_database()

def Printer(name):
    collection_name = dbname[name]
    item_details = collection_name.find({}, {'_id': 0, 'Name':1, 'Runtime':1, 'Producer':1, 'Poster':1,'IMDb Rating':1 })
    items_df = DataFrame(item_details)
    print("Showing results for collection:", name)
    print(items_df)

def PrintComment(name):
    collection_name = dbname[name]
    item_details = collection_name.find({}, {'_id': 0, 'Movie':1, 'Comment':1})
    items_df = DataFrame(item_details)
    print(items_df)


def main():
    collection1 = Printer("Ghibli")
    collection2 = Printer("Disney")
    collection3 = Printer("Marvel")

    ques = input("Would you like to read extra comments I have about each movie?(y/n) ")
    if ques == 'y':
        comments = PrintComment("Comments")
    else:
        print("Thanks for looking!")



if __name__ == "__main__":
    main()
