print("Welcome to Leap Year Finder")
year=int(input("Enter the year you wish to checkout for \n"))
if(year%4==0):
    if(year%100==0):
      if(year%400==0):
        print(f"Given year {year} is a leap year")
      else:
            print(f"given year {year}is not a leap year")
    else:
        print(f"Given year {year} is a leap year")       
else:
    print(f"Given year {year} is not a leap year") 