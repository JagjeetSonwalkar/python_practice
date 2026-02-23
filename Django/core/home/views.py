from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse("Hi am home page!")
    # return HttpResponse("<h1>Hi am home page</h1>")
    # return render(request, "home/index.html")

    peoples = [
        {"name": "Rohit", "age": 45},
        {"name": "Virat", "age": 18},
        {"name": "SKY", "age": 44},
        {"name": "Varma", "age": 59},
        {"name": "Rahul", "age": 17},
        {"name": "hardik", "age": 33},
    ]

    text = '''Lorem ipsum dolor sit amet consectetur adipisicing elit. Nam, necessitatibus sit aut expedita, est laboriosam eveniet distinctio nemo natus consequatur rerum placeat nihil molestias explicabo, corporis animi eligendi fugit accusantium!
Illo culpa, quaerat deleniti consequatur ab, quibusdam fugit porro sed possimus vel animi, obcaecati natus aspernatur debitis dolore nam incidunt officiis. Porro, pariatur vel similique obcaecati in eveniet architecto quia.
Consequuntur consectetur accusantium ut facere ex nulla, modi porro, accusamus omnis et enim quidem id maiores dolorem autem repudiandae doloremque rerum est? Saepe facere eius ad dolorum minima fuga consectetur.
Fugit dignissimos fugiat tempore unde maiores explicabo sed, hic facilis consequatur doloremque eveniet nesciunt quam earum dicta iusto optio dolorem ipsum? Aliquam ipsam explicabo distinctio quos culpa recusandae libero veritatis!
Commodi iste soluta provident fuga mollitia alias officiis modi aliquid vero error minus dolorum earum expedita hic adipisci, repudiandae vitae saepe. Nesciunt quaerat sequi accusamus dolore nihil necessitatibus aut repellendus.
Assumenda deserunt amet vel laboriosam dolores odio corrupti dicta, ullam, error alias, facilis beatae! Pariatur sapiente facere odit obcaecati. Impedit inventore dignissimos suscipit exercitationem fugiat odit minima reprehenderit eius fuga.
Officia id sunt assumenda odio eius recusandae, aut pariatur distinctio doloremque minus laudantium possimus voluptas consequuntur molestias sed in ab facere nostrum maxime quam repellat. Iste maiores alias doloribus nostrum.
Sequi quibusdam fugiat vel error unde suscipit laudantium veniam, quia tempora aut voluptatem omnis iure impedit maxime totam. Dolores earum architecto quas eveniet quasi nulla totam, sint ipsum! Eveniet, quam!
Quibusdam fugiat aut distinctio, voluptates adipisci quasi dolorem consequuntur cumque officia nesciunt ut officiis libero odio. Illum obcaecati eaque vitae earum blanditiis eligendi ad excepturi, alias corporis, facere nobis? Expedita?
Consequatur amet harum possimus porro? Dolorum mollitia rem asperiores aperiam, omnis fugiat iste tenetur non officiis quod soluta aliquid id inventore ut nostrum dignissimos cupiditate incidunt porro ea nemo facere.
    '''

    vegetbales = {"Pumpkin", "Tomato", "Patato"}

    return render(request, "home/index.html", context= {"page":"Django","peoples" : peoples, "text":text, "vegetables" : vegetbales})

def success(request):
    return HttpResponse("<h1>hey this an success page</h1>")

def contact(request):
    context = {"page": "contact"}
    return render(request, "home/contact.html")

def about(request):
    context = {"page": {about}}
    return render(request, "home/about.html")