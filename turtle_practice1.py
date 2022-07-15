from turtle import*

# speed(0)
#
# for k in range(30):
#     a = k*10
#     for i in range(4):
#         left(90)
#         fd(a)
# done()

#太阳花
speed(0)
color('red','yellow')
begin_fill()
while True:
    fd(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

#五角星
# color("red","yellow")
#
# begin_fill()
# while True:
#     forward(200)
#     rt(144)
#     if abs(pos()) < 1:
#         break
# end_fill()
# hideturtle()
# done()
#




