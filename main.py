from gtts import gTTS


#functions
def convert():
  def doc():
   fh = open('word.txt', 'w')
   fh.write(first_word + second_word + extra_word)
   fh.write("made with word maker https://github.com/gamemake-eng/word-maker") 


  def tts():
    text = gTTS(text=first_word + second_word + extra_word, lang='en')
    text.save('word.mp3')




#program
first_word = input("first silable:")
second_word = input("second silable:")
extra_word = input("etra silable OPTIONAL:")
print(first_word + second_word + extra_word)
convert()
