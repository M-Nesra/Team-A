import sys
def dog_years(age):
    return (
      0 if age == 0 else
      15 if age == 1 else
      24 if age == 2 else 24 + 5 * (age - 2)
    )
    
    
if __name__ == "__main__":
    age = int(sys.argv[1])
    human_age = dog_years(age)
    print (f"A {age}-year-old dog is eqivalent to a {human_age}-year-old"
          f"person.")
