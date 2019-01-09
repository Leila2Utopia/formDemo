from django.shortcuts import render,HttpResponse
from django import forms
from django.forms import widgets
# Create your views here.

class UserForm(forms.Form):
    user = forms.CharField(label="用户名",
                           min_length=5,
                           error_messages={"required":"不能为空","min_length":"不少于5位"},
                           widget=widgets.TextInput(attrs={"class":"form-control"}))
    pwd = forms.CharField(label="密码",
                          max_length=8,
                          widget=widgets.TextInput(attrs={"class":"form-control"}))

    def clean_user(self):
        val = self.cleaned_data.get("user")
        if len(val)<10:
            return val
        else:
            raise ValueError('长度应小于10')

    # def clean(self):
    #     if self.cleaned_data['pwd']==self.cleaned_data['repeat_pwd']:
    #         return self.cleaned_data



def login(request):
    if request.method == 'POST':
        print(request.POST)
        #< QueryDict: {'pwd': [''], 'user': ['']} >
        form = UserForm(request.POST)
        if form.is_valid():
            print("cleaned_data",form.cleaned_data)
            print("errors",form.errors)
            return HttpResponse('OK')
        else:
            print("cleaned_data", form.cleaned_data)
            #cleaned_data    {}
            print("errors", form.errors)
            #errors < ul class ="errorlist" > < li > pwd < ul class ="errorlist" > < li > This field is required.< / li > < / ul > < / li > < li > user < ul class ="errorlist" > < li > This fi
            # print('form.errors["user"]',form.errors["user"])
            # #form.errors["user"] < ul class ="errorlist" > < li > This field is required.< / li > < / ul >
            # print('form.errors["user"][0]',form.errors["user"][0])
            # #form.errors["user"][0] Thisfield is required.

            return render(request,'login.html',{"form":form})
    form = UserForm()
    return render(request,'login.html',{"form":form})