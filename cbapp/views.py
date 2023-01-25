import os

from django.shortcuts import render,redirect
from django.views import generic
from .forms import *
from django.urls import reverse_lazy
from django.http import HttpResponse

# Create your views here.

# generic:generic in django is an inbuilt view were developed to ease your pgms.They are the advanced set of
# built in views that are used to implement the selective crud.Using class based views we can easily handle
# the get,post request for a view.            ie,django de inbuilt view ne aanu generic ennu vilikkunnnathu.

# the post() method that is used to input a data into a database field.
# register,login,file upload ithellam post() il varunnathanu.ie,angotekku data type cheythu kodukkunnathu.

# the get() method is used to retrieve a data from database.
# database il ninnu ingotekku data edukkunnathinanu get() method use cheyyyunnathu.

# CreateView : it is a view that is used for creating an instance.
# ListView   : it is a view that is used to list all instances.ie,ella instance neyum list cheyyan Listview.
# UpdateView : it is a view that is used for editing an existing object and saving changes to the object.
# DeleteView : it is a view that is used to delete an existing object.
# DetailView : it's used to get a single instance.ie,single instance ne matram get cheyyan DetailView use cheyunu.


# generic     : from django.views import generic
# form_class  : from .forms import *                    ie,forms ne ee pagil kittan vendi
# success_url : from django.urls import reverse_lazy

# reverse_lazy:it is used to implies a lazy implementation of url.
# django de inbuilt aayittulla oru url aanu reverse_lazy.success_url nu vendi use cheyyunnathanu.
# register cheythu kazhinjal ee pagine aduthathu engotekku aanu konduponathu ennu teerumanikkunna oru url
# method aanu success_url.athinu upayogikkunna fn aanu reverse_lazy.reverse_lazy redirect (here login page lekku)
# cheyyyan use cheyyunnu.

class register(generic.CreateView):       # new instance created.
    form_class = regform
    template_name = 'register.html'
    success_url = reverse_lazy('login')         # registration success aayi kazhinjal login lekku pokanam.

# 30/11/2022

class login(generic.View):
    form_class=logform
    template_name='login.html'
    def get(self,request):                # get method use cheyyunnathu oru data ne retrieve cheythu edukkan.
        form=self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):               # post method use cheyyunnathu data ne input cheythu kodukkanum aanu.
        if request.method=='POST':
            a=logform(request.POST)
            if a.is_valid():
                em=a.cleaned_data['email']
                ps=a.cleaned_data['password']
                b=regmodel.objects.all()
                for i in b:
                    if em==i.email and ps==i.password:
                        return HttpResponse("login success")
                else:
                    return HttpResponse("login faild")


# 1/12/2022
# User oru inbulit class aanu.athu kond models.py il code kodukkenda avashyam illa.

############ registration using User Model #################

class regclass(generic.CreateView):
    form_class = reg
    template_name = 'reg.html'
    success_url = reverse_lazy('logclass')

# CreateView aanennu paranju kodukkanam.use cheyyunna form ethanennu paranju kodukkanam(reg).Template ethanennu
# paranju kodukkanam.itrayum ok anegil engottekku aanu redirect cheythu pokendathennnu success_url use cheythu
# paranju kodukkanam(logclass lekku).Alredy CreateView aayathu kond thanne form ne ariyam.athukond reg.html
# pagil poyi {{form.as_p}} ennu call cheythal mathy(only use CreateView).

############ login using User Model ############

class logi(generic.View):
    from_class = lo               # lo ennathu form nte name aanu.
    template_name='lo.html'
    def get(self,request):
        a=lo                      # form(lo) ne a enna variable lekku assign cheythu.
        return render(request,'lo.html',{'form':a})      # lo.html lekku form ne pass cheythu.

# template ne front end il kananam engil get cheyyyanam.
# verum View matram aanu generic il use cheyyunnathengil front end lekku nammal aayittu pass cheythu vidanam.
# {'form':a} ingane kodukkanam.ithinu shesham front end aaya lo.html chennu interpolation use cheythu form ne
# get cheyyichu.

    def post(self,request):
        if request.method=='POST':
            a=lo(request.POST)
            if a.is_valid():
                em=a.cleaned_data['email']
                ps=a.cleaned_data['password']
                b=User.objects.all()
                for i in b:
                    if i.email==em and i.password==ps:
                        return HttpResponse("login success")
                else:
                    return HttpResponse("login failed")



################## List objects ################### ,views.py,disp.html,urls.py

class dis(generic.ListView):
    model = User
    template_name = 'disp.html'
    def get(self,request):
        a=self.model.objects.all()             # a enna variable lekku data ne assign cheythu.
        return render(request,self.template_name,{'a':a})   # a ne template_name(disp.html) lekku 'a' enna
                                                            # veroru variable vazhi pass cheythu.


################# delete objects ################### views.py,delete.html,disp.html,urls.py

class re(generic.DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('disp')    # delete aayashesham display pagilekku varan.disp ennathu display
                                          # paginte url name aanu.


################# detail view  ###################### views.py,detail.html,disp.html,urls.py

class detail(generic.DetailView):
    model = User
    template_name = 'detail.html'



# 2/12/2022

################ update user ##################### views.py,update.html,disp.html,urls.py

class up(generic.UpdateView):
    model = User
    template_name = 'update.html'
    fields = ['username','email']
    success_url = reverse_lazy('disp')


############### file upload ###################

class fileclass(generic.CreateView):
    form_class = fileform
    template_name = 'file.html'
    success_url = reverse_lazy("filedis")

    # def post(self,request):     # url venda.pakrm oru msg matram display ayal mathy engil post fn use cheyanam.
    #     try:
    #         return HttpResponse("success")
    #     except:
    #         return HttpResponse("failed")

##############  file display  ################## views.py,filedisp.html,urls.py

class filedis(generic.ListView):
    model = filemodel
    template_name = 'filedisp.html'
    def get(self,request):
        a=self.model.objects.all()
        image=[]
        name=[]
        id1=[]
        for i in a:
            id=i.id
            id1.append(id)
            im=str(i.image).split('/')[-1]
            image.append(im)
            nm=i.itemname
            name.append(nm)
        mylist=zip(image,name,id1)
        return render(request,self.template_name,{'a':mylist})


#############  file delete  ###################  views.py,urls.py,filedisp.html,models.py

class filedelete(generic.DeleteView):
    model = filemodel
    template_name = 'delete.html'
    success_url=reverse_lazy('filedis')


# 06/12/2022

##############  file detail ################    views.py,filedetail.html,urls.py,filedisp.html

class filedetail(generic.DetailView):
    model = filemodel
    template_name = 'filedetail.html'
    def get(self,request,**kwargs):
        val=kwargs.get('pk')                                     # pk=1
        a=self.model.objects.get(id=val)                         # val=1
        b=a.itemname                                             # iphone
        img=a.image                                              # cbapp/static/iphone.png
        j=str(img).split('/')[-1]               # path il ninnu image ne matram edukkan split method use chethu.
        return render(request,'filedetail.html',{'j':j,'b':b})

# **kwargs:keyword arguments.
# get(): it is a fn that is used in dictonary to get the value of a key.

# 07/12/2022
############## file update ############### views.py,fileupdate.html,filedisp.html,urls.py

class fileup(generic.UpdateView):
    model = filemodel
    template_name = 'fileupdate.html'
    fields = '__all__'
    form_class=fileform

    def get(self,request,**kwargs):                 # get method vazhi fileform ne eduthu.
        a=self.form_class                           # a enna variable lekku form_class(fileform) ne assign cheythu.
        return render(request,'fileupdate.html',{'form':a})                 # form ne front end lekku pass cheythu.

    def post(self, request,**kwargs):                # html page lekku data ne i/p cheyyan post use cheyyyunnu.
        id1=kwargs.get('pk')
        a=self.model.objects.get(id=id1)
        image=str(a.image).split('/')[-1]
        if request.method=='POST':
            if len(request.FILES) !=0:
                if len(a.image)>0:
                    os.remove(a.image.path)           # os ivide koduthal mukalil import os illengil error kanikkum.
                a.image=request.FILES['image']
            a.itemname=request.POST.get('itemname')
            a.save()          # ivde redirect koduthathukond ettavum mukalil render kazhinju redirect kodukkanam.
            return redirect('http://127.0.0.1:8000/cbapp/filedis')


###################################################################################################################
###################################################################################################################

################ static loading ##################
def index(request):
    return render(request,'index.html')


##################################################
# 08/12/2022  ithu fn based aanu

def regview(request):
    if request.method=='POST':
        a=newreg(request.POST)
        if a.is_valid():
            nm=a.cleaned_data['name']
            add=a.cleaned_data['address']
            gen=a.cleaned_data['gender']
            stat=a.cleaned_data['state']
            b=newmodel(name=nm,address=add,gender=gen,state=stat)
            b.save()
            return HttpResponse('registered')
        else:
            return HttpResponse('failed')

    else:
        return render(request,'regb.html')








#####################################################################################################
#####################################################################################################
# 02/12/2022

# work:
# create a crud system using class based view
#
# create :product_name,price,customer_name,customer_id,phone
#
# delete view,update view,detail view,list view


class product(generic.CreateView):
    form_class = productform
    template_name = 'product.html'
    success_url = reverse_lazy('plogin')


class plogin(generic.View):
    form_class= plogform
    template_name='plogin.html'
    def get(self,request):                # get method use cheyyunnathu oru data ne retrieve cheythu edukkan.
        form=self.form_class
        return render(request,self.template_name,{'form':form})

    def post(self,request):               # post method use cheyyunnathu data ne input cheythu kodukkanum aanu.
        if request.method=='POST':
            a=plogform(request.POST)
            if a.is_valid():
                cn=a.cleaned_data['customername']
                ci=a.cleaned_data['customerid']
                b=productmodel.objects.all()
                for i in b:
                    if cn==i.customername and ci==i.customerid:
                        return HttpResponse("login success")
                else:
                    return HttpResponse("login faild")

######################### display/list objects ##################

class pdis(generic.ListView):
    model = productmodel
    template_name = 'pdisp.html'
    def get(self,request):
        a=self.model.objects.all()
        return render(request,self.template_name,{'a':a})

########################### delete objects ######################

class pre(generic.DeleteView):
    model = productmodel
    template_name = 'pdelete.html'
    success_url=reverse_lazy('pdisp')


################# detail view  ###################### views.py,pdetail.html,pdisp.html,urls.py

class pdetail(generic.DetailView):
    model = productmodel
    template_name = 'pdetail.html'


################ update view #####################

class pup(generic.UpdateView):
    model = productmodel
    template_name = 'pupdate.html'
    fields = ['productname','price','customername','customerid','phone']
    success_url = reverse_lazy('pdisp')



























