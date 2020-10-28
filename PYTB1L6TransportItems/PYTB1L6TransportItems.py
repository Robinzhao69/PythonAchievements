import time
import os

def opnieuw():
    os.system("cls")
    while True:
        ans1 = input("Factory[]\nDistribution[]\nShop[]\nRestart?   \nY/N: ")
        if ans1.lower() == "y":
            alles()
            os.system("cls")
            continue
        else:
            os.system("cls")
            break

def leeg():
    print("Factory[]\nDistribution[]\nShop[]")

def ssShop(Factory,Distribution,Shop):
    Shop.append("car")
    os.system("cls")
    print("Factory" + str(Factory) + "\nDistribution" + str(Distribution) + "\nShop" + str(Shop))
    time.sleep(1)
    Shop.remove("car")
    os.system("cls")
    print("Factory" + str(Factory) + "\nDistribution" + str(Distribution) + "\nShop" + str(Shop))

def ssDistribution(Factory,Distribution,Shop):
    Distribution.append("car")
    os.system("cls")
    print("Factory" + str(Factory) + "\nDistibution" + str(Distribution) + "\nShop" + str(Shop))
    time.sleep(1)
    Distribution.remove("car")
    os.system("cls")
    print("Factory" + str(Factory) + "\nDistribution" + str(Distribution) + "\nShop" + str(Shop))
    ssShop(Factory,Distribution,Shop)

def ssFactory():
    Factory = []
    Distribution = []
    Shop = []
    Factory.append("car")
    os.system("cls")
    print("Factory" + str(Factory) + "\nDistribution" + str(Distribution) + "\nShop" + str(Shop))
    time.sleep(1)
    Factory.remove("car")
    os.system("cls")
    print("Factory" + str(Factory) + "\nDistribution" + str(Distribution) + "\nShop" + str(Shop))
    ssDistribution(Factory,Distribution,Shop)

def alles():
    ssFactory()
    os.system("cls")
    print("Factory[]\nDistribution[]\nShop[]\nRestart?   \nY/N: ")


os.system("cls") 
ans = input("Factory[]\nDistribution[]\nShop[] \nBegin? \nY/N: ")
if ans.lower() == "y":
    alles() 
else:
    exit()

opnieuw()



