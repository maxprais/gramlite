from django.shortcuts import render, redirect
from .models import User, Image
import requests
from django.views.generic import View


class Check_User(View):

    def check_user(self, request):
        username = request.POST['username']
        if username:
            user_id = self.get_user_id(username, request)
            if user_id:
                user = self.user_already_exists(username, user_id)
                images = self.get_images(user)
                user_info = {
                    'images': images,
                    'username': username

                }

                return redirect('gallery/'+username+'/1')
                # return render(request, 'gramlite/template1.html', user_info)
                # return HttpResponseRedirect("https://api.instagram.com/v1/users/%s/media/recent/?access_token=1497402817.1fb234f.1b8969bb3b304945a6782ae574069017" % user_id)
        return self.no_user_case(request)



    def get_user_id(self, username, request):
        response = requests.get('https://api.instagram.com/v1/users/search?access_token=1497402817.1fb234f.1b8969bb3b304945a6782ae574069017&q=' + username)
        res = response.json()['data']
        if len(res) > 0:
            for user in res:
                if username == user['username']:
                    user_id = user['id']
                    print user_id
                    return user_id
        else:
            return 0

    def user_already_exists(self, username, user_id):
        user= User.objects.filter(name=username)
        if not user:
            user = User(name=username, user_id=user_id)
            user.save()
        else:
            user = user[0]
        return user

    def get_images(self, user):
        image_link = requests.get("https://api.instagram.com/v1/users/%s/media/recent/?access_token=1497402817.1fb234f.1b8969bb3b304945a6782ae574069017" % user.user_id)
        image_data = image_link.json()
        image_list = []
        for i in image_data['data']:
            image_data = i['images']
            image_o = image_data['standard_resolution']
            new_img = image_o['url']
            image_search = Image.objects.filter(image_link=new_img)
            if image_search:
                image_list.append(image_search)
            else:
                img = Image(image_link=new_img, user_id=user)
                img.save()
                image_list.append(img)
        return image_list

    def no_user_case(self, request):
        context = {'status': 'not found'}
        return render(request, 'gramlite/home.html', context)

    def post(self, request):
        return self.check_user(request)



def home(request):
    return render(request, 'gramlite/home.html')


class Styles(View):
    def get(self, request, username, templateid):
        user = User.objects.get(name=username)
        username = user.name
        images = user.image_set.all()
        user_info = {
                    'images': images,
                    'username': username
                }
        return render(request, 'gramlite/'+'template'+templateid+'.html', user_info)

