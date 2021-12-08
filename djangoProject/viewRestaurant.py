from rest_framework.views import APIView
from rest_framework.response import Response

class Attend(APIView):
    def post(self, request):
        """
        슬랙에서 채팅 이벤트가 있을 때 호출하는 API
        :param request:
        :return:
        """

        # 요청이 어떻게 들어오나 찍어보기
        print(request.body)

        # 그냥 응답 성공으로 줘보기
        return Response(status=200)