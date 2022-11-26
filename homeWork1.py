## 1
print('........... №1 ...........','Проверка дня недели',sep='\n')
print('да' if int(input('Укажите номер дня недели: ')) in (6,7) else 'нет')


# 2
print('........... №2 ...........','Проверка тождества',sep='\n')
for x in range(2):
   for y in range(2):
       for z in range(2):
           print(f'¬({x} ⋁ {y} ⋁ {z}) = ¬{x} ⋀ ¬{y} ⋀ ¬{z}',not(x or y or z) == ((not x) and (not y) and (not z)))


## 3
print('........... №3 ...........','Поределение координатной черверти',sep='\n')
x,y = map(int, input('Укажтите координаты x,y: ').split(','))
if x > 0 and y > 0:
   print('1')
elif x > 0 and y < 0:
   print('4')
elif x < 0 and y < 0:
   print('3')
else:
   print('2')


## 4
print('........... №4 ...........','Опредение диапазона координат по четверти',sep='\n')
a = int(input('Укажите четверть: '))
if a == 1:
   print('[0,oo),[0,oo)')
elif a == 2:
   print('(-oo,0],[0,oo)')
elif a == 3:
   print('(-oo,0],(-oo,0]')
else:
   print('[0,oo),(-oo,0]')


## 5
print('........... №5 ...........','Опредение растояния между 2-мя точками',sep='\n')
x1,y1 = map(int,input('Точка 1 => x1,y1: ').split(','))
x2,y2 = map(int,input('Точка 2 => x2,y2: ').split(','))
print(int(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 * 100) / 100)