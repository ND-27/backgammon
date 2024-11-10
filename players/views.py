from django.shortcuts import get_object_or_404
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from home.views import calculate_level
from .models import User, Referral, GameHistory
from .serializers import UserSerializer, ReferralSerializer, GameHistorySerializer


def profile_page(request):
    my_user = get_object_or_404(User, username=request.user)
    back_game = GameHistory.objects.filter(user1=my_user).reverse()
    total_back_matches = back_game.count()

    current_lvl = calculate_level(my_user.level_xp)
    next_lvl = current_lvl + 1
    my_user.level = current_lvl
    my_user.save()

    pool_lvl = current_lvl * 1000
    pool_fill = my_user.level_xp
    for i in range(current_lvl):
        x = i
        pool_fill -= (x * 1000)
    bar_percent = int((pool_fill * 100) / pool_lvl)

    context = {
        "back_game_history": back_game,
        "total_back_matches": total_back_matches,
        "total_back_wins": my_user.backgammon_game_wins,
        "current_lvl": current_lvl,
        "next_lvl": next_lvl,
        "pool_lvl": pool_lvl,
        "pool_fill": pool_fill,
        "bar_percent": bar_percent
    }
    return render(request, "profile_page.html", context=context)


def referral_page(request):
    my_user = get_object_or_404(User, username=request.user)
    referrals = Referral.objects.filter(inviter=my_user)
    context = {
        "my_user": my_user,
        'referrals': referrals,
        'referral_count': referrals.count(),
    }
    return render(request, 'referral_page.html', context=context)


# ویو برای User
class UserAPIView(APIView):
    def get(self, request, username=None):
        if username:
            user = get_object_or_404(User, username=username)
            serializer = UserSerializer(user)

        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, username):
        user = get_object_or_404(User, username=username)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, username):
        user = get_object_or_404(User, username=username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ویو برای Referral
class ReferralAPIView(APIView):
    def get(self, request):
        referrals = Referral.objects.all()
        serializer = ReferralSerializer(referrals, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReferralSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ویو برای GameHistory
class GameHistoryAPIView(APIView):
    def get(self, request):
        game_histories = GameHistory.objects.all()
        serializer = GameHistorySerializer(game_histories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = GameHistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
