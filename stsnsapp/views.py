from .form import SignupForm,LoginForm,UserUpdateForm
from django.shortcuts import render,redirect,get_object_or_404,resolve_url
from django.views import generic
from django.contrib.auth.mixins import UserPassesTestMixin 
from django.views.generic import CreateView,DeleteView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import get_user_model,login
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from stsnsapp.models import liquor,cigalettes,CustomUser,BoardModel
from django.contrib.auth import login
from .form import H_liquor,H_cigalettes,createform
from django.urls import reverse_lazy
from . import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#トップページ

#ファーストページ
def first_page(request):
    return render(request,'first_page.html',{})

#ログイン
class Login(LoginView):
    form_class = LoginForm
    template_name = "login.html"
#ログアウト
class Logout(LoginRequiredMixin,LogoutView):
    template_name = 'logout.html'


#サインアップ
class Signup(generic.CreateView):
    template_name = 'user_form.html'
    form_class = SignupForm

    def form_valid(self, form):
        user = form.save() # formの情報を保存
        return redirect('stsnsapp:signup_done')

    # データ送信
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "Sign up"
        return context


#サインアップ完了
class SignupDone(generic.TemplateView):
    template_name = 'sign_up_done.html'

#マイページ機能
class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
        user = self.request.user
        return user.pk == self.kwargs['pk']

class UserUpdate(LoginRequiredMixin,OnlyYouMixin, generic.UpdateView):
    model = CustomUser
    form_class = UserUpdateForm
    template_name = 'user_form.html'

    def get_success_url(self):
        return resolve_url('stsnsapp:mypage', pk=self.kwargs['pk'])

    # contextデータ作成
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["process_name"] = "更新"
        return context

class UserDeleteView(LoginRequiredMixin,OnlyYouMixin, generic.DeleteView):
    template_name = "user_delete.html"
    success_url = reverse_lazy("stsnsapp:login")
    model = CustomUser
    slug_field = 'username'
    slug_url_kwarg = 'username'



#マイページ
@login_required
class MyPage(OnlyYouMixin, generic.DetailView):
    model = CustomUser
    template_name = 'mypage.html'
    # モデル名小文字(useルインスタンスがテンプレートファイルに渡される

#ゲストログイン
def guest_login(request):
    guest_user = CustomUser.objects.get(email='guestuser@example.com')
    login(request, guest_user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('stsnsapp:top_page')


#トップページの掲示板
@login_required
def listfunc(request):
    object_list = BoardModel.objects.order_by('-date')
    return render(request,'toppage.html',{'object_list':object_list})
@login_required
def mypage_liquor(request,pk):
    liquor_form = H_liquor()
    cigalettes_form = H_cigalettes()
    forms = {"form":liquor_form,"c_form":cigalettes_form,"value":"","value2":"","all_value":"","guest_user":"","authentication":""}

    forms["guest_user"] = CustomUser.objects.filter(pk=3).first()
    if request.user == forms["guest_user"]:
        forms["authentication"] = "success"
    if request.method == 'GET':
        liquor_date = liquor.objects.filter(user_liquor=request.user).first()
        cigalettes_date = cigalettes.objects.filter(user_cigalettes=request.user).first() 
        if liquor_date:
            forms["value"] = liquor_date.how_many_liquor2
        else:
            Liquors = liquor.objects.create(
                how_many_liquor2=0,
                user_liquor=request.user
            )
            liquor_date = Liquors
            forms["value"] = liquor_date.how_many_liquor2
        if cigalettes_date:
            forms["value2"] = cigalettes_date.how_many_cigalettes2
        else:
            Cigalettes = cigalettes.objects.create(
                    how_many_cigalettes2=0,
                    user_cigalettes=request.user
                )
            cigalettes_date = Cigalettes
            forms["value2"] = cigalettes_date.how_many_cigalettes2
        forms["all_value"] = liquor_date.how_many_liquor2 + cigalettes_date.how_many_cigalettes2
        return render(request, 'mypage.html', forms)

    if request.method == 'POST':
        liquor_before = liquor.objects.filter(user_liquor=request.user).first()
        cigalettes_before = cigalettes.objects.filter(user_cigalettes=request.user).first() 
        if request.POST.get("how_many_liquor"):
            if liquor.objects.filter(user_liquor=request.user).exists():
                how_many_liquor = 0
                how_many_liquor2 = int(request.POST.get("how_many_liquor")) * 250 + liquor_before.how_many_liquor2
                liquor_before.how_many_liquor2 = how_many_liquor2
                liquor_before.save()
            else:
                how_many_liquor2 = int(request.POST.get("how_many_liquor")) * 250
                Liquors = liquor.objects.create(
                    how_many_liquor2=how_many_liquor2,
                    user_liquor=request.user
                )
            if cigalettes.objects.filter(user_cigalettes=request.user).exists():
                how_many_cigalettes2 = cigalettes.objects.filter(user_cigalettes=request.user).first().how_many_cigalettes2
        else:
            if cigalettes.objects.filter(user_cigalettes=request.user).exists():
                how_many_cigalettes = 0
                how_many_cigalettes2 = int(request.POST.get("how_many_cigalettes")) * 550 + cigalettes_before.how_many_cigalettes2
                cigalettes_before.how_many_cigalettes2 = how_many_cigalettes2
                cigalettes_before.save()

            else:
                how_many_cigalettes2 = int(request.POST.get("how_many_cigalettes")) * 550
                Cigalettes = cigalettes.objects.create(
                    how_many_cigalettes2=how_many_cigalettes2,
                    user_cigalettes=request.user
                )
            if liquor.objects.filter(user_liquor=request.user).exists():
                how_many_liquor2 = liquor.objects.filter(user_liquor=request.user).first().how_many_liquor2



        forms["value"] = liquor_before.how_many_liquor2
        forms["value2"] = cigalettes_before.how_many_cigalettes2
        forms["all_value"] = liquor_before.how_many_liquor2 + cigalettes_before.how_many_cigalettes2
        return render(request, 'mypage.html', forms)
 

class BoardCreate(LoginRequiredMixin,CreateView):
    template_name = "create.html"
    form_class = createform    
    success_url = reverse_lazy('stsnsapp:top_page')
@login_required
def detailfunc(request,pk):
    detail_view = {"object":"","can_delete":"",}
    detail_view["object"] = get_object_or_404(BoardModel,pk=pk)
    if request.user == detail_view["object"].author:
        detail_view["can_delete"] = "success"
    return render(request,'detail.html',detail_view)

def how_many_good(request,pk):
    try:
        article = models.BoardModel.objects.get(pk=pk)
    except models.BoardModel.DoesNotExist:
        raise Http404
    article.good = article.good + 1
    article.save() 
    return redirect('stsnsapp:top_page')

class deletefunc(LoginRequiredMixin,DeleteView):
    template_name = 'delete.html'
    model = BoardModel
    success_url = reverse_lazy("stsnsapp:top_page")

@login_required
def ranking_view(request):
    datas = []
    for user in CustomUser.objects.all():
        liquor_data = liquor.objects.filter(user_liquor=user).first()
        cigalettes_data = cigalettes.objects.filter(user_cigalettes=user).first()
        if liquor_data:
            pass
        else:
            Liquors = liquor.objects.create(
                    how_many_liquor2=0,
                    user_liquor=user
                )
        if cigalettes_data:
            pass
        else:
            Cigalettes = cigalettes.objects.create(
                    how_many_cigalettes2=0,
                    user_cigalettes=user
                )
        try:
            total_value = liquor_data.how_many_liquor2 + cigalettes_data.how_many_cigalettes2
        except AttributeError:
            Liquors = liquor.objects.create(
                    how_many_liquor2=0,
                    user_liquor=user
                )
            liquor_data = Liquors
            Cigalettes = cigalettes.objects.create(
                    how_many_cigalettes2=0,
                    user_cigalettes=user
                )
            cigalettes_data = Cigalettes
            total_value = liquor_data.how_many_liquor2 + cigalettes_data.how_many_cigalettes2
        total_value = int(total_value)
        data = {
            "username":user.username,
            "total_value": total_value
        }
        
        datas.append(data) 
        data_sorted = sorted(datas, key=lambda x:x["total_value"],reverse=True)


    return render(request,'ranking.html',{'data_sorted':data_sorted})

