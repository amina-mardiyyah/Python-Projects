
# A simple BMI calculator with a verdict

weight = float(input('Enter your weight: '))
height = float(input('Enter your height: '))

bmi = weight/(height*height)

bmi = round(bmi,1)

if bmi<18.5:
    print('You are underweighted')
elif((bmi>=18.5) and (bmi<25)):
    print('You have a normal weight')
elif((bmi>=25) and (bmi<30)):
    print('You are overweighted')
else:
    print('You are Obese')
