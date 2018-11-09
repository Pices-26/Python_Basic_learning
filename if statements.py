is_male = True
''' changing it to false will not make it print'''
is_tall = True
if is_male and is_tall:
    print('you are a tal male')
elif is_male and not(is_tall):
    print('you are a short male')
elif not(is_male and is_tall):
    print('you are not a male but you are tall')
else:
    print('you are not a male and you are small')
