find it: edit.find()

next one: edit.find_next()

draw:
    edit.word_left()
draw <number_small>:
    edit.word_left()
    repeat(number_small-1)

spring:
    edit.word_right()
spring <number_small>:
    edit.word_right()
    repeat(number_small-1)

go left: edit.left()
go left <number_small>: 
    edit.left()
    repeat(number_small-1)

go right: edit.right()
go right: 
    edit.right()
    repeat(number_small-1)

go up: edit.up()
go up: 
    edit.up()
    repeat(number_small-1)

go down: edit.down()
go down <number_small>: 
    edit.down()
    repeat(number_small-1)
scratch <number_small>: 
    key(backspace)
    repeat(number_small-1)
drill <number_small>: 
    key(delete)
    repeat(number_small-1)
(drill | scratch) tail: 
    key(shift-end)
    key(delete)
(drill | scratch) head: 
    key(shift-home)
    key(delete)

head:
    edit.line_start()
    
tail:
    edit.line_end()

far left:
    edit.line_start()
    edit.line_start()

far right:
    edit.line_end()

far down:
    edit.file_end()

far up:
    edit.file_start()

# go page down:
#     edit.page_down()

# go page up:
#     edit.page_up()

# selecting
sell line:
    edit.select_line()

sell all:
    edit.select_all()

sell left:
    edit.extend_left()

sell right:
    edit.extend_right()

sell up:
    edit.extend_line_up()

sell down:
    edit.extend_line_down()

sell word:
    edit.select_word()
    
sell draw:
    edit.extend_word_left()

sell spring:
    edit.extend_word_right()

sell far left:
    edit.extend_line_start()

sell far right:
    edit.extend_line_end()

sell far up:
    edit.extend_file_start()

sell far down:
    edit.extend_file_end()

# editing
tab:
    edit.indent_more()

retab:
    edit.indent_less()

# deleting
void line:
    edit.delete_line()

# void left:
#     key(backspace)

# void right:
#     key(delete)
    
void up:
    edit.extend_line_up()
    edit.delete()
    
void down:
    edit.extend_line_down()
    edit.delete()
    
void word:
    edit.delete_word()
    
void draw:
    edit.extend_word_left()
    edit.delete()
    
void spring:
    edit.extend_word_right()
    edit.delete()
    
void far left:
    edit.extend_line_start()
    edit.delete()
    
void far right:
    edit.extend_line_end()
    edit.delete()
    
void far up:
    edit.extend_file_start()
    edit.delete()
    
void far down:
    edit.extend_file_end()
    edit.delete()
    
clear all:
    edit.select_all()
    edit.delete()
    
#copy commands
copy all:
    edit.select_all()
    edit.copy()
#to do: do we want these variants, seem to conflict
# copy left:
#      edit.extend_left()
#      edit.copy()
# copy right:
#     edit.extend_right()
#     edit.copy()
# copy up:
#     edit.extend_up()
#     edit.copy()
# copy down:
#     edit.extend_down()
#     edit.copy()
    
copy word:
    edit.select_word()
    edit.copy()
    
copy draw:
    edit.extend_word_left()
    edit.copy()
    
copy spring:
    edit.extend_word_right()
    edit.copy()
    
copy line:
    edit.select_line()
    edit.copy()
    
copy far left:
    edit.extend_line_start()
    edit.delete()
    
copy far right:
    edit.extend_line_end()
    edit.copy()
    
copy far up:
    edit.extend_file_start()
    edit.copy()
    
copy far down:
    edit.extend_file_end()
    edit.copy()
    
#cut commands
cut all:
    edit.select_all()
    edit.cut()
    
#to do: do we want these variants
# cut left:
#      edit.select_all()
#      edit.cut()
# cut right:
#      edit.select_all()
#      edit.cut()
# cut up:
#      edit.select_all()
#     edit.cut()
# cut down:
#     edit.select_all()
#     edit.cut()
    
cut word:
    edit.select_word()
    edit.cut()
    
cut draw:
    edit.extend_word_left()
    edit.cut()
    
cut spring:
    edit.extend_word_right()
    edit.cut()
    
cut line:
    edit.select_line()
    edit.cut()
(pace | paste) all:
    edit.select_all()
    edit.paste()