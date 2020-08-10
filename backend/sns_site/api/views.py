from django.views import View
from django.http import JsonResponse

from sns.models import Tweet, Comment, Tweet_like, Comment_like


class LikeView(View):
    def post(self, request, *args, **kwargs):
        res = {
            "result": False, 
            "countNum": None, 
        }

        if (not "comment_id" in request.POST) and (not "tweet_id" in request.POST):
            return JsonResponse(res, status=400)
        
        comment_id = int(request.POST["comment_id"])
        tweet_id = int(request.POST["tweet_id"])

        if comment_id == -1:
            like_num = Tweet_like.objects.filter(tweet=Tweet.objects.get(pk=tweet_id), user=request.user).count()
            if like_num == 0:
                Tweet_like.objects.create(tweet=Tweet.objects.get(pk=tweet_id), user=request.user)
                res["result"] = True
                res["countNum"] = Tweet_like.objects.filter(tweet=Tweet.objects.get(pk=tweet_id)).count()
                return JsonResponse(res, status=201)
            elif like_num == 1:
                Tweet_like.objects.get(tweet=Tweet.objects.get(pk=tweet_id), user=request.user).delete()
                res["result"] = True
                res["countNum"] = Tweet_like.objects.filter(tweet=Tweet.objects.get(pk=tweet_id)).count()
                return JsonResponse(res, status=201)
            else:
                print("Error!!! Unknown tweet like number.")
            return JsonResponse(res, status=500)
        elif tweet_id == -1:
            like_num = Comment_like.objects.filter(user=request.user, comment_id=comment_id).count()
            if like_num == 0:
                Comment_like.objects.create(comment=Comment.objects.get(pk=comment_id), user=request.user)
                res["result"] = True
                res["countNum"] = Comment_like.objects.filter(comment_id=comment_id).count()
                return JsonResponse(res, status=201)
            elif like_num == 1:
                Comment_like.objects.get(user=request.user, comment_id=comment_id).delete()
                res["result"] = True
                res["tweet_like_num"] = -1
                res["countNum"] = Comment_like.objects.filter(comment_id=comment_id).count()
                return JsonResponse(res, status=201)
            else:
                print("Error!!! Unknown comment like number.")
            return JsonResponse(res, status=500)