import math
import random
import collections

class SendOTP(APIView):
    permission_classes = (AllowAny, )
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if email:
            email = str(email)
            user = User.objects.filter(email__iexact=email)

            if user.exists():
                key = send_otp(email)

                if key:
                    old = User.objects.filter(email__iexact=email)
                    if old.exists():
                        old = old.first()
                        count = old.count
                        old.count = count + 1
                        old.otp = key
                        old.save()
                        print('Count Increase', count)
                        return Response({
                            'status': True,
                            'detail': 'OTP sent successfully.'
                        })

def send_otp(email):
    if email:
        digits = [i for i in range(0, 10)]
        key = ""
        for i in range(6):
            index = math.floor(random.random() * 10)
            key += str(digits[index])
        print(key)
        return key
    else:
        return False

class VerifyOTP(APIView):
    permission_classes = (AllowAny, )
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        otp = request.data.get('otp')
        if email and otp:
            email = str(email)
            otp = str(otp)
            user = User.objects.filter(email__iexact=email)
            if user.exists():
                user = user.first()
                if user.otp == otp:
                    return Response({
                        'status': True,
                        'detail': 'OTP verified successfully.'
                    })
                else:
                    return Response({
                        'status': False,
                        'detail': 'OTP not verified.'
                    })
            else:
                return Response({
                    'status': False,
                    'detail': 'User not found.'
                })
        else:
            return Response({
                'status': False,
                'detail': 'Email or OTP not provided.'
            })