from pywebio import *
from pywebio import start_server 
from pywebio.input import * 
from pywebio.output import put_table, put_text, put_image, put_html 
from pywebio.session import * 
from pywebio.pin import *
from pywebio import config
css="""
body{
background-color: red;
Color:white;
}
"""
@config(css_style=css)
def App():
  put_image('https://images.alwatanvoice.com/news/large/9998983191.jpg', width='100%')
  put_image('https://i.pinimg.com/originals/ed/0e/87/ed0e87943ea3207d9a3f20b870541afd.gif',width='100%' )
  put_html("""
  <center>
  <h2></h2>
  <h2>🔊🔊برعاية اوريدو😂😂</h2>
  <audio controls
  <source src="" type="audio/mp3"autoplay></audio>
  <br>
   <video controls
  <source src="https://mp4loop.xyz/videos/shakira-chantaje_906857.mp4" width='100%'></video>
  <p1>📼📼📼📼📼📼📼</p1>
  <video controls
  <source src="https://mp4loop.xyz/videos/shakira-loca_161452.mp4" type="video/mp4" width='100%'></video>
<p1>📼📼📼📼📼📼📼</p1>
  <video controls
  <source src="https://mp4loop.xyz/videos/eminem-the-monster_203244.mp4" type="video/mp4" width='100%'></video>
<p1>📼📼📼📼📼📼📼</p1>
  <video controls
  <source src="https://mp4loop.xyz/videos/eminem-not-afraid_183086.mp4" type="video/mp4" width='100%'></video>
<p1>📼📼📼📼📼📼📼</p1>

  <iframe width="100%" src="https://www.youtube.com/embed/ix1HQbbI3rQ?si=OpbdQ1PheQgUJm4O" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
  <p1>Made by Khalil</p1>

  </center>


  """)
  put_image('https://cdn.dribbble.com/users/497438/screenshots/2084032/xtyf_1.gif', width='100%')

start_server(App, port=443 , debug=True)