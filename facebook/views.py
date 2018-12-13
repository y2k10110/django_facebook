from django.shortcuts import render, redirect
from facebook.models import Article, Comment

# Create your views here.

def play(request):
    return render(request, 'play.html')

count = 0

def play2(request):
    name = '김양연'
    global count
    count = count + 1

    age = 20

    if age < 19:
        status = '미성년자'
    else:
        status = '성인'

    diary = ['11월 22일', '11월 23일', '11월 24일']

    return render(request, 'play2.html',
                  {'name': name, 'count':count, 'status':status, 'diary':diary}) #render는 그려주는거. play2를 읽어서 장고의 방식으로 보여준다

def profile(request):
    return render(request, 'profile.html')

def event(request):
    name = '김양연'
    global count
    count = count + 1

    age = 20

    if age < 19:
        status = '미성년자'
    else:
        status = '성인'

    if count == 7:
        lucky = '당첨!'
    else:
        lucky = '꽝...'

    return render(request, 'event.html',
                  {'name': name, 'count':count, 'status':status, 'lucky':lucky}) #render는 그려주는거. play2를 읽어서 장고의 방식으로 보여준다

def help(request):
    return render(request, 'help.html')

def fail(request):
    return render(request, 'fail.html')

def warn(request):
    return render(request, 'warn.html')

def newsfeed(request):
    articles = Article.objects.all().order_by('-created_at')

    for article in articles:
        article.length = len(article.text)

    return render(request, 'newsfeed.html', {'articles':articles})

def detail_feed(request, pk):
    article = Article.objects.get(pk=pk) # primary key. 게시물 아이디 같은거. 앞에 pk는 예약어. 뒤에 pk가 변수

    if request.method == 'POST':
        Comment.objects.create(
            article = article,
            author = request.POST['nick_name'],
            text = request.POST['reply'],
            password = request.POST['password']
        )

        return redirect(f'/feed/{ article.pk }')

    return render(request, 'detail_feed.html', {'article':article})

def new_feed(request):
    if request.method == 'POST':
        new_article = Article.objects.create( #대문자 article은 페이스북 모델
            author = request.POST['author'],
            title = request.POST['title'],
            password = request.POST['password'],
            text = request.POST['content'],
        )
        return redirect(f'/feed/{ new_article.pk }') #변수를 넣을땐 앞에 f를 넣어줘야해. 이게 변수가 나중에 바
    return render(request, 'new_feed.html') #Get 요청을 보내면 위에 post 요청은 걸러서 아래 렌더만 실행된다.

def edit_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.author = request.POST['author']
            article.title = request.POST['title']
            article.text = request.POST['content']
            article.save()
            return redirect(f'/feed/{ article.pk }')
        else:
            return redirect('/fail')

    return render(request, 'edit_feed.html', {'article':article})

def remove_feed(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        if article.password == request.POST['password']:
            article.delete()
            return redirect('/')
        else:
            return redirect('/fail')

    return render(request, 'remove_feed.html', {'article':article})