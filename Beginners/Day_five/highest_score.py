print('Welcome to heighest score generator')
try:
    score_list = input('Enter a list of score: ').split()
    for score in range(0, len(score_list)):
        score_list[score] = int(score_list[score])
    print (score_list)   
    #score_list.sort()
    #highest_score = score_list[-1]
    #print(f"The highest score is {highest_score}")
# another approach better way
    highest_score = 0
    for high in score_list:
        if high > highest_score:
            highest_score = high
    print(f"The highest score is {highest_score}")    

except:    
    print('one or more items is not a number')  


  
