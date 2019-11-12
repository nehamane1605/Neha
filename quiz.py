print('Welcome to this small quiz.Let us see how much you know about Neha')

ans = input('Are you ready to play (yes/no) : ')
score = 0
total_q = 6

if ans.lower() == 'yes':
    ans = input('1.What is the birth month of Neha(january or december)?')
    if ans.lower() == 'december':
       score +=1
       print('Correct')
    else:
       print('Incorrect')

    ans = input('2.Which is the favourite sport of Neha(hockey or badminton?')
    if ans.lower() == 'badminton':
       score +=1
       print('Correct')
    else:
       print('Incorrect')

    ans = input('3.What does Neha use the most(instagram or whatsapp)?')
    if ans.lower() == 'instagram':
       score +=1
       print('Correct')
    else:
       print('Incorrect')

    ans = input('4.What does Neha prefer(reading or blogging)?')
    if ans.lower() == 'blogging':
       score +=1
       print('Correct')
    else:
       print('Incorrect')

    ans = input('5.Is Neha good in cooking(yes or no)?')
    if ans.lower() == 'no':
       score +=1
       print('Correct')
    else:
       print('Incorrect')

    ans = input('1.What would Neha like to do during her free time(sleeping or webseries?')
    if ans.lower() == 'sleeping':
       score +=1
       print('Correct')
    else:
       print('Incorrect')

print('Thankyou for playing, you got',score, "questions correct.")
mark = (score/total_q) * 100

print("Mark:", str(mark) + ' % ')

