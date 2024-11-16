from datetime import datetime

def main1():
    print("I am main one")
    a=datetime.now().time().hour
    print(a)

def main():
    print("I am main")

if __name__=="__main__":
    main()

main1()
##