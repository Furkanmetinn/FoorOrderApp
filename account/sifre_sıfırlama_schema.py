# from graphql_jwt.decorators import jwt_required
# from graphql_jwt.utils import jwt_payload
# from django.contrib.auth import authenticate, login
# from .models import Kullanici
# from django.core.mail import send_mail
# from django.conf import settings
# from django.contrib.auth.tokens import PasswordResetTokenGenerator
# from django.utils.http import urlsafe_base64_encode, urlsafe_token_generator
# from django.contrib.auth.models import User
# import graphene

# class SifreSıfırlaMutation(graphene.Mutation):
#     class Arguments:
#         email = graphene.String(required=True)

#     message = graphene.String()

#     def mutate(self, root, info, email):
#         try:
#             kullanici = Kullanici.objects.get(email=email)
#         except Kullanici.DoesNotExist:
#             return SifreSıfırlaMutation(message="Bu e-posta adresine kayıtlı bir kullanıcı bulunamadı.")

#         # Kullanıcı için bir parola sıfırlama token'ı oluşturun
#         token_generator = PasswordResetTokenGenerator()
#         token = token_generator.get_token(kullanici)

#         # Kullanıcıya token'ı içeren bir e-posta gönderin
#         subject = "Şifrenizi Sıfırlayın"
#         message = f"Merhaba {kullanici.isim},\n\nŞifrenizi sıfırlamak için lütfen aşağıdaki linke tıklayın:\n\n{settings.SITE_URL}/sifre-sifirla/{urlsafe_base64_encode(kullanici.pk)}/{token}/\n\nBu link 24 saat geçerli olacaktır.\n\nSaygılarımızla,\n{settings.EMAIL_HOST_USER}"
#         send_mail(subject, message, settings.EMAIL_HOST_USER, [email], fail_silently=False)

#         return SifreSıfırlaMutation(message="Şifrenizi sıfırlamak için bir e-posta gönderdik.")

# class Mutation(graphene.ObjectType):
#     sifre_sifirla = SifreSıfırlaMutation()
