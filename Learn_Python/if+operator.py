Indian = ["samosa","daal","naan"]
Chinese = ["egg role","pot sticker","fired rice"]
Italian = ["pizza","pasta","risotto"]

dish = input("Enter Dish Name : ")

if dish in Indian:
    print(f"{dish} is Indian")
elif dish in Chinese:
    print(f"{dish} is Chinese")
elif dish in Italian:
    print(f"{dish} is Italian")
else:
    print(f"Based on little acknowledgement i donot ans which cusine it is ")