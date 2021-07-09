
import vlc 
import pafy
import youtube_dl
print ( 'hello' )
hi=input( 'will u talk to me ? ')
if hi == "yes" :
    print ('yay')
    name=input('what is your name : ')
    print ( 'hii ',name,'i am albert')
    mood = input ('how are u ')
    if mood == "good":
      print ('nice!!')
      print ('what are ur hobbies ?')
      hobbies =input('')
      if hobbies == "nothing" :
          print ("oh okay ")
          print (' DO U KNOW PEWDIPIE ')
          ans=input('')
          if ans == "yes" :
              print ('great ')
              print ('here is a  song for ya ')
              url = "https://www.youtube.com/watch?v=UAlIq7BKNxg"
              video = pafy.new(url)
              best = video.getbest()
              media = vlc.MediaPlayer(best.url)
              media.play()
              
          else :
              print ( ' ur life is wasted bye ')
              print ('listen this')
              url = "https://www.youtube.com/watch?v=UAlIq7BKNxg"
              video = pafy.new(url)
              best = video.getbest()
              media = vlc.MediaPlayer(best.url)
              media.play()
      else :
              print ('ohh great hobbies')
              print ('i like talking to people thats what i do ')
              print (' DO U KNOW PEWDIPIE ')
              ans=input('')
              if ans == "yes" :
                print ('great ')
                print ('here is a  song for ya ')
                url = "https://www.youtube.com/watch?v=UAlIq7BKNxg"
                video = pafy.new(url)
                best = video.getbest()
                media = vlc.MediaPlayer(best.url)
                media.play()
              else :
                print ( ' ur life is wasted bye ')
                print ('listen this ')
                url = "https://www.youtube.com/watch?v=UAlIq7BKNxg"
                video = pafy.new(url)
                best = video.getbest()
                media = vlc.MediaPlayer(best.url)
                media.play()
                
                        
    
              
      
      
    elif mood == "sad" or " not fine" or "bad":
        print ( ' ohh can i know why are u  ' ,mood,)
        reason=input(' ')
        print ('ok hope u become good ')
        print ( ' shall i tell u a joke to make u happy ' )
        yes=input('  ')
        if yes == "yes":
             My_joke = pyjokes.get_joke(language="en", category="neutral")
             print(My_joke)
             print ('did u get laugh')
             no=input('')
             if no == "no":
                 print('shall i tell another one ?? ' )
                 ok=input('')
                 if ok == "ok" :
                     print (My_joke)
                 else :
                     print ('ok i am out of jokes ')
                     print ( ' i ll tell u song instead to make ur mood better ')
                     oh=input('ok ?')
                     if oh =="ok" :
                         url = "https://www.youtube.com/watch?v=SC8kqAiZ8eE"
                         video = pafy.new(url)
                         best = video.getbest()
                         media = vlc.MediaPlayer(best.url)
                         media.play()
                     else :
                         print ('fine')
                        
             else :
                 print ('i know thats quite funny ')
                 print : ( 'want to listen a song ? ')
                 oh=input('ok ?')
                 if oh =="ok" :
                         url = "https://www.youtube.com/watch?v=SC8kqAiZ8eE"
                         video = pafy.new(url)
                         best = video.getbest()
                         media = vlc.MediaPlayer(best.url)
                         media.play()
        
            
            
            
        else :
             print('ok then ')
                


             

    else :
        print ('hmm ok')
        print ('fine i wont disturb you byee ')
        
   
        

else :
   
        print ('ok sorry for disturbing u ')



 
