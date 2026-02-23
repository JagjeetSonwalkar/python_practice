# Check if two strings are anagrams. race = care, heart = earth

def isAnagrams(getString1, getString2):
    word1 = []
    word2 = []

    for i in getString1:
        word1.append(i)
    word1.sort()

    for i in getString2:
        word2.append(i)
    word2.sort()

    if(word1 == word2):
        print("It is anagrams")
    else:
        print("It is NOT anagrams")

if __name__ == "__main__":
    myString1 = "race"
    myString2 = "care"

    isAnagrams(myString1, myString2)

    myString1 = "heart"
    myString2 = "earth"

    isAnagrams(myString1, myString2)