start = "You really like computer science but your path may be different if you are a girl or boy. Insert boy or girl to see your path"
print(start)

user_input=input()
if user_input == "girl":
    print("You tell your counselor about your goals but because you are a girl he suggests a creative writing class instead. Next it is time to apply for college. If you want to go to college and major in Art type art or if you want to continue your dreams, type computer science.")
    user_input=input()
    if user_input=="art":
        print("You did not follow your dreams and are now unhappy at an art school")
    elif user_input =="computer science":
        print("You are in a classroom with all male and they try to discourage you. Are you going to let them get to you. Type yes tp leave school and type no to stay studying.")
        user_input=input()
        if user_input =="yes":
            print("You left school and becoming a stay at home mom.")
        elif user_input =="no":
            print("You apply for a job and are hired because the boss notices your hard work throughout your education. Congratulations!")



elif user_input == "boy":
    print("You are placed into a AP computer science class and you excell in the class because you are supported by your peers. Now you must decide your future. Type college to go to earn a bachelors in CS or type work to not go to college")
    user_input=input()
    if user_input =="college":
        print("You are recruited on campus for an internship and get a permanent job with that company. Congratulations!")
    elif user_input =="work":
        print("You get an internship and get hired at that same company. Congratulations!")
else:
    print("Please type a given answer.")
