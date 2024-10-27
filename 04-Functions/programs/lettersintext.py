def lettersintext(text,letter):
    count=0
    for i in range(0,len(text)):
        if text[i]==letter:
            count+=1
    print(f"The number of letter:\"{letter}\": {count}")

def main():
    lettersintext("You never get a second chance to make a first impression","e")

if __name__ == "__main__":
    main()